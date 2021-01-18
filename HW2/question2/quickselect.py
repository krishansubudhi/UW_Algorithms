'''
Show that if the pivot is always the median, then the selection algorithm makes (about) 2n comparisons. 
(The code, as presented in class, returns the pivot if it is the element we are looking for. 
To avoid this issue, you can show that if the pivot is always the median, then the selection 
algorithm takes 2n comparisons to find the maximum element.)
'''
import random
import pandas as pd
import collections
class QuickSelect:
    def __init__(self):
        self.comparison_count = 0
        self.partition_count = 0

    def kth_largest(self, data :list, k: int):
        '''
        Find k th largest element in data. K should be between 1 and length of data (inclusive)
        '''
        self.data = data
        self.comparison_count = 0
        self.partition_count = 0
        assert k<=len(self.data) and k>0, 'K out of range'
        element =  self._kth_largest(k, 0, len(data)-1)
        return element
    
    def _kth_largest(self, k: int, start : int, end : int):
        """
        Given a list, find it's kth largest element using Quick select algorithm
        """
        # 1. select a random pivot
        pivotIndex = self.get_pivot_index(start, end)
        # print('Before partition start, end, pivotIndex ',  start, end, pivotIndex)
        pivotIndex = self.partition(pivotIndex, start, end)
        # print(f'After partition , data = {data}, pivotIndex = {pivotIndex}')

        if end-pivotIndex >=k:
            return self._kth_largest(k, pivotIndex+1, end)
            
        elif end-pivotIndex+1 == k:
            return pivotIndex, self.data[pivotIndex]
        else:
            return self._kth_largest(k-1-(end-pivotIndex), start , pivotIndex-1)

    def partition(self, pivotIndex, start, end):
        self.partition_count += 1
        pivotValue = self.data[pivotIndex]
        # Move pivot to right
        self.swap(end , pivotIndex)
        pivotIndex = end
        leftIndex = start
        # Loop till end-1.
        for i in range(start, end):
            self.comparison_count += 1
            if data[i] < pivotValue:
                self.swap(leftIndex, i)
                leftIndex += 1
        self.swap(leftIndex, pivotIndex)
        return leftIndex
    
    def swap(self, i , j):
        t = self.data[j]
        self.data[j] = self.data[i]
        self.data[i] = t

    def get_pivot_index(self,start, end):
        randomIndex = random.randint(start,end)
        # print('pivot index, value =',randomIndex,self.data[randomIndex])
        return randomIndex

    def __str__(self):
        return 'Quick select random pivot'

class QuickSelectMedianSort(QuickSelect):
    def get_pivot_index(self, start, end):
        randomIndex = range(start, end+1)
        # Use inbuilt sort
        randomIndex = sorted(randomIndex, key = lambda index: self.data[index])
        median = randomIndex[(end-start)//2]
        # print(f'{start}:{end} - pivot index, value =',median,self.data[median])
        return median

    def __str__(self):
        return f'Quick select Median from sorting'

class QuickSelectMedianQS(QuickSelect):
    def get_pivot_index(self, start, end):
        q= QuickSelect()
        q.data = self.data
        median, medianval = q._kth_largest( (end-start)//2+1, start, end) # this manipulates the input though
        # print(f'{start}:{end} - comparisons = {q.comparison_count} , pivot index, value =',median,self.data[median])
        return median

    def __str__(self):
        return f'Quick select Median from quick select'

class QuickSelectMiddleIndex(QuickSelect):
    # Only works with identity permutation
    def get_pivot_index(self, start, end):
        median = start + (end-start)//2
        # print(f'{start}:{end} - pivot index, value =',median,self.data[median])
        return median

    def __str__(self):
        return f'Quick select middle index'

import time
if __name__ == '__main__':
    import sys
    algos = [QuickSelect(), QuickSelectMiddleIndex(), QuickSelectMedianSort(), QuickSelectMedianQS()]
    iterations  =10
    results = []
    for n in [1_000, 10_000, 100_000,1_000_000]:
        data = [i for i in range(1,n+1)]
        for q in algos:
            print(q)
            random.seed(48)
            comparisons = 0
            partitions = 0
            start = time.time()
            for _ in range(iterations):
                # data = [random.randint(0,n) for i in range(1,n+1)]
                k = 1 #max
                element = q.kth_largest(data, k)
                print(f'q: max index =  {element[0]}, max value = {element[1]}')
                comparisons += q.comparison_count
                partitions += q.partition_count
            end = time.time()
            results.append(pd.Series({
                'n':n,
                'algorithm':str(q),
                'expected partitions':partitions/iterations,
                'expected comparisons' :f'{comparisons/iterations/n:.2f} n',
                'expected runtime' : f'{(end-start)/iterations:.4f} seconds'
            }))
    df = pd.DataFrame(results).set_index(['n','algorithm'])
    print(df)
    # print(df.to_latex(multirow = True, multicolumn_format = 'c'))
