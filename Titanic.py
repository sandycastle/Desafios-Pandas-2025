import pandas as pd
from pydataset import data
print("Problem definition: Given that you are working with a group of historians who are analyzing the sinking of the Titanic, ask the historians the following questions:")

df_titanic = data("titanic")

# 1. Overall survival rate
overall_survival_rate = df_titanic['survived'].value_counts(normalize=True)*100
print(f"Overall survival rate: {str(overall_survival_rate['yes'])}%")

# 2. Survival rate by class (Pclass)
survival_rate_by_class = (df_titanic.groupby('class')['survived'].value_counts(normalize=True)*100).unstack()
print("\n2. Survival rate by class:\n", survival_rate_by_class['yes'])



# 3. Survival rate by sex
print("\n3. Which sex has the highest survival rate?\n")
survival_rate_by_sex = (df_titanic.groupby('sex')['survived'].value_counts(normalize=True)*100).unstack()

if survival_rate_by_sex['yes']['man'] > survival_rate_by_sex['yes']['women']:
  print(f"Men had a highest survival rate: {str(survival_rate_by_sex['yes']['men'])} %" )
else:
  print(f"Women had a highest survival rate: {str(survival_rate_by_sex['yes']['women'])} %")


# 4. Number of adults and children (survivors and non-survivors)
survivors = df_titanic.groupby('age')['survived'].value_counts()

print("\n4. Number of survivors and non-survivors by age group:\n", survivors.unstack())