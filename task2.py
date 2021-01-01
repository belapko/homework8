# class MyZeroDivisionError(Exception):
#     @staticmethod
#     def quotient():
#         while True:
#             try:
#                 divisible = int(input())
#                 divisor = int(input())
#                 quotient = divisible / divisor
#                 if divisor <= 0:
#                     raise ZeroDivisionError
#             except ZeroDivisionError:
#                 print ("Недопустимо деление на ноль")
#             else:
#                 return (quotient)
#
# print(MyZeroDivisionError.quotient())

class MyZeroDivisionError(ZeroDivisionError):
    @staticmethod
    def quotient():
        while True:
            try:
                divisible = input("Введите делимое или 'q' для выхода: ")
                if divisible == 'q':
                    return ("Работа завершена!")
                    break
                divisor = input("Введите делитель: ")
                if float(divisor) <= 0:
                    raise MyZeroDivisionError("Недопустимо деление на нуль")
                print(float(divisible) / float(divisor))

            except MyZeroDivisionError as err:
                print(err)

print(MyZeroDivisionError.quotient())