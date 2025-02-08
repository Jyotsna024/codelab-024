import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the specified path
file_path = r'C:\Users\user\Downloads\robot_dataset(robot_dataset)_1.csv'
robot_data = pd.read_csv(file_path)

# Rename column for clarity
robot_data = robot_data.rename(columns={"Energy_Consumption (kWh)": "Energy_Consumption"})

# Perform statistical calculations
mean_interaction_count = robot_data['Interaction_Count'].mean()
total_steps_walked = robot_data['Steps_Walked'].sum()
max_energy_consumption = robot_data['Energy_Consumption'].max()
min_energy_consumption = robot_data['Energy_Consumption'].min()
correlation_steps_energy = robot_data['Steps_Walked'].corr(robot_data['Energy_Consumption'])
variance_learning_sessions = robot_data['Learning_Sessions'].var()

# Display results
print("Analysis Results:")
print(f"Mean Interaction Count: {mean_interaction_count}")
print(f"Total Steps Walked: {total_steps_walked}")
print(f"Max Energy Consumption: {max_energy_consumption} kWh")
print(f"Min Energy Consumption: {min_energy_consumption} kWh")
print(f"Correlation (Steps vs Energy): {correlation_steps_energy}")
print(f"Variance in Learning Sessions: {variance_learning_sessions}")

# Plot distribution of Objects_Recognized
plt.figure(figsize=(12, 6))

# Histogram
plt.subplot(1, 2, 1)
sns.histplot(robot_data['Objects_Recognized'], bins=10, kde=True, color="blue")
plt.title("Histogram of Objects Recognized")
plt.xlabel("Objects Recognized")
plt.ylabel("Frequency")

# Box Plot
plt.subplot(1, 2, 2)
sns.boxplot(y=robot_data['Objects_Recognized'], color="orange")
plt.title("Box Plot of Objects Recognized")
plt.ylabel("Objects Recognized")

plt.tight_layout()
plt.show()
