#!/usr/bin/python3
import numpy as np
import math
from fractions import Fraction

a = 2 + Fraction(1,6)
b = 3

def bag_size1(t,d):
    return (2*t)+d+1

def bag_size2(t, d):
    return check(t,d) + 1

def check(t, d):
    return a*t*Fraction(2,3)**(d) + (b+1)*d

def optimal_t(d):
    return ((b+1)*d) / (1-a*Fraction(2,3)**(d))


# print("t(5) = {}".format(t(5)))

# find miminum t such that 2*t*(2/3)**(d-1) + 4*d <= t
q = [optimal_t(d) for d in range(20)]
h = -1
for i in range(len(q)):
  if q[i] > 0 and (h == -1 or q[i] < q[h]):
      h = i
# print(a)
t = q[h]
print("h = {}, t = {} ≈ {:.40f}".format(h, t, t))

for d in range(h+1):
  bag_size = min(bag_size1(t,d), bag_size2(t,d))
  print("Depth {}, |B_x| <= {} ≈ {:.40f}".format(d, bag_size, bag_size))


# dopt = np.argmin(a)
#
# dopt =
#
# print(a)
# print(dopt+3, a[dopt])
# topt = math.ceil(a[dopt])
# print([min(tw1(topt,d), tw2(topt,d)) for d in range(dopt+4)])
