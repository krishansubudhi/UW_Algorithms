'''
Implement the randomized selection algorithm from class, where the pivot is chosen at random
from the array. What is the expected number of comparisons that you do between data elements
to find the median?
'''
import random
class QuickSelect:

    def kth_largest(self, data :list, k: int):
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
            return self.data[pivotIndex]
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
        return randomIndex

    def __str__(self):
        return 'Quick select random pivot'

class QuickSelectMedian(QuickSelect):
    def __init__(self,median_of = 3):
        self.median_of = median_of
    def get_pivot_index(self, start, end):
        randomIndex = [random.randint(start,end) for _ in range(self.median_of)]
        # Use inbuilt sort
        randomIndex = sorted(randomIndex, key = lambda index: self.data[index])
        median = randomIndex[self.median_of//2]
        return median

    def __str__(self):
        return f'Quick select Median of {self.median_of}'

if __name__ == '__main__':
    import sys
    algos = [QuickSelect(), QuickSelectMedian(3), QuickSelectMedian(5)]
    iterations  =100
    for n in [100000, 100000]:
        print(f'\nn = {n}')
        for q in algos:
            random.seed(49)
            print('\n',q)
            comparisons = 0
            partitions = 0
            for _ in range(iterations):
                data = [i for i in range(1,n)]
                k = len(data)//2+1 #median
                element = q.kth_largest(data, k)
                comparisons += q.comparison_count
                partitions += q.partition_count
                print(q.partition_count)
            print(f'Average pivot selection per run = {partitions/iterations}')
            print(f'Average comparisons per run = {comparisons/iterations} = {comparisons/iterations/len(data)} n')



