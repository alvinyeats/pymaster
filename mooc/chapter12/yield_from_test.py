# _*_ coding: utf-8 _*_
from itertools import chain


my_list = [1, 2, 3, 5]
my_dict = {
    "a1": "url1",
    "a2": "url2"
}


def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for value in my_iterable:
        #     yield value


# chain内部的可迭代对象是顺序相加然后再迭代的
# for value in chain(my_list, my_dict, range(5, 10)):
#     print(value)


for value in my_chain(my_list, my_dict, range(5, 10)):
    print(value)
