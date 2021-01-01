class MyStrError(ValueError):
    def __init__(self, *args):
        self.my_list = []

    def values(self):
        while True:
            try:
                value = input("Введите число или 'q' для выхода: ")
                if value == 'q':
                    return (f"Ваш список: {self.my_list}")
                    break
                if not value.isdigit():
                    raise MyStrError("Вы ввели не число")

                self.my_list.append(value)
                print (f"Ваш список: {self.my_list}")
            except MyStrError as err:
                print(err)

ex = MyStrError()
print(ex.values())