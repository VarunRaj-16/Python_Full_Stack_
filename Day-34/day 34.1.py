# DAY 35 - MATPLOTLIB & DATA VISUALIZATION
import matplotlib.pyplot as plt
import seaborn as sns
print("1. LINE PLOT")
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20000, 25000, 22000, 30000, 35000]
plt.plot(months, sales,
         color="blue",
         marker="o",
         linestyle="-",
         linewidth=2,
         label="Monthly Sales")
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()
plt.show()
print("2. BAR CHART")
departments = ["CSE", "ECE", "EEE", "MECH"]
students = [120, 95, 80, 60]
plt.bar(departments, students,
        color="green",
        edgecolor="black",
        width=0.6)
plt.title("Department Strength")
plt.xlabel("Department")
plt.ylabel("Students")
plt.show()

