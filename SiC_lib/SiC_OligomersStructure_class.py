# -*- coding: utf-8 -*-
"""
Created on Wed May 18 21:13:11 2022

@author: Всеволод
"""

from SiC_lib.SiC_Structure_class import Structure
from SiC_lib.SiC_UniqueStructures_class import UniqueOligomers

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
        self._UniqueStructures = UniqueOligomers()
    
    def add_oligomer(self, xyz_file: str, oligomer_structure: Structure):
        """
        Добавить олигомер в базу данных
        Дополнтельно проверить на присутствие
        подобного в уникальных фтруктурах

        Parameters
        ----------
        xyz_file : str
            Файл *.xyz
        oligomer_structure : Structure
            Структура олигомера типа Structure

        Returns
        -------
        None.

        """
        self._Structures[xyz_file] = ( oligomer_structure.get_K_code(), 
                                      oligomer_structure.get_oligomerization_degree() )
        self._UniqueStructures.add_structure(oligomer_structure)
        
    def get_unique_structures(self):
        """
        Получить уникальные структуры

        Returns
        -------
        : UniqueStructures
            Объект типа UniqueStructures

        """
        return self._UniqueStructures
    
    def get_all_structures(self):
        """
        Получить все структуры

        Returns
        -------
        Structures
            Объект типа Structures

        """
        return self._Structures
    
    