from collections.abc import MutableSequence


class Table(MutableSequence):
    def __init__(self, *args):
        self.__data = list(args)
        self.__index = -1

    @property
    def data(self):
        return self.__data

    def __setitem__(self, index, value):
        self.__data[index] = value

    def __getitem__(self, index):
        return self.__data[index]

    def __len__(self):
        return len(self.__data)

    def __delitem__(self, index):
        del self.__data[index]

    def insert(self, index, value):
        self.__data.insert(index, value)

    def __repr__(self):
        return "{}".format(str(self.__data))

    def __iter__(self):
        return self

    def __next__(self):
        self.__index+=1
        if self.__index < len(self.__data):
            return self.__data[self.__index]
        else:
            return None

if __name__ == '__main__':
    t = Table("item1", "item2")
    print(t)
    t.clear()
    print(t.extend())