# 生成器函数

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # for word in self.words:
        #     yield word
        # return
        return iter(self.words)


s = Sentence('"the time has come," the Walrus said,')
for word in s:
    print(word)
