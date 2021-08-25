def solution(s):
    l = []
    for i in s:
        if i.isupper():
              l.append("000001")
        
        if " " in i:
          l.append("000000")
        i = i.lower()
        if 'a'in i:
          l.append('100000')
        if 'b' in i:
          l.append('110000')
        if 'c' in i:
          l.append('100100')
        if 'd' in i:
          l.append('100110')  
        if 'e' in i:
          l.append('100010')
        if 'f' in i:
          l.append('110100')  
        if 'g' in i:
          l.append('110110')
        if 'h' in i:
          l.append('110010')
        if 'i' in i:
          l.append('010100')
        if 'j' in i:
          l.append('010110')
        if 'k' in i:
          l.append('101000')
        if 'l' in i:
          l.append('111000')
        if 'm' in i:
          l.append('101100')
        if 'n' in i:
          l.append('101110')
        if 'o' in i:
          l.append('101010')
        if 'p' in i:
          l.append('111100')
        if 'q' in i:
          l.append('111110')
        if 'r' in i:
          l.append('111010')
        if 's' in i:
          l.append('011100')
        if 't' in i:
          l.append('011110')
        if 'u' in i:
          l.append('101001')
        if 'v' in i:
          l.append('111001')
        if 'w' in i:
          l.append('010111')
        if 'x' in i:
          l.append('101101')
        if 'y' in i:
          l.append('101111')
        if 'z' in i:
          l.append('101011')     
        
    print("".join(str(x) for x in l))
    
solution("The quick brown fox jumps over the lazy dog")