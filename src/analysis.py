
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\data-science assignment\data\students.csv")
dataset

dataset["average"] = dataset[["maths", "science", "english"]].mean(axis=1)
print("Average Marks per student:")
print(dataset[["student_name", "average"]])

class_average = dataset[["maths", "science", "english"]].mean()
print("\nClass Average per student :")
print(class_average)

topper = dataset.loc[dataset["average"].idxmax()]
print("\nTopper:")
print(topper["student_name"], "-", topper["average"])

plt.figure()
plt.bar(dataset["student_name"], dataset["average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average Marks per Student")
plt.savefig("output/plot.png")
plt.show
