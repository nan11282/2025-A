import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 假设楼梯的磨损数据（位置和对应的磨损深度）
x_data = np.array([1, 2, 3, 4, 5,6])  # 楼梯位置（台阶编号）
W_data = np.array([0.1, 0.2,0.8,1,2,3])  # 每个位置的磨损深度（单位可以是毫米）

# 假设磨损的速率与使用频率成正比的模型
def wear_model(x, a, b):
    return a * np.power(x, b)  # 使用幂函数来模拟磨损与位置的关系

# 使用curve_fit来拟合磨损数据，推算模型的参数
params, covariance = curve_fit(wear_model, x_data, W_data)#curve_fit函数给他你的因变量和自变量以及函数 就会返回最佳的函数参数值（这里的a,b）

# 输出拟合的参数
a, b = params
print(f"拟合参数：a = {a}, b = {b}")

# 绘制拟合的曲线与原始数据
x_fit = np.linspace(1, 6, 100)
y_fit = wear_model(x_fit, *params)

plt.scatter(x_data, W_data, color='red', label='origin data')
plt.plot(x_fit, y_fit, label='nihe', color='blue')

# 添加坐标轴标签和标题
plt.xlabel('place', fontsize=12)
plt.ylabel('depth', fontsize=12)
plt.title('relation', fontsize=14)

# 显示图例
plt.legend()

# 显示图形
plt.show()

# 改进后的使用频率模型：使用频率与磨损深度成反比例关系
def calculate_usage_frequency(W, k):
    return W / k  # k 为常数，与材料和磨损特性相关

# 计算每个位置的使用频率
k = 0.05  #待改进
u_data = calculate_usage_frequency(W_data, k)
print(f"楼梯使用频率（每个位置的频率）：{u_data}")
# 计算拟合值
W_fit = wear_model(x_data, *params)

# 计算每个点的百分差
percentage_diff = np.abs((W_data - W_fit) / W_data) * 100

# 输出每个点的百分差
for i, diff in enumerate(percentage_diff):
    print(f"位置 {x_data[i]} 的百分差: {diff:.2f}%")
    # 将 x_data 分成三部分
n = len(x_data)
part1_x = x_data[:n//3]
part2_x = x_data[n//3:2*n//3]
part3_x = x_data[2*n//3:]

# 计算每个部分的拟合磨损深度之和
part1_W_fit = np.sum(wear_model(part1_x, *params))
part2_W_fit = np.sum(wear_model(part2_x, *params))
part3_W_fit = np.sum(wear_model(part3_x, *params))

# 计算拟合磨损深度之和的总和
total_W_fit = part1_W_fit + part2_W_fit + part3_W_fit

# 计算每个区域的拟合磨损深度之和的百分比
part1_percentage = (part1_W_fit / total_W_fit) * 100
part2_percentage = (part2_W_fit / total_W_fit) * 100
part3_percentage = (part3_W_fit / total_W_fit) * 100

# 计算区域之间的百分差
part1_part2_diff = np.abs(part1_percentage - part2_percentage)
part1_part3_diff = np.abs(part1_percentage - part3_percentage)
part2_part3_diff = np.abs(part2_percentage - part3_percentage)

# 输出区域之间的百分差
print(f"区域1和区域2之间的百分差: {part1_part2_diff:.2f}%")
print(f"区域1和区域3之间的百分差: {part1_part3_diff:.2f}%")
print(f"区域2和区域3之间的百分差: {part2_part3_diff:.2f}%")