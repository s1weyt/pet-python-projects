from fractions import Fraction

a = Fraction(6,4)
b = Fraction(7,12)
c = a * b
print(c)

#Получение числителя/знаменателя
print("Числитель=", c.numerator)
print("Знаменатель=", c.denominator)

#Конвертирование в float
print(float(c))

#Ограничение значения знаменателя
print(c.limit_denominator(8))

#Преобразование из float в дробь
x = 5.75
y = Fraction(*x.as_integer_ratio())
print(y)