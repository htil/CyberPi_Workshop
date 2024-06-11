# Importing the required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_name = "enter_file_name.csv"
df = pd.read_csv(file_name)

# Plotting the line graph
sns.lineplot(x=df.index, y='Sound_Value', hue='Label', data=df)

# Adding titles and labels
plt.title('Sound Sensor Readings Over Time')
plt.xlabel('Sample Number')
plt.ylabel('Sound Value')

# Show the plot
plt.show()