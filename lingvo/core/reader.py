# -*- coding: utf-8 -*-
from pathlib import Path

lst  = []
p = r"E:\pyprojects\ling\lingvo\core\dict.txt"
p2 = r"E:\pyprojects\ling\lingvo\core\dict2.txt"




if __name__ == '__main__':
    r = Reader(p)
    print(r.data)
    print(r.load(p2))
