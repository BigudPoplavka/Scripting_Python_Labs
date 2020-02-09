import math
from math import *
import numbers
import enum
import random
import time
import datetime

#global variables
msgEnText = 'Enter the text: '

# Преобрахование введенного дробного числа к денежному формату
def Ex1():
    summ = input('Enter sum: ').replace(',', '.').split('.')
    if int(summ[0]) < 0:
        raise Exception('ERROR! Incorrect format!')
    else:
        print(summ[0] + ' руб. ' + summ[1] + ' коп.')

# Проверка программно задаваемого списка на возрастание
def Ex2():
    maxSize = 100
    i = 0
    l = []

    while i < maxSize:
        l.append(int(input('Add elem: ')))
        if len(l) > 1:
            if l[i] > l[i - 1]:
                print('true - flaxiness is increasing')
            else:
                print ('false - flaxiness is decreasing')
                break
        i += 1

# Замена символов на * с 4-го и до 4-х последних
def Ex3():
    maxLen = 16
    num = input('Enter card-number: ')
    passw = '********'

    if len(num) < maxLen:
        raise Exception('Incorrect number format!')
    else:
        preNum = num[:4]
        pastNum = num[12:maxLen]
    print ('Your card-number: {0}{1}{2}'.format(preNum, passw, pastNum))

# Разделение текста на слова. Вывод слов длиной > 7, потом от 4 до 7, потом остальных
def getWords(text):
    text = text.replace('\n', ' ')
    text = text.replace('.', '').replace(',', '').replace('?', '').replace('!', '').replace(':', '')
    words = text.split()
    return words

def processText(array):
    print('\nДлины больше 7 символов: \n')
    for i in range(0, len(array)):
        if len(array[i]) > 7:
            print('{0} - {1} символов'.format(array[i], len(array[i])))

    print('\nДлины от 4 до 7 символов:\n')
    for i in range(0, len(array)):
        if len(array[i]) > 4 and len(array[i]) < 7:
            print('{0} - {1} символов'.format(array[i], len(array[i])))

    print('\nОстальные длины слов: \n')
    for i in range(0, len(array)):
        if len(array[i]) <= 4:
            print('{0} - {1} символов'.format(array[i], len(array[i])))

def Ex4():
    minLen = 4
    maxLen = 7

    sourse = input(msgEnText)
    print(processText(getWords(sourse)))

# Привести к верхнему регистру все слова, начинающиеся с заглавной буквы
def Ex5():
    sourse = input(msgEnText)
    words = sourse.split()

    for i in range(len(words)):
        if words[i] == words[i].title():
            sourse = sourse.replace(words[i], words[i].upper())
    print(sourse)

# Вывести символы, встречающиеся в строке только один раз
def Ex6():
    sourse = input(msgEnText)
    count = 0

    for i in range(len(sourse)):
        if sourse.count(sourse[i]) == 1:
            count += 1
            print(sourse[i])
    print('Всего уникальных символов: {0}'.format(count))

# Скрипт должен обрабатывать список веб-адресов и проверять
# начинается ли с 'www.' - есил да, то дописать 'http://' и затем
# проверить окончание на '.com' - если отсутствует - дописать
# Испольвать генераторы списков
def Ex7():
    www = 'www.'
    com = '.com'
    http = 'http://'
    urlList = ['www.facebook.com', 'webpage.com', 'www.vk', 'Animevost.org']

    AddStart = [http + i for i in urlList if(www in i)]
    AddEnd = [i + com if(not com in i) else i for i in AddStart]

    print(AddEnd)

# Скрипт долен генерировать случайным образом число n от 1 до 10000 и
# создать массив из n целых чисел и дополнить его до размера ближайшей сверху степенью двойки
def Ex8():
    maxRand = 10000
    maxPow = 14    #т.к. 14-я степень двойки = первому числу больше 10000
    k = 0
    n = int(random.uniform(1, maxRand))
    array = []

    for i in range(0, n):
        array.append(int(random.uniform(1, maxRand)))

    for i in range(0, maxPow):
        if 2**i > n:
            k = 2**i
            break

    while len(array) != k:
        array.append(0)

