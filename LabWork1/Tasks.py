import math
import datetime
import random
import itertools
from math import *
import numbers
import enum
import time


msgEnText = 'Enter the text: '

# Преобразование введенного дробного числа к денежному формату

def Ex1():
    summ = input('Enter sum: ').replace(',', '.').split('.')
    if int(summ[0]) < 0:
        raise Exception('ERROR! Incorrect format!')
    else:
        print(summ[0] + ' руб. ' + summ[1] + ' коп.')

        
# Проверка программно задаваемого списка на возрастание

def Ex2():
    flaxiness = [i for i in input('Add numbers: ').split(' ')]
    print(True) if [i for i in range(len(flaxiness) - 1) if flaxiness[i] <= flaxiness[i + 1]] else print(False)

    
# Замена символов на * с 4-го и до 4-х последних

def Ex3():
    MAX_LEN = 16

    card = input('Enter card-number: ').replace(' ', '').replace('-', '')
    print(card[:4] + '*' * 8 + card[12:MAX_LEN]) if len(card) == MAX_LEN else print('ERROR! Incorrect format!')

    
# Разделение текста на слова. Вывод слов длиной > 7, потом от 4 до 7, потом остальных

def Ex4():
    text = input(msgEnText).split(' ')
    print('Length > 7: {0}\n'.format([i for i in text if len(i) > 7]))
    print('Length 4 - 7: {0}\n'.format([i for i in text if len(i) >= 4 and len(i) <= 7]))
    print('Length <= 4: {0}\n'.format([i for i in text if len(i) < 4]))

    
# Привести к верхнему регистру все слова, начинающиеся с заглавной буквы

def Ex5():
    sourse = input().split(' ')
    print(' '.join([i.upper() if i == i.title() else i for i in sourse]))

    
# Вывести символы, встречающиеся в строке только один раз

def Ex6():
    sourse = input(msgEnText)
    print('Unique symbols:', ', '.join([i for i in sourse if sourse.count(i) == 1]))

    
# Скрипт должен обрабатывать список веб-адресов и проверять
# начинается ли с 'www.' - если да, то дописать 'http://' и затем
# проверить окончание на '.com' - если отсутствует - дописать
# Испольвать генераторы списков

def Ex7():
    urlList = ['www.facebook.com', 'webpage.com', 'www.vk', 'Animevost.org']
    AddStart = ['http://' + i if ('www.' in i) else 'http://www.' + i for i in urlList]
    print([i + '.com' if (not '.com' in i) else i for i in AddStart])
    

# Скрипт долен генерировать случайным образом число n от 1 до 10000 и
# создать массив из n целых чисел и дополнить его до размера ближайшей сверху степенью двойки

def Ex8():
    array = [int(random.uniform(1, 1000)) for i in range(0, int(random.uniform(1, 10000)))]
    newSize = 2 ** math.ceil(math.log2(len(array)))

    print('Size before: {0}\n'.format(len(array)))
    [array.append(random.uniform(1, 1000)) for i in range(len(array), newSize)]
    print('Size after: {0}\n'.format(len(array)))

    
# При вводе от пользователя суммы денег скрипт должен выдать
# кол-во купюр каждого наименования, иначе сообщение "Операция не может быть выполнена"

def PrintBank(bank):
    return bank[1000] * 1000 + bank[500] * 500 + bank[100] * 100 + bank[50] * 50 + bank[10] * 10


def GetBanknotes(bank, summ):
    for nominal in bank:
        _take = int(summ / nominal) // 1 if int(summ / nominal) // 1 <= bank[nominal] else bank[nominal]
        summ -= _take * nominal
        bank[nominal] = _take
    print(str(bank).replace(': ', '*').replace(', ', ' + '))

    
def Ex9():
    bank = {1000: 20, 500: 10, 100: 10, 50: 10, 10: 10}
    print('Bank summ: {0}\nBank: {1}'.format(PrintBank(bank), bank))

    money = int(input('Enter summ: '))
    if money > PrintBank(bank):
        raise Exception('ERROR! Operation can\'t be executed!')
    GetBanknotes(bank, money)

    
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
    playDate = datetime.datetime(2020, 9, 14, 22, 45)

    random.shuffle(teamList)
    groups = [teamList[i*4:i*4+4] for i in range(4)]
    [print('Group #:', i+1, ' - ', groups[i]) for i in range(len(groups))]

    for i in range(len(teamList)):
        print("Game #:", i, playDate.strftime("%d/%m/%Y %H:%M"))
        playDate += datetime.timedelta(days=14)
        
