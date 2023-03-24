# Creation d'un classe representant un Ns a deux valeurs et 3 enfants d'un arbre binaire
class Noeud:
    def __init__(self, valeur1, valeur2, enfant1, enfant2, enfant3):
        self.valeur1 = valeur1
        self.valeur2 = valeur2
        self.enfant1 = enfant1
        self.enfant2 = enfant2
        self.enfant3 = enfant3
    
    def have_enfant(self):
        if(self.enfant1 == None and self.enfant2 == None and self.enfant3 == None):
            return False
        
        return True
    
    def in_N(self,valeur):
        if(self.valeur1 == valeur or self.valeur2 == valeur or self.enfant1 == valeur or self.enfant2 == valeur or self.enfant3 == valeur):
            return True
       
        return False

    def full_noeuf_parent(self):
        if(self.valeur1 != None and self.valeur2 != None):
            return True
       
        return False
        
    def full_N_feuille(self):
        if(self.enfant1 == None and self.enfant2 == None and self.enfant3 == None):
            return True
     
        return False

    def full_Noeud(self):
        if(self.full_noeuf_parent() and self.full_N_feuille()):
            return True
     
        return False
    
    def insertion(self,valeur):
        while(self.have_enfant()):
            if(self.valeur1 > valeur):
                self = self.enfant1
            elif(self.valeur1 < valeur and self.valeur2 > valeur):
                self = self.enfant2
            elif(self.valeur2 < valeur):
                self = self.enfant3
                

# Creation d'un classe representant un arbre binaire composé de notre class N
class Arbre:
    def __init__(self, racine):
        self.racine = racine
    
    def in_arbre(self,valeur):
        
        if(self.in_N(valeur)):
            return True
        
        while(self.have_enfant()):
            if(self.in_N(valeur)):
                return True
        
        return False
    
    def is_feuille(self):
        if(self.racine.have_enfant() == False):
            return True
        return False
                 
    def add_Noeud(self,arbre):
        if(self.fullArbreFeuille(arbre)):
            
            return False
    
    def is_feuille(self):
        while(self.have_enfant()):
            return False


noeud = Noeud(1,3,2,None,None)
arbre = Arbre(noeud)