import Book
from abc import *


class Library(object):

    book_code = 0

    def __init__(self, num, adr):
        self._num = num
        self._adr = adr
        self._book_collection = []
        book_code = len(self._book_collection)

        if num == '' or adr == '':
            raise ValueError('ERROR!!! Number field or addres field can\'t be empty!')


    def __iadd__(self, new_book):
        return self.__add__(new_book)


    def __add__(self, new_book):
        new_book._code = len(self._book_collection)
        self._book_collection += [new_book]
        return  self


    def __iter__(self):
        for book in self._book_collection:
            yield book