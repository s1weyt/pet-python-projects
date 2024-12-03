import matplotlib.pyplot as plt

labels = ['2017', '2018', '2019', '2020', '2021']
android_users = [53, 75, 85, 75, 86]
ios_users = [14, 21, 13, 22, 11]

width = 0.35  #Задаем ширину столбцов
fig, ax = plt.subplots()

ax.bar(labels, android_users, width, label='Android')
ax.bar(labels, ios_users, width, bottom=android_users, label='ios')
#Указываем с помощью параметра bottom, что значения в столбце должны быть выше значений переменной android_users

ax.set_ylabel('Соотношение, в %')
ax.set_title('Распределение устройств на Android и ios')
ax.legend(loc='lower left', title='Устройства')
#Сдвигаем легенду в нижний левый угол, чтобы она не перекрывала часть графика

plt.tight_layout()
plt.show()