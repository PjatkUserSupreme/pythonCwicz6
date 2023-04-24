import Element


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        tmp = self.head
        str = ""
        str += tmp.data
        str += ", "
        while 1 == 1:
            tmp = tmp.nextE
            str += tmp.data
            if tmp == self.tail:
                break
            str += ", "
        return str

    def get(self, e):
        i = 0
        tmp = self.head
        while i < e:
            tmp = tmp.nextE
            i += 1
        return tmp

    def delete(self, e):
        if e == 0:
            self.head = self.head.nextE
            return 0

        i = 0
        previous = None
        tmp = self.head

        while i < e:
            previous = tmp
            tmp = tmp.nextE
            i += 1

        previous.nextE = tmp.nextE
        return 0

    def append(self, e, func=None):
        if func is None:
            func = lambda a, b: a >= b

        if self.size == 0:
            self.head = e
            self.tail = e
            self.size = self.size + 1
            return 0

        i = 0
        if func(e.data, self.head.data):
            e.nextE = self.head
            self.head = e
            self.size = self.size + 1
            return 0
        tmp = self.head
        while i < self.size:
            if func(e.data, tmp.nextE.data):
                e.nextE = tmp.nextE
                tmp.nextE = e
                self.size = self.size + 1
                return 0

        self.tail.nextE = e
        self.size = self.size + 1
        return 0

