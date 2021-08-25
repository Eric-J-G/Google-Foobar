from fractions import Fraction
import numpy as np
from sympy import *

m = [
    [0, 1, 0, 0, 0, 1], 
    [4, 0, 0, 3, 2, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0]
    ]
m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]


order = list(range(len(m)))
sums = [sum(q) for q in m]
new = [q for _, q in sorted(zip(sums, m))]
new_order = [q for _, q in sorted(zip(sums, order))]

zeros = 0
final = [[0 for _ in new] for _ in new]
for q in range(len(new)):
    sum_ = sum(new[q])
    if sum_ == 0:
        zeros += 1
    for w in range(len(new[q])):
        if new[q][w] != 0:
            final[q][new_order.index(w)] = Fraction(new[q][w], sum_)

i = []
r = []
for q in range(len(final)):
    layer = []
    temp = []
    for w in range(len(final[q])):
        if q >= zeros:
            if w >= zeros:
                if q == w:
                    layer.append(final[q][w] + 1)
                else:
                    layer.append(-final[q][w])
            else:
                temp.append(final[q][w])
    if layer:
        i.append(layer)
    if temp:
        r.append(temp)

'''
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*r)] for X_row in i]

[1, 0, 0, 0,    0, 0]           [1, 0]  -   [0, 1/2]
[0, 1, 0, 0,    0, 0]           [0, 1]      [4/9, 0]
[0, 0, 1, 0,    0, 0]     
[0, 0, 0, 1,    0, 0] 
    
[0, 0, 0, 1,    0, 1]     
[0, 3, 2, 0,    4, 0]

from sympy import *
# other stuff 
integrate(8*x**Rational(6, 5) - 7*x**Rational(3, 2),x)

Matrix([[1, -1], [3, 4], [0, 2]])
'''

final_matrix = Matrix(i).inv() * Matrix(r)

answer = (np.array(final_matrix.row(0)))

q = []
for i in answer[0]:
    q.append(i)


solution = []
den = []
for i in range(len(q)):
    solution.append(Rational.as_numer_denom(q[i])[0])
    den.append(Rational.as_numer_denom(q[i])[1])

lcm = (np.lcm.reduce(den))

for index, i in enumerate(den):
    if i != lcm:
        solution[index] = solution[index] * (lcm / i)

solution.append(lcm)
solution = list(map(int, solution))
print(solution)
exit()


import numpy as np
from fractions import Fraction
#m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

cons = 1
if len(m) == 6:
    cons = 2


standard_matrix = []
standard = []
x = 0
for index, element in enumerate(m):
    if sum(element) == 0:
        if index + 1 == len(m):

            standard_matrix.append(-1 + cons)
        else:
            standard_matrix.append(index + cons)
        standard_matrix.append(element)
    
for index, element in enumerate(m):
    if sum(element) != 0:
        standard.append(element)
        standard_matrix.append(index + cons)
        standard_matrix.append(element)

for index, element in enumerate(standard_matrix):
    if type(element) != int:
        if sum(list(element)) == 0:
            element[x] = 1
            x += 1

permutation = []

for index, element in enumerate(standard_matrix):
    if index % 2 == 0:
        permutation.append(element)



for index, element in enumerate(permutation):
    if element == len(permutation):
        permutation[index] = 0

a = np.array(standard)

idx = np.empty_like(permutation)
idx[permutation] = np.arange(len(permutation))
a[:, idx]  # return a rearranged copy

a[:] = a[:, idx]  # in-place modification of a


# a = [[0 0 0 1 0 1] [0 3 2 0 4 0]]

a = list(a)

for i in a:
    s = sum(i)
    for index, element in enumerate(i):
        if element != 0:
            i[index] = Fraction(element, s)

for q in range(len(a)):
    a[q] = list(a[q])
print(list(a))

# a = [[0 0 0 0 0 0] [0 0 0 0 0 0]]
# What a should be: [[0, 0, 0, Fraction(1, 2), 0, Fraction(1, 2)], 
# [0, Fraction(1, 3), Fraction(2, 9), 0, Fraction(4, 9), 0]]

'''Q = []
R = []

column_length = len(a)
row_length = len(a[0])
for element in a:
    for r in range(column_length):
        element = list(element)
        element.pop(column_length + 1)
    R.append(element)

for element in a:
    for r in range(column_length + cons):
        element = list(element)
        element.pop(0)

    Q.append(element)

print(R)

I_ =[[], [], [], [], [], [], [], [], [], [], [], []]
x = 0
for index_1, element_1 in enumerate(Q):
    for index, element in enumerate(element_1):
        if index_1 == index:
            I_[x].append(1)
        else:
            I_[x].append(0)
    x += 1


I =[]
for element in I_:
    if sum(element) != 0:
        I.append(element)

print(I)
print(Q)

F = np.linalg.inv(np.subtract(I, Q))

print(F)

solution = []


result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*R)] for X_row in F]


print(result[0])'''