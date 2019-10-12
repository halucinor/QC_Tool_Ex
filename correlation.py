import init
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import matplotlib.font_manager as fm

init.initilize()

data = pd.read_csv('correlation.csv')

df = pd.DataFrame(data)

corr = df.corr(method = 'pearson').sort_values('채수량', ascending=False)

print(corr["채수량"])