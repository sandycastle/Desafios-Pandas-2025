import pandas as pd
from pydataset import data
print("Problem Definition: Given that you are working in an insecticide lab, you need to survey all the insecticide sprays and determine which one is the most effective.")

df_InsectSprays = data('InsectSprays')

# 1. Calculate the total number of insects killed (count) by spray type.
total_insects_killed = df_InsectSprays.groupby('spray')['count'].sum()
print("1. Total number of insects killed by spray type: \n", total_insects_killed.reset_index())

# 2. Identify which spray was the most effective in killing insects.
most_effective_spray = total_insects_killed.idxmax()
print("\n 2. The most effective spray in killing insects is:", most_effective_spray)

# 3. Calculate the overall average and filter the data to show only sprays with above-average effectiveness.
average_effectiveness = total_insects_killed.mean()
above_average_sprays = total_insects_killed[total_insects_killed > average_effectiveness]
print("\n 3. Sprays with above-average effectiveness:\n", above_average_sprays.reset_index())