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
        """
        Parcourt chaque case de la grille et met à jour le nombre de mines adjacentes pour 
        chaque case qui n'est pas une mine.
        
        Pour chaque case qui ne contient pas une mine (grille[i][j] != -1), 
        la fonction appelle nombre_mine_adjacente(i, j) pour calculer et 
        stocker le nombre de mines adjacentes dans la case correspondante.
        
        Returns:
        None
        """
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if self.grille[i][j] != -1:  # Si ce n'est pas une bombe
                    self.nombre_mine_adjacente(i, j)
        self.afficher_grille()

    def nombre_mine_adjacente(self, x, y):
        
        """
        Calcule le nombre de mines adjacentes à la case (x, y).
    
        La fonction parcourt les 8 cases autour de la case donnée (x, y) 
        en utilisant une liste de directions, vérifie si les cases adjacentes 
        existent dans les limites de la grille, et si elles contiennent une mine.
    
        Args:
            x (int): L'indice de la ligne de la case dans la grille.
            y (int): L'indice de la colonne de la case dans la grille.
    
        Returns:
            int: Le nombre de mines adjacentes à la case (x, y).
        """
        
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
            
        self.grille[x][y] = compteur
        
    def All_bombes(self):
        toutes_bombes = []
        for i in range(self.lignes):
            for j in range(self.colonnes):
                if self.grille[i][j] == -1:
                    toutes_bombes.append((i,j))
        return toutes_bombes
        
        
        
        
if __name__ == "__main__":
    
    
    niveau_choisi = input("Choisissez un niveau (débutant, intermédiaire, difficile) : ").lower()

    if niveau_choisi not in ['débutant', 'intermédiaire', 'difficile']:
        print("Niveau invalide. Par défaut, le niveau débutant sera utilisé.")
        niveau_choisi = 'débutant'

    grille = Case(niveau_choisi)
    grille.placer_bombe_aleatoirement()

    # Afficher la grille avec les valeurs des mines adjacentes
    grille.afficher_grille()
    
    # Calculer les mines adjacentes et afficher la grille mise à jour
    grille.calculer_mines_adjacentes()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    