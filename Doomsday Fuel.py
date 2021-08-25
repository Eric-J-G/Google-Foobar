import numpy as np 
def solution(m):

    n = []
    y = 0
    for r in range(len(m)):
        j = sum(m[y])

        if j != 0:
            n.append(j)

        y = y + 1

    lcm = (np.lcm.reduce(n))
    s1 = 0
    s2 = 0
    s3 = 0


    l = []
    for e in range(len(m) - 1):
        l.append(0)



    for i in m[0]:

        if i != 0:
            x = ([m[0].index(i)])[0]

            if sum(m[m[0].index(i)]) == 0:

                if x == 1:
                    
                    s1 = s1 + i
                    if sum(m[0]) != lcm:
                        s1 * (lcm / sum(m[0]))
                
                elif x == 2:
                    print(x)
                    
                    if sum(m[2]) != 0:
                        for w in m[2]:
                            if w != 0:
                                z = ([m[0].index(w)])[0]

                                if sum(m[m[0].index(w)]) == 0:
                                    
                    else:
                        s2 = s2 + i

                        if sum(m[0]) != lcm:
                            s2 = s2 * (lcm / sum(m[0]))

            '''else:

                for q in m[x]:

                    if q != 0:
   
                        if sum(m[m[x].index(q)]) == 0:

                            if x == 1:
                                
                                s1 = s1 + q
                                if sum(m[x]) != lcm:
                                    s1 * (lcm / sum(m[0]))
                            
                            elif x == 2:
                                s2 = s2 + q
                                
                                if sum(m[x]) != lcm:
                                    s2 = s2 * (lcm / sum(m[x]))'''

                            
    l[0] = int(s1)
    l[1] = int(s2)    
    l[3] = lcm
    print(l)

solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
