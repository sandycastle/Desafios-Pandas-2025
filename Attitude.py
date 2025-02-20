from pydataset import data

print("Problem statement: From a survey of administrative employees of a large financial organization, data is aggregated from the questionnaires of approximately 35 employees for each of 30 departments (randomly selected). The numbers give the percentage proportion of favorable responses to seven questions in each department.")

df_attitude = data("attitude")

# 1. Calculate the average "learning" by motivation level (rating).
average_learning_by_rating = df_attitude.groupby('rating')['learning'].mean()
print("\n1. Average learning by motivation level:\n", average_learning_by_rating.reset_index())  

# 2. Find the combination of rating and complaints that has the highest average learning value.
avg_learning = df_attitude.groupby(['rating', 'complaints'])['learning'].mean()
highest_avg_learning = avg_learning.idxmax()
print("\n2. Combination of rating and complaints with the highest average learning value:", highest_avg_learning)

# 3. What is the average learning level for employees who received above-average raises?
average_raise = df_attitude['raises'].mean()
above_average_raises_learning = df_attitude[df_attitude['raises'] > average_raise]['learning'].mean()
print("\n3. Average learning level for employees who received above-average raises: ", above_average_raises_learning)