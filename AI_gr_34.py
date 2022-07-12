from precedent import*
import time

def alentour_loup(dic,row,col,position_x,position_y,equipe):

    """get the elements around a wolf
    
    Parameters
    ---------
    dic: the dictionary contains all the data relating to the wolves of the different teams (dict)

    row: the number of rows on our board (int)

    col:the number of columns of our tray (int)

    position_x: line number of the first element(int)

    position_y: culunm number of the first element(int)

    equipe: player's team number(int)

    Return
    -------

    liste_ami: list containing the wolves friends of our wolf (list)
    liste_ennemi: list containing the enemies of our wolf (list)
    case_vide: list containing the empty boxes around our wolf (list)

    specification: KETEB Dehbia (v.1 09/04/2022)
    implimentation : KETEB Dehbia (v.1 10/04/2022)
    """

    x=position_x 
    y=position_y
    liste_ami=[]
    liste_ennemi=[]
    case_vide= []
    liste_pres_alentour=[[x-1,y-1],[x-1,y],[x-1,y+1] ,[x+1,y+1],[x+1,y],[x+1,y-1],[x,y+1],[x,y-1]]  
    for i in liste_pres_alentour:
        if int(i[0])> 0 and int(i[0])<=int(row) and int(i[1])> 0 and int(i[1])<= int(col):
            cle=(int(i[0]),int(i[1]))
            if cle in dic:
                if dic[cle][0]== equipe:
                    liste_ami.append(cle)
                else:   
                    liste_ennemi.append(cle)
            else:
                    case_vide.append(cle)
    return liste_ami,liste_ennemi,case_vide

def Coin_plus_proche(team,position_x_alpha,position_y_alpha,row,col,equipe):

    """get the nearest corner for a wolf
    
    Parameters
    ---------
    team: the dictionary contains all the data relating to the wolves of the different teams (dict)

    position_x_alpha: line number of our alpha(int)

    position_y_alpha: culunm number of our alpha(int)

    row: the number of rows on our board (int)

    col:the number of columns of our tray (int)

    equipe: player's team number(int)

    Return
    -------
    coin_proche: position of our nearest corner (list)

    specification: KETEB Dehbia (v.1 09/04/2022)
    implimentation : KETEB Dehbia (v.1 11/04/2022)
    """



    liste_coin=[[1,col],[1,1],[row,1],[row,col]]
    coin_proche=[]
    #liste contenant les coins où notre loup alpha peut acceder car il nya pas un loup ennemi dans ce coin
     
    if [position_x_alpha,position_y_alpha] in liste_coin: # verifier si le loup alpha est déja dans l'un des coins
        return [position_x_alpha,position_y_alpha]

    else: #s'il n'est pas dans l'un des coin 
        for coin in liste_coin: #selectionner les coins où il nya pas d'ennemis 
            if (coin[0],coin[1])  in team:
                liste_coin.remove(coin)


        if liste_coin!=[]: #verifier si cette liste n'est pas vide c'est a dire qu'il y'a un coin où notre loup alpha peu se deplacer
            min=100
            for i in range(len(liste_coin)):
                dis=distance(position_x_alpha,position_y_alpha, int(liste_coin[i][0]),int(liste_coin[i][1]))
                if dis<=min:
                    coin_proche=[liste_coin[i][0],liste_coin[i][1]]
                    min= dis 
            return coin_proche #le coin le plus proche ou il nya pas d'ennemis 

        else:#le loup alpha reste à sa plaçe
            return [position_x_alpha,position_y_alpha]

def Calcule_Cordonner_Deplacement(position_1,position_2):

    """calculate the data to make a move
    
    Parameters
    ---------

    position_1: first coordinate(int)

    position_2: second coordinate(int)

    Return
    -------
    new coordinates(int)

    specification: KETEB Dehbia? VICTORIEN FOTSO (v.1 09/04/2022)
    implimentation : VICTORIEN FOTSO (v.1 10/04/2022)
    """

    if position_1>position_2:
        return position_1-1
    elif position_1==position_2:
        return position_1
    else:
        return position_1+1

