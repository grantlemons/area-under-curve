import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon

y = lambda x : eval(func, {__builtins__: {}, "np": np}, {"x": x})

def compile_func(str):
    str = str.replace('ln', 'np.log')
    str = str.replace('^', '**')
    str = str.replace('sqrt', 'np.sqrt')
    str = str.replace('sin', 'np.sin').replace('cos', 'np.cos').replace('tan', 'np.tan')
    # try to remove the possibility of malicious code injection
    str = str.replace('_', '').replace('\"', '').replace('[', '').replace(']', '')
    str = str.strip()
    return compile(str, 'input', 'eval')

def area_rectangles(graph):
    height = 0
    width = (bnd_r-bnd_l)/s_int
    for i in range(0, s_int):
        mp = bnd_l+(width/2)+(width*i)
        height += abs(y(mp))
        if graph: graph_rectangle(mp-(width/2), width, y(mp))
    return height*width

def area_trapezoids(graph):
    height = 0
    width = (bnd_r-bnd_l)/s_int
    for i in range(0, s_int):
        height += abs((y(bnd_l+(width*i)) + y(bnd_l+(width*i+1)))/2)
        if graph: graph_trapezoid(bnd_l+(width*i), width, y)
    return height*width

# graph functions
fig, ax = plt.subplots()
def graph_func():
    nums = np.linspace(int(bnd_l), int(bnd_r), int((bnd_r-bnd_l)*100))
    ax.plot(nums, y(nums), color='blue')
    ax.plot([bnd_l, bnd_r], [0, 0], color='gray', alpha=1)
    
def graph_rectangle(x, w, h):
    ax.add_patch(Rectangle((x,0), w, h, alpha=0.2))

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
graph_func()
try:
    if graph: plt.show()
except KeyboardInterrupt:
    exit()