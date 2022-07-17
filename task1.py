# Задание сформулированно несколько некорректно - так, в задание сказано, что подается массив чисел, состоящйий
# из единиц и нулей, тогда как в примере, в функцию подается строка, к тому же в задание
# сказано, что "Найти индекс первого нуля", а в примере возвращается иднекс последней единицы  
import unittest
from functools import singledispatch

@singledispatch
def task(array):
    if array[0] == 0:
        return 0
    def find_zero(array,  start, end):
        if end - start >= 2 or end  - start == 0 :
            
            mid = (start + end) // 2
            if array[mid] == 0:
                return find_zero(array,start = start ,end = mid)
            else:
                return find_zero(array, start = mid, end = len(array) - 1)
        else:
            return end
    return find_zero(array=array, start=0, end=len(array) - 1)


@task.register(str)
def _(array):
    if array[0] == '0':
        return 0    
    def find_zero(array,  start, end):
        
        if end - start >= 2 or end  - start == 0 :
            
            mid = (start + end) // 2
            if array[mid] == '0':
                return find_zero(array,start = start ,end = mid)
            else:
                return find_zero(array, start = mid, end = len(array) - 1)
        else:
            return end
    return find_zero(array=array, start=0, end=len(array) - 1)

class TestTask1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(task([1,1,1,0]),3)
        self.assertEqual(task([1,1,1,1,1,0,0]),5)
        self.assertEqual(task([0,0,0,0]), 0)
        self.assertEqual(task("111111111110000000000000000"),11)
        self.assertEqual(task([1,1,1,1,1,1,1,0]), 7)
    

if __name__ == '__main__':
    unittest.main()