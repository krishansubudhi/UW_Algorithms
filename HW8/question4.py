# from heatmap import makeHeatMap
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from collections import defaultdict, Counter

class SimilarityCalculator:
    def __init__(self,data_file, labels_file,group_file):
        self.doc_bow = self.create_doc_bow(data_file)#defaultdict(Counter)
        self.label_doc_map = self.create_label_doc_map(labels_file)
        self.label_name_map = self.create_label_name_map(group_file)
    
    def create_doc_bow(self,data_file):
        doc_bow = defaultdict(Counter)
        with open(data_file,'r') as f:
            lines = f.readlines()
            for line in lines[:1000]:#remove
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
    
if __name__ =='__main__':
    c = SimilarityCalculator('data50.csv', 'label.csv', 'groups.csv')
    print(c.doc_bow.keys(), c.doc_bow[1])
    print(c.label_doc_map)
    print(c.label_name_map)
