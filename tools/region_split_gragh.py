import matplotlib.pyplot as plt

# 区域边界（和你图里的数值一致即可自行改）
x_lines = [-20, -10, 10, 20]
y_lines = [-20, 0, 30, 50]

fig, ax = plt.subplots(figsize=(6, 10))

# 画边框
ax.plot([x_lines[0], x_lines[-1], x_lines[-1], x_lines[0], x_lines[0]],
        [y_lines[0], y_lines[0], y_lines[-1], y_lines[-1], y_lines[0]],
        linewidth=2)

# 画分割线
for x in x_lines[1:-1]:
    ax.plot([x, x], [y_lines[0], y_lines[-1]], linestyle='--')

for y in y_lines[1:-1]:
    ax.plot([x_lines[0], x_lines[-1]], [y, y], linestyle='--')

# 区域编号
region_id = 0
for i in range(3):
    for j in range(3, 0, -1):
        cx = (x_lines[j] + x_lines[j-1]) / 2
        cy = (y_lines[2-i] + y_lines[3-i]) / 2
        ax.text(cx, cy, str(region_id),
                ha='center', va='center', fontsize=16)
        region_id += 1

# 自车位置（中心）
ax.scatter(0, 0, s=200, color='red', zorder=5)
ax.text(0, -3, 'Ego', ha='center', color='red')

# 车头方向箭头
ax.arrow(0, 0, 0, 8,
         head_width=1.5, head_length=3,
         fc='black', ec='black')

# 坐标轴设置
ax.set_xlim(22, -22)
ax.set_ylim(-22, 52)
ax.set_xlabel('Y (m)')
ax.set_ylabel('X (m)')
ax.set_aspect('equal')
ax.grid(False)

plt.show()
