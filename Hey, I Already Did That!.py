def solution(n, b):
    
    l = []
    k = len(str(n))
    if b == 10:
        k = len(str(n))

        l.append(str(n))
        for m in range(8):
            ascending = "".join(sorted(str(n)))

            descending = "".join(sorted(str(n), reverse=True))

            n = int(descending) - int(ascending)


            if len(str(n)) != k:
                n = str(n).zfill(k)
            
            
            if str(n) in l:

                a = l.index(str(n))
                for i in range(a):
                    l.pop(0)
                
                
                return len(l)

            else:
                l.append(str(n))

    else:

        l.append(str(n))
        for m in range(8):
            ascending = "".join(sorted(str(n)))

            descending = "".join(sorted(str(n), reverse=True))
        
            ascend = []
            descend = []


            for i in ascending:
                ascend.append(i)

            for j in descending:
                descend.append(j)

            x = len(ascend) - 1
            h = 0
            c = []
            while h < len(ascend):

                top = int(descend[x])
                bottom  = int(ascend[x])

                q = top - bottom
                if q < 0:
                    
                    if descend[x - 1] == 0:
                        descend[x - 2] = int(descend[x - 2]) - 1
                        descend[x - 1] = int(descend[x - 1]) + b

                    descend[x - 1] = int(descend[x - 1]) - 1
                    descend[x] = int(descend[x]) + b

                else:
                    x = x - 1
                    h = h + 1

                    c.append(q)
            c.reverse()
            strings = [str(integer) for integer in c]
            a_string = "".join(strings)
            n= int(a_string)



            if len(str(n)) != k:
                n = str(n).zfill(k)
            
            
            if str(n) in l:

                a = l.index(str(n))
                for i in range(a):
                    l.pop(0)
                
                print(len(l))
                return len(l)

            else:
                l.append(str(n))

solution()
