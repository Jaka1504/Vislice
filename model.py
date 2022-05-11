import random


STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = "+", "o", "-"
ZMAGA, PORAZ = "W", "X"
ZACETEK = "Z"


class Vislice:
    def __init__(self):
        self.igre = {}

    
    def prost_id_igre(self):
        return len(self.igre)

    
    def nova_igra(self):
        novo = nova_igra()
        id = self.prost_id_igre()
        self.igre.update({id: (novo, ZACETEK)})
        return id
        
    
    def ugibaj(self, id_igre, crka):
        igra = self.igre[id_igre][0]
        izid = igra.ugibaj(crka)
        self.igre.update({id_igre: (igra, izid)})


class Igra:
    def __init__(self, geslo, crke=[]) -> None:
        self.geslo = geslo.upper()
        self.crke = crke[:]

    
    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]


    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    
    def stevilo_napak(self):
        return len(self.napacne_crke())

    
    def zmaga(self):
        return len(set(self.geslo)) == len(self.pravilne_crke())


    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    
    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka
            else:
                niz += "_"
        return niz    
        # return "".join([(crka if crka in self.crke else "_") for crka in self.geslo])
    

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    
    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if crka in self.geslo:
                return ZMAGA if self.zmaga() else PRAVILNA_CRKA
            else:
                return PORAZ if self.poraz() else NAPACNA_CRKA


with open("besede.txt", "r", encoding="utf-8") as d:
    bazen_besed = d.read().split("\n")


def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)