# При вводе от пользователя суммы денег скрипт должен выдать
# кол-во купюр каждого наименования, иначе сообщение "Операция не может быть выполнена"
def PrintBank(bank):
    return bank[1000] * 1000 + bank[500] * 500 + bank[100] * 100 + bank[50] * 50 + bank[10] * 10

def printBanknotes(bank):
      res = ''
      for i in bank.keys():
            res = res + str(i) + '*' + str(bank[i]) + '+'
      print(res)

def Calculating(bank, summ, nominal):
    _ToTake = int(summ / nominal) // 1
    _TryTake = nominal * bank[nominal] - _ToTake * nominal

    if _TryTake >= 0:
        _CanTake = _ToTake * nominal
        bank[nominal] = _ToTake
        summ -= _CanTake
        return _ToTake, int(summ)
    else:
        return 0

def GetBanknotes(bank, summ, nominal):
    if PrintBank(bank) < summ:
        raise Exception('ERROR! Ammount too big!')
    newSumm = 0
    bank[nominal], newSumm = Calculating(bank, summ, nominal)

    return int(newSumm)

def Ex9():
    bank = {1000: 20, 500: 10, 100: 10, 50: 10, 10: 10}
    BANK_MAX = PrintBank(bank)
    print('Bank: {0}'.format(PrintBank(bank)))

    try:
        money = int(input('Enter summ: '))
        if money % 10 != 0:
            raise Exception('ERROR! Impossible to execute!')

        for banknote in bank.keys():
            money = GetBanknotes(bank, money, banknote)

        print('---------------------\n')
        printBanknotes(bank)
        print('Bank: '.format(BANK_MAX - money))
        print('Your payment: {0}'.format(PrintBank(bank)))
    except ValueError:
        print('ERROR! Incorrect input!')

# Скрипт, провер\ющий надежность введенного пароля
# хорошая длина пароля - защита беззащитной лоле =)
def CheckPassword(passw, maxSize):
    if len(passw) < 1 or len(passw) > maxSize:
        raise Exception('ERROR! Incorrect length of password!')

    notUnique = passw.isalpha() or passw.islower() or passw.isupper() or passw.isnumeric()
    unique = not passw.isalpha() and passw.islower()
    fullUnique = not passw.isalpha() and not passw.islower() and not passw.isnumeric()

    lowDef = len(passw) < 5
    middleDef = len(passw) >= 5 and len(passw) <= 7 and unique or notUnique
    goodDef = len(passw) >= 5 and len(passw) <= 8 and fullUnique
    veryGoodDef = len(passw) > 8 and fullUnique

    if lowDef:
        print('Low defence!\n You can create a long password with numbers and symbols\n:(')
    elif middleDef:
        print('Middle (not bad) defence!\n You can create a longer password with numbers and with different case characters\n:|')
    elif goodDef:
        print('Good defence!\n Password is not very long but with different case characters and numbers\n:)')
    elif veryGoodDef:
        print('Very good defence!\n Password is long enough with different case characters and numbers\n:)')


def Ex10():
    MAX_LEN = 12
    password = input('Create password max (size 12): ')
    CheckPassword(password, MAX_LEN)


# Написать генератор frange как аналог range с дробным шагом
def frange(start, end, step):
    while start <= (end - step):
        yield float('{:.1f}'.format(start + step))
        start += step

def Ex11():
    for x in frange(1, 5, 0.1):
        print(x)

# напишите генератор get_frames(), который производит "оконную декомпозицию сигнала"
# на основе входного списка генерирует набор списков размера size и степенью перекрытия overlap
# Пример вызова:
# for frame in get_frames(signal, size=2, overlap=0.5):
#   print(frame)
def get_frames(signal, size, overlap):
    showLen = int(size * overlap)
    currStep = 0

    while currStep < len(signal) - 1:
        yield signal[currStep: currStep + size]
        currStep += showLen

