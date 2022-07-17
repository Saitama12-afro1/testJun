import unittest

def task(x1,y1,x2,y2,x3,y3,x4,y4):
    if (x3 - x1) > 0 and  (a:=(x2 - x3)) > 0 and (b:=(y1-y3)) > 0 and (y3 - y2) > 0:
        return True,a * b
    if (a:=(x4 - x1)) > 0 and  (x2 - x4) > 0 and (y1-y4) > 0 and (b:=(y4 - y2)) > 0:
        return True, a * b
    if (x3 - x1) > 0 and  (a:=(x2 - x3)) > 0 and (b:=(y3-y1)) > 0 and (y2 - y3) > 0:
        return True, abs(a * b)
    if (x4 - x1) > 0 and  (a:=(x2 - x4)) > 0 and (y4-y1) > 0 and (b := (y2 - y4)) > 0:
        return True, a * b
    
    return False
print(task(2,2,5,5,1,7,3,3)) 
class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(task(2,2,5,5,1,7,3,3), (True,4))
        self.assertEqual(task(1,1,4,6,2,3,5,1),(True,4))
        self.assertEqual(task(5,3,7,1,6,2,8,4),(True, 1))
        self.assertEqual(task(25,100,100,25,50,50,0,0),(True, 2500))
        self.assertEqual(task(5,5,7,7,7,9,5,5),False)
        self.assertEqual(task(1,1,2,2,3,3,4,4),False)

if __name__ == '__main__':
    unittest.main()