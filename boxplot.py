# importing the required library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
file_name = "shake.csv"
df = pd.read_csv(file_name)
 
sns.boxplot(x = 'Label', y = 'Shake_Value', hue="Label", palette=["m", "g"], data = df)
 
# Show the plot
plt.show()