import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/College.csv')

accept_array = df['Accept'].values
print('Avg Acceptances:', round(accept_array.mean()))
print('Max Acceptances:', accept_array.max())
print('Min Acceptances:', accept_array.min())

grad_rates = df['Grad.Rate'].values
print('Avg Grad Rates:', round(grad_rates.mean()))
print('Max Grad Rate:', grad_rates.max())
print('Min Grad Rate:', grad_rates.min())
x = accept_array
y = grad_rates
plt.scatter(x,y)
plt.xlabel('Acceptances')
plt.ylabel('Grad Rates')


df.head()