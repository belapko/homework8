class Data():
    def __init__(self, date):
        self.date = str(date)

    def __str__(self):
        return self.date

    @classmethod
    def extr(cls, date):
        new_date = []
        for i in date.split():
            if i.isdigit():
                new_date.append(int(i))
        return f"{new_date[0]} {new_date[1]} {new_date[2]}"

    @staticmethod
    def extr_2(date):
        new_date = []
        for i in date.split():
            if i.isdigit():
                new_date.append(int(i))

        if 1 <= new_date[0] <= 31 and 1 <= new_date[1] <= 12:
            return f"{new_date[0]} {new_date[1]} {new_date[2]}"
        else:
            return 'Недопустимое число или месяц'


date = Data('28 - 12 - 2020')
print(date)

print(date.extr('28 - 12 - 2020'))


print(date.extr_2('32 - 13 - 2020'))
print(Data.extr_2('28 - 12 - 2020'))


