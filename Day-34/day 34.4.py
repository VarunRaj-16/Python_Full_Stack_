import matplotlib.pyplot as plt
import seaborn as sns
print("7. HEATMAP")
data = [
    [80,75,90],
    [60,70,85],
    [95,88,92]
]
sns.heatmap(data,
            annot=True,
            cmap="YlOrRd",
            linewidths=1)
plt.title("Student Marks")
plt.show()
print("8. SUBPLOTS (Multiple Charts in One Figure)")
months = ["Jan","Feb","Mar","Apr"]
sales = [20,25,30,35]
profit = [5,7,8,10]
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(months, sales, marker="o")
plt.title("Sales")
plt.subplot(1,2,2)
plt.bar(months, profit)
plt.title("Profit")
plt.tight_layout()
plt.show()