import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Arun", "Bala", "Karthik", "Ravi", "Vijay"],
    "Marks": [85, 92, 78, 88, 95]
}

df = pd.DataFrame(data)

plt.bar(df["Student"], df["Marks"])

plt.title("Student Marks Analysis")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
