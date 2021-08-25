positive = []
negative = []
xs = [-4]


#In case xs only contains one number, and it's negative
if len(xs) == 1 and xs[0] < 0:
    print(str(xs[0]))

else:
    for i in xs:


        #sort numbers into seperate positive and negative lists
        if i == 0:
            continue 
        elif i > 0:
            positive.append(i)

        elif i < 0:
            negative.append(i)

    #Checking if there is an odd amount of negatives, and if there is getting rid of the smallest one
    if negative:
        negative.sort(reverse = True)
        if len(negative) % 2 != 0:

            negative.pop(0)
    new_negative = negative

    m = 0

    if positive:
        
            xpos = 1
            for e in positive:
                xpos = xpos * e
    
            xneg = 1
            for n in new_negative:
                xneg = xneg * n

            m = xneg * xpos

    print(str(m))