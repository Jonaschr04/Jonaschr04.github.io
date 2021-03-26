# Døme på lister med klassen
import random as r

klassen = ["Jonas", "Pijus", "Adrian", "Kristina", "Andreas"]

print (klassen)

klassen.append ("Faris")
klassen.append ("May linn")
klassen.append ("Henrik")
klassen.append ("Ignacio")

print (klassen)

print ("Antall elever er:", len(klassen))

print ("Dagens elev er", klassen[r.randrange(0, len(klassen))])

print ("Dagens bandit er", klassen[r.randrange(0, len(klassen))])