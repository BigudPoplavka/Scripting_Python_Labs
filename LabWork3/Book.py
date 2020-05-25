from abc import abstractmethod


class ITaggable:

    @abstractmethod
    def tag(self):
        pass


class Book(ITaggable):

    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self._code = 0

        if title == '' or author == '':
            raise ValueError('ERROR!!! Title field or aouthor field can\'t be empty!')

    def tag(self):
        key_words = self.__title.replace(',', ' ').split()
        return [word for word in key_words if word.istitle()]

    def __str__(self):
        return "%s '%s'" % (self.__title, self.__author)




