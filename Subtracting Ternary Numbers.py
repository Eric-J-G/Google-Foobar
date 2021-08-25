def subtracting_ternary_num():
    n = '210022'
    b = 3
    ascend = []
    descend = []

    ascending = "".join(sorted(str(n)))
    descending = "".join(sorted(str(n), reverse=True))

    for i in ascending:
        ascend.append(i)

    for j in descending:
        descend.append(j)

    print(descend)
    print(ascend)
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
            print(q)
            c.append(q)
    c.reverse()
    strings = [str(integer) for integer in c]
    a_string = "".join(strings)
    an_integer = int(a_string)
    print(an_integer)
    return an_integer

subtracting_ternary_num()