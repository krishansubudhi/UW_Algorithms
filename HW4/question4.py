'''
#Algo
Two choice hashing uses two hash function and assigns items to the least used bucket. 

# Assumptions
For this problem, you will assume a chaining implementation of hashing, since you are counting the number of elements assigned to buckets (but you don’t need to implement chaining, since you only need the counts.


You may assume that your hash functions are perfectly random. 

For each experiment you run, you should hash n items into n cells. 

# Metric
The statistic of most interest is the maximum number of items assigned to a cell, 

but computing the standard deviation is also of interest.
'''
import random
import numpy as np
import logging
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
class KchoiceHashing():
    def __init__(self, n, k):
        self.n = n
        self.k = k
        # Buckets only store counts in this simulation.
        self.buckets = [0] * self.n #nothing is assigned to the buckets yet
        self.logger = logging.getLogger(name = __name__)
        # random hash functions with different seeds.
        # Each hash function is a random number generator.
        self.h = [random.Random(i) for i in range(k)]

    def assign_item(self, item = None):
        '''Assigns a new item to a bucket.
        For this simulation, we don't need to assign actual items.
        We will just increment item count in the assigned bucket 
        '''
        # Compute hash functions and shortlist buckets
        selected_buckets = [h.randint(0, n-1) for h in self.h]
        current_items = np.array([self.buckets[b] for b in selected_buckets])
        # select bucket with least amount of items in it
        min_bucket = selected_buckets[np.argmin(current_items)]

        self.logger.debug(f'selected bucket {min_bucket} from {selected_buckets}')

        # assign item to that bucket
        self.buckets[min_bucket] += 1

        self.logger.debug(self.buckets)

    def assign_n_items(self):
        for i in range(n):
            self.logger.debug(f'iteration {i}')
            self.assign_item(i)
    
    def max_items(self):
        return max(self.buckets)

    def std(self):
        return np.array(self.buckets).std()

import pandas as pd
import matplotlib.pyplot as plt
if __name__ == '__main__':

    # logging.basicConfig(level=logging.INFO)
    # logger = logging.getLogger(name = __name__)
    # series = []
    # for n in [1_000,10_000,100_000,1_000_000]:
    #     for k in [1,2,3]:
    #         hashing = KchoiceHashing(n,k)
    #         hashing.assign_n_items()
    #         max_items = hashing.max_items()
    #         ratio = max_items/np.log(np.log(n))
    #         ratio2 = max_items/(np.log(n)/np.log(np.log(n)))
    #         s = {
    #             'n':n,
    #             'k':k,
    #             'max_items':max_items,
    #             'max_items/log logn': ratio,
    #             'max_items/(log n/ log log n)': ratio2,
    #             'standard Deviation':hashing.std()
    #         }
    #         series.append(s) 
    #         logger.info(f'n = {n}, k = {k}, max_items = {max_items}, ratio = {ratio:.3}, std = {hashing.std():.3}')
    # df = pd.DataFrame(series)
    # df = df.set_index(['n','k'])
    # print(df.to_latex())

    # df.to_csv('q4_out.csv')

    n = 1024
    vals = {}
    for k in range(0,int(np.log2(n))+1):
        print(k)
        k = 2**k
        print(k)
        hashing = KchoiceHashing(n,k)
        hashing.assign_n_items()
        max_items = hashing.max_items()
        vals[k]= max_items
    plt.plot(vals.keys(), vals.values())
    plt.xlabel('k')
    plt.ylabel('max_items')
    
    plt.show()
    



