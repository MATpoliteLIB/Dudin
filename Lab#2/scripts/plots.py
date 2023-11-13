import matplotlib.pyplot as plt 
import math 
import numpy as np

data = []
p0=1056
b=[0]*100
for i in range (100):
    b[i]=-15.12+i*0.3424

f=open('00mm.txt')
for line in f:
    data.append([float(x) for x in line.split()])
for i in range (100):
    print (data[i],"\n")
a0m=[0]*100
for i in range (100):
    a0m[i]=data[i][1]
    if ((p0-a0m[i])<0):
        a0m[i]=0
    else:
        a0m[i]=math.sqrt((p0-a0m[i])*2/1.2)
f.close()

coefficients = np.polyfit(b, a0m, 5)
poly = np.poly1d(coefficients)

data1=[]
f1=open('10mm.txt')
for line in f1:
    data1.append([float(x) for x in line.split()])
for i in range (100):
    print (data1[i],"\n")
a1m=[0]*100
for i in range (100):
    a1m[i]=data1[i][1]
    if ((p0-a1m[i])<0):
        a1m[i]=0
    else:
        a1m[i]=math.sqrt((p0-a1m[i])*2/1.2)
f1.close()

coefficients1 = np.polyfit(b, a1m, 6)
poly1 = np.poly1d(coefficients1)

data2=[]
f2=open('20mm.txt')
for line in f2:
    data2.append([float(x) for x in line.split()])
for i in range (100):
    print (data2[i],"\n")
a2m=[0]*100
for i in range (100):
    a2m[i]=data2[i][1]
    if ((p0-a2m[i])<0):
        a2m[i]=0
    else:
        a2m[i]=math.sqrt((p0-a2m[i])*2/1.2)
f2.close()

data3=[]
f3=open('30mm.txt')
for line in f3:
    data3.append([float(x) for x in line.split()])
for i in range (100):
    print (data3[i],"\n")
a3m=[0]*100
for i in range (100):
    a3m[i]=data3[i][1]
    if ((p0-a3m[i])<0):
        a3m[i]=0
    else:
        a3m[i]=math.sqrt((p0-a3m[i])*2/1.2)
f3.close()

data4=[]
f4=open('40mm.txt')
for line in f4:
    data4.append([float(x) for x in line.split()])
for i in range (100):
    print (data4[i],"\n")
a4m=[0]*100
for i in range (100):
    a4m[i]=data4[i][1]
    if ((p0-a4m[i])<0):
        a4m[i]=0
    else:
        a4m[i]=math.sqrt((p0-a4m[i])*2/1.2)
f4.close()

data5=[]
f5=open('50mm.txt')
for line in f5:
    data5.append([float(x) for x in line.split()])
for i in range (100):
    print (data5[i],"\n")
a5m=[0]*100
for i in range (100):
    a5m[i]=data5[i][1]
    if ((p0-a5m[i])<0):
        a5m[i]=0
    else:
        a5m[i]=math.sqrt((p0-a5m[i])*2/1.2)
f5.close()

data6=[]
f6=open('60mm.txt')
for line in f6:
    data6.append([float(x) for x in line.split()])
for i in range (100):
    print (data6[i],"\n")
a6m=[0]*100
for i in range (100):
    a6m[i]=data6[i][1]
    if ((p0-a6m[i])<0):
        a6m[i]=0
    else:
        a6m[i]=math.sqrt((p0-a6m[i])*2/1.2)
f6.close()

data7=[]
f7=open('70mm.txt')
for line in f7:
    data7.append([float(x) for x in line.split()])
for i in range (100):
    print (data7[i],"\n")
a7m=[0]*100
for i in range (100):
    a7m[i]=data7[i][1]
    if ((p0-a7m[i])<0):
        a7m[i]=0
    else:
        a7m[i]=math.sqrt((p0-a7m[i])*2/1.2)
f7.close()

fig, ax = plt.subplots()
ax.plot(b,a0m,label='00mm')
plt.plot(b,-1*poly(a0m), label='Аппроксимация')
plt.plot(b,-1/9*poly1(a1m), label='Аппрокс323имация')
#ax.plot(b,a1m)
#ax.plot(b,a2m)
#ax.plot(b,a3m)
#ax.plot(b,a4m)
#ax.plot(b,a5m)
#ax.plot(b,a6m)
#ax.plot(b,a7m)
ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which='minor', linestyle = ':')

ax.set_xlabel("Положение трубки Пито относительно центра струи [мм]")
ax.set_ylabel("Скорость воздуха [м/с]")
ax.set_title("Скорость потока воздуха в сечении затопленной струи")

ax.legend()

plt.show()
print (data[1])