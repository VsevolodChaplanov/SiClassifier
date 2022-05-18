# -*- coding: utf-8 -*-
"""
Created on Wed May 18 21:46:47 2022

@author: Всеволод
"""

import os
import shutil
from SiC_OligomersStructure_class import OligomersStructures
from SiC_UniqueStructures_class import UniqueOligomers

class CopyWhriterProcessor():
    
    def __init__(self, data_directory, write_directory):
        self._work_dir = data_directory
        self._write_dir = write_directory

    def makeDirectories(self, UniqueStructures: UniqueOligomers):

        for degree in UniqueStructures.getUniqueOligomerizationDegrees():
            os.mkdir(self._write_dir + str(degree))
            os.mkdir(self._write_dir + str(degree) + "/all")
        
        for kcode, kcodedegree in UniqueStructures.getUniqueStructures().items():
            os.mkdir(self._write_dir + str(kcodedegree) + '/' + str(kcode))
        
    def writeAllUniqueStructs(self, UniqueStructures: UniqueOligomers):
        with open(self._write_dir + "AllUniqueStructures.txt", "w") as file:
            for kcode, degree in UniqueStructures.getUniqueStructures().items():
                file.write('{}:{}\n'.format(kcode,degree))
            
    def writeAllStructs(self, AllStructures: dict):
        with open(self._write_dir + "AllStructures.txt", "w") as file:
            for kcode, degree in AllStructures.items():
                file.write('{}:{}\n'.format(kcode,degree))
                
    def doSort(self, AllStructures: dict):
        
        for file_name, kcodedegree in AllStructures.items():
            shutil.copy(self._work_dir + str(file_name) , self._write_dir + str(kcodedegree[1]) + '/' + str(kcodedegree[0]) + '/' + str(file_name))
            shutil.copy(self._work_dir + str(file_name) , self._write_dir + str(kcodedegree[1]) + '/all/' + str(file_name))