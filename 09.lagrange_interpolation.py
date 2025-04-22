#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @ author: Koorye
# @ date: 2021-7-26
# @ function: 使用 scipy 包进行拉格朗日插值

# %%

import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# %%

# 输入源数据
x_input = input("请输入 x 数据,用英文逗号分隔:")
y_input = input("请输入 y 数据,用英文逗号分割:")
target_x = float(input("请输入要预测的 x 值："))

x = np.array([float(i) for i in x_input.split(',')])
y = np.array([float(i) for i in y_input.split(',')])

# %%

# 拉格朗日插值
poly = lagrange(x, y)
res = poly(target_x)

# %%

# 格式化输出
def format_polynomial(coeffs):
    terms = []
    degree = len(coeffs)
    for i, coeff in enumerate(coeffs):
        power = degree - i
        if coeff == 0:
            continue
        # 处理系数符号
        sign = '-' if coeff < 0 else '+' if terms else ''
        abs_coeff = abs(coeff)

        if power == 0:
            terms.append(f"{sign}{abs_coeff}")
        elif power == 1:
            if abs_coeff == 1:
                terms.append(f"{sign}x")
            else:
                terms.append(f"{sign}{abs_coeff}x")
        else:
            if abs_coeff == 1:
                terms.append(f"{sign}x^{power}")
            else:
                terms.append(f"{sign}{abs_coeff}x^{power}")
    
    result = ''.join(terms)
    # 如果第一个字符是 +，去掉它
    if result.startswith('+'):
        result = result[1:]
    return result

# 格式化输出
formatted_poly = format_polynomial(poly)
print("Lagrange多项式表达式:",formatted_poly)
print(f"x={target_x}时,Lagrange预测值:{res}")

# %%

# 画图
x1 = np.linspace(min(x)-0.2*min(x), max(x)+0.2*max(x), 1000)
y1 = poly(x1)

plt.rcParams['figure.dpi'] = 500
plt.plot(x1, y1, label='拉格朗日插值曲线', color='blue', linewidth=2)
plt.scatter(x, y, label='原始数据点', color='red', s=25)
plt.scatter(target_x, res, label=f'预测点 (x={target_x:.2f}, y={res:.2f})', color='green', s=50)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
