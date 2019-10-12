import init
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter
from scipy.stats import norm

init.initilize()

df = pd.read_csv('histogram_data.csv', encoding='CP949')
data = df["data"]
std = np.std(data)
mean = np.mean(data)
median = np.median(data)
rv = norm(mean, std)



xx = np.linspace(45, 55, 100)

mean_text = "평균(mean) : " + str(mean)

std_text = "분산(standard)  : " + str(round(std,3))

median_text = "중앙값(median)) : " + str(median)

fig, ax = plt.subplots()

ax.hist(data)
ax2 = ax.twinx()
ax2.plot(xx, rv.pdf(xx),color="C1")
plt.text(52,0.36, mean_text, fontsize = 10)
plt.text(52,0.32, median_text, fontsize = 10)
plt.text(52,0.28, std_text, fontsize = 10)

plt.grid()
plt.show()