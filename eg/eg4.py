#!/usr/bin/env python
# Author:zhangq
import copy

person = ["a",["s",100]]
p1 = list(person)
p2 = list(person)
p1[0] = "alex"
p1[-1][1] = 50
p1[-1][0] = "abs"


print(p1)
print(p2)

