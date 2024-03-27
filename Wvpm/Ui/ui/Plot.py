# -*- coding: utf-8 -*-
# @Time : 2023/4/18 20:10
# @Author : DanYang
# @File : Plot.py
# @Software : PyCharm
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib.style.core import use
from Algorithm import PropsSI

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'


def set_style(style):
    use(style)


def plot_data(p, T, goal, goal_name, if_plot_p=False, if_plot_T=False, if_plot_all=False, method='classic'):
    set_style(method)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(p, T, goal, color='#54278f', label='Raw data')
    plt.title(f'p-T-{goal_name}')
    ax.set_xlabel('p/Mpa')
    ax.set_ylabel('T/K')
    if goal_name == 'v':
        an = '$m^3.kg$'
    elif goal_name == 'h':
        an = '$kJ.kg^{-1}$'
    elif goal_name == 's':
        an = '$kJ.kg^{-1}$'
    ax.set_zlabel(f'{goal_name}/{an}')
    if if_plot_all:
        x, y = np.meshgrid(np.linspace(min(p), max(p), 100), np.linspace(min(T), max(T), 100))
        x = np.ravel(x)
        y = np.ravel(y)
        z = np.array([PropsSI(goal_name.upper(), 'P', i*10**6, 'T', j, 'Water') for i, j in zip(x, y)])
        x = x.reshape((100, 100))
        y = y.reshape((100, 100))
        z = z.reshape((100, 100))
        ax.plot_surface(x, y, z, color='#efedf5')
        plt.legend()
        plt.show()
        return
    if if_plot_p:
        x, y = np.meshgrid(np.linspace(min(T), max(T), 100), np.linspace(min(goal), max(goal), 100))
        x = np.ravel(x)
        y = np.ravel(y)
        z = np.array([PropsSI('P', goal_name.upper(), i, 'T', j, 'Water') / 1000000 for i, j in zip(y, x)])
        x = x.reshape((100, 100))
        y = y.reshape((100, 100))
        z = z.reshape((100, 100))
        ax.plot_surface(z, x, y, color='#6baed6')
    if if_plot_T:
        x, y = np.meshgrid(np.linspace(min(p), max(p), 100), np.linspace(min(goal), max(goal), 100))
        x = np.ravel(x)
        y = np.ravel(y)
        z = np.array([PropsSI('T', goal_name.upper(), i, 'P', j*10**6, 'Water') for i, j in zip(y, x)])
        x = x.reshape((100, 100))
        y = y.reshape((100, 100))
        z = z.reshape((100, 100))
        ax.plot_surface(x, z, y, color='#ef3b2c')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    plot_data(np.linspace(3, 80, 10), np.linspace(300, 500, 10), np.linspace(300, 600, 10), 's', if_plot_all=True, method='seaborn')
