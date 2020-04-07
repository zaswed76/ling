
import pandas as pd
import paths
from collections.abc import MutableSequence
from random import shuffle



class Item:
    def __init__(self, en, ru, rutrans, trans, image=None, index=0):
        self.index = index
        self.image = image
        self.en = en
        self.ru = ru
        self.rutrans = rutrans
        self.trans = trans

    def __lt__(self, other):
        return self.index < other.index

    def __gt__(self, other):
        return self.index > other.index

    def __repr__(self):
        return str([self.en, self.ru, self.index])

class Table(MutableSequence):
    def __init__(self, path):
        df = pd.ExcelFile(path)
        self.df1 = df.parse(df.sheet_names[0])
        self._lst = []
        self._init()
        self._index = -1


    def _init(self):
        for index, row in self.df1.iterrows():
            item = Item(row[0], row[1], row[2], row[3], index=index)
            self._lst.append(item)



    def reset(self):
        self._index = -1

    def shuffle(self):
        shuffle(self._lst)

    def reverse(self):
        self._lst.reverse()

    @property
    def data(self):
        return self._lst

    def __setitem__(self, index, value):
        self._lst[index] = value

    def __getitem__(self, index):
        return self._lst[index]

    def __len__(self):
        return len(self._lst)

    def __delitem__(self, index):
        del self._lst[index]

    def insert(self, index, value):
        self._lst.insert(index, value)

    def __repr__(self):
        return "-{}=".format(str(self._lst))

    def __iter__(self):
        return self

    def __next__(self):
        self._index+=1
        if self._index < len(self._lst):
            return self._lst[self._index]
        else:
            return None

if __name__ == '__main__':
    readTable = Table()
    readTable.shuffle()
    print(readTable.data)
