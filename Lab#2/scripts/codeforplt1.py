import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
a=233.6
b=[0]*8
c=[0]*8
for i in range (8):
    b[i]=i
    c[i]=i*a
_, ax = plt.subplots()
#ax.yaxis.set_major_locator(ticker.MultipleLocator(100))
ax.plot([0, b[7]], [0, c[7]],color='purple')
ax.grid(True)
ax.text(5.2,500, f"K = 233.6 st/sm")
plt.title("График зависимости пройденного кареткой \nрасстояния от количества шагов мотора")
plt.show()