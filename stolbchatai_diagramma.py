import matplotlib.pyplot as plt

a = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
b = [2,4,3,1,7]

plt.bar(a, b, label='Величина прибыли')  #Параметр label позволяет задать название величины для легенды
plt.plot(a, b, color='green', marker='o', markersize=7)

plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Комбинирование графиков')
plt.legend()

plt.tight_layout()
plt.show()