import matplotlib.pyplot as plt
import seaborn as sns
print("3. HISTOGRAM")
marks = [45,56,67,78,89,90,55,60,61,70,72,85,92,68,73,81,65,74,77,88]
plt.hist(marks,
         bins=5,
         color="orange",
         edgecolor="black")
plt.title("Exam Score Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()
print("4. SCATTER PLOT")
hours = [1,2,3,4,5,6,7,8]
marks = [30,40,50,60,70,80,90,95]
plt.scatter(hours, marks,
            s=100,
            c="red",
            marker="o")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()
