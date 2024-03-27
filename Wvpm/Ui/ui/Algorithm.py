# -*- coding: utf-8 -*-
# @Time : 2023/4/5 14:55
# @Author : DanYang
# @File : Algorithm.py
# @Software : PyCharm
import numpy as np
import pandas as pd
from sympy import symbols, Function, summation, Array, diff
from CoolProp.CoolProp import PropsSI

pd.set_option('display.precision', 13)

R = 0.46126  # kJ/(kg.K)
Tc = 647.096  # K
pc = 22.064  # Mpa
vc = 322  # kg/m^3

test_data_2_3 = [0.623_150_000e3, 0.165_291_643e2, 'T', 'P']


def test(func, odata):
    pre = func(odata[2], odata[0], odata[3])
    if abs(pre-odata[1]) >= 10**-4:
        raise ValueError(f"Wrong Function old:{odata[1]} pre:{pre}")
    else:
        print(f'Success old:{odata[1]} pre:{pre}')


def boundary_between_2_3(known, param, goal):
    ni = np.array([0.348_051_856_289_69e3, -0.116_718_598_799_75e1, 0.101_929_700_393_26e-2,
                   0.572_544_598_627_46e3, 0.139_188_397_788_70e2])
    n = symbols('n')
    if known == 'T' and goal == 'P':
        fun1 = ni[0] + ni[1]*n + ni[2]*n**2
        return fun1.subs(n, param)
    elif known == 'P' and goal == 'T':
        fun1 = ni[3] + ((n-ni[4])/ni[2])**(1/2)
        return fun1.subs(n, param)


def boundary_1(pn, Tn, goal):
    T0 = 1386
    p0 = 16.53
    coe = pd.read_csv('../../data/boundary_1.csv')
    p = symbols('p', positive=True)
    T = symbols('T', positive=True)
    j = symbols('j', integer=True)
    gamma = Function('gamma')(p, T)
    Ii = Array(coe['Ii'])
    Ji = Array(coe['Ji'])
    ni = Array(coe['ni'])

    gamma = R * T * summation(ni[j]*(7.1-p/p0)**Ii[j]*(T0/T-1.222)**Ji[j], (j, 0, 33))
    v = diff(gamma, p, 1) / 1000
    h = (gamma - T * (diff(gamma, T, 1))) * 1000
    s = -(diff(gamma, T, 1)) * 1000
    if goal == 'v':
        return v.evalf(subs={p: pn, T: Tn}, n=13)
    elif goal == 'h':
        return h.evalf(subs={p: pn, T: Tn}, n=13)
    elif goal == 's':
        return s.evalf(subs={p: pn, T: Tn}, n=13)


def other(p, T, goal):
    if goal == 'v':
        goal = 'D'
        return 1 / PropsSI(goal.upper(), 'T', T, 'P', p*10**6, 'Water')
    return PropsSI(goal.upper(), 'T', T, 'P', p*10**6, 'Water')


if __name__ == '__main__':
    pass