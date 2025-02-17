class LinkedList:
    def __init__(self):
        self.head = None

    def vloz_prvok(self, prvok):
        if self.head == None:
            self.head = prvok
        else:
            aktualny = self.head
            while aktualny.dalsi_prvok != None:
                aktualny = aktualny.dalsi_prvok
            aktualny.dalsi_prvok = prvok

    def vymaz_prvok(self, target):
        if not self.head:  # Case: Empty list
            return

        # Case: If head contains the target value
        if self.head.data == target:
            self.head = self.head.dalsi_prvok
            return

        # Traverse to find the node before the one to delete
        current = self.head
        while current.dalsi_prvok and current.dalsi_prvok.data != target:
            current = current.dalsi_prvok

        # If found, remove the node
        if current.dalsi_prvok:
            current.dalsi_prvok = current.dalsi_prvok.dalsi_prvok

    def vypis_vsetky(self):
        aktualny = self.head
        while aktualny.dalsi_prvok != None:
            print(aktualny.data)
            aktualny = aktualny.dalsi_prvok

        print(aktualny.data)

    def najdi_prvok(self, target):
        aktualny = self.head
        count=0
        found=False
        while aktualny.dalsi_prvok != None:
            count+=1
            if aktualny.data==target:
                print('Prvok najdeny na pozicii ', count)
                found=True
                break
            else:
                aktualny = aktualny.dalsi_prvok
        if aktualny.data == target and found!=True:
            print('Prvok najdeny na pozicii ', count+1)

class Prvok:
    def __init__(self, data):
        self.data = data
        self.dalsi_prvok = None

moj_zoznam=LinkedList()
while True:
    x=input('Enter an integer, when done, enter x:')
    if x == 'x':
        break
    else:
        entry=Prvok(int(x))
        moj_zoznam.vloz_prvok(entry)
moj_zoznam.vypis_vsetky()

def show_menu():
    print('What would you like to do next?')
    print("1. Add an item to the list")
    print("2. Delete an item from the list")
    print("3. Show the list contents")
    print("4. Check if the list contains this value")
    print("5. Replace a value in the list")
    print("6. Exit")

while True:
    show_menu()
    choice = int(input("Choose your option: "))
    if choice == 1:
        x = int(input('Enter an integer:'))
        moj_zoznam.vloz_prvok(Prvok(x))
    if choice == 2:
        x=int(input('Ktory prvok treba vymazat?:'))
        moj_zoznam.vymaz_prvok(x)
    if choice == 3:
        print('zoznam prvkov je nasledovny:')
        moj_zoznam.vypis_vsetky()
    if choice == 4:
        x=int(input('aku hodnotu chces overit, ci sa nachadza v zozname?:'))
        moj_zoznam.najdi_prvok(x)
    if choice == 6:
        break

