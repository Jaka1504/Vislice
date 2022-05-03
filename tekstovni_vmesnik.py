
import model
SLIKICE = [
"""      



        
     
""",
"""      



        
      ________
""",
"""      
          
          
         
       |  
      _|______
""",
"""      
       |   
       |   
       |  
       |  
      _|______
""",
"""       _____
       |   
       |   
       |  
       |  
      _|______
""",
"""       _____
       |   |
       |   
       |  
       |  
      _|______
""",
"""       _____
       |   |
       |   o
       |  
       |  
      _|______
""",
"""       _____
       |   |
       |   o
       |   |
       |  
      _|______
""",
"""       _____
       |   |
       |   o
       |  /|
       |  
      _|______
""",
"""       _____
       |   |
       |   o
       |  /|\\
       |  
      _|______
""",
"""       _____
       |   |
       |   o
       |  /|\\
       |  / 
      _|______
""",
"""       _____
       |   |
       |   o
       |  /|\\
       |  / \\
      _|______
""",
]

def izpis_igre(igra: model.Igra):
    return f"""{igra.pravilni_del_gesla()}
{igra.nepravilni_ugibi()}
{SLIKICE[igra.stevilo_napak()]}
Dovoljenih napačnih ugibov še {model.STEVILO_DOVOLJENIH_NAPAK + 1 - igra.stevilo_napak()}."""


def izpis_zmage(igra: model.Igra):
    return f"Čestitke! Uganili ste geslo {igra.geslo}."


def izpis_poraza(igra: model.Igra):
    return f"Oh, ne! Izgubili ste. Pravilno gelso je bilo {igra.geslo}."


def zahtevaj_vnos():
    while True:
        crka = input("Vnesite črko: ")
        if len(crka) == 1:
            return crka
        else:
            print("Vnesli ste več kot eno črko! Poskusite ponovno.")


def pozeni_vmesnik():
    igra = model.nova_igra()
    print(izpis_igre(igra))
    while True:
        izid = igra.ugibaj(zahtevaj_vnos())
        print(izpis_igre(igra))
        if izid == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif izid == model.PORAZ:
            print(izpis_poraza(igra))
            break
    if input("Želite igrati ponovno? (DA / NE) ").upper() == "DA":
        pozeni_vmesnik()
