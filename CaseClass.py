# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:31:11 2024

@author: Formation
"""

import GrilleClass as GC

class Case(GC.Grille):
    
    def __init__(self, niveau='débutant'):
        
        super().__init__(niveau)  # Appelle le constructeur de la classe Grille
        self.coordonnées = [(i, j) for i in range(self.lignes) for j in range(self.colonnes)]
        
        self.calculer_mines_adjacentes()

    def calculer_mines_adjacentes(self):
        # Parcourir chaque case de la grille
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if self.grille[i][j] != -1:  # Si ce n'est pas une bombe
                    self.grille[i][j] = self.nombre_mine_adjacente(i, j)

    def nombre_mine_adjacente(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        compteur = 0

        # Vérifie toutes les directions adjacentes
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.lignes and 0 <= ny < self.colonnes:
                if self.grille[nx][ny] == -1:  # Vérifie si c'est une bombe
                    compteur += 1
        
        return compteur
        
        
        
        
if __name__ == "__main__":
    
    
    niveau_choisi = input("Choisissez un niveau (débutant, intermédiaire, difficile) : ").lower()

    if niveau_choisi not in ['débutant', 'intermédiaire', 'difficile']:
        print("Niveau invalide. Par défaut, le niveau débutant sera utilisé.")
        niveau_choisi = 'débutant'

    grille = Case(niveau_choisi)
    grille.placer_bombe_aleatoirement()

    # Afficher la grille avec les valeurs des mines adjacentes
    grille.afficher_grille()