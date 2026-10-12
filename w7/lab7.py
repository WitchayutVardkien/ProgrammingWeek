temps = [[30, 32, 35, 34, 31, 38, 32],
         [28, 36, 31, 37, 35, 39, 31]]              

def summary(t):                    
    biggest = t[0][0]               
    smallest = t[0][0]
    total = 0
    i = 0
    while i < len(t):              
        j = 0                      
        while j < len(t[i]):       
            if t[i][j] > biggest:
                biggest = t[i][j]
            if t[i][j] < smallest:
                smallest = t[i][j]
            total = total + t[i][j]
            j = j + 1              
        i = i + 1
    avg = total / (len(t) * len(t[0]))
    return biggest, smallest, avg

big, small, avg = summary(temps)
print("max =", big, " min =", small, " avg =", avg)