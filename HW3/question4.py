"""
Implement the Gayle Shapley algorithm


Algorithm Traces.  The input is the M preferences (with row i giving the preference
order for m_i) and the W preferences (with row i giving the preference order for w_i).

The output is the matching computed with respect to M - so the i-th entry is the W that m_i is _matched to.  

The trace is the list proposals with the result given.  The pair in brackets [i, j] indicates that at the time of 
the proposal w_i is _matched with m_j.   (A -1 is used to indicate w_i is un_matched.)   The trace is from one partcular 
implementation of the Gale-Shapley algorithm - you may get different proposals,  but you should get the same overall result.
The specific implementation uses a Stack for ordering the un_matched W's.

==================================== 




Input:
[2, 0, 1]
[2, 0, 1]
[2, 1, 0]


[2, 0, 1]
[0, 2, 1]
[2, 0, 1]

Output:
[0, 1, 2]

Trace
2 _proposes to 2 [2,-1]  Accepted
1 _proposes to 2 [2,2]  Rejected
1 _proposes to 0 [0,-1]  Accepted
0 _proposes to 2 [2,2]  Rejected
0 _proposes to 0 [0,1]  Accepted
1 _proposes to 1 [1,-1]  Accepted

"""


import numpy as np
import dataclasses


@dataclasses.dataclass
class Person:
    index: int
    pref_list: list
    current_match: int = -1  # accepted

class Man(Person):
    total_proposed: int = 0  # may or may not be accepted
    def get_next_woman(self):
        return self.pref_list[self.total_proposed]
    @property
    def mrank(self):
        return self.total_proposed


class Woman(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pref_dict = {m: i for i, m in enumerate(self.pref_list)}
        del self.pref_list
    def __str__(self):
        return super().__str__() + str(self.pref_dict)
    def __repr__(self):
        return super().__repr__() + str(self.pref_dict)
    @property
    def wrank(self):
        return self.pref_dict[self.current_match]


class GayleShapely:
    def __init__(self, m: list, w: list, trace=True):

        m = np.array(m)
        w = np.array(w)
        self.men = [Man(i, pref) for i, pref in enumerate(m)]
        self.women = [Woman(i, pref) for i, pref in enumerate(w)]
        self.trace = trace
        
        self.free_men = set([m.index for m in self.men])
        if trace:
            print('men')
            print(m)
            print('women')
            print(w)

    def _get_next_free_m(self):
        return self.men[self.free_men.pop()] if len(self.free_men) >0 else None

    def _matched(self, man: Man, woman: Woman):
        man.current_match = woman.index
        if woman.current_match > -1:
            self.men[woman.current_match].current_match = -1
            self.free_men.add(woman.current_match)
        woman.current_match = man.index

        


    def _propose(self, man, woman):
        man.total_proposed += 1
        result = "Rejected"
        woman_prev_match = woman.current_match
        if (
            woman.current_match == -1
            or woman.pref_dict[man.index] < woman.pref_dict[woman.current_match] #this is rank so lower is better
        ):
            self._matched(man, woman)
            result = "Accepted"

        if self.trace:
            print(
                f"{man.index} proposes to {woman.index} [{woman.index},{woman_prev_match}] {result}"
            )
        return result == "Accepted"

    def match(self):
        """
        m and w are objects
        """
        m = self._get_next_free_m()
        
        while m is not None:
            accepted = False
            while not accepted:
                # select next woman
                w = self.women[ m.get_next_woman()]
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

def main():
    m = [
        [2,1,3,0],
        [0,1,3,2],
        [0,1,2,3],
        [0,1,2,3]
    ]

    w = [
        [0,2,1,3],
        [2,0,3,1],
        [3,2,1,0],
        [2,3,1,0]
    ]
    algo = GayleShapely(m,w)
    algo.match()

if __name__ == "__main__":
    # m = [[2, 0, 1], [2, 0, 1], [2, 1, 0]]

    # w = [[2, 0, 1], [0, 2, 1], [2, 0, 1]]

    m = [
        [3, 1, 0, 2],
        [3, 0, 1, 2],
        [3, 1, 2, 0],
        [0, 3, 2, 1]
    ]

    w = [
            [3, 0, 2, 1],
            [3, 1, 2, 0],
            [0, 1, 3, 2],
            [3, 0, 2, 1]
        ]
    algo = GayleShapely(m, w, trace = False)

    algo.match()

    assert algo.get_matches() == [3, 1, 2, 0]
    main()

    #assignment
