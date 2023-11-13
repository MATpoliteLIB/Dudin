import matplotlib.pyplot as plt
import numpy as np
from random import randint
import math 
data = []
e=0
z=0
p0=1056

f=open('00mm.txt','r')
for line in f:
    data.append([float(x) for x in line.split()])
a=[0]*100
for i in range (100):
    a[i]=data[i][1]

print (a[41],'\n')
d=[0]*100
for i in range (100):
    d[i]=i-49

b=[0]*100
for i in range (100):
    f=p0-a[i]
    if (f<0):
        f=0
    b[i]=math.sqrt(f*2/1.2)
f.close()

f1=open('60mm.txt','r')
for line in f1:
    data.append([float(x) for x in line.split()])
a1=[0]*100
for i in range (100):
    a1[i]=data[i][1]

print (a1[41])
d1=[0]*100
for i in range (100):
    d1[i]=i-49

b1=[0]*100
for i in range (100):
    f=p0-a1[i]
    if (f<0):
        f=0
    b1[i]=math.sqrt(f*2/1.2)

fig, ax = plt.subplots()
ax.plot(d1, b1, label=f'Q (00 мм) = [г/с]', color='red')
ax.scatter(d, b, label=f'Q (10 мм) = [г/с]', color='orange')

ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which='minor', linestyle = ':')

ax.set_xlabel("Положение трубки Пито относительно центра струи [мм]")
ax.set_ylabel("Скорость воздуха [м/с]")
ax.set_title("Скорость потока воздуха в сечении затопленной струи")


ax.legend()

plt.show()