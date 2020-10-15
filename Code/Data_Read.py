import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, fftshift
import pandas as pd

# Import csv file
df= pd.read_csv('intentional.csv', header = None)


nt = df.T

print(nt)
#nt= nt.head(1000)
arr = nt.to_numpy()
n1= pd.DataFrame(arr)

plt.figure(figsize=(40,20))
plt.plot(n1.index,n1[1])
plt.show()

print(len(nt[0]))
N = len(n1[0])
yf = fft(n1[1])
yf = yf/np.sqrt(N)

plt.figure(figsize=(20,10))
plt.plot(abs(yf))
print(abs(yf)[0])
plt.show()