# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:58:18 2024

@author: Formation
"""


#-----------Projet Démineur----------VanessaM-------------------------

import random

class Grille:
    

    def __init__(self, niveau='débutant', lignes=None, colonnes=None, nombre_de_bombes=None):
        
        
        self.niveau = niveau
        self.nb_lignes, self.nb_colonnes, self.nombre_de_bombes = self.set_niveau(niveau)
        
        print(f"Grille de {self.nb_lignes} lignes et {self.nb_colonnes} colonnes avec {self.nombre_de_bombes} bombes.")
        
        # Création de la grille
        self.grille = [[0 for _ in range(self.nb_colonnes)] for _ in range(self.nb_lignes)]
        
        print("Grille vide initialisée :")
    
    def set_niveau(self, niveau):
        # Configure la taille de la grille et le nombre de bombes selon le niveau choisi
        if niveau == 'débutant':
            return 9, 9, 10
        elif niveau == 'intermédiaire':
            return 16, 16, 40
        elif niveau == 'difficile':
            return 16, 30, 99
        else:
            raise ValueError("Niveau invalide")
        
    
    def afficher_grille(self):
        
        """
        Affiche la grille dans la console.
        """
        
        for ligne in self.grille:
            print(" ".join(str(cell) for cell in ligne))
        print("\n")  # Saut de ligne pour mieux voir la grille
        
        

    def placer_bombe_aleatoirement(self, premier_clic):
        
        """
        Permet de placer aléatoirement des bombes, en s'assurant qu'aucune bombe 
        n'est placée dans les cases adjacentes au premier clic.
        
        """
        
        x, y = premier_clic
        
        # Générer toutes les positions possibles dans la grille
        positions_possibles = [(i, j) for i in range(self.nb_lignes) for j in range(self.nb_colonnes)]
        
        # Exclure la case du premier clic et ses cases adjacentes
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        
        # Exclure les cases adjacentes au premier clic
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.nb_lignes and 0 <= ny < self.nb_colonnes:
                if (nx, ny) in positions_possibles:
                    positions_possibles.remove((nx, ny))
        
        # Enlever la case du premier clic elle-même
        if (x, y) in positions_possibles:
            positions_possibles.remove((x, y))

        # Sélectionner aléatoirement un nombre donné de positions
        positions_choisies = random.sample(positions_possibles, self.nombre_de_bombes)
        
        for k in positions_choisies:
            self.grille[k[0]][k[1]] = -1  # Placer la bombe
        
        print("Grille actualisée après le premier clic :")

    


    
    
    
    
    
    
    
    
    
    
    
    