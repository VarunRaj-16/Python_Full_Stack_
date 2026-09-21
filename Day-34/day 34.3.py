import matplotlib.pyplot as plt
import seaborn as sns
print("5. PIE CHART")
brands = ["Apple","Samsung","OnePlus","Others"]
share = [35,30,20,15]
plt.pie(share,
        labels=brands,
        autopct="%1.1f%%",
        startangle=90,
        shadow=True)
plt.title("Mobile Market Share")
plt.show()
print("6. BOX PLOT")
salary = [25000,27000,30000,32000,35000,36000,38000,40000,42000,70000]
plt.boxplot(salary,
            showmeans=True,
            patch_artist=True)
plt.title("Salary Distribution")
plt.show()
