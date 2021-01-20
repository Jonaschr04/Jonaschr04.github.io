# 
import random

x = "j"

print("Du har 3 forsøk på å få 50")
print("Får du 50 vinner du, premien(Beste elev i klassen)")

while x == "j":
    x = input("Vil du ha eit nytt tal(j eller n)")
    print(random.randint(1, 100))

print("Takk for at du spilte.")
