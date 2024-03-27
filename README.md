# 工程热力学大作业

作者：能动B2104 杨牧天 2212212998



## 项目背景

> ​	水作为地球上分布做广泛的液态流体具有十分重要的研究意义，它被用作动力循环中的工作流体，为工业化国家提供了大量的电力。
>
> 在化工行业，水是最常见的溶剂。而在生物领域，水占人体的60%~70%，其重要意义显而易见。
>
> ​	除了在常规领域，水在一些特殊应用中也发挥了重大的价值，例如超临界水氧化，超临界水氧化技术对处理有毒有害的废水和污泥具有非常好的效果，其在化工工业，制药工业，食品工业，电子工业都有所应用。
>
> ​	因此在实际生产中，明确水的物性至关重要，在以往的探索中，人们积累了大量实验数据，但由于现代工业对水的物性的精度不断提升，应用更加普遍，开发一个计算水及其蒸汽的物性的计算方法显得尤为重要。**水和蒸汽性质国际协会（IAPWS）**于2007年8月26-31日在瑞士卢塞恩举行会议，拟定发布了适用于工业用途的计算方法，称为IAPWS水和蒸汽热力学能性能工业方案1997，简称**IAPWS-IF97**
>
> ​	**本项目基于Python科学计算模块（Sympy，Scipy，Numpy， Pandas） 以及可视化模块Qt5 for Python（PyQt5）进行对IAPWS-IF97的编程实现并制作可视化界面。**



## 算法简介

> 算法可用范围：
> $$
> 273.15~k\le t \le 1073.15~k~~~~~~~~~~p\le 100~Mpa\\
> 1073.15~k\le t \le 2273.15~k~~~~~~~~~~p\le 50~Mpa
> $$
> <img src=".\picture\1.png" style="zoom: 33%;" />
>

​	依据IAPWS-IF97，将整个有效范围划分为五个区域，其中，每个区域都有决定其性质的方程，根据此方程，我们可以通过数学运算将比体积，焓，熵等性质计算出来。



### 例：1区域的计算公式

$$
\frac{g(p, T)}{RT}=\sum_{i=1}^{34}n_i(7.1-\pi)^{I_i}(\tau-1.222)^{J_i}
$$

其中，$\pi=p/p^*,~\tau=T^*/T$，$p^*=16.53Mpa,~T^*=1386K$

由此，如果已知上述正则方程式所拟合而成系数$n_i,I_i,J_i$，那么便可以求出**无量纲吉布斯自由能**的表达式

再根据如下关系：
$$
v=(\frac{\delta g}{\delta p})_T\\
s = -(\frac{\delta g}{\delta T})_p\\
h = g - T(\frac{\delta g}{\delta T})_p\\
...
$$
即可以求出比体积，比焓，比熵等热力学性质。

系数具体数值如下表：

| i    | Ii   | Ji   | ni        |
| ---- | ---- | ---- | --------- |
| 1    | 0    | -2   | 0.14633   |
| 2    | 0    | -1   | -0.84548  |
| 3    | 0    | 0    | -3.756360 |
| 4    | 0    | 1    | 3.39E+00  |
| 5    | 0    | 2    | -0.95792  |
| 6    | 0    | 3    | 0.15772   |
| 7    | 0    | 4    | -1.66E-02 |
| 8    | 0    | 5    | 8.12E-04  |
| 9    | 1    | -9   | 2.83E-04  |
| 10   | 1    | -7   | -6.07E-04 |
| 11   | 1    | -1   | -1.90E-02 |
| 12   | 1    | 0    | -3.25E-02 |
| 13   | 1    | 1    | -2.18E-02 |
| 14   | 1    | 3    | -5.28E-05 |
| 15   | 2    | -3   | -4.72E-04 |
| 16   | 2    | 0    | -3.00E-04 |
| 17   | 2    | 1    | 4.77E-05  |
| 18   | 2    | 3    | -4.41E-06 |
| 19   | 2    | 17   | -7.27E-16 |
| 20   | 3    | -4   | -3.17E-05 |
| 21   | 3    | 0    | -2.83E-06 |
| 22   | 3    | 6    | -8.52E-10 |
| 23   | 4    | -5   | -2.24E-06 |
| 24   | 4    | -2   | -6.52E-07 |
| 25   | 4    | 10   | -1.43E-13 |
| 26   | 5    | -8   | -4.05E-07 |
| 27   | 8    | -11  | -1.27E-09 |
| 28   | 8    | -6   | -1.74E-10 |
| 29   | 21   | -29  | -6.88E-19 |
| 30   | 23   | -31  | 1.45E-20  |
| 31   | 29   | -38  | 2.63E-23  |
| 32   | 30   | -39  | -1.19E-23 |
| 33   | 31   | -40  | 1.82E-24  |
| 34   | 32   | -41  | -9.35E-26 |



