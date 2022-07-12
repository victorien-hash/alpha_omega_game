from telnetlib import IAC
from time import *
from blessed import Terminal
term = Terminal()
from remote_play import*
import random


def Data_Structures(path):

    """This function generates our data structures
    
    Parameters
    ---------
    path: path to our .ano file which allows us to obtain our structures


    Return
    -------
    team: the dictionary contains all the data relating to the wolves of the different teams (dict)

    foods: the dictionary contains all the data relating to the resources (dict)

    row: the number of rows on our board (int)

    col:the number of columns of our tray (int)
    
    version
    -------  
    
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implimentation : victorien fotso (v.1 22/02/2022 v.2 v.3 13/03/2022)

    """

    team={}
    foods={}

    file = open (path,"r").readlines()

    element= str.split(file[1].rstrip("\n"), " ") 
    row=element[0]  
    col=element[1]

    for line in file[3:21]:  
        element =str.split(line.rstrip("\n"), " ")
        team[int(element[1]), int(element[2])]=[int(element[0]),element[3],100,False]

    for line in file[22:len(file)]:
        element=str.split(line.rstrip("\n"), " ")
        foods[int(element[0]), int(element[1])]=[element[2],int(element[3])]
    
    return team, foods , row, col

def Board (team,foods,row,col): 

    """this function displays our board which corresponds to the data structures
    
    Parameters
    ----------
    team: it is the data structure that contains the data relating to the different teams (dict)
    
    foods: it is the data structure that contains the data relating to the different resources (dict)

    row : the number of lines that our board must have (int)

    col: the number of colomuns that our board must have (int)


    version
    -------

    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implementation :(v.1 22/02/2022 v.2 24/03/2022)
    """

    food={"berries":'🍇',"apples":  '🍎',"mices": '🐁' , "rabbits":'🐇',"deers":'🦌'}   

    for i in range(1,(row+1)):
        ecart=0
        for j in range(1,(col*2),2):
            
            if((i,j-ecart) in team ):

                if (team[i,j-ecart][0]==1):
                    if ( team[i,j-ecart][3]==False ):
                        if(team[i,j-ecart][1]=="omega"  ):
                            print(term.move_yx(i, (j)) +term.on_color_rgb(red=100,green=20,blue=250) +  '🦊'  + term.normal, end='', flush=True)
                        elif (team[i,j-ecart][1]=="alpha"):
                            print(term.move_yx(i, (j)) +term.on_color_rgb(red=10,green=250,blue=100) +  '🦊'  + term.normal, end='', flush=True)    
                        else:
                            print(term.move_yx(i, (j)) +term.on_color_rgb(red=100,green=20,blue=12) +  '🦊'  + term.normal, end='', flush=True)    
                    else:
                        print(term.move_yx(i, (j)) +term.on_color_rgb(red=100,green=20,blue=12) +  '👨'  + term.normal, end='', flush=True)

                elif (team[i,j-ecart][0]==2):
                    if ( team[i,j-ecart][3]==False ):
                        if(team[i,j-ecart][1]=="omega"):
                            print(term.move_yx(i, (j)) +term.on_color_rgb(red=100,green=20,blue=250) +  '🐺'  + term.normal, end='', flush=True)
                        elif (team[i,j-ecart][1]=="alpha"):
                            print(term.move_yx(i, (j)) +term.on_color_rgb(red=10,green=250,blue=100) +  '🐺'  + term.normal, end='', flush=True)
                        else:
                            print(term.move_yx(i, (j)) +term.on_color_rgb(red=10,green=20,blue=12) +  '🐺'  + term.normal, end='', flush=True)   
                    else:
                        print(term.move_yx(i, (j)) +term.on_color_rgb(red=100,green=20,blue=12) +  '👨'  + term.normal, end='', flush=True)

            elif ((i,j-ecart) in foods):
                for cle, valeur in food.items():
                    if(foods[i,j-ecart][0]==cle):
                        print(term.move_yx(i, (j)) +term.on_color_rgb(red=100,green=20,blue=12) +  valeur  + term.normal, end='', flush=True)
                
            else:
                print(term.move_yx(i, (j)) + term.on_color_rgb(red=98,green=98,blue=98) +  '🔲' + term.normal, end='', flush=True) 
            
            ecart=ecart+1

    print(term.move_yx(2,100) + "----ETATS DES ENERGIES-----")

    cmpt=3
    for cle in team:
        print(term.move_yx(cmpt,100) + "energy"+' '+ str(team[cle][2]) +' '+ str(team[cle][1])+' --> '+ str(cle[0]), str(cle[1])+' ')
        cmpt+=1

