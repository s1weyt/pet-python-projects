import matplotlib.pyplot as plt

vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]

plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title("Распределение марок автомобилей на дороге")

plt.tight_layout()
plt.show()