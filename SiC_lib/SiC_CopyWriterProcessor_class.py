# -*- coding: utf-8 -*-
"""
Created on Wed May 18 21:46:47 2022

@author: Всеволод
"""

import os
import shutil
from SiC_lib.SiC_OligomersStructure_class import OligomersStructures
from SiC_lib.SiC_UniqueStructures_class import UniqueOligomers

class CopyWhriterProcessor():
    """
    Класс для работы с созданием каталогов и копированием структур
    
    Parameters
    ----------
    working_dir: str
        Рабочая директория
    write_dir: str
        Директория записи
    ----------
    """
    def __init__(self, working_dir: str, write_dir: str):
        self._work_dir = working_dir
        self._write_dir = write_dir

    def make_directories(self, unique_structures: UniqueOligomers):
        """
        Создать директории по степеням олигомеризации
        Создать директории по кодировкам K
        Parameters
        
        ----------
        unique_structures : UniqueOligomers
            Уникальные структуры - объект типа UniqueOligomers

        Returns
        -------
        None.

        """
        for degree in unique_structures.get_unique_oligomerization_degrees():
            os.mkdir(self._write_dir + str(degree))
            os.mkdir(self._write_dir + str(degree) + "/all")
        
        for kcode, kcodedegree in unique_structures.get_unique_structures().items():
            os.mkdir(self._write_dir + str(kcodedegree) + '/' + str(kcode))
        
    def write_all_unique_structures(self, unique_structures: UniqueOligomers):
        """
        Записать все уникальные K кодировки в файл формата:
            Ki1Kj2Km3Kn4

        Parameters
        ----------
        unique_structures : UniqueOligomers
            Уникальные структуры - объект типа UniqueOligomers

        Returns
        -------
        None.

        """
        with open(self._write_dir + "AllUniqueStructures.txt", "w") as file:
            for kcode, degree in unique_structures.get_unique_structures().items():
                file.write('{}:{}\n'.format(kcode,degree))
            
    def write_all_structures(self, all_structures: dict):
        """
        Записать все уникальные K кодировки в файл формата:
            имя файла: (Ki1Kj2Km3Kn4, степень олигомеризации)

        Parameters
        ----------
        all_structures : dict
            Все полученные структуры - имя файла: (Ki1Kj2Km3Kn4, степень олигомеризации)

        Returns
        -------
        None.

        """
        with open(self._write_dir + "AllStructures.txt", "w") as file:
            for kcode, degree in all_structures.items():
                file.write('{}:{}\n'.format(kcode,degree))
                
    def do_sort(self, all_structures: dict):
        """
        Провести сортировку структур по директориям
        !Перед данной процедурой необходимо вызвать метод make_directories

        Parameters
        ----------
        all_structures : dict
            Все полученные структуры - имя файла: (Ki1Kj2Km3Kn4, степень олигомеризации)

        Returns
        -------
        None.

        """
        for file_name, kcodedegree in all_structures.items():
            shutil.copy(self._work_dir + str(file_name) , self._write_dir + str(kcodedegree[1]) + '/' + str(kcodedegree[0]) + '/' + str(file_name))
            shutil.copy(self._work_dir + str(file_name) , self._write_dir + str(kcodedegree[1]) + '/all/' + str(file_name))