def Position_In_Board(position_x_1,position_y_1,position_x_2,position_y_2,row,col,team,player_equipe):

    """check if the coordinates of an order are in the tray
    
    Parameters
    ----------
    position_x_1: line number of the first element(int)

    position_y_1: column number of the first element (int)

    position_x_2: line number of the second element (int)

    position_y_1: column number of the second element (int)

    team: it is the data structure that contains the data relating to the different teams (dict)
    
    foods: it is the data structure that contains the data relating to the different resources (dict)

    row : the number of lines that our board must have (int)

    col: the number of colomuns that our board must have (int)

    player_equipe: player's team number(int)

    Return
    -------
    True or False (bool)

    version
    -------
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implimentation : keteb dehbia (v.1 22/02/2022 v.2 13/03/2022)
    """

    if (1<=position_x_1<=row) and (1<=position_x_2<=row)and (1<=position_y_1<=col) and (1<=position_y_2<=col) and ((position_x_1,position_y_1) in team) and (team[position_x_1,position_y_1][0]==player_equipe) :
        return True
    else:
        return False

def Test_Single_Order_Wolf (dictionnary_ordre,position):

    """verify that a wolf receives a single order
    
    Parameters
    ----------

    dictionnary_ordre: dictionnary of coordinates of wolves having received orders(dict)

    position: position of the wolf (list)

    Return
    -------
    True or False (bool)

    version
    -------
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implimentation : Loïc Franck KAMGAIN, keteb dehbia( V.1 22/02/2022 v.2 13/03/2022)
    """

    for valeur in dictionnary_ordre.values():
        if valeur!=[]:
            for j in valeur :
                if([j[0][0],j[0][1]] ==position): 
                    return True
                
    return False

def Sort_Orders (Ordre, row, col,type_player,team,equipe_palyer):

    """filter and classify the orders received
    
    Parameters
    ----------
    Ordre: liste des ordres (string)

    row : the number of lines that our board must have (int)

    col: the number of colomuns that our board must have (int)

    type_player: type of the player (string)

    team: it is the data structure that contains the data relating to the different teams (dict)

    equipe_player: player's team number(int)

    Return
    -------
    dic_ordres: dictionnary of sorted and filtred orders (dict)

    version
    -------
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implimentation : keteb dehbia (v.1 23/02/2022 v.2 13/03/2022)
    """


    dic_ordres={"pacify":[],
        "eat":[],
        "fight":[],
        "move":[]
    }
    sytaxe=True
    resultat=[]
    resultat_1=[]
    resultat_2=[]
    Liste_Ordre=Ordre.split(" ")

    for ordre in Liste_Ordre:
        if ordre !="":
            if (":@" in ordre ): 
                resultat=ordre.split(":@") 
                resultat_2=resultat[1].split("-")   
            elif (":<" in ordre ): 
                resultat=ordre.split(":<")                
                resultat_2=resultat[1].split("-")
            elif (":*" in ordre ): 
                resultat=ordre.split(":*")
                resultat_2=resultat[1].split("-")
            if("pacify" in ordre):
                resultat=ordre.split(":pacify")
                resultat_2=["1","1"]

            resultat_1=resultat[0].split("-")        
            if (type_player=="human" or type_player=="remote" ):
                syntaxe= Position_In_Board(int(resultat_1[0]),int(resultat_1[1]),int(resultat_2[0]),int(resultat_2[1]),row,col,team,equipe_palyer)
            if  sytaxe==True:
                not_in_ordre=Test_Single_Order_Wolf(dic_ordres,[int(resultat_1[0]),int(resultat_1[1])])
                if not_in_ordre==False:
                    if (":@" in ordre ): 
                        dic_ordres["move"].append([[int(resultat_1[0]),int(resultat_1[1])],[int(resultat_2[0]),int(resultat_2[1])]])
                    elif (":<" in ordre ): 
                        dic_ordres["eat"].append([[int(resultat_1[0]),int(resultat_1[1])],[int(resultat_2[0]),int(resultat_2[1])]])
                    elif (":*" in ordre ): 
                        dic_ordres["fight"].append([[int(resultat_1[0]),int(resultat_1[1])],[int(resultat_2[0]),int(resultat_2[1])]])
                    elif (":pacify" in ordre):
                        if(len(dic_ordres["pacify"])==0):
                            dic_ordres["pacify"].append([[int(resultat_1[0]),int(resultat_1[1])]])
    return dic_ordres

