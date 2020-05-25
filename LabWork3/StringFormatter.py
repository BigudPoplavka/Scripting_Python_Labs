import string
import re
import os


class StringFormatter(object):
    separators = [' ']

    def __init__(self, txt):
        self._txt = txt

    def sf_delete(self, n):
        return ' '.join([word for word in self._txt.split(' ') if len(word) > n])

    def sf_digit_replace(self):
        return re.sub('\d', '*', self._txt)

    def sf_insert_spaces(self):
        return ' '.join([i for i in ' '.join(self._txt)])

    def sf_sort_by_size(self):
        return ' '.join(sorted(self._txt.split(), key=lambda word: len(word)))

    def sf_sort_by_lec(self):
        return ' '.join(sorted(self._txt.split()))
    
