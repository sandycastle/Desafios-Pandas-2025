from pydataset import data
print("Problem statement: Given that you are working with a group of researchers who are analyzing the combination of people's hair color and eye color.\n")

df_haireyecolor = data("HairEyeColor")

hair_eye_counts = df_haireyecolor.groupby(["Hair", "Eye"])["Freq"].sum().reset_index()
print("1. Total number of people for each combination of hair color (Hair) and eye color (Eye):\n", hair_eye_counts)

brown_eyes = df_haireyecolor[df_haireyecolor["Eye"] == "Brown"]
most_common_hair_brown = brown_eyes.loc[brown_eyes["Freq"].idxmax(), "Hair"]
print("\n 2. Most common hair color among people with brown eyes:", most_common_hair_brown)

hair_counts = df_haireyecolor.groupby("Hair")["Freq"].sum().reset_index()
print("\n 3. Table with the total count of people by hair color: \n", hair_counts)

