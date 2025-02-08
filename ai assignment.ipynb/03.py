import pandas as pd
link = r"C:\Users\user\Downloads\robot_dataset(robot_dataset)_1.csv"
df=pd.read_csv(link)
conversation_mean = df["Interaction_Count"].mean()
total_steps=df["Steps_Walked"].sum()
max_energy = df["Energy_Consumption (kWh)"].max()
min_energy = df["Energy_Consumption (kWh)"].min()
correlation = df["Steps_Walked"].corr(df["Energy_Consumption (kWh)"])
variance_of_learning_session = df["Learning_Sessions"].var()
print(f"mean of conversation: {conversation_mean}")
print(f"total steps : {total_steps}")
print(f"Maximum Energy Consumption: {max_energy} ")
print(f"Minimum Energy Consumption: {min_energy} ")
print(f"Correlation between Steps Walked and Energy Consumption: {correlation}")
print(f"variance of learning session:{variance_of_learning_session}")
