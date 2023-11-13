import matplotlib.pyplot as plt

fig, ax = plt.subplots()
a=[9.57,11.64,12.22,13.34,14.06,14.77,16.24,14.70]
b=[0,10,20,30,40,50,60,70]

ax.plot(b,a,label='Расход Q(0-70мм)')
ax.scatter(b,a)
ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which='minor', linestyle = ':')

ax.set_xlabel("Расстояние от трубки Пито до сопла")
ax.set_ylabel("Расход [г/с]")
ax.set_title("График зависимости расхода от расстояния до сопла")

ax.set_xlim([-5, 80])
ax.set_ylim([8, 18])

ax.legend()
plt.show()