def End_Game(team):

    """mark the end of the game
    
    Parameters
    ----------

    team: it is the data structure that contains the data relating to the different teams (dict)

    Return
    -------
    equipe_perdante: list containing the number of the losing team (list)

    version
    -------
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implimentation : keteb dehbia ( 23/02/2022 v.2 13/03/2022)
    """

    equipe_perdante=[]

    for cle in team:
        if team[cle][2]>0 and team[cle][3]==True:
            team[cle][3]=False
        elif team[cle][2]<=0 and team[cle][3]==False:
            if team[cle][1]=="alpha":
                equipe_perdante.append(team[cle][0])
            else:
                team[cle][3]=True                            
    return equipe_perdante

def distance(position_x1, position_y1, position_x2, position_y2):

    """calculate the distance between two squares on the board
    
    Parameters
    ----------
    position_x1: line number of the first square (int)

    position_y1: column number of the first square (int)

    position_x2: line number of the second square (int)

    position_y2: column number of the second square (int)

    Return
    -------
    distance between two squares on the board (int)

    version
    -------
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implimentation :Chaimae Moussa(v.1 24/02/2022) Victorien fotso (v.2 13/03/2022)
    """
    
    if abs(position_x2- position_x1 )>abs(position_y2-position_y1):
        return abs(position_x2-position_x1)
    else:
        return abs(position_y2-position_y1)

def get_AI_orders(team,foods,equipe):

    """generate orders by IA
    
    Parameters
    ----------
    team: it is the data structure that contains the data relating to the different teams (dict)
    
    foods: it is the data structure that contains the data relating to the different resources (dict)
 
    equipe: team number (int)

    return
    -------
    syntaxe: all orders (str)

    version
    -------

    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implimentation : keteb dehbia (v.1 24/02/2022 v.2 13/03/2022)
    """

    liste_position_1=[]
    liste_position_2=[]
    syntaxe=""

    nombre_ordre=random.randint(1,9)  #choisis le nombre d'ordre qu'on souhaite générer

    #choisir un loup parmi les loup du joeur 
    for cle in team:
        if team[cle][0]==equipe:
            liste_position_1.append(cle)

    for i in range(nombre_ordre):   

        type_ordre= random.choice([":pacify",":<",":*",":@"])

        position_1=random.choice(liste_position_1)
            
        if type_ordre==":<": #si le choix fait est la nourriture, je dois choisir des position qui sont dans le dic de foods
            for j in foods:
                if distance(position_1[0],position_1[1],j[0],j[1])<=1:
                    liste_position_2.append(j)
            if(liste_position_2!=[]):
                position_2=random.choice(liste_position_2)
                syntaxe=  str(position_1[0]) +"-"+  str(position_1[1])+ type_ordre+ str(position_2[0]) + "-" + str(position_2[1])+' '+syntaxe 
            else:
                syntaxe=syntaxe
        elif type_ordre==":*" or type_ordre==":@":
            p1=random.randint(1,20)
            p2=random.randint(1,20)
            dis = distance(position_1[0],position_1[1],p1,p2)
            while(dis>1):
                p1=random.randint(1,20)
                p2=random.randint(1,20)
                dis = distance(position_1[0],position_1[1],p1,p2)
            syntaxe= str(position_1[0]) +"-"+  str(position_1[1])+ type_ordre+ str(p1)+"-"+str(p2) +' '+syntaxe 
        
        elif type_ordre==":pacify":
            syntaxe=str(position_1[0]) +"-"+  str(position_1[1])+ type_ordre +' '+syntaxe    
    
    return syntaxe

def Pacify(position_x, position_y, team):

    """pacifying wolves

    Parameters
    ---------
    position_x:  his number in the line on the set (int)

    position_y: his number in the column on the board (int)

    team: it is the data structure that contains the data relating to the different teams (dict)



    return
    -------
    Liste_Loup_Pacify: list of wolves that are pacified (list)
    
    version
    --------
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implimentation : Chaimae Moussa, keteb dehbia (v.1 24/02/2022 v.3 14/03/2022)
    
    """
    
    Liste_Loup_Pacify=[]
    if (position_x, position_y) in team:
        if (team[(position_x, position_y)][2])>=40 and (team[(position_x, position_y)][1])=="omega":
            team[(position_x, position_y)][2]-=40
            for element in team:
                if element!=(position_x, position_y):
                    if distance(position_x, position_y, element[0], element[1])<=6:
                        Liste_Loup_Pacify.append([element[0], element[1]])

    return Liste_Loup_Pacify #list containing positions of pacified wolf 

