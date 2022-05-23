# -*- coding: utf-8 -*-
"""
@author: Всеволод
"""
import os
import sys
from SiC_lib.SiC_DataProcessor_class import DataProcessor

"""
Входная точка программы

Задание рабочих директорий с помощью командной строки:
    ***
    python SiC_main.py Путь_к_директории_из_котрой_берутся_файлы/ Путь_директории_сортировки/
    ***
Пометка: ставить / необходимо как в примере

Задание рабочих директорий в скрипте
изменить переменные 
working_dir
write_dir
Запуск скрипта:
    ***
    python SiC.py
    ***
"""

# Директория содержащая в себе классифицируемые структуры формата .xyz
working_dir = os.getcwd() + "\\Tests\\Structures\\"
# Директория записи сортированных структур
write_dir = os.getcwd() + "\\Tests\\Classification\\"
    
if __name__ == "__main__":    

    # При задании директорий из которых будут браться файлы
    # как аргументы командной строки
    if len(sys.argv) > 1:
        print("Started sorting...")
        
        working_dir = sys.argv[1]
        write_dir = sys.argv[2]
        
        OligomersAnalysis = DataProcessor(working_dir, write_dir)
        OligomersAnalysis.do_classification()
        OligomersAnalysis.do_sort()
        
        print("Sorting finished")
        
    # Ручное задание директорий работы
    else:
        print("Started sorting...")
                
        OligomersAnalysis = DataProcessor(working_dir, write_dir)
        OligomersAnalysis.do_сlassification()
        OligomersAnalysis.do_sort()
        
        print("Sorting finished")