import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_name = "data4.csv"
df = pd.read_csv(file_name)

sns.displot(data=df, x="Shake_Value", hue="Label", kind="kde")

# Show the plot
plt.show()