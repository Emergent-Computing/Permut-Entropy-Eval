import unittest
import numpy as np
import random

#from PeEn-class_20250928 import perm_entropy
#from PeEn_evaluation import PeEn.perm_entropy as perm_entropy
from PeEn_evaluation import PeEn

#target = __import__("PeEn-2025-09-15.py")

#resultPeEn = target.perm_entropy

myPeEn = PeEn()

class TestPeE(unittest.TestCase):
    def test_PeE(self):
        """
        A battery of tests of the Permutation Entropy function. 

        """
        print('### ********************************************* ###\n')
        print('A battery of tests of the Permutation Entropy function.\n') 
        print('### ********************************************* ###\n')
        
        ### ********************************************* ###
        print('### ********************************************* ###\n')
        print('Test number 1:\n')
        print('### ********************************************* ###')
        array_size = 10
        data = np.zeros((array_size))
        data = [1,4,2,7,10,5,2,1,6,6]
        print(data)        
        pattern_length = 3
        delay = 1
        # perm_entropy(time_series, embed_dim, embed_delay)
        result = myPeEn.perm_entropy(data, pattern_length, delay)
        self.assertEqual(result, 0.8704188162777186) 
        ### ********************************************* ###

        ### ********************************************* ###
        print('\n### ********************************************* ###\n')
        print('Test number 2:\n')
        print('### ********************************************* ###')
        array_size = 7
        pattern_length = 3
        delay = 1
        data = np.zeros((array_size))
        data = [4,7,9,10,6,11,3]
        print(data)        
        # perm_entropy(time_series, embed_dim, embed_delay)
        result = myPeEn.perm_entropy(data, pattern_length, delay)
        self.assertEqual(result, 0.5887621559162939)
        ### ********************************************* ###

        ### ********************************************* ###
        print('\n### ********************************************* ###\n')
        print('Test number 3:\n')
        print('### ********************************************* ###')
        array_size = 8
        pattern_length = 3
        delay = 1
        data = np.zeros((array_size))
        data = [19,21,8,14,3,55,43,28,4,3]
        print(data)        
        # perm_entropy(time_series, embed_dim, embed_delay)
        result = myPeEn.perm_entropy(data, pattern_length, delay)
        self.assertEqual(result, 0.8339150226079424)
        ### ********************************************* ###
        
        ### ********************************************* ###
        print('\n### ********************************************* ###\n')
        print('Test number 4:\n')
        print('### ********************************************* ###')
        array_size = 20
        pattern_length = 3
        delay = 1
        data = np.zeros((array_size))
        random.seed(10)
        list_of_rnd_numbers = list(range(101))
        for i in range(array_size):
            data[i] = random.choice(list_of_rnd_numbers)
        print(data)
        # data = [1, 18, 17, 9, 1, 7, 3, 17, 0, 11, 0, 11, 4, 5, 8, 9, 18, 3, 2, 0]        
        # perm_entropy(time_series, embed_dim, embed_delay)
        result = myPeEn.perm_entropy(data, pattern_length, delay)
        self.assertEqual(result, 0.971093972079518)
        ### ********************************************* ###

        
        ### ********************************************* ###
        print('\n### ********************************************* ###\n')
        print('Test number 5:\n')
        print('### ********************************************* ###')
        array_size = 20
        pattern_length = 3
        delay = 2
        data = np.zeros((array_size))
        random.seed(10)
        list_of_rnd_numbers = list(range(101))
        for i in range(array_size):
            data[i] = random.choice(list_of_rnd_numbers)
        print(data)
        # data = [1, 18, 17, 9, 1, 7, 3, 17, 0, 11, 0, 11, 4, 5, 8, 9, 18, 3, 2, 0]        
        # perm_entropy(time_series, embed_dim, embed_delay)
        result = myPeEn.perm_entropy(data, pattern_length, delay)
        self.assertEqual(result, 0.9607329284860074)
        ### ********************************************* ###

        
        ### ********************************************* ###
        print('\n### ********************************************* ###\n')
        print('Test number 6:\n')
        print('### ********************************************* ###')
        array_size = 20
        pattern_length = 3
        delay = 4
        data = np.zeros((array_size))
        random.seed(10)
        list_of_rnd_numbers = list(range(101))
        for i in range(array_size):
            data[i] = random.choice(list_of_rnd_numbers)
        print(data)
        # data = [1, 18, 17, 9, 1, 7, 3, 17, 0, 11, 0, 11, 4, 5, 8, 9, 18, 3, 2, 0]        
        # perm_entropy(time_series, embed_dim, embed_delay)
        result = myPeEn.perm_entropy(data, pattern_length, delay)
        self.assertEqual(result, 0.9756641375534827)
        ### ********************************************* ###
        
        
        

if __name__=="__main__":
    unittest.main()