def Chose_Plus_Proche(position_x,position_y,structure,equipe):

    """find the nearest element
    
    Parameters
    ---------

    position_x: line number of our wolf element(int)

    position_y: culunm number of our wolf(int)

    structure: the dictionary contains all the data relating to the wolves of the different teams (dict)

    equipe: player's team number(int)

    Return
    -------

    position of the nearest element(list)

    specification: fotso Victorien (v.1 09/04/2022)
    implimentation : FOTSO Victorien, KETEB Dehbia (v.1 13/04/2022)
    """

    position=[]
    dist=[]
    proche=[] 
    
    for loup in structure:
        if equipe==1 or equipe==2:#l'ennemie ou l'ami le plus proche
            if structure[loup][0]==equipe:
                dis= distance(position_x,position_y,loup[0],loup[1])
                position.append([loup[0],loup[1]])
                dist.append(dis)
        else:
            
            dis= distance(position_x,position_y,loup[0],loup[1])
            position.append([loup[0],loup[1]])
            dist.append(dis)

    for i in range(len(dist)):
        if dist[i] ==min(dist):
            
            return position[i]
        
def ordre_alpha(liste_ennemie, liste_ami, case_vide, row, col, team, alpha, food, equipe ):

    """creating order for the alpha wolf
    
    Parameters
    ---------
    
    liste_ennemie:list containing the enemies of our alpha wolf (list)

    liste_ami:list containing the wolves friends of our alpha wolf (list)

    case_vide:list containing the empty boxes around our alpha wolf (list)

    row: the number of rows on our board (int)

    col:the number of columns of our tray (int)

    team: the dictionary contains all the data relating to the wolves of the different teams (dict)

    alpha: position of our alpha wolf(list)

    food: the dictionary contains all the data relating to the foods(dict) 

    equipe: player's team number(int)

    Return
    -------
    order for our alpha wolf(str)

    Notes
    -------
    oders can be empty

    
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 16/04/2022  )  
    implimentation : victorien fotso, keteb dehbia (v.1 22/02/2022 v.2 v.3 23/04/2022)
    """


    #le cas où le loup alpha est proche d'une ressource et son ennergie est inferieure à 60
    if team[(alpha[0],alpha[1])][2]<60 : 
        for cle in food:
            if distance(alpha[0],alpha[1],cle[0],cle[1])<=1 and food[cle][1]>0:
                return str(alpha[0])+"-"+ str(alpha[1]) + ":<" + str(cle[0])+ "-" + str(cle[0])
        return " "

    else:
        #le cas où le loup alpha n'est entouré ni d'amis ni d'ennemis  
        if liste_ami==[] and liste_ennemie==[] and case_vide!=[]: 
            if [alpha[0],alpha[1]] not in [[1,col],[1,1],[row,1],[row,col]]: # si alpha n'est pas dans le coin
                return " "
            else:
                coin_proche=Coin_plus_proche(team,alpha[0],alpha[1],row,col,equipe)  
                x= Calcule_Cordonner_Deplacement(int(alpha[0]),int(coin_proche[0])) 
                y= Calcule_Cordonner_Deplacement(int(alpha[1]),int(coin_proche[1]))
                return str(alpha[0])+"-"+ str(alpha[1]) + ":@" + str(x)+ "-" + str(y) #faire avancer alpha vers le coin le plus proche
                
        #le cas où notre loup alpha est complètement entouré des ennemis 
        if case_vide==[] and liste_ami==[] and liste_ennemie!=[]: 
            max =0
            loup_fort=[]
            for i in liste_ennemie:
                if team[(i[0],i[1])][1]=="alpha":
                    return str(alpha[0])+"-"+ str(alpha[1]) + ":*" + str(i[0])+ "-" + str(i[1])
                else:
                    if team[(i[0],i[1])][2]>=max:
                        max=team[(i[0],i[1])][2]
                        loup_fort=i
            return str(alpha[0])+"-"+ str(alpha[1]) + ":*" + str(loup_fort[0])+ "-" + str(loup_fort[1]) #il attaque le loup le plus fort
        
        #le cas où le loup alpha est entouré de quelques loups ennemies ou bien entouré de quelques ennemis et amis  
        if (case_vide!=[] and liste_ami!=[] and liste_ennemie!=[]) or (case_vide!=[] and liste_ami==[] and liste_ennemie!=[]): 
            case_disponible=[] #liste des cases vide où mon loup alpha peut acceder et les loup ennemis non 
            case_deplacement=[] 
            for j in case_vide:
                cmp=0
                for k in liste_ennemie:
                    if distance(j[0],j[1],k[0],k[1])>1:
                        cmp=cmp+1
                if cmp==len(liste_ennemie): #le cas où on a plusieurs case vide où notre loup alpha peut se deplacer
                    case_disponible.append(j)
            if case_disponible !=[]:
                case_deplacement=random.choice(case_disponible)
                return str(alpha[0])+"-"+ str(alpha[1]) + ":@" + str(case_deplacement[0])+ "-" + str(case_deplacement[1])
            else:
                for i in liste_ennemie:#voir si parmis les ennemis, il y'a un loup alpha. si oui, on attaque 
                    if team[(i[0],i[1])][1]=="alpha":
                        return str(alpha[0])+"-"+ str(alpha[1]) + ":*" + str(i[0])+ "-" + str(i[1])

                case_deplacement=random.choice(case_vide) #sinon s'il y'a pas de loup alpha ennemis, on se deplace vers une case vide disponible 
                return str(alpha[0])+"-"+ str(alpha[1]) + ":@" + str(case_deplacement[0])+ "-" + str(case_deplacement[1])
        
        #cas où a notre alhpa est completement entouré d'amis et d'ennemis
        if (case_vide==[] and liste_ami!=[] and liste_ennemie!=[]):  
            loup_enemie=[]
            for z in liste_ennemie:
                if team[(z[0],z[1])][1]=="alpha":
                    return str(alpha[0])+"-"+ str(alpha[1]) + ":*" + str(z[0])+ "-" + str(z[1])
                else:
                    loup_enemie=random.choice(liste_ennemie)
                    return str(alpha[0])+"-"+ str(alpha[1]) + ":*" + str(loup_enemie[0])+ "-" + str(loup_enemie[1])

        #le cas où notre loup alpha n'a pas d'ennemis autour de lui
        if  liste_ennemie==[] and liste_ami!=[]:  
            if [alpha[0],alpha[1]] not in [[1,col],[1,1],[row,1],[row,col]]:
                coin=[]
                coin=Coin_plus_proche(team,alpha[0],alpha[1],row,col, equipe)
                x=Calcule_Cordonner_Deplacement(int(alpha[0]),int(coin[0]))
                y=Calcule_Cordonner_Deplacement(int(alpha[1]),int(coin[1]))
                if [x,y]in liste_ami:
                    if case_vide!=[]:
                        local=random.choice(case_vide)
                        return str(alpha[0])+"-"+ str(alpha[1]) + ":@" + str(local[0])+ "-" + str(local[1])
                    else:
                        return " "
                else:
                    return str(alpha[0])+"-"+ str(alpha[1]) + ":@" + str(x)+ "-" + str(y)
            else:
                return " "

