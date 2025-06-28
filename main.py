import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.style 


plt.style.use('fivethirtyeight') 

v1 = float(input("Enter the first object's velocity: "))
thetadeg1 = float(input("Enter the first object's angle from the ground: "))
v2 = float(input("Enter the second object's velocity: "))
thetadeg2 = float(input("Enter the second object's angle from the ground: "))
theta1=np.deg2rad(thetadeg1)
theta2=np.deg2rad(thetadeg2)

g = 9.81

total_time1 = ((v1*np.sin(theta1))/g)*2
total_time2 = ((v2*np.sin(theta2))/g)*2
t = 0
xmax = 0
ymax = 0

if (v1*np.cos(theta1) > v2*np.cos(theta2)):
    xmax = total_time1*v1*np.cos(theta1)
    
else:
    xmax = total_time2*v2*np.cos(theta2)
    
    
if (v1*np.sin(theta1) > v2*np.sin(theta2)):
    ymax = 0.5*total_time1*v1*np.sin(theta1) - 0.5*g*((total_time1*0.5)**2)
    t = total_time1
else:
    ymax = 0.5*total_time2*v2*np.sin(theta2) - 0.5*g*((total_time2*0.5)**2)
    t = total_time2
    

    
x = np.arange(0, (round(xmax/10)*10) * 1.1, 1)

y1 = (x*np.tan(theta1)) - ((g*(x**2))/(2*(v1**2)*np.cos(theta1)**2))
y2 = (x*np.tan(theta2)) - ((g*(x**2))/(2*(v2**2)*np.cos(theta2)**2))


fig, ax = plt.subplots()
ax.set_ylim(0, round(ymax) * 1.1)
ax.plot(x, y1, color="palegreen", label="Trajectory 1: " + str(v1) + " m/s at angle of " + str(thetadeg1) + " degrees")
ax.plot(x, y2, color="lightcoral", label="Trajectory 2: " + str(v2) + " m/s at angle of " + str(thetadeg2) + " degrees")
ax.set_title("Trajectories of two objects in free-fall motion")
ax.set_ylabel("Height (m)")
ax.set_xlabel("Horizontal distance (m)")
text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

line1, = ax.plot([], [], color="darkgreen", alpha = 0.5)
line2, = ax.plot([], [], color="darkred", alpha = 0.5)

xdata1 = list()
ydata1 = list()
xdata2 = list()
ydata2 = list()


def update(frame):
    current_x1 = v1 * np.cos(theta1) * frame * 0.05
    current_y1 = v1 * np.sin(theta1) * frame * 0.05 - 0.5 * g * (frame * 0.05)**2

    current_x2 = v2 * np.cos(theta2) * frame * 0.05
    current_y2 = v2 * np.sin(theta2) * frame * 0.05 - 0.5 * g * (frame * 0.05)**2

    xdata1.append(current_x1)
    ydata1.append(current_y1)
    xdata2.append(current_x2)
    ydata2.append(current_y2)

    line1.set_data(xdata1, ydata1)
    line2.set_data(xdata2, ydata2)
    text.set_text("Time: " + str(frame/20) + "s\nSpeed 1: " + str(np.sqrt(v1*np.cos(theta1)**2 + (v1*np.sin(theta1)-g*frame/20)**2)) + " m/s\nSpeed 2: " + str(np.sqrt(v2*np.cos(theta2)**2 + (v2*np.sin(theta2)-g*frame/20)**2)) + " m/s")
    return line1, line2,

ani = FuncAnimation(fig, update, frames=21*round(t), interval=50, repeat=False)
plt.legend(loc="best", borderpad = 0.1)
plt.show()
