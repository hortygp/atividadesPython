import pandas as pd

titanic_df = pd.read_csv("train.csv")
titanic_df.describe()
name_class_df = titanic_df[9]
