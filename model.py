import random
import json
import time



velikost_plosce = 10

stevilo_ladij = 4

konec_igre = False

abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

datoteka_s_stanjem = 'stanje.json'



def odstotek(stevec, imenovalec):
    return round(int(stevec) / int(imenovalec) * 100)


class Igra():

    def __init__(self, plosca=[], pozicija_ladij=[], st_preostalih_strelov=40, st_potopljenih_ladij=0,
        cas=time.time(), zadnji_strel=None, st_zadetih_strelov=0, natancnost=0, stanje=None):
        self.plosca = plosca
        self.pozicija_ladij = pozicija_ladij
        self.st_preostalih_strelov = st_preostalih_strelov
        self.st_potopljenih_ladij = st_potopljenih_ladij
        self.cas = cas
        self.zadnji_strel = zadnji_strel
        self.st_zadetih_strelov = st_zadetih_strelov
        self.natancnost = natancnost
        self.stanje = stanje




    def ustvari_plosco(self):
        # Ustvari 10x10 plosco in nakljucno postavi 
        # lajde razlicnih velikosti v razlicne smeri

        for vrstica in range(velikost_plosce):
            vrstica = []
            for stolpec in range(velikost_plosce):
                vrstica.append('.')
            self.plosca.append(vrstica)

        stevilo_postavljenih_ladij = 0

        indeks = 0
        while stevilo_postavljenih_ladij != stevilo_ladij:
            nakljucna_vrstica = random.randint(0, velikost_plosce - 1)
            nakljucni_stolpec = random.randint(0, velikost_plosce - 1)
            smer = random.choice(['levo', 'desno', 'gor', 'dol'])
            velikost_ladje = [2, 3, 4, 5]
            if self.poskusi_postavit_ladjo(nakljucna_vrstica, nakljucni_stolpec, smer, velikost_ladje[indeks]):
                stevilo_postavljenih_ladij += 1
                indeks += 1 
                   

    def izpisi_plosco(self):
        # Izpise plosco z vrsticami A-J in stolpci 0-9
        global abeceda
        debug_mode = True
        abeceda = 'ABCDEFGHIJKLMNOP'
        #abeceda = abeceda[0: len(self.plosca) + 1]
        x = ''
        y = []

        for vrstica in range(len(self.plosca)):
            vrst = []
            x += str(abeceda[vrstica])
            vrst.append(abeceda[vrstica])
            for stolpec in range(len(self.plosca[vrstica])):
                if self.plosca[vrstica][stolpec] == 'O':
                    if debug_mode:
                        x += '.'
                        vrst.append('.')
                    else:
                        vrst.append('.')
                        x += '.'
                else:
                    vrst.append(str(self.plosca[vrstica][stolpec]))
                    x += str(self.plosca[vrstica][stolpec])

            x += ' , ' 
            y.append(vrst)

        x += '  '

        st = ['/']
        for i in range(len(self.plosca[0])):
            x+= str(i)
            st.append(str(i))
        y.append(st)
        return y

    def izstreli_strel(self, ugib):
        if self.sprejmi_veljavni_strel(ugib):
            lokacija = ugib.upper()
            vrstica = abeceda.find(lokacija[0])
            stolpec = int(lokacija[1])
            print("")
            print("----------------------------")

            if self.plosca[vrstica][stolpec] == ".":
                print("Zgresen strel, nobena ladja ni bila zadeta")
                self.plosca[vrstica][stolpec] = "#"
            elif self.plosca[vrstica][stolpec] == "O":
                print("Zadetek!", end=" ")
                self.plosca[vrstica][stolpec] = "X"
                self.st_zadetih_strelov += 1
                if self.preveri_potopljeno_ladjo(vrstica, stolpec):
                    print("Ladja je potopljena!")
                    self.st_potopljenih_ladij += 1
                else:
                    print("Ladja je bila zadeta!")

            self.st_preostalih_strelov -= 1
            self.zadnji_strel = ugib
            st_strelov = 40 - int(self.st_preostalih_strelov)
            self.natancnost = odstotek(self.st_zadetih_strelov, st_strelov)
            
        else:
            return None


    def izpisi_strel(self):
        if self.zadnji_strel != None:
            strel = self.zadnji_strel.upper()
            vrstica = abeceda.find(strel[0])
            stolpec = int(strel[1]) 
            if self.plosca[vrstica][stolpec] == '#':
                return "Zgrešen strel, nobena ladja ni bila zadeta!"
            elif self.plosca[vrstica][stolpec] == 'X':
                if self.preveri_potopljeno_ladjo(vrstica, stolpec):
                    return 'Zadetek, ladja je potopljena!'
                else:
                    return 'Zadetek, ladja je bila zadeta!'      
        else:
            return ''


    def preveri_plosco_in_postavi_ladjo(self, zacetna_vrst, koncna_vrst, zacetni_stol, koncni_stol, smer, dolzina):
        # Preveri, ce lahko tam postavi ladjo 
        vse_velja = True

        if smer == 'levo' or smer == 'desno':

            for vrstica in range(zacetna_vrst, koncna_vrst+1):
                for stolpec in range(zacetni_stol, koncni_stol):
                    if self.plosca[vrstica][stolpec] != '.': 
                        vse_velja = False   
                        break
        if smer == 'dol' or smer == 'gor':
            for vrstica in range(zacetna_vrst, koncna_vrst):
                for stolpec in range(zacetni_stol, koncni_stol+1):
                    if self.plosca[vrstica][stolpec] != '.': 
                        vse_velja = False
                        break

        if vse_velja:
            if smer == 'dol' or smer == 'gor':
                self.pozicija_ladij.append([zacetna_vrst, koncna_vrst-1, zacetni_stol, koncni_stol])
                for vrstica in range(zacetna_vrst, koncna_vrst):
                    for stolpec in range(zacetni_stol, koncni_stol+1):
                        self.plosca[vrstica][stolpec] = 'O'
            elif smer == 'levo' or smer == 'desno':               
                self.pozicija_ladij.append([zacetna_vrst, koncna_vrst, zacetni_stol, koncni_stol-1])
                for vrstica in range(zacetna_vrst, koncna_vrst+1):
                    for stolpec in range(zacetni_stol, koncni_stol):
                        self.plosca[vrstica][stolpec] = 'O'

        return vse_velja


    def poskusi_postavit_ladjo(self, vrstica, stolpec, smer, dolzina):
        # Glede na smer poskusi postavit ladjo
        global velikost_plosce

        # Definiramo zato, da se premikamo samo po eni vrstici/stolpci naenkrat
        zacetna_vrstica, koncna_vrstica, zacetni_stolpec, koncni_stolpec = vrstica, vrstica +1, stolpec, stolpec +1

        if smer == 'levo':
            if stolpec - dolzina < 0:
                return False
            zacetni_stolpec = stolpec - dolzina +1

            koncna_vrstica = vrstica

        elif smer == 'desno':
            if stolpec + dolzina >= velikost_plosce:
                return False
            koncni_stolpec = stolpec + dolzina 
        
            koncna_vrstica = vrstica
        elif smer == 'gor':
            if vrstica - dolzina < 0:
                return False
            zacetna_vrstica = vrstica - dolzina +1 
            koncni_stolpec = stolpec
        elif smer == 'dol':
            koncna_vrstica = vrstica + dolzina
            koncni_stolpec = stolpec
            if vrstica + dolzina >= velikost_plosce:
                return False
        return self.preveri_plosco_in_postavi_ladjo(zacetna_vrstica, koncna_vrstica, zacetni_stolpec, koncni_stolpec, smer, dolzina)



    def preveri_potopljeno_ladjo(self, vrstica, stolpec):
        # Preveri, ce so vsi deli ladje zadeti
        for pozicija in self.pozicija_ladij:
            zacetna_vrstica = pozicija[0]
            koncna_vrstica = pozicija[1]
            zacetni_stolpec = pozicija[2]
            koncni_stolpec = pozicija[3]
            if zacetna_vrstica <= vrstica <= koncna_vrstica and zacetni_stolpec <= stolpec <= koncni_stolpec:
                # Ladja najdena, preveri ce je potopljena
                if zacetni_stolpec == koncni_stolpec:
                    for vrst in range(zacetna_vrstica, koncna_vrstica+1):
                        if self.plosca[vrst][zacetni_stolpec] != 'X':
                            return False
                if zacetna_vrstica == koncna_vrstica:
                    for stolp in range(zacetni_stolpec, koncni_stolpec+1):
                        if self.plosca[zacetna_vrstica][stolp] != 'X':
                            return False
        return True



    def sprejmi_veljavni_strel(self, lokacija):
        # Pridobi veljavno vrstico in stolpec za strel
        je_veljavno = False
        vrstica = -1
        stolpec = -1
        #lokacija = input('Vnesi vrstico (A-J) in stolpec (0-9), primer B4: ')
        lokacija = str(lokacija).upper()
        while not je_veljavno:
            if len(lokacija) != 2:
                print('Napaka: Vnesi eno vrstico in en stolpec kot B4') 
                return False
            vrstica = lokacija[0]
            stolpec = lokacija[1]

            if not vrstica.isalpha() or not stolpec.isnumeric():
                print('Napaka: Vnesi crko (A-J) za vrstico in stevilko (0-9) za stolpec ')
                return je_veljavno
            vrstica = abeceda.find(vrstica)

            if not (-1 < vrstica < velikost_plosce):
                print('Napaka: Vnesi crko (A-J) za vrstico in stevilko (0-9) za stolpec ')
                return je_veljavno
            stolpec = int(stolpec)

            if not (-1 < stolpec < velikost_plosce):
                print('Napaka: Vnesi crko (A-J) za vrstico in stevilko (0-9) za stolpec ')
                return je_veljavno

            if self.plosca[vrstica][stolpec] == '#' or self.plosca[vrstica][stolpec] == 'X':
                print('Na to pozicijo je ze bil ustreljen strel, izberi drugo pozicijo')
                return je_veljavno

            if self.plosca[vrstica][stolpec] == '.' or self.plosca[vrstica][stolpec] == 'O':
                je_veljavno = True
        return je_veljavno



    def preveri_konec_igre(self):
        # Ali so potopljene vse ladje, ali nam je zmanjkalo strelov
        L = 'Poraz'
        W = 'Zmaga'

        if self.st_potopljenih_ladij == stevilo_ladij:
            print('Cestitke, zmagali ste!')
            Z = 'Zmaga'
            self.stanje = W
            print(self.stanje)
            return Z          
        elif self.st_preostalih_strelov <= 0:
            print('Zal ste izgubili! Zmanjkalo vam je strelov')
            P1 = 'Poraz1'
            self.stanje = L
            return P1
        elif int(time.time()) - int(self.cas) > 180:
            print('Zal ste izgubili, zmanjkalo vam je casa')
            P2 = 'Poraz2'
            self.stanje = L
            return P2
        return False

