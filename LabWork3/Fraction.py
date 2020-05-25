class Fraction(object):

    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        self.reduce()


    def __str__(self):
        return "%d/%d" % (self.__num, self.__den)


    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)


    def __neg__(self):
        a = self.__num * -1
        return Fraction(a, self.__den)


    def __invert__(self):
        a, b = self.__den, self.__num
        return Fraction(a, b)


    def __pow__(self, power, modulo=None):
        a, b = self.__num ** power, self.__den ** power
        return Fraction(a, b)


    def __float__(self):
        return self.__num / self.__den


    def __int__(self):
        return int(self.__num)

    def reduce(self):
        self.gcd(self.__num, self.__den)