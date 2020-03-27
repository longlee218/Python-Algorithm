class Parent:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    @property
    def getName(self):
        return self.name

    @property
    def getOld(self):
        return self.old

    @getName.setter
    def setName(self, name):
        self.name = name

    @getName.deleter
    def setName(self):
        self.name = None


if __name__ == '__main__':
    parent = Parent("Long", 18)
    print(parent.getName)
    print(parent.getOld)
    parent.name = "Hoang"
    print(parent.getName)
    del parent.setName
    print(parent.setName)
