import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
from scipy import stats

data = pd.read_csv("WHO-COVID-19-global-data.csv", low_memory=False)

dates = data.loc[data['Country_code']=='KR'][['Date_reported']]
dates = dates.values.tolist()
dates = [datetime.datetime.strptime(str(d),"['%Y-%m-%d']").date() for d in dates]
ax = plt.gca()
formatter = mdates.DateFormatter("%Y-%m-%d")
locator = mdates.DayLocator()

fig = plt.figure()
fig.suptitle('No. of New COVID-19 Cases Daily in Korea', fontsize=20)
plt.xticks(rotation=20)

newCase = data.loc[data['Country_code']=='KR'][['New_cases']]

x = np.arange(46)+1
targ=newCase[760:806].values.tolist()
targ=sum(targ,[])

slope, intercept, r, p, std_err = stats.linregress(x,targ)

def output(x):
    return slope * x + intercept

mymodel = list(map(output, x))

print(mymodel)
plt.plot(dates[760:806],mymodel)
plt.scatter(dates[760:806],newCase[760:806])
plt.show()
print(output(53))



print(slope)
print(intercept)
print(r)