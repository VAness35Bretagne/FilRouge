# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:31:11 2024

@author: Formation
"""

import GrilleClass as GC

class Case(GC.Grille):
    
    def __init__(self, niveau='débutant'):
        
        super().__init__(niveau)  # Appelle le constructeur de la classe Grille
        
        self.coordonnées = [(i, j) for i in range(self.nb_lignes) for j in range(self.nb_colonnes)]
        self.calculer_mines_adjacentes()

    def calculer_mines_adjacentes(self):

        """
        Parcourt chaque case de la grille et met à jour le nombre   de mines adjacentes pour 
        chaque case qui n'est pas une mine.
        
        """
        directions = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),          (0, 1),
                    (1, -1), (1, 0), (1, 1)]
        
        for (i, j) in self.coordonnées:
            if self.grille[i][j] != -1: #Si ce n'est pas une bombe 
            
                compteur = 0
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < self.nb_lignes and 0 <= ny < self.nb_colonnes:
                        if self.grille[nx][ny] == -1:  # Vérifie si c'est une bombe
                            compteur += 1
                self.grille[i][j] = compteur
        
        self.afficher_grille()
        
    def All_bombes(self):
        "Return une liste qui stocke les positions de chaque bombe du jeu"
        toutes_bombes = [(i, j) for (i, j) in self.coordonnées if self.grille[i][j] == -1]
        return toutes_bombes
        
    
        

    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    