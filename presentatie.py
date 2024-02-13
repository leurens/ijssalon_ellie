def presenteer(dict, totaal):
    for key, value in dict.items():
        print(key, ":", value)
    print("==========================")
    print(f"totaal : {totaal} euro")

mijn_dict = {
    'vis' : 10, 
    'vlees': 25, 
    'overig' : 15
    }

totaal = 50
