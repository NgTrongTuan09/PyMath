from matplotlib.pyplot import figure , plot , xlabel , ylabel, show, axhline , axvline , grid , xticks , yticks , xlim , ylim , legend , title

from numpy import *
import colorama
colorama.init()
fig= figure()
fig.set_facecolor("black")
ax = fig.add_subplot(111)
ax.set_facecolor("black")

hsb2_3=5
x = arange(-10,10, 0.01)
y13=hsb2_3*x**2
plot(x, y13)


xlabel("y", color='white')
ylabel("x", color='white')
axhline(y=0, color='white')
axvline(x=0, color='white')
plot([0, 1], [0, 0], color='white')
plot([0, -1], [0, 0], color='white')
grid(True, which="both", axis="both", color='white', linewidth=1, alpha=0.2)
xticks(arange(-51, 51, 1), color='white', size=8)
yticks(arange(-51, 51, 1),color='white', size=8)
xlim(-12,12)
ylim(-12,12)
legend()
title("created by: \n Nguyễn Trọng Tuấn " , fontsize = 8, loc="right", color = 'white')
show()