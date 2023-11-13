import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
a=6.561776631729762
b=[0]*50
c=[0]*50
for i in range (50):
    b[i]=i
    c[i]=946+i*a
_, ax = plt.subplots()
#ax.yaxis.set_major_locator(ticker.MultipleLocator(100))
ax.plot(b,c,color='purple')
ax.grid(True)
ax.text(32,1025, f"K = 6.56177 st/Pa")
plt.title("График зависимости отчета АЦП от показаний барометра")
plt.show()