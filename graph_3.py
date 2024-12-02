import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]

plt.plot(x, y, color='green', marker='o', markersize=5)
plt.xlabel('Ось x') #Подпись для оси x
plt.ylabel('Ось y') #Подпись для оси y
plt.title('Первый график') #Название
plt.show()