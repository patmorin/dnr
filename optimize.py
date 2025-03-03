#!/usr/bin/python3
import numpy as np
import math

a = 2+1/6
b = 3

def bag_size1(t,d):
    return (2*t)+d+1

def bag_size2(t, d):
    return check(t,d) + d

def check(t, d):
    return 2*t*(2/3)**(d) + (b+1)*d

def optimal_t(d):
    return ((b+1)*d) / (1-a*(2/3)**(d))


# print("t(5) = {}".format(t(5)))

# find miminum t such that 2*t*(2/3)**(d-1) + 4*d <= t
a = [optimal_t(d) for d in range(20)]
mn = -1
for i in range(len(a)):
  if a[i] > 0 and (mn == -1 or a[i] < a[mn]):
      mn = i
# print(a)
print(mn, a[mn])

topt = a[mn]
print("Best (integer) solution: t = {}, h = {}, |B_x| = {}".format(topt, mn, check(topt, mn)))

for d in range(mn+1):
  print("Depth {}, |B_x| <= {}".format(d, min(bag_size1(topt,d), bag_size2(topt,d))))


# dopt = np.argmin(a)
#
# dopt =
#
# print(a)
# print(dopt+3, a[dopt])
# topt = math.ceil(a[dopt])
# print([min(tw1(topt,d), tw2(topt,d)) for d in range(dopt+4)])
