from pydataset import data

df = data("PlantGrowth")

#Calculate the average chick weight for each feed type.
avg = df.groupby('group')["weight"].mean()
print('1. Average weight for each group: \n' , avg.reset_index())

#Identify the feed that resulted in the highest average weight.
avg_6 = (avg > 6).any()
result = 'No' if not avg_6 else 'Yes'
print('\n 2. Any average weight greater than 6? ',result )

#Create a table showing the maximum, minimum, and average weight for each feed type.
peso_max_min = df.groupby("group")["weight"].agg(["max", "min"])
print('\n 3. Table showing the maximum and minimum weights per group: \n', peso_max_min.reset_index())