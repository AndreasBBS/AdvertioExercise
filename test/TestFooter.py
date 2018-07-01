import unittest
from Footer import Footer
from FooterExceptions import FooterError

class TestUnsucessfulFooter(unittest.TestCase):
    """Tests the Footer class for incorrect input values and method use"""

    def testNegativeTotalPages(self):
        """Test passes if trying to create a Footer with a number of total pages equal to a negative ammount produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(-1, 0, 0)

    def testZeroTotalPages(self):
        """Test passes if trying to create a Footer with no total pages produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(0,0,0)

    def testFloatTotalPages(self):
        """Test passes if trying to create a Footer with a float for the total number of pages produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1.1,0,0)

    def testBoundariesHigherThanTotalPages(self):
        """Test passes if trying to create a Footer with the boundarie value higher than the total number of pages produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 2, 0)

    def testBoundariesInvalidTotalPages(self):
        """Test passes if trying to create a Footer with the boundarie value higher than (totalPages-1)/2 produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(3, 2, 0)

    def testNegativeBoundaries(self):
        """Test passes if trying to create a Footer with the boundarie value negative produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, -1, 0)

    def testFloatBoundaries(self):
        """Test passes if trying to create a Footer with the boundarie value a float produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 1.1, 0)

    def testAroundHigherThanTotalPages(self):
        """Test passes if trying to create a Footer with the around value higher than the total number of pages produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 0, 2)

    def testAroundInvalidTotalPages(self):
        """Test passes if trying to create a Footer with the around value higher than (totalPages-1)/2 produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(3, 0, 2)
    
    def testNegativeAround(self):
        """Test passes if trying to create a Footer with a negative around value produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 0, -1)

    def testFloatAround(self):
        """Test passes if trying to create a Footer with a float around value produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 0, 1.1)

class TestSucessfulFooter(unittest.TestCase):
    """Tests the Footer class for the expected behavior when the correct usage of the class is made"""

    def setUp(self):
        self.footer = Footer(10, 1, 1)

    def testFooterInit(self):
        """Tests the Footer initialization class"""
        self.assertEqual(self.footer.totalPages, 10)
        self.assertEqual(self.footer.boundaries, 1)
        self.assertEqual(self.footer.around, 1)
        self.assertEqual(self.footer.currentPage, 1)
    
    def testFooterStr(self):
        """Tests the Footer str class"""
        self.assertEqual(str(self.footer), "1|2|...|10")