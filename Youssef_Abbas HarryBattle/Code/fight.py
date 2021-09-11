'''
Author : youssef abbas 
Date   : 11/9/2021
About  : Hogwarts Fight

'''
from xml.dom import minidom
import os 
  
# take Data from  file
mf = open("spells.txt", "r+")
file_content = mf.readlines() # Read all lines in the file
file_content[-1] = file_content[-1]+'\n'
mf.close()


#this block of code to organize data in two dictionary harry and voldemart  
harry = {}      
voldemart = {}
for line in file_content:
    line = line.split(' ')
  
    if line[0] == 'A':
        harry[line[1]] = int(line[2][:-1])
        voldemart[line[1]] = int(line[2][:-1])
        
    elif line[0] == 'H':
        harry[line[1]] = int(line[2][:-1])

    elif line[0] == 'V':
        voldemart[line[1]] = int(line[2][:-1])

    else :
        continue           

#Class of Battle routine
class Battel:
    '''
    Battle between Harry And Voldmord
    '''
    def __init__(self):
        #Parameter of Harry
        self.h_health = 100
        self.h_energy = 500
        self.h_sheild = 3
        #Parameter of Voldmord
        self.v_health = 100
        self.v_energy = 500
        self.v_sheild = 3 

    
    def round(self,h_spell,v_spell):
        '''
        Round Cell 
        intput : take Harry spell and Voldmort spell
        output : Adjust attributes of Harry and Voldmort
        '''
        h_pow = harry[h_spell]
        v_pow = voldemart[v_spell] 

        if h_pow <= self.h_energy:
            self.h_energy = self.h_energy - h_pow
        else :
            h_pow = 0

        if v_pow <= self.v_energy:        
            self.v_energy = self.v_energy - v_pow
        else:
            v_pow = 0

        if h_spell == 'sheild' and v_spell != 'sheild':
            if self.h_sheild > 0 :
                self.h_sheild -= 1
            else : 
                self.h_health -= v_pow   

        elif v_spell == 'sheild' and h_spell != 'sheild':
            if self.v_sheild > 0:
                self.v_sheild -= 1
            else :
                self.v_healt -= h_pow

        elif h_pow > v_pow:
            self.v_health  -= (h_pow - v_pow)

        elif h_pow < v_pow:
            self.h_health -=  (v_pow - h_pow )   

        else:
            pass


    def display(self):
        '''
        Display parameter of Harry and voldmort
        '''
        print('\tHarry\tVoldmort')
        print('Health : %-3d \t     %-3d'%(self.h_health,self.v_health),sep = '')
        print('Energy : %-3d \t     %-3d'%(self.h_energy,self.v_energy),sep = '')
        print('Sheild : %-3d \t     %-3d'%(self.h_sheild,self.v_sheild),sep = '')
        
    def finish(self):
        '''
        Check if Battle is finished and who's Win
        '''
        #Harr Win
        if self.v_health <= 0 and self.h_health > 0:
            return 1 
        #Voldmord Win       
        elif self.v_health > 0 and self.h_health <= 0:
            return 2
        #Both Exhausted    
        elif self.v_health <= 0  and self.h_health <= 0:
            return -1
        #Still Fight    
        else : 
            return 0          


battle = Battel()
i = 1
print("Battle Gonna be started \n")        
while(True):
    print("----------------Round %d-------------"%i)
    #take input from user
    print("Spells : ")
    battle_input = input()
    battle_input = battle_input.split(' ')
    harry_move    = battle_input[0]
    voldmort_move = battle_input[1]

    #play round
    battle.round(harry_move,voldmort_move) 
    i += 1

    #check round dependencies 
    if  battle.finish() == 0 :
        battle.display()
    elif battle.finish() == 1:
        result = "HARR WIN"
        print("\n\tHARRY WIN")
        break
    elif battle.finish() == 2:
        result = "VOLDMORD WIN"
        print("\n\tVOLDMORT WIN")
        break       
    else:
        print("\n\tBoth Exhausted")

#Write output to XML file
root = minidom.Document()  
xml = root.createElement('root') 
root.appendChild(xml) 
productChild = root.createElement('product')
productChild.setAttribute('name', result)  
xml.appendChild(productChild)
xml_str = root.toprettyxml(indent ="\t") 
save_path_file = "output.xml"
  
with open(save_path_file, "w") as f:
    f.write(xml_str) 
