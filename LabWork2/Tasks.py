import re
from math import *
import pathlib
import shutil
import glob
import re
import os
import hashlib

# Прочитать текстовые данные из файла, игнорируя знаки препинания и проблелы.
# Вывести все символы в порядке частоты встречаемости в тексте

def ex1():
    try:
        with open(r'.\test_1.txt', 'r') as file:
            text = file.read().replace(' ', '').replace(',', '').replace('.', '').replace('-', '').lower()
            count_symb = {i:text.count(i) for i in text}
            print(count_symb, '\n', [i[0] for i in sorted(count_symb.items(), reverse=True)], '\n')
    except FileNotFoundError:
        print('ERROR! File not found!')


# Вывести все файлы-дубликаты на основе сравнения их контрольных сумм (MD5)
# Файлы могут иметь одно содержимое, но отличаться именами

def ex2():
    curr_path = os.getcwd()
    file_hash = dict()

    for files in os.listdir(curr_path):
        if os.path.isfile(files):
            with open(files, "rb") as file:
                file_hash.setdefault(hashlib.md5(file.read()).digest(), []).append(file.name)
    print(str([file_hash[f_name] for f_name in file_hash if len(file_hash[f_name]) > 1]).replace('[', '').replace(']', ''), '\n')


# Считать из файла названия музыкальных файлов и переименовать на их основе все файлы в папке

def ex3():
    path = './test_3'

    try:
        if not os.path.exists(path):
            raise Exception('ERROR!!! Folder not found!')
        with open('./test_3.txt', 'r', encoding='utf-8') as names:
            for file in os.listdir(path):
                os.replace(path + '/' + file, path + '/' + names.readline().rstrip() + '.mp3')
        os.startfile(path + '/Periphery - MAKE TOTAL DESTROY.mp3')     #GOT DJENT!!!
    except FileNotFoundError:
        print('ERROR! File not found!')


# С помощью регулярного выражения найти все подстроки вида 83ххх, где ххх - любые 3 цифры
# Текст считывается из файла, имя которого вводится с клавиатуры

def get_file(file_name):
    if os.path.exists(os.getcwd() + '\\' + file_name):
        with open(file_name, 'r') as file:
            text = [i for i in file]
        return text


def get_substrings(text, expr):
    for str_index in range(len(text)):
        curr_count = 0
        curr_substr = re.search(expr, text[str_index])

        while curr_substr != None:
            yield str_index + 1, curr_substr.regs[0][0] + curr_count + 1, curr_substr.group
            curr_count += curr_substr.regs[0][1]
            text[str_index] = text[str_index][curr_substr.regs[0][1]:]
            curr_substr = re.search(expr, text[str_index])


def ex4():
    expr = r'83\d\d\d'
    output = 'Строка №{0}, позиция: {1} - найдено [{2}]'

    try:
        text = get_file(input('Enter file-name: '))
        print([output.format(line, pos, substr) for line, pos, subsrt in get_substrings(text, expr)])
    except FileNotFoundError:
        print('ERROR! File not found!')


def ex5():
    expr = r'[A-Z][A-Za-z]+([0-9]{2}$|[0-9]{4}$)'
    text = input('Enter text: ')
    print([str(substr) for line, pos, subsrt in get_substrings(text, expr)])


def ex6():
    os.mkdir(r'D:\\Lab2Test')
    subprocess.call('reorganize.py --sourse \'D:\\Lab2Test\' --days 2 --size 4096', shell=True)
