import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

data = pd.read_csv("data.csv", low_memory=False)
data.drop([],[],[],[],[],[], axis=1, inplace=True)
print(data)
print(data.shape)
print(data.isna().sum())