# liste over mine drøme motorsykler
import random as x

Sykkler =["Husqvarna 701 sm", "Husqvarna fs 450", "Yamaha mt07"]

print(*Sykkler)

Sykkler.append ("Ktm exc 500")
Sykkler.append ("Husqvarna fe 501")

print(*Sykkler)

print("Antall sykkler er", len(Sykkler))

print("Dagens beste sykkel er", Sykkler[x.randrange(0, len(Sykkler))])

print("Dagens verste sykkel er", Sykkler[x.randrange(0, len(Sykkler))])
