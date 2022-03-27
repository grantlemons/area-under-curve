import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon

func = input('y = ')

bnd_l = int(input('left bound: '))
bnd_r = int(input('right bound: '))
s_int = int(input ('sub-intervals: '))

r_area = lambda x, y : abs(x * y)
t_area = lambda x, y, z : abs(((x+y)/2)*z)
y = lambda x : eval(parse_func(func))

fig, ax = plt.subplots()

def parse_func(str):
    str = str.replace('ln', 'np.log')
    str = str.replace('^', '**')
    str = str.strip()
    return str

def area_rectangles():
    area = 0
    for i in range(0, s_int):
        width = (bnd_r-bnd_l)/s_int
        mp = bnd_l+(width/2)+(width*i)
        graph_rectangle(mp-(width/2), width, y(mp))
        area += r_area(width, y(mp))
    return area

def area_trapezoids():
    area = 0
    for i in range(0, s_int):
        width = (bnd_r-bnd_l)/s_int
        l_x = bnd_l+(width*i)
        r_x = l_x+width
        graph_trapezoid(l_x, width, y)
        area += t_area(y(l_x), y(r_x), width)
    return area

def graph_func():
    nums = np.linspace(bnd_l, bnd_r, (bnd_r-bnd_l)*100)
    ax.plot(nums, y(nums), color='blue')
    ax.plot([bnd_l, bnd_r], [0, 0], color='gray', alpha=1)
    
def graph_rectangle(x, w, h):
    ax.add_patch(Rectangle((x,0), w, h, alpha=0.2))

def graph_trapezoid(x, w, func):
    x_cords = [x, x+w, x+w      , x      ]
    y_cords = [0, 0  , func(x+w), func(x)]
    ax.add_patch(Polygon(xy=list(zip(x_cords,y_cords)), alpha=0.1, color='red'))

print('area with rectangles: {:0.3f}'.format(area_rectangles()))
print('area with trapezoids: {:0.3f}'.format(area_trapezoids()))
graph_func()
try:
    plt.show()
except KeyboardInterrupt:
    exit()