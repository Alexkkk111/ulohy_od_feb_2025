#systému pre správu knižničných zdrojov:
class Kniha:
    def __init__(self, nazov, autor, ISBN, rok_vydania, dostupna=True):
        self.nazov=nazov
        self.autor = autor
        self.ISBN = ISBN
        self.dostupna = dostupna
        self.rok_vydania = rok_vydania
    #def set_property(self, property, value):
        #self.property=value
    def vypozicaj(self):
        if self.dostupna==True:
            self.dostupna=False
        else:
            print('Tato kniha nie je teraz k dispozicii.')
    def vratit(self):
        self.dostupna=True
    def __str__(self):
        return f"Nazov: {self.nazov}, Autor: {self.autor}, ISBN: {self.ISBN}, dostupna: {self.dostupna}, rok: {self.rok_vydania}"

class Kniznica:
    def __init__(self, zoznam_knih=None):
        self.zoznam_knih=[] if zoznam_knih is None else zoznam_knih #tento riadok poradil Chat GPT, ale neviem presne preco
    def pridat_knihu(self, kniha):
        self.zoznam_knih.append(kniha)
    def zoznam_dostupnych_knih(self):
        print('Zoznam dostupnych knih:')
        for kniha in self.zoznam_knih:
            if kniha.dostupna==True:
                print(kniha)
    def vratit_knihu(self, ISBN):
        for kniha in self.zoznam_knih:
            if kniha.ISBN==ISBN:
                kniha.vratit()
    def vypozicat_knihu(self, ISBN):
        for kniha in self.zoznam_knih:
            if kniha.ISBN==ISBN:
                kniha.vypozicaj()
    def najdi_knihu(self, name):
        success=0
        for kniha in self.zoznam_knih:
            if kniha.nazov == name:
                success+=1
                print('Hladam knihu: ', name,' ...Nasiel som knihu:\n',kniha)
        if success==0:
            print('Hladam knihu ', name,'.....Kniha sa nenasla')

#vystupy:
kniha1=Kniha('Harry Potter', 'JK Rowling', '3567', 2001)
kniha2=Kniha('Lord of the Rings', 'JRR Tolkien', '3987', 1956)
kniha3=Kniha('Palenica', 'B Filan', '9283', 2009)

moja_kniznica=Kniznica()
moja_kniznica.pridat_knihu(kniha1)
moja_kniznica.pridat_knihu(kniha2)
moja_kniznica.pridat_knihu(kniha3)

print(kniha1)
print(kniha2)
print(kniha3)
print('-----')
moja_kniznica.zoznam_dostupnych_knih()
print('-----')
moja_kniznica.najdi_knihu('Harry Potter')
print('-----')
moja_kniznica.najdi_knihu('Winnetou')
print('-----')
moja_kniznica.vypozicat_knihu('3567')
print(kniha1)
moja_kniznica.vratit_knihu('3567')
print(kniha1)##
print('-----')
moja_kniznica.zoznam_dostupnych_knih()