def ordre_omega(row,col,team, omega, food, liste_ennemie_alpha, alpha, liste_ami_alpha, equipe):

    """creating order for the omega wolf
    
    Parameters
    ---------
    
    row: the number of rows on our board (int)

    col:the number of columns of our tray (int)

    team: the dictionary contains all the data relating to the wolves of the different teams (dict)

    omega: position of our omega wolf(list)

    food: the dictionary contains all the data relating to the foods(dict)
    
    liste_ennemie_alpha:list containing the enemies of our alpha wolf (list)

    alpha: position of our alpha wolf(list)

    liste_ami_alpha:list containing the wolves friends of our alpha wolf (list)

    equipe: player's team number(int)

    Return
    -------
    order for our omega wolf(str)

    Notes
    -------
    oders can be empty

    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 16/04/2022  V.2 28/04/2022)  
    implimentation : victorien fotso, keteb dehbia, Loïc Franck KAMGAIN  (v.1 23/04/2022 v.2 27/04/2022)
    
    """

    #recuperer ce qui entoure notre loup omega 
    liste_ami_omega, liste_ennemie_omega, case_vide_omega=alentour_loup(team,20,20,omega[0],omega[1],equipe)
    
    if team[(omega[0],omega[1])][2]<40: #si le loup omega n'a pas assez d'energie pour pacifier 
        
        if team[(omega[0],omega[1])][3]!=True and liste_ennemie_omega!=[] : #notre loup omega n'est pas humain et il a des ennemis autour de lui 
  
            for ennemi in liste_ennemie_omega: #parcourir la liste des ennemis qui entourent notre loup omega 
                    if team[(ennemi[0],ennemi[1])][1]==alpha: #voir si parmis les loups qui entourent notre loup omega,il y'a le loup alpha enemi 
                        #si le loup alpha est à coté, on attaque 
                        return str(omega[0])+"-"+str(omega[1])+":*" + str(ennemi[0]) + "-" + str(ennemi[1])
                    
                    #sinon s'il y'a pas de loup alpha ennemi,on attaque le loup le plus fort qui est à coté   
                    else:
                        max=0
                        if max <= team[(ennemi[0],ennemi[1])][2]:
                            max= team[(ennemi[0],ennemi[1])][2]
                            position= ennemi
                        else:
                            max=max
                            position=position
                        
            return str(omega[0])+"-"+str(omega[1])+":*" + str(position[0]) + "-" + str(position[1])
                        
        else:#le cas où mon omega est humain ou il n'a pas d'ennemis autour de lui 
            nourriture=Chose_Plus_Proche(omega[0],omega[1],food,0)
            #si notre loup est à coté ou sur la ressource 
            if distance(omega[0],omega[1],nourriture[0],nourriture[1])<=1:
                return str(omega[0])+"-"+str(omega[1])+":<"+str(nourriture[0])+ "-" + str(nourriture[1]) 
                
            else: #si il n'est pas sur la ressource on donne l'ordre de se deplacer vers cette ressource 
                position_dep_x=Calcule_Cordonner_Deplacement(omega[0],nourriture[0])
                position_dep_y=Calcule_Cordonner_Deplacement(omega[1],nourriture[1])
                if (position_dep_x,position_dep_y) in case_vide_omega:
                    return str(omega[0])+"-"+str(omega[1])+":@"+str(position_dep_x)+ "-" + str(position_dep_y)
                else:
                    return " "
                

    else: #le cas où notre omega a l'energie suffisante 
        dis= distance(omega[0],omega[1],alpha[0],alpha[1])
        #calculer le nombre de loups amis qui sont autour à une distance de 2 
        cpt=0
        for cle in team:
            if team[cle][0]==equipe and distance(alpha[0],alpha[1],cle[0],cle[1]==2):
                cpt=cpt+1
            else:
                cpt=cpt

        if (dis<=5 ): # voir si il y'a des ennemies autour de mon alpha 
            
            #le cas où le loup alpha est entouré des ennemis  
            if (len(liste_ennemie_alpha)>1 and [alpha[0],alpha[1]] in [[1,col],[1,1],[row,1],[row,col]] and len(liste_ennemie_alpha)>cpt) or (len(liste_ennemie_alpha)>2 and [alpha[0],alpha[1]] not in [[1,col],[1,1],[row,1],[row,col]] and len(liste_ennemie_alpha)>cpt):
                
                return str(omega[0])+"-"+str(omega[1])+":pacify"
            else: #le cas où le loup alpha n'est pas en danger 
                
                if liste_ennemie_omega!=[]:
                    
                    max=0
                    position=[]
                    for ennemi in liste_ennemie_omega: #parcourir la liste des ennemis qui entourent notre loup omega 
                        if team[(ennemi[0],ennemi[1])][1]==alpha: # voir si parmis les loups qui entourent notre loup omega il y'a le loup alpha enemmi 
                        #le cas où le loup alpha est à coté de nous, on attaque 
                            return str(omega[0])+"-"+str(omega[1])+":*" + str(ennemi[0]) + "-" + str(ennemi[1])
                        else: 
                                if max <= team[(ennemi[0],ennemi[1])][2]:
                                    max= team[(ennemi[0],ennemi[1])][2]
                                    position= ennemi
                    return str(omega[0])+"-"+str(omega[1])+":*" + str(position[0]) + "-" + str(position[1])
                else:
                    
                    return " "
        else: #sinon on s'approche du loup alpha  
            position_dep_x=Calcule_Cordonner_Deplacement(omega[0],alpha[0])
            position_dep_y= Calcule_Cordonner_Deplacement(omega[1],alpha[1])
            if (position_dep_x,position_dep_y) in case_vide_omega:
                return str(omega[0])+"-"+str(omega[1])+":@"+str(position_dep_x)+ "-" + str(position_dep_y)
            else:
                if case_vide_omega!=[]: #voir s'il y'a des cases vides autour de mon omega 
                    position=random.choice(case_vide_omega) 
                    return str(omega[0])+"-"+str(omega[1])+":@"+str(position[0])+ "-" + str(position[1])
                else: #le cas où il nya pas de cases vides 
                    return " "

