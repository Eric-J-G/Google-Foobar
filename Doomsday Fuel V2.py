import numpy as np
def solution(m):

    lvl0 = []
    lvl1 = []
    lvl2 = []
    lvl3 = []
    lvl4 = []
    sums = []

    odds1 = []
    odds2 = []
    odds3 = []
    odds4 = []

    x = 0
    while True:

        for i in m[x]:

            if i != 0:
                if x == 0:
                    lvl0.append(i)
                    lvl0.append(([m[x].index(i)])[0])

                if x == 1:
                    lvl1.append(i)
                    lvl1.append(([m[x].index(i)])[0])

                if x == 2:
                    lvl2.append(i)
                    lvl2.append(([m[x].index(i)])[0])

                if x == 3:
                    lvl3.append(i)
                    lvl3.append(([m[x].index(i)])[0])

                if x == 4:
                    lvl4.append(i)
                    lvl4.append(([m[x].index(i)])[0])
                
                #x = ([m[x].index(i)])[0]

        if x == 0:
            sums.append(sum(m[x]))

        if x == 1:
            sums.append(sum(m[x]))

        if x == 2:
            sums.append(sum(m[x]))

        if x == 3:
            sums.append(sum(m[x]))

        if x == 4:
            sums.append(sum(m[x]))

        x = x + 1
        if x >= len(m):
            break

    l = []
    x = lvl0
    for index, element in enumerate(x):
        top = 1
        bottom = 1
        l.clear()
        if index % 2 == 0:
            if x[index + 1] == 1:
                x = lvl1
                print(x)
                l.append(element)
                l.append(sums[0])
        
                for index, element in enumerate(x):
                    if index % 2 == 0:
                        x = lvl1
                        if x[index + 1] == 3:
                            x = lvl3
                            l.append(element)
                            l.append(sums[1])
                    
                            if sum(x) == 0:
                                top = 1
                                bottom = 1
                                for index, element in enumerate(l):
                                    if index % 2 == 0:
                                        top = top * element
                                    elif index % 2 != 0:
                                        bottom = bottom * element
                                odds3.append(top)
                                odds3.append(bottom)
                                print('run')
                                l.pop(len(l) - 1)
                                print(x)
                                l.pop(len(l) - 2)
                        
                        elif x[index + 1] == 4:
                            x = lvl4
                            l.append(element)
                            l.append(sums[1])
                    
                            if sum(x) == 0:
                                top = 1
                                bottom = 1
                                for index, element in enumerate(l):
                                    if index % 2 == 0:
                                        top = top * element
                                    elif index % 2 != 0:
                                        bottom = bottom * element
                                odds4.append(top)
                                odds4.append(bottom)
                        
                                l.clear()    
            

            elif x[index + 1] == 2:
                    x = lvl2
                    l.append(element)
                    l.append(sums[0])
        
                    if sum(x) == 0:
                                top = 1
                                bottom = 1
                                for index, element in enumerate(l):
                                    if index % 2 == 0:
                                        top = top * element
                                    elif index % 2 != 0:
                                        bottom = bottom * element
                                odds2.append(top)
                                odds2.append(bottom)
                    
                                l.clear()
                    
                    for index, element in enumerate(x):
        
                        if index % 2 == 0:
                
                            if x[index + 1] == 4:
                                x = lvl4
                                l.append(element)
                                l.append(sums[1])
                
                                if sum(x) == 0:
                                    for index, element in enumerate(l):
                                        if index % 2 == 0:
                                            top = top * element
                                        elif index % 2 != 0:
                                            bottom = bottom * element
                                    odds3.append(top)
                                    odds3.append(bottom)
                    
                                    l.clear()             



    denom = []
    denom.append(odds2[1])
    denom.append(odds3[1])
    denom.append(odds4[1])


    lcm = (np.lcm.reduce(denom))


    if int(odds2[1]) != lcm:
        odds2[0] = int(odds2[0] * (lcm / odds2[1]))

    final = []

    for d in odds2:
        if odds2.index(d) % 2 == 0:

            final.append(int(d))

    for d in odds3:
        if odds3.index(d) % 2 == 0:

            final.append(int(d))

    for d in odds4:
        if odds4.index(d) % 2 == 0:
            final.append(int(d))

    final.append(int(lcm))

    print(final)


solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])