def Bonus_Assignments(position_x,position_y, equipe_player, team):

    """function allows you to assign a bonus to each wolf who wishes to attack (or who has received an attack order)

    Parameters
    ---------
    position_x: his number in the line on the set (integer)

    position_y: his number in the column on the board (integer)

    equipe_player: team number (int)

    team: it is the data structure that contains the data relating to the different teams (dict)



    Return
    ------
    Bonus: the bonus that will be used in the fight (int)

    version
    --------
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implimentation : Chaimae Moussa (v.1 25/02/2022 v.3 14/03/2022)
    
    """

    bonus=0
    if (position_x, position_y) in team:
        for element in team:
            if element!=(position_x, position_y):
                dis=distance(position_x, position_y, element[0], element[1])
                if team[element[0], element[1]][1]!="alpha" and (dis <=2) and team[element[0], element[1]][3]==False:
                    bonus =bonus+10
                elif team[element[0], element[1]][1]=="alpha" and (dis <=4):
                    bonus=bonus+30

    return bonus

def To_Eat(position_x1,position_y1, position_x2, position_y2, team, foods):

    """allow a wolf to feed

    Parameters
    ---------
    position_x1: position of our wolf on the line (int)

    position_y1: position of our wolf on the column (int)

    position_x2: position of our resource on the line (int)

    position_y2: position of our resource on the column (int)

    team: it is the data structure that contains the data relating to the different teams (dict)
    
    foods: it is the data structure that contains the data relating to the different resources (dict)

    version
    -------  
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implimentation : Loïc Franck KAMGAIN, victorien fotso (v.1 25/02/2022 v.2 14/03/2022)
    
    """

    if ((position_x2, position_y2) in foods) and (distance(position_x1, position_y1, position_x2, position_y2)<=1) and ((position_x1, position_y1) in team):
        energy_wolf=team[(position_x1, position_y1)][2]
        energy_food=foods[(position_x2, position_y2)][1]

        if energy_wolf < 100 and energy_food!=0 :

            lack_energy_wolf = 100-energy_wolf #get the missing amount of energy for the wolf in order to have the 100
            if lack_energy_wolf >= energy_food:
                new_energy_wolf = energy_wolf+energy_food
                team[(position_x1, position_y1)][2]=new_energy_wolf
                foods[(position_x2, position_y2)][1]=0
                

            else:  
                surplus_conso = energy_food-lack_energy_wolf
                new_energy_wolf = energy_wolf+lack_energy_wolf 
                team[(position_x1, position_y1)][2]=new_energy_wolf
                foods[(position_x2, position_y2)][1]=surplus_conso

def fight(position_x1, position_y1, position_x2, position_y2, team, Liste_Loup_Pacify):

    """perform the fight between two wolves

    Parameters
    ---------
    position_x1 position of our attacking wolf on the line (int)

    position_y1: position of our attacking wolf on the column (int)

    position_x2 : position of our attacked wolf on the line (int)

    position_y2: position of our attacked wolf on the line (int)

    team: it is the data structure that contains the data relating to the different teams (dict)

    Liste_Loup_Pacify: list of pacified wolfs (list)


    version
    --------
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implimentation : Loïc Franck KAMGAIN, victorien fotso (v.1 26/02/2022 v.2 1/03/2022 v.3 14/03/2022)
    
    """

    if ((position_x1, position_y1) in team) and ((position_x2, position_y2)  in team):
        if [position_x1, position_y1] not in Liste_Loup_Pacify:

            if team[(position_x1, position_y1)][3]==False and team[(position_x2, position_y2)][3]==False:
                if distance(position_x1, position_y1, position_x2, position_y2)==1:
                    surplus=Bonus_Assignments(position_x1, position_y1, team[(position_x1, position_y1)][0], team)
                    team[(position_x2, position_y2)][2]-=round((team[(position_x1, position_y1)][2]+(surplus))/10)
                    if team[(position_x2, position_y2)][2]<0:
                        team[(position_x2, position_y2)][2]=0
                    return True
    return False

def Move(position_x1, position_y1, position_x2, position_y2, team):

    """allows you to move a wolf from one square to a neighboring square

    Parameters
    --------
    position_x1: his number in the line on the set (int)

    postion_y1: his number in the column on the board (int)

    position_x2: the line where the wolf wants to move (int)

    postion_y2: the column where the wolf wants to move(int)

    team: it is the data structure that contains the data relating to the different teams (dict)
    
    version
    --------
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 21/02/2022  V.2 25/02/2022)  
    implimentation : victorien fotso (v.1 27/02/2022 v.2 14/03/2022) 
    
    """

    if ((position_x2, position_y2) not in team) and ((position_x1, position_y1) in team):
        if distance(position_x1, position_y1, position_x2, position_y2)<=1:
            team[(position_x2, position_y2)]=team[(position_x1, position_y1)]
            del team[(position_x1, position_y1)]