def ordre_normal(teams,food, row, col ,normal,equipe,alpha_ennemi ):

    """creating orders for the normal wolf
    
    Parameters
    ---------

    teams: the dictionary contains all the data relating to the wolves of the different teams (dict)

    food: the dictionary contains all the data relating to the foods(dict)

    row: the number of rows on our board (int)

    col:the number of columns of our tray (int)

    normal: position of our normal wolf(list)
    
    equipe: player's team number(int)

    alpha_ennemi: enemy alpha position (list)


    Return
    -------
    orders for our normals wolfs(str)

    Notes
    -------
    oders can be empty

    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 16/04/2022  V.2 28/04/2022)  
    implimentation : victorien fotso, keteb dehbia, Chaimae Moussa  (v.1 221/04/2022 v.2 29/04/2022)
    """
  
    #recuperer les alentours de mon loup normal 
    alountour=alentour_loup(teams,row,col,normal[0],normal[1],teams[normal][0]) 
    
    if teams[normal][2]>0: #le cas où le loup n'est pas humain 
        if alountour[1]!=[]: #le cas où à coté de mon loup, il y'a des ennemis 
            for j in alountour[1]:
                if teams[j][1]=="alpha" :
                    return  str(normal[0])+"-"+str(normal[1])+":*"+str(j[0])+"-"+str(j[1]) 
            loup_attque=random.choice(alountour[1])
            return  str(normal[0])+"-"+str(normal[1])+":*"+str(loup_attque[0])+"-"+str(loup_attque[1]) 
        else:#le cas où il nya pas d'ennemis  
            x=Calcule_Cordonner_Deplacement(int(normal[0]),int(alpha_ennemi[0][0]))
            y=Calcule_Cordonner_Deplacement(int(normal[1]),int(alpha_ennemi[0][1]))
            if (x,y) in teams:
                if alountour[2]!=[]:
                    case_libre=random.choice(alountour[2])
                    return str(normal[0])+"-"+str(normal[1])+":@"+str(case_libre[0])+"-"+str(case_libre[1]) 
                else:
                    return " "   
            else:
                return str(normal[0])+"-"+str(normal[1])+":@"+str(x)+"-"+str(y)        
    else:
        nourriture_proche=Chose_Plus_Proche(normal[0],normal[1],food,0)
        
        if distance(normal[0],normal[1],nourriture_proche[0],nourriture_proche[1])<=1 and food[(nourriture_proche[0],nourriture_proche[1])][1]>0:
            
            return str(normal[0])+"-"+str(normal[1])+":<"+str(nourriture_proche[0])+"-"+str(nourriture_proche[1]) 
        else:
            x=Calcule_Cordonner_Deplacement(normal[0],nourriture_proche[0])
            y=Calcule_Cordonner_Deplacement(normal[1],nourriture_proche[1])
            if alountour[2]!=[]:
                if [x,y] in alountour[2]:
                    print(normal[0],normal[1],"deplacer vers la nourriture",x,y,"les alountour de mon loup sont",alountour[2])  
                    return str(normal[0])+"-"+str(normal[1])+":@"+str(x)+"-"+str(y) 
                else:
                    case_libre=random.choice(alountour[2])
                    return str(normal[0])+"-"+str(normal[1])+":@"+str(case_libre[0])+"-"+str(case_libre[1])
            else:
                return " " 

