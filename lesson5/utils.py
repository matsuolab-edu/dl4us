from collections import OrderedDict

import numpy as np

class Node:
    def __init__(self, data):
        self.data = data
        self.children = OrderedDict()
        self.best = False
        self.depth = 1

    def __str__(self):
        return str(self.data)

    def add_child(self, path):
        if len(path) == 2:
            self.children[path[-1]] = Node(path[-1])
        else:
            self.children[path[1]].add_child(path[1:])

    def set_coordinates(self, x, y, ax, i2w, tree_depth):
        self.x = x
        self.y = y
        if self.best == True:
            ax.text(x, y+0.2, i2w[self.data], ha='center', fontsize=100/tree_depth, fontweight='bold', color='blue')
        else:
            ax.text(x, y+0.2, i2w[self.data], ha='center', fontsize=100/tree_depth, fontweight='bold', color='black')
        if self.best == True:
            ax.scatter(x, y, s=200/tree_depth, c='cyan', edgecolor='blue', linewidth=1, zorder=2)
        else:
            ax.scatter(x, y, s=200/tree_depth, c='grey', edgecolor='black', zorder=1)
        if len(self.children) != 0:
            for child_str, child_node in self.children.items():
                x += 1
                if self.best == True and child_node.best == True:
                    ax = plot_curve(self.x, x, self.y, y, ax, c='blue', linewidth=2, zorder=2, alpha=0.6)
                else:
                    ax = plot_curve(self.x, x, self.y, y, ax, c='grey', linewidth=2, zorder=1, alpha=0.6)
                x, y, ax = self.children[child_str].set_coordinates(x, y, ax, i2w, tree_depth)
                x -= 1
            return x, y, ax
        else:
            y -= 0.8
            return x, y, ax

    def mark_best_path(self, path):
        if len(path) != 1:
            self.best = True
            self.children[path[1]].mark_best_path(path[1:])
        else:
            self.best = True

def plot_curve(x_begin, x_end, y_begin, y_end, ax, c, linewidth, zorder, alpha):
    xs = np.linspace(x_begin, x_end, 1000)
    if y_begin != y_end:
        ys = (np.cos(np.linspace(0, np.pi, 1000)) - 1) * (y_begin - y_end) / 2 + y_begin
    else:
        ys = np.ones(1000) * y_begin

    ax.plot(xs, ys, c=c, linewidth=linewidth, zorder=zorder, alpha=alpha)
    return ax