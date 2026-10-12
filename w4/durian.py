n = 0
wa = 0
while True:
    n = n + 1
    w = int(input('Please input Durian Weight: '))
    wa = wa + w
    if w == 0 :
        n = n - 1
        wa = wa / n
        break
    else:
        continue
print('Total of',n,'Durians')
print('average weight is',wa)