def IA_Intelligent(team,food,row,col,equipe):

    """creating final orders for our artificial intelligence
    
    Parameters
    ---------

    team: the dictionary contains all the data relating to the wolves of the different teams (dict)

    food: the dictionary contains all the data relating to the foods(dict)

    row: the number of rows on our board (int)
    
    equipe: player's team number(int)

    Return
    -------
    orders for our artificial intelligence(str)
    
    specification: Chaimae Moussa, Loïc Franck KAMGAIN, victorien fotso, keteb dehbia (v.1 16/04/2022  )  
    implimentation : victorien fotso, keteb dehbia  (v.1 25/04/2022 )
    """


    ordre_alpha_a=" "
    ordre_omega_o=" "
    ordre_loup_normal=" "

    alpha=[] 
    omega=[]
    position_alpha_ennemie=[]    

    for cle,valeur in team.items():
        if valeur[0]==equipe and valeur[1]=="alpha":       
            alpha.append(cle[0])
            alpha.append(cle[1])

        elif valeur[0]==equipe and valeur[1]=="omega":
            omega.append(cle[0])
            omega.append(cle[1])
        elif valeur[0]!=equipe and valeur[1]=="alpha":
            position_alpha_ennemie.append(cle)

    liste_ami_alpha, liste_ennemie_alpha, case_vide_alpha =alentour_loup(team,row,col,alpha[0],alpha[1],equipe)

    #générer un ordre pour le alpha 
    ordre_alpha_a = ordre_alpha(liste_ennemie_alpha, liste_ami_alpha, case_vide_alpha, row, col, team, alpha ,food, equipe)
    
    #générer un ordre pour le omega
    ordre_omega_o=ordre_omega(row, col, team, omega, food, liste_ennemie_alpha, alpha, liste_ami_alpha, equipe)
    

    #generer des ordres pour tout les loups normaux
    for cle, valeur in team.items():
        if valeur[1]=="normal" and valeur[0]==equipe:
            ordre=ordre_normal(team,food, row, col ,cle,equipe,position_alpha_ennemie)
            if ordre!=" " :
                if ordre_loup_normal!=" ": 
                    ordre_loup_normal=ordre_loup_normal+" "+ ordre 
                else:
                    ordre_loup_normal=ordre 
            else:
                ordre_loup_normal=ordre_loup_normal
    
    

    #gnerer l'ensemble des ordres finaux pour l'intelligence artificielle
    if type(ordre_alpha_a)!=None and type(ordre_loup_normal)!=None and type(ordre_omega_o)!=None:
        if ordre_alpha_a!=[] and ordre_omega_o==[] and ordre_loup_normal!=[]:
            return ordre_loup_normal+" "+ ordre_alpha_a
        elif ordre_alpha_a!=[] and ordre_omega_o==[] and ordre_loup_normal==[]:
            return ordre_alpha_a
        elif ordre_alpha_a!=[] and ordre_omega_o!=[] and ordre_loup_normal!=[]:
            return ordre_loup_normal+" "+ ordre_omega_o+" "+ ordre_alpha_a
        elif ordre_alpha_a!=[] and ordre_omega_o!=[] and ordre_loup_normal==[]:
            return ordre_omega_o+" "+ordre_alpha_a
        elif ordre_alpha_a==[] and ordre_omega_o==[] and ordre_loup_normal!=[]:
            return ordre_loup_normal
        elif ordre_alpha_a==[] and ordre_omega_o!=[] and ordre_loup_normal!=[]:
            return ordre_loup_normal+" "+ ordre_omega_o
        elif ordre_alpha_a==[] and ordre_omega_o!=[] and ordre_loup_normal==[]:
            return ordre_omega_o



