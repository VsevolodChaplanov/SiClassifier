# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:29:22 2022

@author: Всеволод
"""
import os
from SiC_DataProcessor_class import DataProcessor

if __name__ == "__main__":

    print("Started sorting...")
    
    working_dir = 'D:/QuantumChem/TestingPotent/Structures/'
    write_dir = 'D:/QuantumChem/TestingPotent/Classification/'
    
    OligomersAnalysis = DataProcessor(working_dir, write_dir)
    xyz_files = OligomersAnalysis._get_xyz_files()
    print(OligomersAnalysis._get_atoms((xyz_files[0])))
    OligomersAnalysis.doClassification()
    OligomersAnalysis.doSort()
    print(OligomersAnalysis._Oligomers)