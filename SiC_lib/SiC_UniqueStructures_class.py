# -*- coding: utf-8 -*-
"""
@author: Всеволод
"""

from SiC_lib.SiC_Structure_class import Structure

class UniqueOligomers():
    
    def __init__(self):
        self._unique_structres = {}

    
    def add_structure(self, oligomer_struct: Structure):
        """
        Добавляет данные структуры: К-код и степень олимгоеризации
        если они являются уникальными, для выделения присутсвующих 
        типов структур и степеней олигомеризации
        Parameters
        ----------
        oligomers_struct : Structure
            Структура олигомера типа Structure

        Returns
        -------
        None.

        """
        kcode = oligomer_struct.get_K_code()
        degree = oligomer_struct.get_oligomerization_degree()
        if kcode not in self._unique_structres.keys():
            self._unique_structres[kcode] = degree
            
    def get_unique_oligomerization_degrees(self) -> list:
        """
        Возваращет уникальные стпени олигомеризации

        Returns
        -------
        list
             [2,3,4 ...].

        """        
        return set(self._unique_structres.values())
    
    def get_unique_structures(self):
        """
        Возвращает уникальеные структуры

        Returns
        -------
        dist
            Уникальные структуры {'K1NK2MK3LK4P' : степень олигомеризации}

        """
        return self._unique_structres