def nova_igra():
    igra = Igra([],[],40,0, time.time(), None,0,None)
    igra.ustvari_plosco()
    igra.izpisi_plosco()
    return igra

class Potapljanje_ladjic:

    def __init__(self, datoteka_s_stanjem, statistika={}):
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.statistika = statistika

    
    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
    
    def ugibaj(self, id_igre, ugib):
        self.nalozi_igre_iz_datoteke()
        igra = self.igre[id_igre]
        igra.preveri_konec_igre()
        igra.izstreli_strel(ugib)
        self.igre[id_igre] = (igra)
        self.zapisi_igre_v_datoteko()


    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as f:
            igre = json.load(f)
            print(igre)
            for id_igre in igre.keys():
                plosca, pozicija_ladij, st_preostalih_strelov, st_potopljenih_ladij, zacetni_cas, zadnji_strel, st_zadetih_strelov, natancost, stanje = self.preberi_podatke(igre, id_igre)
                self.igre.update({int(id_igre[0]):
                 Igra(plosca,pozicija_ladij, st_preostalih_strelov, st_potopljenih_ladij, zacetni_cas, zadnji_strel, st_zadetih_strelov, natancost, stanje)})
            print(self.igre)

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f:
            igre = {id_igre: (igra.__dict__) 
                        for id_igre, igra in self.igre.items()}
            json.dump(igre, f)


    def preberi_podatke(self, datoteka, id_igre):

        podatki_igre = datoteka.get(str(id_igre))
        plosca = podatki_igre.get('plosca')
        pozicija_ladij = podatki_igre.get('pozicija_ladij')
        st_preostalih_strelov = podatki_igre.get('st_preostalih_strelov')
        st_potopljenih_ladij = podatki_igre.get('st_potopljenih_ladij')
        zacetni_cas = podatki_igre.get('cas')
        zadnji_strel = podatki_igre.get('zadnji_strel')
        st_zadetih_strelov = podatki_igre.get('st_zadetih_strelov')
        natancnost = podatki_igre.get('natancnost')
        stanje = podatki_igre.get('stanje')
        return plosca, pozicija_ladij, st_preostalih_strelov, st_potopljenih_ladij, zacetni_cas, zadnji_strel, st_zadetih_strelov, natancnost, stanje

    def nova_igra(self):
        #se enkrat zapisemo, da se zapisa zmaga ali poraz
        self.zapisi_igre_v_datoteko()
        print(napisi_statistiko(self.datoteka_s_stanjem))
        self.nalozi_igre_iz_datoteke()
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = (igra)
        self.zapisi_igre_v_datoteko()
        return id_igre


