# from heatmap import makeHeatMap
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from collections import defaultdict, Counter
import math

class DocData:
    def __init__(self,data_file, labels_file,group_file):
        self.doc_bow = self.create_doc_bow(data_file)#defaultdict(Counter)
        self.label_doc_map = self.create_label_doc_map(labels_file)
        self.label_name_map = self.create_label_name_map(group_file)
    
    def create_doc_bow(self,data_file):
        doc_bow = defaultdict(Counter)
        with open(data_file,'r') as f:
            lines = f.readlines()
            for line in lines[:10000]:#remove
                columns = line.split(',')
                doc_bow[int(columns[0])][int(columns[1])] += int(columns[2])
        return doc_bow

    def create_label_doc_map(self, label_file):
        label_doc_map = defaultdict(list)
        with open(label_file,'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                label_doc_map[int(line)].append(i+1)
        return label_doc_map

    def create_label_name_map(self, group_file):
        label_name_map = {}
        with open(group_file,'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                label_name_map[i+1] = line.strip()
        return label_name_map

    def find_average_similarity(self,groupA, groupB, sim_fun):
        sumscores = 0
        docsA = self.label_doc_map[groupA]
        docsB = self.label_doc_map[groupB]
        for idA in docsA:
            for idB in docsB:
                # print(idA,idB)
                sim = sim_fun(self.doc_bow[idA], self.doc_bow[idB])
                sumscores += sim
                # print(sim)

        return sumscores/(len(docsA)* len(docsB))
    def get_avg_sim_matrix(self, sim_fun):
        rows = []
        for l1 in self.label_doc_map.keys():
            print(l1)
            rows.append(
                [self.find_average_similarity(l1,l2, sim_fun) for l2 in self.label_doc_map.keys()] 
            )
        return np.array(rows)

def get_xy_forsim(x:Counter, y:Counter):
    # print(x,y)
    keys =  set(x.keys()).union(set(y.keys()))
    x = np.array([x[dim] for dim in keys])
    y = np.array([y[dim] for dim in keys])
    # print(x,y)
    return x,y
def jaccard(x:Counter, y:Counter):
    x,y = get_xy_forsim(x,y)#list of dims
    num = 0
    den = 0
    for xi,yi in zip(x,y):
        num += min(xi,yi)
        den += max(xi,yi)
    return num/den

def cosine(x:Counter, y:Counter):
    x,y = get_xy_forsim(x,y)#list of dims
    # print(x,y)
    num = sum([xi*yi for xi,yi in zip(x,y)])
    den = np.linalg.norm(x)* np.linalg.norm(y)
    return num/den

def l2(x:Counter, y:Counter):
    x,y = get_xy_forsim(x,y)#list of dims
    # print(x,y)
    return -np.sqrt(
        ((x-y)**2).sum()
    )

#b


if __name__ =='__main__':
    c = DocData('data50.csv', 'label.csv', 'groups.csv')
    # print(c.doc_bow.keys(), c.doc_bow[1])
    # print(c.label_doc_map)
    # print(c.label_name_map)

    assert jaccard(
        x = Counter({0:2}),
        y = Counter({0:1})
    ) ==0.5

    print(    cosine(
        x = Counter({0:2}),
        y = Counter({0:1})
    )) # should be near to 1

    print(    l2(
        x = Counter({0:2}),
        y = Counter({0:1})
    )) # should be near to -1

    #print(c.find_average_similarity(1,1, cosine))
    # c.find_average_similarity(1,1, cosine)
    print(c.get_avg_sim_matrix(cosine))
    # get_xy_forsim(c.doc_bow[5],c.doc_bow[44])

