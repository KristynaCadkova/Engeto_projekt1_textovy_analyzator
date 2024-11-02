
'''
projekt_1_textovy_analyzator.py
author: Kristýna Čadková
email: kristyna.posingerova@seznam.cz
discord: kristyna_90682

'''

from collections import Counter

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

texty2 = (dict(enumerate(TEXTS,1))) 
oddelovac = "-" * 40

#seznam registrovanych uzivatelu:
users = {"u1": {"jmeno": "bob", "heslo": "123"},
         "u2": {"jmeno": "ann", "heslo": "pass123"},
         "u3": {"jmeno": "mike", "heslo": "password123"},
         "u4": {"jmeno": "liz", "heslo": "pass123"}}

#zadani uzivatele:
uzivatelske_jmeno = input("username: ").lower()
heslo = input("password: ").lower()

print(oddelovac)

#overeni uzivatele:
while True:
    for user, hodnoty in users.items():
        if hodnoty["jmeno"] == uzivatelske_jmeno and hodnoty["heslo"] == heslo:
            print(f"Welcome to the app, {uzivatelske_jmeno}\nWe have 3 texts to be analyzed.\n{oddelovac}")
            for klic, hodnota in texty2.items():
                print(f"Text number {klic}:")        #nabidne texty pro analyzu
                print(hodnota)
                print(oddelovac)  
            
            cislo = input("Enter a number btw. 1 and 3 to select:")
            print(oddelovac)

            #podminka pro vyber a analyza textu:
            if cislo.isdigit() and int(cislo) in range(1, 4):
                cislo = int(cislo)
                text_to_be_analyzed = (texty2[cislo].split())
                pocet_slov = (len(text_to_be_analyzed))

                pocet_velka_pismena = 0
                pocet_mala_pismena = 0
                pocet_cisel = 0
                pocet_titlecase = 0
                cislice = []
                delky_slov = []
         
                for slovo in text_to_be_analyzed:       
                    slovo_bez_interpunkce = slovo.strip(".,!?;:()[]\"'")
                    delky_slov.append(len(slovo_bez_interpunkce))  
                    if slovo[0].istitle():
                        pocet_titlecase += 1
                    if slovo.isupper() and slovo.isalpha():
                        pocet_velka_pismena += 1
                    if slovo.islower():
                        pocet_mala_pismena += 1
                    if slovo.isdigit():
                        pocet_cisel += 1
                        cislice.append(int(slovo))

                #vypis vysledku analyzy:

                print(f"There are {pocet_slov} words in the selected text."
                    f"\nThere are {pocet_titlecase} titlecase words."
                    f"\nThere are {pocet_velka_pismena} uppercase words."
                    f"\nThere are {pocet_mala_pismena} lowercase words."
                    f"\nThere are {pocet_cisel} numeric strings."
                    f"\nThe sum of all the numbers {sum(cislice)}.")
            
                #sloupcovy graf:

                pocitadlo = Counter(delky_slov)
                max_sirka = max(int(hodnota) for hodnota in pocitadlo.values())
                
                pocitadlo = sorted(pocitadlo.items())
    
                print(oddelovac)
                print("LEN|","OCURENCES".center(max_sirka),"|NR.".ljust(0))
                print(oddelovac) 
                for delka,pocet in sorted(pocitadlo):
                    pocitadlo = {delka:pocet}
                    print(f"{str(delka).rjust(3)}|{(pocet * '*').ljust(max_sirka+2)}|{pocet}")
            else: 
                print("invalid input, terminating the program..") #chybne zadani pro vyber textu
            exit()
         
    else:
        print("unregistred user, terminating the program..") #chybne zadani uzivatele
    break
        
    