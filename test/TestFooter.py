import unittest
from Footer import Footer
from FooterExceptions import FooterError

class TestUnsucessfulFooter(unittest.TestCase):
    """Tests the Footer class for incorrect input values and method use"""

    def testNegativeTotalPages(self):
        """Test passes if trying to create a Footer with a number of total pages equal to a
        negative ammount produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(-1, 0, 0)

    def testZeroTotalPages(self):
        """Test passes if trying to create a Footer with no total pages produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(0, 0, 0)

    def testFloatTotalPages(self):
        """Test passes if trying to create a Footer with a float for the total number of pages
        produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1.1, 0, 0)

    def testBoundariesHigherThanTotalPages(self):
        """Test passes if trying to create a Footer with the boundarie value higher than the total
        number of pages produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 2, 0)

    def testBoundariesInvalidTotalPages(self):
        """Test passes if trying to create a Footer with the boundarie value higher than
        (totalPages-1)/2 produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(3, 2, 0)

    def testNegativeBoundaries(self):
        """Test passes if trying to create a Footer with the boundarie value negative produces a
        FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, -1, 0)

    def testFloatBoundaries(self):
        """Test passes if trying to create a Footer with the boundarie value a float produces a
        FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 1.1, 0)

    def testAroundHigherThanTotalPages(self):
        """Test passes if trying to create a Footer with the around value higher than the total
        number of pages produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 0, 2)

    def testAroundInvalidTotalPages(self):
        """Test passes if trying to create a Footer with the around value higher than
        (totalPages-1)/2 produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(3, 0, 2)

    def testNegativeAround(self):
        """Test passes if trying to create a Footer with a negative around value produces a
        FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 0, -1)

    def testFloatAround(self):
        """Test passes if trying to create a Footer with a float around value produces a
        FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 0, 1.1)

    def testSetCurrentPageNegative(self):
        """Test passes if trying to set a Negative number for the current page produces
        a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 0, 0).setCurrentPage(-1)

    def testSetCurrentPageFloat(self):
        """Test passes if trying to set a float for the current page produces a
        FooterError"""
        with self.assertRaises(FooterError):
            Footer(2, 0, 0).setCurrentPage(1.1)

    def testSetCurrentPageHigherTotalPages(self):
        """Test passes if trying to set a number higher than the number of total pages
        for the current page produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 0, 0).setCurrentPage(2)

    def testSetCurrentPageZero(self):
        """Test passes if trying to set zero for the current page produces a FooterError"""
        with self.assertRaises(FooterError):
            Footer(1, 0, 0).setCurrentPage(0)

class TestSucessfulFooter(unittest.TestCase):
    """Tests the Footer class for the expected behavior when the correct usage of the class is
    made"""

    def testSetCurrentPage(self):
        """Tests the Footer setCurrentPage method for its expected behavior"""
        footer = Footer(10, 0, 0)
        self.assertEqual(footer.currentPage, 1)
        footer.setCurrentPage(5)
        self.assertEqual(footer.currentPage, 5)

    def testDefaultPrintB0A0(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 0,
        around = 0, current page = 1"""
        self.assertEqual(Footer(10, 0, 0).print(), "1 ...")

    def testDefaultPrintB1A0(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 1,
        around = 0, current page = 1"""
        self.assertEqual(Footer(10, 1, 0).print(), "1 ... 10")

    def testDefaulPrintB0A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 0,
        around = 1, current page = 1"""
        self.assertEqual(Footer(10, 0, 1).print(), "1 2 ... ")

    def testDefaultPrintB1A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 1,
        around = 1, current page = 1"""
        self.assertEqual(Footer(10, 1, 1).print(), "1 2 ... 10")

    def testDefaultPrintB1A2(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 1,
        around = 2, current page = 1"""
        self.assertEqual(Footer(10, 1, 2).print(), "1 2 3 ... 10")

    def testDefaultPrintB2A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 2,
        around = 1, current page = 1"""
        self.assertEqual(Footer(10, 2, 1).print(), "1 2 ... 9 10")

    def testDefaultPrintB3A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 3,
        around = 1, current page = 1"""
        self.assertEqual(Footer(10, 3, 1).print(), "1 2 3 ... 8 9 10")

    def testCP3B3A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 3,
        around = 1, current page = 3"""
        self.assertEqual(Footer(10, 3, 1).setCurrentPage(3).print(), "1 2 3 4 ... 8 9 10")

    def testPrintCP5B0A0(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 0,
        around = 0, current page = 5"""
        self.assertEqual(Footer(10, 0, 0).setCurrentPage(5).print(), "... 5 ...")

    def testPrintCP5B1A0(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 1,
        around = 0, current page = 5"""
        self.assertEqual(Footer(10, 1, 0).setCurrentPage(5).print(), "1 ... 5 ... 10")

    def testPrintCP5B0A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 0,
        around = 1, current page = 5"""
        self.assertEqual(Footer(10, 0, 1).setCurrentPage(5).print(), "... 4 5 6 ...")

    def testPrintCP5B1A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 1,
        around = 1, current page = 5"""
        self.assertEqual(Footer(10, 1, 1).setCurrentPage(5).print(), "1 ... 4 5 6 ... 10")

    def testPrintCP5B3A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 3,
        around = 1, current page = 5"""
        self.assertEqual(Footer(10, 3, 1).setCurrentPage(5).print(), "1 2 3 4 5 6 ... 8 9 10")

    def testPrintCP5B3A2(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 3,
        around = 2, current page = 5"""
        self.assertEqual(Footer(10, 3, 2).setCurrentPage(5).print(), "1 2 3 4 5 6 7 8 9 10")

    def testPrintCP5B4A4(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 4,
        around = 4, current page = 5"""
        self.assertEqual(Footer(10, 4, 4).setCurrentPage(5).print(), "1 2 3 4 5 6 7 8 9 10")

    def testPrintCP6B3A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 3,
        around = 1, current page = 6"""
        self.assertEqual(Footer(10, 3, 1).setCurrentPage(6).print(), "1 2 3 ... 5 6 7 8 9 10")

    def testPrintCP10B0A0(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 0,
        around = 0, current page = 10"""
        self.assertEqual(Footer(10, 0, 0).setCurrentPage(10).print(), "... 10")

    def testPrintCP10B1A0(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 1,
        around = 0, current page = 10"""
        self.assertEqual(Footer(10, 1, 0).setCurrentPage(10).print(), "1 ... 10")

    def testPrintCP10B0A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 0,
        around = 1, current page = 10"""
        self.assertEqual(Footer(10, 0, 1).setCurrentPage(10).print(), "... 9 10")

    def testPrintCP10B1A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 1,
        around = 1, current page = 10"""
        self.assertEqual(Footer(10, 1, 1).setCurrentPage(10).print(), "1 ... 9 10")

    def testPrintCP10B2A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 2,
        around = 1, current page = 10"""
        self.assertEqual(Footer(10, 2, 1).setCurrentPage(10).print(), "1 2 ... 9 10")

    def testPrintCP10B1A2(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 2,
        around = 1, current page = 10"""
        self.assertEqual(Footer(10, 1, 2).setCurrentPage(10).print(), "1 ... 8 9 10")

    def testPrintCP10B3A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 3,
        around = 1, current page = 10"""
        self.assertEqual(Footer(10, 3, 1).setCurrentPage(10).print(), "1 2 3 ... 8 9 10")

    def testPrintCP8B3A1(self):
        """Tests the Footer print method for an instance with total 10 pages, boundaries = 3,
        around = 1, current page = 8"""
        self.assertEqual(Footer(10, 3, 1).setCurrentPage(8).print(), "1 2 3 ... 7 8 9 10")
    