import numpy as np
import dataclasses
import random
import sys

'''
Rewrite your stable matching generator, so that you compute stable matchings for very large, random instances. The key idea is to generate the random permutations incrementally, so that you only construct the random preferences when they are needed
'''
@dataclasses.dataclass
class Man():
    index: int
    n:int
    proposed_set: set = dataclasses.field(default_factory=set)
    current_match: int = -1  # accepted

    def get_random_proposee(self):
        random_woman = random.randint(0,self.n-1)
        if random_woman in self.proposed_set:
            return self.get_random_proposee()
        self.proposed_set.add(random_woman)
        return random_woman

    def accepted(self,w):
        self.current_match = w

    def dumped(self):
        self.current_match = -1

    @property
    def mrank(self):
        assert self.current_match > -1
        return len(self.proposed_set)

    def __repr__(self):
        return str(self.index)

@dataclasses.dataclass
class Woman():
    index: int
    n:int
    proposed_set: set = dataclasses.field(default_factory=set)
    current_match: int = -1  # accepted
    current_match_rank: int = -1

    def accept_proposal(self, m):
        preference = self.get_random_rank()
        if preference > self.current_match_rank:
            self.current_match = m
            self.current_match_rank = preference
            return True
        return False

    def get_random_rank(self):
        random_rank = random.randint(0,self.n-1)
        if random_rank in self.proposed_set:
            return self.get_random_rank()
        self.proposed_set.add(random_rank)
        return random_rank

    @property
    def wrank(self):
        return self.current_match_rank
    
    
    def __repr__(self):
        return str(self.index)


class GayleShapelyRandom:
    def __init__(self, n, trace=True):

        self.men = [Man(i, n) for i in range(n)]
        self.women = [Woman(i, n) for i in range(n)]
        self.trace = trace
        
        self.free_men = set([m.index for m in self.men])
        if trace:
            print('men')
            print(self.men)
            print('women')
            print(self.women)

    def _get_next_free_m(self):
        return self.men[self.free_men.pop()] if len(self.free_men) >0 else None

    def _matched(self, man: Man, woman: Woman, woman_prev_match:int):
        man.accepted(woman.index)
        if woman_prev_match > -1:
            self.men[woman_prev_match].dumped()
            self.free_men.add(woman_prev_match)


    def _propose(self, man, woman):

        woman_prev_match = woman.current_match
        accepted = woman.accept_proposal(man.index)

        if accepted:
            self._matched(man, woman, woman_prev_match)

        if self.trace:
            print(
                f"{man.index} proposes to {woman.index} [{woman.index},{woman_prev_match}] {accepted}"
            )
        return accepted

    def match(self):
        """
        m and w are objects
        """
        m = self._get_next_free_m()
        
        while m is not None:
            accepted = False
            while not accepted:
                # select next woman
                w = m.get_random_proposee()
                w = self.women[w]
                # _propose
                accepted = self._propose(m, w)
            m = self._get_next_free_m()
        if self.trace:
            print('matches\n',self.get_matches())

    def get_matches(self):
        return [m.current_match for m in self.men]

    def get_mranks(self):
        return [m.mrank for m in self.men]
    
    
    def get_wranks(self):
        return [w.wrank for w in self.women]

    @property
    def MGoodness(self):
        return sum(self.get_mranks())/len(self.men)
    
    @property
    def WGoodness(self):
        return sum(self.get_wranks())/len(self.women)

def main(n):
    algo = GayleShapelyRandom(n)
    algo.match()
    return algo

import time
import pandas as pd
def main2():
    results = {}
    for n in [1_000_000]:
        random.seed(46)
        algo = GayleShapelyRandom(n, trace = False)
        start = time.time()
        algo.match()
        end = time.time()
        
        total_time = end-start
        
        results[n]= pd.Series({
                'time_s':total_time,
                'MGoodness':algo.MGoodness,
                'WGoodness':algo.WGoodness
            })
    df =  pd.DataFrame(results).T
    print(df)
    return df

if __name__ == "__main__":

    # main(int(sys.argv[1]))
    main2()

    #assignment

#python question6.py 3