def Ex12():
    try:
        slen = int(input('Enter length of signal: '))
        signal = [i for i in range(slen)]

        for frame in get_frames(signal, 4, 0.5):
            print(frame)
    except ValueError:
        print('ERROR! Incorrect format')


# Написать генератор extra_enumerate()
# пример вызова: for i, elem, sum, frac in extra_enumerate(x): рrint(elem, sum, frac)
# где sum хранит накопленную сумму на момент текущей итерации i,
# frac хранит долю накопленной суммы от всей суммы: например
# для списка x = [1, 3, 4, 2] выведет: [1, 1, 0.1]   [3, 4, 0.4]   [4, 8, 0.8]   [2, 10, 1]
def extra_enumerate(x):
    temp = 0
    for i in x:
        temp += i
        yield i, temp, temp/sum(x)

def Ex13():
    x = [1, 3, 4, 2]
    for elem, summ, frac in extra_enumerate(x):
        print(elem, summ, frac)


# Написать декоратор non_empty, проверяющий списковый результат любой функции:
# если в нем содержатся пустые строки или значение None, то они удаляются
def non_empty(listRetFunction):
    def wrapper():
        returned = listRetFunction()
        deleted = 0

        for i in returned:
            if i is None or i == '':
                returned.pop(deleted)
            deleted += 1
        return returned
    return  wrapper

@non_empty
def getList():
    return ['chapter1', '', 'contents', '', 'line1']

def Ex14():
    print(getList())


# Напишите параметризированный декоратор pre_process, осуществляющий
# предварительную обработку (цифровую фильтрацию) списка по алгоритму:
# s[i] = s[i]-a*s[i - 1]. Параметр а можно задать в коде
def pre_process(a):
    def middleDecorator(listRetFunction):
        def wrapper(*args):
            s = args[0]
            for i in range(len(s)):
                s[i] = s[i] - a * s[i - 1]
                print('a = {0}'.format(a))
                listRetFunction(s)
        return  wrapper
    return middleDecorator

@pre_process(a=0.95)
def plot_signal(s):
    for sample in s:
        print(sample)

def Ex15():
    signal = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    plot_signal(signal)


# Напишите скрипт, который на основе списка из 16 названий футбольных команд случайным образом
# формирует 4 группы по 4 команды, а также выводит на консоль календарь всех игр (игры
# должны проходить по средам, раз в 2 недели, начиная с 14 сентября текущего года).
# команды, а также выводит на консоль календарь всех игр (игры должны проходить по средам, раз в 2 недели,
# начиная с 14 сентября текущего года). Даты игр необходимо выводить в формате «14/09/2016, 22:45».
# Используйте модуль random.
def Ex16():
    teamList = [
        'Барселона', 'Реал Мадрид', 'Манчестер Юнайтед', 'Наполи',
        'Ювентус', 'Бавария', 'Галатасарай', 'Милан',
        'Ливерпуль', 'Интер', 'Марсель', 'Арсенал',
        'Боруссия', 'Челси', 'Лион', 'Фенербахче'
    ]
    groups = [[], [], [], []]

    random.shuffle(teamList)
    for i in range(0, 16, 4):
        groups[int(i / 4) - 1] = teamList[i:i + 4]

    for i in range(len(groups)):
        print('Group #{0}: {1}\n'.format(i + 1, groups[i]))

    playDate = datetime.datetime(2020, 9, 14, 22, 45)
    match = ''
    i = 0
    while i < len(teamList):
        match += 'MATCH: {1} VS. {0}'.format(teamList[i], teamList[i+1])
        print(match, playDate.strftime("%d/%m/%Y %H:%M"))
        match = ''
        playDate = playDate + datetime.timedelta(days=14)
        i += 2





















#дней в году