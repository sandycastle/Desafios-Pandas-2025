import pandas as pd
from pydataset import data
print("Problem statement: An experiment was conducted to measure and compare the effectiveness of various feed supplements on the growth rate of chickens.\n\nNewly hatched chicks were randomly allocated into six groups, and each group received a different feed supplement. Their weights in grams after six weeks are provided along with the feed types.\n")

df_Chickwts = data("chickwts")

# 1. Calculate the average chick weight for each feed type
average_weight = df_Chickwts.groupby('feed')['weight'].mean()
print("1. Average chick weight for each feed type: \n", average_weight.reset_index())

# 2. Identify the feed that resulted in the highest average weight
highest_avg_feed = average_weight.idxmax()
print("\n 2. Feed that resulted in the highest average weight:", highest_avg_feed)


# 3. Create a table showing the maximum, minimum, and average weight for each feed type
summary_table = df_Chickwts.groupby('feed')['weight'].agg(['max', 'min', 'mean'])
print("\n 3. Table showing the maximum, minimum, and average weight for each feed type:\n", summary_table.reset_index())
