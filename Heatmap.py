print("Generating heatmap...")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

week_1 = [10,20,30,40,50]
week_2 = [60,70,80,90,100]
week_3 = [110,120,130,140,150]
week_4 = [160,170,180,190,200]
week_5 = [210,220,230,240,250]

data = np.array([week_1, week_2, week_3, week_4, week_5])
#data = np.random.randn(30,30)
plt.title("HEATMAP")
sns.heatmap(data)
plt.show()

print("Heatmap generated successfully.")