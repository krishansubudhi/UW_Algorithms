
from question4 import Man, Woman, GayleShapely
import random
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
import math
plt.style.use('ggplot')
'''
Write an input generator which creates completely random preference lists, so that each M has a random permutation of the W’s for preference, and vice-versa
'''
def generate_random_permutations(n):
    return [np.random.permutation(range(n)).tolist() for i in range(n)]

def main():
    results = {}
    for n in [8000]:
        random.seed(46)
        
        m = generate_random_permutations(n)
        w = generate_random_permutations(n)

        algo = GayleShapely(m, w, trace = False)
        
        start = time.time_ns()/1000
        algo.match()
        end = time.time_ns()/1000
        
        total_time = end-start
        
        results[n]= pd.Series({
                'time_micros':total_time,
                'MGoodness':algo.MGoodness,
                'WGoodness':algo.WGoodness,
                'time_ms/CouponCollector':total_time/theoritical_cn(n)
            })
    df =  pd.DataFrame(results).T
    return df

def theoritical_cn(n):
    return n * math.log(n) + 0.57 * n

if __name__=='__main__':
    result = main()
    print(result)

    fig, axes = plt.subplots(2,2, sharex = True)
    axes = axes.reshape(-1)
    # print(axes)
    for i, col in enumerate(result.columns):
        axes[i].plot(result.index, result[col])
        axes[i].set_ylabel(col)
        axes[i].set_xlabel('n')
    
    # axes[2].plot(result.index, result['time_ms'])
    # axes[2].plot(result.index, result['CouponCollector_Cn'])
    # axes[2].legend(['time_ms', 'CouponCollector_Cn'])
    # axes[2].set_xlabel('n')

    plt.show()



# n=4
# print(generate_random_permutations(n))