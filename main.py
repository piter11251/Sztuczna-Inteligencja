import pandas as pd
import numpy as np

heart_disease = pd.read_csv(
    "../../dane/heartdisease.txt",
    sep=" ",
    header=None,
    names=["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13"]
)

# 3a, symbole klas decyzyjnych
print(heart_disease["a13"].unique())

# 3b, wielkosci klas decyzyjnych
print(len(heart_disease))

# 3c, min i max wartosci poszczegolnych atrybutow
print(f"Max: {heart_disease.max(axis=0)}\n")
print(f"Min: {heart_disease.min(axis=0)}\n")

# 3d, liczba roznych dostepnych wartosci
print("Liczba roznych dostepnych wartosci: \n")
print(heart_disease.nunique())
print("\n")

# 3e
print("Lista wszystkich roznych dostepnych wartosci dla kazdego atrybutu")
for columns in heart_disease.columns:
    print(f"{columns}: {list(heart_disease[columns].unique())}")
print("\n")

print("Odchylenie standardowe")
print(heart_disease.std())

# 4a
unknown_values = int(0.1*len(heart_disease))
mode = heart_disease.mode()
new_data={}
for columns in heart_disease.columns:
    new_data[columns] = [mode[columns]]*unknown_values
df = pd.DataFrame(new_data)
print(df)

heart_disease = pd.concat([heart_disease, df], ignore_index=False)
print(heart_disease)

# 4b
def normalization(attr, a, b):
    min_value = attr.min()
    max_value = attr.max()
    return a+((attr-min_value)*(b-a))/(max_value-min_value)

intervals = {
    "<0,1>":(0,1),
    "<-1,1":(-1,1),
    "<-10,10>":(-10,10)
}

normalized_df = pd.DataFrame()

for columns in heart_disease.columns:
    if heart_disease[columns].dtype == 'float64' or heart_disease[columns].dtype == 'int64':
        for interval_name, interval_range in intervals.items():
            normalized_column = normalization(heart_disease[columns], *interval_range)
            normalized_df[f'{col}_{interval_name}'] = normalized_col

print(normalized_df)

# 4d

churn = pd.read_csv("../../dane/Churn_Modelling.csv")
print(churn.columns)
churn = pd.get_dummies(churn, columns=["Geography"], drop_first=True)
print(churn.columns)