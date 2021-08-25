positive = []
negative = []
xs = []
for i in xs:


    if i == 0:
        continue 
    elif i > 0:
        positive.append(i)

    elif i < 0:
        negative.append(i)

if not negative:
    a = 0
else:
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