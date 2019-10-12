import init
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter
from scipy.stats import norm

init.initilize()
data = pd.read_csv('scatter.csv', encoding='CP949')

df = pd.DataFrame(data)


cor = df.corr(method = 'pearson')
cor_text = "상관계수 : " + str(round(cor["x"]["y"],3))

plt.text(155,94, cor_text, fontsize = 15)

plt.scatter(df['x'], df['y'])
plt.show()