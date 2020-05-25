from Fraction import  *
from Book import  *
from Library import  *
from StringFormatter import  *

def ex1():
    frac = Fraction (2, 7)

    print(-frac)
    print(~frac)
    print(frac**2)
    print(float(frac))
    print(int(frac))


def ex2():
    lib_1 = Library(12, '12 BooksWay St.')
    lib_1 += Book('Call of Cthulhu', 'Howard Lovecraft')
    lib_1 += Book('Sherlock Holmes', 'Arthur Conan Doyle')
    lib_1 += Book('Tokyo Ghoul', 'Sui Ishida')

    lib_2 = Library(13, '157 Church ave.')
    lib_2 += Book('Bible', 'Holy Spirit')
    lib_2 += Book('Writings from Africa', 'Curry R. Blake')
    lib_2 += Book('Divine Healing: A Gift from God', 'John G Lake')

    for book in lib_1._book_collection:
        print(book._code, book, ' - ', book.tag())

    print('\n', '*' * 16, '\n')

    for book in lib_2._book_collection:
        print(book._code, book, ' - ', book.tag())


#def ex3():


def ex4():
    test = 'loli loli2 loli3 111 hellooo00 rytrytrryty666 animation wooord'

    sf = StringFormatter(test);
    print(sf.sf_delete(5))
    print(sf.sf_digit_replace())
    print(sf.sf_sort_by_size())
    print(sf.sf_insert_spaces())
    print(sf.sf_sort_by_lec())


def ex5():