## 可视化

通过使用Qt5 For Python进行可视化界面的设计

可视化界面共分为如下几个功能：

1. 单次计算：即根据输入的p，T的数值计算出对应状态下的v，h，s
2. 批量计算：通过读取输入的csv文件计算对应热力学值，并通过tab表格显示出来xiang
3. 结果绘图：将计算出来的热力学性质数据连同p，T绘制在三维立体图上，并添加绘制等压线，等温线等功能，并提供绘图风格选择



### 可视化成果展示及使用说明



#### 主界面及图标

![image-20230419002124943](C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419002124943.png)

> 左上角为作者昵称，封面为蒸汽，与软件功能相扣；中间偏左区域为一个简短的功能说明以及参考资料来源

![image-20230419002310997](C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419002310997.png)

> 图标模仿某知名游戏平台



#### 点击Start进入功能界面

<img src="C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419002428878.png" alt="image-20230419002428878" style="zoom:50%;" />

> 软件共分为四个功能区域
>
> 1. **最上方区域**为使用说明区域，说明软件的使用方法以及注意事项
>
> 2. **左中区域**为单次查询区域，输入T与p点击Calculate即可得到计算结果
>
> 3. **右中区域**为绘图区域，仅在存在输入文件时可以使用，共有三个功能可以使用
>
>    + 绘制等压面
>    + 绘制等温面
>    + 在整个范围内绘制特性曲面
>
>    此外，还提供三种绘图风格，及经典模式，暗背景模式，seaborn模式
>
> 4. **最下方区域**为文件输入与显示区域，**该部分仅支持输入csv文件**，输入文件后可在下方tab表格中显示

#### 单次计算功能介绍

![image-20230419003234596](C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419003234596.png)

如图输入T为300K，p为3Mpa，点击Calculate得到结果如下：

![image-20230419003335777](C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419003335777.png)

（界面有些简陋不要介意）

如此我们计算出了300K温度和3Mpa压强下的比体积，比焓，比熵的数值



#### 批量计算功能介绍

点击Select File按钮进入文件选择界面：

<img src="C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419003555208.png" alt="image-20230419003555208" style="zoom: 50%;" />

选择测试文件1.csv

> <img src="C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419003705727.png" alt="image-20230419003705727" style="zoom:50%;" />
>
> **输入文件说明**：
>
> 撰写文件时第一列为压强，第二列为温度，第三列只需设置标题，可选**h,s,v**

得到如下结果：

![image-20230419003939766](C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419003939766.png)

可见软件已经自动将对应的熵值计算了出来



#### 绘图功能介绍

接着上述操作，直接点击Plot按钮

![image-20230419004218423](C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419004218423.png)

得到如下包含三个散点的散点图

勾选Plot isobaric dirgram，

![image-20230419004329374](C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419004329374.png)

再次点击Plot按钮：

![image-20230419004359808](C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419004359808.png)

**得到包含等压面的三维图像**

同理勾选Plot isothermal maps，点击Plot按钮：

![image-20230419004523397](C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419004523397.png)

**得到包含等温面的三维图像**

勾选Mapping water vapor properties，点击Plot：

![image-20230419004651395](C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419004651395.png)

得到完整的热力学性质图，也就是说，**所有的散点都应落在该曲面上**

接下来，换不同的绘图风格做出包含等压面的图像如下：

> classic:
>
> <img src="C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419005019100.png" alt="image-20230419005019100" style="zoom: 50%;" />
>
> dark_background:
>
> <img src="C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419005100786.png" alt="image-20230419005100786" style="zoom:50%;" />
>
> seaborn:
>
> <img src="C:\Users\DanYang\AppData\Roaming\Typora\typora-user-images\image-20230419005123686.png" alt="image-20230419005123686" style="zoom:50%;" />



## 缺点及不足之处

1. 没有考虑区域边界的连续性
2. 模型系数精确度不高，产生一定的误差
3. 软件仍然存在许多bug



## 感谢您的观看！

