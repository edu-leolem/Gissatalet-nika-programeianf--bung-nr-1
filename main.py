# gor ett gissas ett tal spel snalla...
print( "kåden är mycket fel och det är ett nytt tal varje gång som lycka tillll")
import random
while True: 
    i=0
    for i in range(1,2):
        x = random.randint(1,10)
        i = i+1
    a = int(input("vilket tal tror du att det är ?--> "))

    if a == x :
        print ( "du är fantastiks :D talet", f"{a}", "var korekt ")
        break 




