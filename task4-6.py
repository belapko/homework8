class Eq_Warehouse():
    def __init__(self):
        self.dictionary = {}

    def adding(self, equip):
        self.dictionary.setdefault(equip.group, []).append(equip)


    def delited(self, name):
        if self.dictionary[name]:
            print( f"{self.dictionary[name].pop(0)} отправлен на склад" )


class Equipment():

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.group = self.__class__.__name__
    def group(self):
        return f"{self.group}"

    def __repr__(self):
        return f"{self.name} {self.year}"

class Printer(Equipment):
    def __init__(self, series, name, year):
        super().__init__(name, year)
        self.series = series

    def __repr__(self):
        return f"{self.series} {self.name} {self.year}"

class Scanner(Equipment):
    def __init__(self, color, name, year):
        super().__init__(name, year)
        self.color = color

    def __repr__(self):
        return f"{self.color} {self.name} {self.year}"

class Copy_machine(Equipment):
    def __init__(self, maker, name, year):
        super().__init__(name, year)
        self.maker = maker

    def __repr__(self):
        return f"{self.maker} {self.name} {self.year}"


sklad = Eq_Warehouse()
cp = Copy_machine('hp', 'blabla', 2012)
sklad.adding(cp)
scaner = Scanner('blue', 'iris', 2003)
sklad.adding(scaner)
cp = Copy_machine('xerox', 'b120', 2018)
sklad.adding(cp)
printer = Printer('b2183', 'Kyosera', '2005')
sklad.adding(printer)
print(sklad.dictionary)
sklad.delited('Copy_machine')

print(sklad.dictionary)