def napisi_statistiko(datoteka):
    statistika = {}
    st_zmag = 0
    natancnost_iger = []
    st_strelov = 0
    st_zadetih_strelov = 0
    with open(datoteka, 'r', encoding='utf-8') as f:
        igre = json.load(f)
        st_iger = len(igre.keys())
        for id_igre in igre.keys():
            stanje = igre[id_igre].get('stanje')
            natancnost = igre[id_igre].get('natancnost')
            st_strelov_v_igri = 40 - int(igre[id_igre].get('st_preostalih_strelov'))
            st_strelov += st_strelov_v_igri
            st_zadetih_strelov += int(igre[id_igre].get('st_zadetih_strelov'))
            if natancnost != None and stanje != None:
                natancnost_iger.append(int(natancnost))
            if stanje == 'Zmaga':
                st_zmag += 1

       #Ne deli z 0 
    print(natancnost_iger)  
    statistika['Odstotek zmag'] = 0
    statistika['Stevilo iger'] = st_iger
    statistika['Stevilo strelov'] = st_strelov  
    statistika['Stevilo zadetih strelov'] = st_zadetih_strelov
    statistika['Najboljsa natancnost igre'] = 0  
    if len(igre.keys()) != 0:
        statistika['Odstotek zmag'] = odstotek(st_zmag, st_iger)
        if len(natancnost_iger) != 0:
            statistika['Najboljsa natancnost igre'] = max(natancnost_iger)
    return statistika
nova_igra()