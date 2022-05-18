# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:41:03 2022

@author: Всеволод
"""

from SiC_Structure_class import Structure

class UniqueOligomers():
    
    def __init__(self):
        self._unique_structres = {}

    
    def addStructure(self, oligomer_struct: Structure):
        """
        Добавляет данные структуры: К-код и степень олимгоеризации
        если они являются уникальными, для выделения присутсвующих 
        типов структур и степеней олигомеризации
        Parameters
        ----------
        oligomers_struct : Structure
            DESCRIPTION.

        Returns
        -------
        None.

        """
        kcode = oligomer_struct.getKCode()
        degree = oligomer_struct.getOligomerizationDegree()
        if kcode not in self._unique_structres.keys():
            self._unique_structres[kcode] = degree
            
    def getUniqueOligomerizationDegrees(self) -> list:
        return set(self._unique_structres.values())
    
    def getUniqueStructures(self) -> list:
        return self._unique_structres