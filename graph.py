import matplotlib.pyplot as plt
import matplotlib.animation as animation
from get_quote import get_quote

plt.style.use('dark_background')

# Parameters
x_len = 200         # Number of points to display
y_range = [1.1300, 1.1325]  # Range of possible Y values to display

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

ax.set_ylim(y_range)

linecolour = "#666666"
textcolour = "#b2b2b2"

#Styling

ax.spines['bottom'].set_color(linecolour)
ax.spines['top'].set_color(linecolour)
ax.spines['right'].set_color(linecolour)
ax.spines['left'].set_color(linecolour)

ax.yaxis.label.set_color('red')
ax.xaxis.label.set_color('red')

ax.tick_params(axis='x', colors=textcolour, which='both')
ax.tick_params(axis='y', colors=textcolour, which='both')

ax.yaxis.label.set_color(textcolour)
ax.xaxis.label.set_color(textcolour)

# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys, '#53e669')

# Add labels
#plt.title('EURUSD')
plt.xlabel('Time')
plt.ylabel('EUR/USD')



# This function is called periodically from FuncAnimation
def animate(i, ys):


    # Read temperature (Celsius) from TMP102
    rate = get_quote()

    # Add y to list
    ys.append(float(rate[0]))
    #xs.append(rate[1])

    print(rate)
    # Limit y list to set number of items
    #ys = ys[-x_len:]

    # Update line with new Y values
    line.set_ydata(ys)

    return line,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=1000,
    blit=True)
plt.show()