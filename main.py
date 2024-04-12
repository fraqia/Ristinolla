from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Ruudukko(GridLayout):
    
    def __init__(self):
        super().__init__()
        self.klikattu = 0

    def click(self, id):
        self.klikattu += 1
        if self.klikattu%2 == 0:
            self.ids[str(id)].text = "O"
        else:
            self.ids[str(id)].text = "X"
        if self.klikattu >3:
            self.onko_voitto()

    def onko_voitto(self):
        #rivi tsekkaus
        # self.rivi_tsekkaus()
        self.kolumni_tsekkaus()
        self.risti_tsekkaus()
        
    def rivi_tsekkaus(self):    
        list_X = "XXX"
        list_O = "OOO"
        memory = []
        for i in range(1,10):
                memory.append(self.ids[str(i)].text)
        print(memory)

        substrings = []
        for i in range(0,len(memory),3): 
            substring = memory[i:i+3]
            substring_str = "".join(substring).replace(' ', '')
            substrings.append(substring_str)

        print(substrings)
        if any(list_X in substring for substring in substrings):
            print('The end')
        elif any(list_O in substring for substring in substrings):
            print('The end')

    def kolumni_tsekkaus(self):
        list_X = "XXX"
        list_O = "OOO"
        memory = []
        for i in range(1,10):
                memory.append(self.ids[str(i)].text)
        print(f'muisti {memory}')
        memory2 = []
        i = 0
        while i < 3:
            memory2.append(memory[i])
            memory2.append(memory[i+3])
            memory2.append(memory[i+6])
            i+=1
        print(f'kolumni {memory2}')

        substrings = []
        for i in range(0,len(memory2),3): 
            substring = memory2[i:i+3]
            substring_str = "".join(substring).replace(' ', '')
            substrings.append(substring_str)

        if any(list_X in substring for substring in substrings):
            print('The end')
        elif any(list_O in substring for substring in substrings):
            print('The end')

    def risti_tsekkaus(self):
        

class Ristinolla(App): #pääohjelma, kv-file:myapp
    def build(self): # tätä kutsutaan, Ristinolla kutsutaan
        return Ruudukko()

if __name__=="__main__":

    Ristinolla().run() #run käynnistää ohjelman