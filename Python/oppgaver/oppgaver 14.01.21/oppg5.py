#Terning
import random

Terning = "j"
t1 = 0
t2 = 0
ts = 0

while Terning == "j":
    t1= random.randint(1, 6) 
    t2= random.randint(1, 6) 
    ts = t1 + t2
    print("Terning 1 er",t1)
    print("Terning 2 er",t2)
    print("Sumen er",ts)
    Terning = input("Tril på nytt (j eller n)")
    

print ("Du ville ikkje meir, takk for no")