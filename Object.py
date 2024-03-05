# @brief класс нашего объекта. Именно относително него и будут перегружены операторы >, <, >=, <=
class obj:
    def __init__(self, author:str, book:str, year:int, pages:int):
        self.author = author
        self.book = book
        self.year = year
        self.pages = pages
    # @brief <
    def __lt__(self, other): # <
        if self.author < other.author:
            return True
        elif self.author > other.author:
            return False
        else:
            if self.book < other.book:
                return True
            elif self.book > other.book:
                return False
            else:
                if self.year < other.year:
                    return True
                else:
                    return False
    # @brief <=
    def __le__(self, other): # <=
        if self.author < other.author:
            return True
        elif self.author > other.author:
            return False
        else:
            if self.book < other.book:
                return True
            elif self.book > other.book:
                return False
            else:
                if self.year < other.year:
                    return True
                elif self.year > other.year:
                    return False
                else:
                    return True
    # @brief >
    def __gt__(self, other): # >
        if self.author > other.author:
            return True
        elif self.author < other.author:
            return False
        else:
            if self.book > other.book:
                return True
            elif self.book < other.book:
                return False
            else:
                if self.year > other.year:
                    return True
                else:
                    return False
    # @brief >=
    def __ge__(self, other): # >=
        if self.author > other.author:
            return True
        elif self.author < other.author:
            return False
        else:
            if self.book > other.book:
                return True
            elif self.book < other.book:
                return False
            else:
                if self.year > other.year:
                    return True
                elif self.year < other.year:
                    return False
                else:
                    return True
    # @brief ==
    def __eq__(self, other): # ==
        if self.author != other.author:
            return False
        if self.book != other.book:
            return False
        if self.year != other.year:
            return False
        return True
