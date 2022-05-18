# -*- coding: utf-8 -*-
"""
Created on Wed May 18 21:13:11 2022

@author: Всеволод
"""

from SiC_Structure_class import Structure
from SiC_UniqueStructures_class import UniqueOligomers

class OligomersStructures():
    """
    Словарь харнит структуры в виде
    { "Название файла" : Соответсвующая структура,
      ...
     }
    Содержит в себе уникальные структуры
    """
    
    def __init__(self):
        self._Structures = {}
        self._UniqieStructures = UniqueOligomers()
    
    def addOligomer(self, xyz_file: str, oligomer_structure: Structure):
        self._Structures[xyz_file] = (oligomer_structure.getKCode(), 
                                      oligomer_structure.getOligomerizationDegree())
        self._UniqieStructures.addStructure(oligomer_structure)
        
    def get_unique_structures(self):
        return self._UniqieStructures
    
    def get_all_structures(self):
        return self._Structures
    
    