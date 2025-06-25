import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['red', 'blue', 'green', 'orange', 'purple']

plt.figure(figsize=(8, 6))
plt.bar(products, sales, color=colors)

plt.title("Mahsulotlar bo‘yicha sotuvlar")
plt.xlabel("Mahsulotlar")
plt.ylabel("Sotuv miqdori")
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
