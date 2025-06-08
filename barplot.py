import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_name = "shake.csv"
df = pd.read_csv(file_name)

sns.barplot(x = 'Label',
            y = 'Shake_Value',
            data = df)
 
# Show the plot
plt.show()