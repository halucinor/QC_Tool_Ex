import init
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import matplotlib.font_manager as fm

init.initilize()

data = pd.read_csv('defective_sample.csv', index_col = 0, encoding='CP949')

df = pd.DataFrame(data["수량"])

df = df.sort_values(by = "수량", ascending=False)
df["불량률"] = df["수량"].cumsum()/df["수량"].sum()*100
print(df)
fig, ax = plt.subplots()

plt.ylabel("불량갯수")
ax.bar(df.index, df["수량"], color = "C0")
ax2 = ax.twinx()
ax2.plot(df.index, df["불량률"], color="C1", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

plt.ylabel("불량률")
# plt.figure(figsize = (10,4))
plt.grid()
plt.show()
