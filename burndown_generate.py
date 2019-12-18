import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
plt.ylabel('Burndown')
df = pd.read_excel("C:\\Users\\caique.fonseca\\Documents\\burndown.xlsx")

datas = []
nX = 0
while df.loc[nX, 'data'] != '':
    datas.append(df.loc[nX, 'data'])
    nX = nX + 1

issues = []
nY = 0
while df.loc[nY, 'data'] != '':
    datas.append(df.loc[nY, 'issues'])
    nY = nY + 1

plt.rcParams['figure.figsize'] = (34,26)
plt.plot(datas,issues)
plt.savefig('C:\\Users\\caique.fonseca\\Documents\\burndown.png')
