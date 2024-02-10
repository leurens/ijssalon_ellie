def mijn_functie_1(getal):
    return getal * getal

def mijn_functie_2(getal1, getal2):
    som = getal1 + getal2
    aftrek = getal1 - getal2
    maal = getal1 * getal2
    deling = (int)(getal1 / getal2)
    return f"[{som}, {aftrek}, {maal}, {deling}]"

print(mijn_functie_2(100,20))