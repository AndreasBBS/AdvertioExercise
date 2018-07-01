from FooterExceptions import FooterError

class Footer:

    def __init__(self, totalPages, boundaries, around):
        if(not isinstance(totalPages, int)):
            raise FooterError("Invalid type for totalPages, please provide an Integer(int)")
        if(not isinstance(boundaries, int)):
            raise FooterError("Invalid type for boundaries, please provide an Integer(int)")
        if(not isinstance(around, int)):
            raise FooterError("Invalid type for around, please provide an Integer(int)")
        if(totalPages <= 0):
            raise FooterError("Invalid value for totalPages, please provide a positive value")
        if(boundaries < 0):
            raise FooterError("Invalid value for boundaries, please provide a non negative value")
        if(around < 0):
            raise FooterError("Invalid value for around, please provide a non negative value")
        if(boundaries > (totalPages-1)/2):
            raise FooterError("Invalid value for boundaries, please provide a value that's lower than or equal to " + str((totalPages-1)/2))
        if(around > (totalPages-1)/2):
            raise FooterError("Invalid value for boundaries, please provide a value that's lower than or equal to " + str((totalPages-1)/2))
        
        self.totalPages = totalPages
        self.boundaries = boundaries
        self.around = around
        self.currentPage = 1

    def __str__(self):
        raise NotImplementedError('String Method for Footer not yet implemented')