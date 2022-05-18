# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:53:00 2022

@author: Всеволод
"""

from SiC_Structure_class import Structure
from SiC_UniqueStructures_class import UniqueOligomers
from SiC_OligomersStructure_class import OligomersStructures
from SiC_CopyWriterProcessor_class import CopyWhriterProcessor
import os
import numpy as np

class DataProcessor():
    
    """
    Обработчик ведет работу с файлами из указанного
    рабочего каталога
    """
    
    def __init__(self, working_directory: str, write_directory: str):
        self._CopyWriter = CopyWhriterProcessor(working_directory, write_directory)
        self._Oligomers = OligomersStructures()
        self._work_dir = working_directory
        # Хранитит в себе названия файлов с ошибочными структурами:
        # одиночная молекула ортокремниевой кислоты + олигомер
        self._Defect_Oligonmers_alone = []
        # Хранитит в себе названия файлов с ошибочными структурами:
        # цельная молекула воды
        self._Defect_Oligonmers_H2O = []
        # Координирующий атом
        self._coordinate_atom = 'Si'
        # Атом определяющий силоксановую связь Si - O - Si
        self._bridge_atom = 'O'
        # Расстояние больше которого атомы будут считаться не в связи
        self._cut_length = 1.9
        
    def doClassification(self):
        
        files_to_classify = self._get_xyz_files()
        
        for xyz_file in files_to_classify:
            
            coordinate_numbers = self._calculate_coordinate_numbers(xyz_file)
            Struct = Structure(coordinate_numbers)
            self._Oligomers.addOligomer(xyz_file, Struct)
                   
    def doSort(self):
        self._CopyWriter.makeDirectories(self._Oligomers.get_unique_structures())
        self._CopyWriter.doSort(self._Oligomers.get_all_structures())
        self._CopyWriter.writeAllStructs(self._Oligomers.get_all_structures())
        self._CopyWriter.writeAllUniqueStructs(self._Oligomers.get_unique_structures())
                                               
    # private:
    def _get_xyz_files(self):
        files = os.listdir(self._work_dir)
        """
        Фильтрация по расширению .xyz
        """
        files_read = list(filter(lambda x: x.endswith('.xyz'), files))
        return files_read
    
    def _get_atoms(self, file_name: str):
            """
            Модуль сборки структур
            """
            Atoms = np.genfromtxt(self._work_dir + file_name, \
                                  dtype = np.dtype([('Element','U2'),('X', 'f4'),('Y', 'f4'),('Z', 'f4'),]) \
                                ,skip_header=2)
            return Atoms
        
    def _calculate_coordinate_numbers(self, file_name: str) -> list:
        
        coordinate_numbers = list()      
        Atoms = self._get_atoms(file_name)
        
        for i, atom_1 in enumerate(Atoms):
            
            if atom_1[0] == self._coordinate_atom:
                atom_1_coord_num = 0 # Координационное число атома
                
                for j, atom_2 in enumerate(Atoms):
                    
                    if atom_2[0] == self._bridge_atom:
                        
                        n = 0 # Число атомов кремния связанных с атомом кислорода
                        l = ((atom_1[1]-atom_2[1])**2 + \
                             (atom_1[2]-atom_2[2])**2 + \
                                 (atom_1[3]-atom_2[3])**2)**0.5
                        if l <= self._cut_length:
                            
                            for k, atom_3 in enumerate(Atoms):
                                
                                if atom_3[0] == self._coordinate_atom:
                                    
                                    l = ((atom_3[1]-atom_2[1])**2 + \
                                         (atom_3[2]-atom_2[2])**2 + \
                                             (atom_3[3]-atom_2[3])**2)**0.5
                                    if l <= self._cut_length:                                  
                                        n += 1
                            if n == 2:
                                atom_1_coord_num += 1
                if atom_1_coord_num == 0:
                    self._Defect_Oligonmers_alone.append(file_name)
                
                coordinate_numbers.append(atom_1_coord_num)                    
                
        if self._try_find_H20_defect(Atoms):
            self._Defect_Oligonmers_H2O.append(file_name)
            return

        return coordinate_numbers



    def _try_find_H20_defect(self, Atoms) -> bool:
        
        for i, atom_1 in enumerate(Atoms):
            
            if atom_1[0] == "O":
                n = 0
                
                for j, atom_2 in enumerate(Atoms):
                    
                    if atom_2[0] == "H":
                        l = ((atom_1[1]-atom_2[1])**2 + (atom_1[2]-atom_2[2])**2 + (atom_1[3]-atom_2[3])**2)**0.5
                        if l <= 1.1:
                            n+=1
                if n == 2:
                    return True
        return False
                        

        
            
    
