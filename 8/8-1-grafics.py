import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

data_array=np.loadtxt("data.txt",dtype=int)
data_settings=np.loadtxt("settings.txt",dtype=float)
data_time=np.linspace(0,data_settings[0],data_array.size)

data_array=data_array*data_settings[1]
fig,ax = plt.subplots(figsize=(16,12),dpi=100)
ax.grid(which='major',color='k')
ax.axis([data_array.min(),data_time.max()+1,data_array.min(),data_array.max()+0.2])
ax.minorticks_on()
ax.grid(which='minor',color='gray',linestyle=':')
ax.plot(data_time,data_array,label="Зависимость напряжения от времени",color='purple',linewidth=1)
ax.scatter(data_time[0:data_time.size:5],data_array[0:data_array.size:5],marker='s',c='blue',s=10)
ax.set_title("/n".join(wrap('Процесс зарядки и разрядки конденсатора в RC цепи',60)),loc='center')
ax.set_ylabel("напряжение,В")
ax.set_xlabel("время,с")
ax.legend()
plt.rc('font', **{'family': 'Courier New'})
plt.text(15.5,1.25, 'Время заряда: 13.2756 сек.' )
plt.text(15.5,1.1, 'Время разряда: 10.7131 cек.' )
plt.show()
fig.savefig('graph.svg')