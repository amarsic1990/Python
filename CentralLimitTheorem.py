from math import sqrt
import random
import matplotlib.pyplot as plt


def mean(data):
	return sum(data) / len(data)


def median(data):
    sdata = sorted(data)
    return sdata[(len(data) - 1) / 2]


def mode(data):
    count = 0
    for i in range(len(data)):
        if data.count(data[i]) > count:
            number = data[i]
            count = data.count(data[i])
    return number


def variance(data):
    ndata = []
    for i in range(len(data)):
        ndata.append((data[i]-mean(data))**2)
    return 1.0 / len(data) * sum(ndata)


def stddev(data):
    return sqrt(variance(data))


def flip(N):
    flips = []
    for i in range(N):
        flips.append(random.random()>0.5)
    return flips


def flip1(N):
    return [random.random() > 0.5 for i in range(N) ]


def sample(N):
    return [mean(flip1(N)) for i in range(N)]


outcomes = sample(1000)
plt.hist(outcomes, bins = 30)
plt.show()
