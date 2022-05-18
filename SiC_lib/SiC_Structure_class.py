# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:15:09 2022

@author: Всеволод
"""

class Structure():
    """
    Класс структуры:
        Хранит в себе только данные о кодировке: K1NK2MK3LK4P -> [] -
        - массив координационных чисел всех атомов кремния в структуре
    Степень олигомеризации определяется через сумму атомов кремния        
    
    Parameters
    ----------
    coordinate_numbers : list
        Координационные числа - [1,2,3,...]
    -------

    """    
    
    def __init__(self, coordinate_numbers: list):
        self._coordinate_numbers = coordinate_numbers
        
        
    def get_oligomerization_degree(self):
        """
        Получить степень олигомеризации структуры

        Returns
        -------
        int
            Степень олигомеризации

        """
        return len(self._coordinate_numbers)
    
    def get_K_code(self):
        """
        Возварщает строку кодировки структуры
        в терминах координационных чисел
        
        Returns
        -------
        str
            "K1NK2MK3LK4P"
        
        """        
        # Число атомов со степенью олигомеризации 1
        olig_num_1 = self._coordinate_numbers.count(1)
        # Число атомов со степенью олигомеризации 1
        olig_num_2 = self._coordinate_numbers.count(2)
        # Число атомов со степенью олигомеризации 1
        olig_num_3 = self._coordinate_numbers.count(3)
        # Число атомов со степенью олигомеризации 1
        olig_num_4 = self._coordinate_numbers.count(4)
        
        code = 'K' + str(olig_num_1) + str(1) + 'K' + str(olig_num_2) + str(2) + 'K' + str(olig_num_3) + str(3) + 'K' + str(olig_num_4) + str(4)
        
        return code

        