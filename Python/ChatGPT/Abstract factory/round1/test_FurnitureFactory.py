import unittest

# Assuming the original code is in a module named 'furniture'
from FurnitureFactory import *

class TestFurnitureFactory(unittest.TestCase):

    def test_victorian_chair(self):
        factory = VictorianFurnitureFactory()
        chair = factory.create_chair()
        self.assertIsInstance(chair, VictorianChair)
        self.assertEqual(chair.sit_on(), "Sitting on a Victorian Chair")

    def test_victorian_sofa(self):
        factory = VictorianFurnitureFactory()
        sofa = factory.create_sofa()
        self.assertIsInstance(sofa, VictorianSofa)
        self.assertEqual(sofa.lie_on(), "Lying on a Victorian Sofa")

    def test_modern_chair(self):
        factory = ModernFurnitureFactory()
        chair = factory.create_chair()
        self.assertIsInstance(chair, ModernChair)
        self.assertEqual(chair.sit_on(), "Sitting on a Modern Chair")

    def test_modern_sofa(self):
        factory = ModernFurnitureFactory()
        sofa = factory.create_sofa()
        self.assertIsInstance(sofa, ModernSofa)
        self.assertEqual(sofa.lie_on(), "Lying on a Modern Sofa")

if __name__ == '__main__':
    unittest.main()
