import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon

f = lambda x : eval(func)

# math functions
def area_rectangles(graph):
    nsum = 0
    dx = (bnd_r-bnd_l)/s_int
    for i in range(0, s_int):
        mp = bnd_l+(dx/2)+(dx*i)
        nsum += f(mp)
        if graph: graph_rectangle(mp, dx, f(mp))
    return nsum*dx

def area_trapezoids(graph):
    nsum = 0
    dx = (bnd_r-bnd_l)/s_int
    last_height = f(bnd_l)
    for i in range(0, s_int):
        right_height = f(bnd_l+(dx*(i+1)))
        nsum += (last_height + right_height)/2
        last_height = right_height
        if graph: graph_trapezoid(bnd_l+(dx*i), dx, f)
    return nsum*dx

def simpsons_rule(graph):
    #if graph: graph_parabola()
    x = np.linspace(bnd_l, bnd_r, s_int+1)
    dx = (bnd_r-bnd_l)/s_int
    y = f(x)
    return dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])

# input function
def compile_func(str):
    str = str.replace('ln', 'np.log').replace('e', 'math.e')
    str = str.replace('^', '**')
    str = str.replace('sqrt', 'np.sqrt')
    str = str.replace('sin', 'np.sin').replace('cos', 'np.cos').replace('tan', 'np.tan')
    # try to remove the possibility of malicious code injection
    str = str.replace('_', '').replace('\"', '').replace('[', '').replace(']', '')
    str = str.strip()
    return compile(str, 'input', 'eval')

# graph functions
fig, ax = plt.subplots()
def graph_func():
    nums = np.linspace(int(bnd_l), int(bnd_r), int((bnd_r-bnd_l)*100))
    ax.plot(nums, f(nums), color='blue')
    ax.plot([bnd_l, bnd_r], [0, 0], color='gray', alpha=1)
    
def graph_rectangle(x, w, h):
    plt.bar(x, h, width=w, alpha=0.2, color='b')

def graph_trapezoid(x, w, func):
    x_cords = [x, x+w, x+w      , x      ]
    y_cords = [0, 0  , func(x+w), func(x)]
    ax.add_patch(Polygon(xy=list(zip(x_cords,y_cords)), alpha=0.1, color='red'))
    
print('multiplication must have an asterisk (*) seperating factors')
func = compile_func(input('y = '))
bnd_l = float(input('left bound: '))
bnd_r = float(input('right bound: '))
s_int = int(input ('sub-intervals: '))
graph = True if input('graph func (y/n): ').lower() == 'y' else False

print('area with rectangles: {:0.3f}'.format(area_rectangles(graph)))
print('area with trapezoids: {:0.3f}'.format(area_trapezoids(graph)))
print('area with simpson\'s rule: {:0.3f}'.format(simpsons_rule(graph)))
graph_func()
try:
    if graph: plt.show()
except KeyboardInterrupt:
    exit()