def play_game(map_path, group_1, type_1, group_2, type_2):

    """Play a game.
    
    Parameters
    ----------
    map_path: path of map file (str)
    group_1: group of player 1 (int)
    type_1: type of player 1 (str)
    group_2: group of player 2 (int)
    type_2: type of player 2 (str)
    
    Notes
    -----
    Player type is either 'human', 'AI' or 'remote'.
    
    If there is an external referee, set group id to 0 for remote player.

    Version
    -------
    specification: Prof Benoit Frenay  
    implimentation : Keteb dehbia(v.1 10/03/2022 v.2 25/03/2022) Victorien fotso(v.3 27/03/2022)  
    
    """
    
    tour=0
    Fin_Game=[]
    
    team,foods,row,col=Data_Structures(map_path)

    if type_1 == 'remote':
        connection = create_connection(group_2, group_1,)
    elif type_2 == 'remote':
        connection = create_connection(group_1, group_2)
    
    while tour<200 and Fin_Game==[]:

        Liste_pacify=[]
        Liste_Ordre=[]
        if type_1 == 'remote':
            orders_1 = get_remote_orders(connection)
        else:
            if type_1=="human":
                orders_1=input("veuillez saisir les ordres que vous souhaitez pour le joueur 1\n")
            elif type_1=="AI":
                #orders_1 = get_AI_orders(team,foods,1)
                orders_1 = IA_Intelligent(team,foods,row,col,1)
                
            elif type_2 == 'remote':
                notify_remote_orders(connection, orders_1)
    
        if type_2 == 'remote':
            orders_2 = get_remote_orders(connection)

        else:
            if type_2=="human":
                orders_2=input("veuillez saisir les ordres que vous souhaitez pour le joueur 2")
            elif type_2=="AI":
                #orders_2 = get_AI_orders(team,foods,2)
                orders_2 = IA_Intelligent(team,foods,row,col,2)
            elif type_1 == 'remote':
                notify_remote_orders(connection, orders_2)


        Liste_Ordre.append(orders_1)
        Liste_Ordre.append(orders_2)
        numero_equipe=1
        for i in Liste_Ordre:
            dictionnaire_ordre=Sort_Orders (i, int(row), int(col),type_1,team,numero_equipe)#dictionnaire des ordres du joueur 1 
            if dictionnaire_ordre["pacify"]!=[]:
                Liste_pacify=Pacify(dictionnaire_ordre["pacify"][0][0][0], dictionnaire_ordre["pacify"][0][0][1] ,team)

            if dictionnaire_ordre["eat"]!=[]:
                for i in dictionnaire_ordre["eat"]:
                    To_Eat(i[0][0],i[0][1],i[1][0],i[1][1],team,foods)

            if dictionnaire_ordre["fight"]!=[]:
                for j in dictionnaire_ordre["fight"]:
                    resultat=fight(j[0][0],j[0][1],j[1][0],j[1][1],team,Liste_pacify)
                    if resultat==True:
                        tour=0
                    else:
                        tour+=1
            
            if dictionnaire_ordre["move"]!=[]:
                for k in dictionnaire_ordre["move"]:
                    Move(k[0][0],k[0][1],k[1][0],k[1][1],team) 
                    
            numero_equipe=numero_equipe+1

        end_game=End_Game(team) 
        if end_game!=[]:
            Fin_Game=end_game
        sleep(0.5)
        Board(team,foods,int(row),int(col))
        sleep(0.5)
        print("\n\n\n\n\n")
        print("nombre de tour sans attaque: ",tour)
        
#fin de la while   
    if end_game==[]:
        some_1=0
        some_2=0
        for values in team.values():
            if (values[0]==1):
                some_1=some_1+values[2]
            else:
                some_2=some_2+values[2]
        if some_1>some_2:
            print("le gagnant est le joueur:" ,1)
        elif some_1<some_2:
            print("le gagnant est le joueur:" ,2)
        else:
            print("la partie est nulle")

    elif (len(end_game)==1):
        print("le perdant est le joueur:", end_game[0])
    else:
        print("la partie est nulle")   
    # close connection, if necessary
    if type_1 == 'remote' or type_2 == 'remote':
        close_connection(connection)

play_game("file.ano", 34, "AI", 54, "AI")

