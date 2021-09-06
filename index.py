import math
import numpy as np




def Shannon_index(dataset):
    data = []
    j = sum(dataset)
    for i in dataset:
        p = i/j
        item = math.log(p) * p
        data.append(round(item, 3))
    return data

if __name__ == '__main__':
    dataset = np.genfromtxt('example.csv', delimiter=',')
    dataset = dataset[~np.isnan(dataset)]
    Shannon_index(dataset)