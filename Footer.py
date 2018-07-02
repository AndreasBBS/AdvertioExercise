from FooterExceptions import FooterError

class Footer:
    """This class constitutes a Footer, this is an element that allows to navigate a set \
    of pages"""

    def __init__(self, totalPages=1, boundaries=0, around=0, pagesURLs={1:''}):
        """Constructor"""
        if not isinstance(totalPages, int):
            raise FooterError("Invalid type for totalPages, please provide an Integer(int)")
        if not isinstance(boundaries, int):
            raise FooterError("Invalid type for boundaries, please provide an Integer(int)")
        if not isinstance(around, int):
            raise FooterError("Invalid type for around, please provide an Integer(int)")
        if totalPages <= 0:
            raise FooterError("Invalid value for totalPages, please provide a positive value")
        if boundaries < 0:
            raise FooterError("Invalid value for boundaries, please provide a non negative value")
        if around < 0:
            raise FooterError("Invalid value for around, please provide a non negative value")
        if boundaries > (totalPages-1)/2:
            raise FooterError("Invalid value for boundaries, please provide a value that's lower \
            than or equal to " + str((totalPages-1)/2))
        if around > (totalPages-1)/2:
            raise FooterError("Invalid value for around, please provide a value that's lower \
            than or equal to " + str((totalPages-1)/2))
        if not isinstance(pagesURLs, dict):
            raise FooterError("Invalid URL dictionary, please provide a dictionary")
        for key in list(pagesURLs):
            if not isinstance(key, int):
                raise FooterError("Dictionary can't have keys that are not Integers(int)")
            if key < 1:
                raise FooterError("Dictionary can't have keys that are lower than 1")
            if key > totalPages:
                raise FooterError("Dictionary can't have keys that are higher than" + totalPages)

        self.totalPages = totalPages
        self.boundaries = boundaries
        self.around = around
        self.currentPage = 1
        self.pagesURLs = pagesURLs # Storing pages URLs in dictionary so access time stays constant

    def setCurrentPage(self, desiredPage=1):
        """Setter for the currentPage attribute"""
        if not isinstance(desiredPage, int):
            raise FooterError("Invalid value for desired page, please provide an Integer(int)")
        if desiredPage < 1:
            raise FooterError("Invalid value for desired page, please provide a value higher than \
            0")
        if desiredPage > self.totalPages:
            raise FooterError("Invalid value for desired page, please provide a value lower than \
            the number of total pages")
        self.currentPage = desiredPage

    def _writeValues(self, start, end):
        """Auxiliary function to write the values of the print function"""
        result = ""
        for i in range(start, end+1):
            result += str(i) + " "
        return result

    def print(self):
        """Prints the Footer in time O(n)"""
        left = ""
        right = ""

        if self.currentPage - (self.boundaries + self.around) <= 1:
            #Meaning there's a straight sequence up until the current page
            left += self._writeValues(1, self.currentPage)
        else:
            left += self._writeValues(1, self.boundaries)
            if self.currentPage > 1:
                left += "... "
            if self.currentPage - self.around < self.totalPages - self.boundaries + 1:
                left += self._writeValues(self.currentPage - self.around, self.currentPage)
            else:
                #Accounting for the case when the current page is close to the end and the right
                #boundarie lowest value is lower than the current page minus the around.(ex:
                #TotalPages = 10, CurrentPage = 10, Boundarie = 3, Around = 1)
                left += self._writeValues(self.totalPages - self.boundaries + 1, self.currentPage)

        if self.currentPage + (self.boundaries + self.around) > self.totalPages:
            #Meaning there's a straight sequence from the current page until the total pages
            right += self._writeValues(self.currentPage + 1, self.totalPages)
        else:
            if self.currentPage + self.around > self.boundaries:
                right += self._writeValues(self.currentPage + 1, self.currentPage + self.around)
            else:
                #Accounting for the case when the current page is close to the beggining and the
                #boundarie is bigger than the current page plus the around (ex: TotalPages = 10,
                #CurrentPage = 1, Boundarie = 3, Around = 1)
                right += self._writeValues(self.currentPage + 1, self.boundaries)

            if self.currentPage + self.around < self.totalPages - self.boundaries:
                right += '... '
            right += self._writeValues(self.totalPages - self.boundaries + 1, self.totalPages)

        result = left + right
        result = result.rstrip(' ')
        print(result)
        return result
