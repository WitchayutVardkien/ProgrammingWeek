#Save money program

target = 150         
money  = 0            
day    = 0            

while money < target:             
    day = day + 1                  

    if day % 7 == 0:              
        money = money + 50       
    else:
        money = money + 10        

    print("Days", day, "Money=", money)  

print("Target in days", day)