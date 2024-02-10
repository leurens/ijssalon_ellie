from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    totaal = prijs - (prijs*korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {totaal} euro."

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    bedrag = 0
    for i in inkomsten:
        totaal = totaal + i
        bedrag = totaal * (btw / 100)
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 9))

def laag_en_hoog(mijn_lijst):
    hoog = 0
    laag = 0
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    return f"[{hoog}, {laag}]"
    
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    avg = totaal / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {avg} euro."
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    return korte_lijst

print(combinatie([220, 430, 125, 160, 205, 90, 345]))