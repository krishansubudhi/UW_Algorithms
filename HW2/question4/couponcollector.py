'''
The Coupon Collector problem is: There are n types of coupons. Each time you get a coupon, you are given a coupon of a random type (with equal probability of receiving each type of coupon). The question is how many coupons do you expect to receive, on the average, before you have collected the full set of coupons.

write a simulator of the Coupon Collector Problem, and run simulations to see how many coupons you receive before you have completed the set. You should compare your results with the theoretical analysis, which is that the expected number of coupons is nHn = n ln n +0.57n where Hn is the 
n-th harmonic numberdatetime A combination of a date and a time. Attributes: ()


The analysis of the coupon collector problem is to look at the expected time to get a new coupon if there are k coupons that remain to be collected. If k coupons remain to be collected, then the probability of getting a new coupon is n/k .

Let Xnk be the random variable for the number of coupons needed to get a new coupon when k coupons remain. Experimentally evaluate the expected values of Xn
k . The purpose of this problem it
is to compare the theoretical analysis of the coupon collector with an experimental version (see Wikipedia), so you will need to identify suitable parameters in terms of range of values and number of repetitions.

Summary:

Each time you get a coupon, you are given a coupon of a random type (with equal probability of receiving each type of coupon).

Xnk = number of coupons needed to get a new coupon when k coupons remain = n/k
Cn = how many coupons you receive before you have completed the set = nHn = n ln n +0.57n
'''

from collections import defaultdict
import random, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class CouponCollector():
    def __init__(self,n):
        self.n = n
        self.k = n # remaining coupons to be collected
        self.Xnk =  {}
        self.Cn = 0
        self.unique_coupons_collected = set()
    def collect_all_coupons(self):
        coupons_collected_this_iteration = 0
        while self.k>0:
            coupon = random.randint(1,self.n)
            coupons_collected_this_iteration += 1
            if coupon not in self.unique_coupons_collected:
                #new coupon collected
                self.unique_coupons_collected.add(coupon) # add to collected list
                self.Xnk[self.k] = coupons_collected_this_iteration #update random variable value
                self.k -= 1 # remaining 1 less
                self.Cn += coupons_collected_this_iteration # total count
                coupons_collected_this_iteration = 0 #reset
    
    def __str__(self):
        return f'Cn = {self.Cn}, Xnk = {self.Xnk}'
    @staticmethod
    def theoritical_Xnk(n, k ):
        return n/k
    
    @staticmethod
    def theoritical_cn(n):
        return n * math.log(n) + 0.57 * n

def get_experimental_Cn_Xnk(n, iterations = 5):
    Cns = []
    Xnks = []
    for iteration in range(iterations):
        print('n, iteration', n, iteration)
        collector = CouponCollector(n)
        collector.collect_all_coupons()
        Cns.append(collector.Cn)
        Xnks.append(collector.Xnk)
    #expectation
    Cn = np.array(Cns).mean()
    Xnk = pd.DataFrame(Xnks).mean()
    return Cn, Xnk

def get_theoritical_Cn_Xnk(n):
    Xnk = {k: CouponCollector.theoritical_Xnk(n, k) for k in range( n,0,-1)}
    Cn = CouponCollector.theoritical_cn(n)
    return Cn, pd.Series(Xnk)

# plot Xnk for n = 100,000
n = 10000
c, x = get_experimental_Cn_Xnk(n)
plt.plot(x)
c, x = get_theoritical_Cn_Xnk(n)
plt.plot(x)
plt.legend(['Experimental', 'Theory'])
plt.xlabel('k')
plt.ylabel('Xnk')
plt.title(f'number of coupons needed to get a new coupon when k coupons remain (n = {n})')


plt.figure()
#plot Cn
ns = [100, 1_000,100_00, 100_000, 1000_000]
c_exp = [get_experimental_Cn_Xnk(n)[0] for n in ns]
c_theo = [get_theoritical_Cn_Xnk(n)[0] for n in ns]

plt.plot(ns,c_exp)
plt.plot(ns,c_theo)
plt.legend(['Experimental', 'Theory'])
plt.xlabel('n')
plt.ylabel('total coupons received')
plt.title(f'coupons received before completing the set')


plt.show()