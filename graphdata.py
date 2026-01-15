import numpy as np
from matplotlib import pyplot as plt
import matplotlib

# fname 为 你下载的字体库路径
zhfont1 = matplotlib.font_manager.FontProperties(fname="/data/code/untitled/simhei.ttf")
plt.rcParams['axes.unicode_minus'] = False

# if __name__=='__main__':
region0={'工厂设备': 8106, '噪声': 6833, '乘用车': 30398, '路沿': 1830, '非机动车': 1096, '工业车辆': 289, '商用车': 30565, '小障碍物': 1382, '行人': 4220, '抬杆': 69}
region1={'行人': 26666, '工业车辆': 5700, '工厂设备': 41536, '乘用车': 88781, '噪声': 14256, '路沿': 12756, '商用车': 121907, '非机动车': 1579, '小障碍物': 10105, '抬杆': 2480}
region2={'噪声': 4651, '乘用车': 14422, '商用车': 24259, '行人': 2375, '路沿': 3399, '工厂设备': 1853, '抬杆': 386, '工业车辆': 152, '小障碍物': 532, '非机动车': 59}
region3={'工厂设备': 316247, '行人': 61304, '小障碍物': 61769, '路沿': 206520, '噪声': 9565, '商用车': 727469, '乘用车': 1349915, '非机动车': 57790, '抬杆': 2785, '工业车辆': 594}
region4={'行人': 2268791, '工厂设备': 9113303, '噪声': 451957, '乘用车': 16233464, '抬杆': 252546, '小障碍物': 1184143, '路沿': 4026755, '非机动车': 388155, '商用车': 17370318, '工业车辆': 1325135}
region5={'乘用车': 226618, '路沿': 73280, '噪声': 7948, '商用车': 329460, '小障碍物': 10903, '抬杆': 743, '非机动车': 9123, '行人': 17822, '工厂设备': 195849, '工业车辆': 5289}
region6={'路沿': 62125, '商用车': 242784, '噪声': 5102, '乘用车': 498867, '行人': 11801, '小障碍物': 15571, '抬杆': 16480, '工厂设备': 93024, '非机动车': 15571, '工业车辆': 1461}
region7={'商用车': 3396404, '工厂设备': 1386306, '路沿': 225712, '噪声': 45050, '乘用车': 2200054, '行人': 774006, '小障碍物': 82960, '抬杆': 37705, '非机动车': 88789, '工业车辆': 107570}
region8={'行人': 5323, '商用车': 62851, '乘用车': 35939, '路沿': 12866, '噪声': 3392, '工厂设备': 64577, '抬杆': 440, '工业车辆': 473, '小障碍物': 1982, '非机动车': 2368}
# categories = list(region0.keys())  # 分类名称
# values = list(region0.values())  # 分类对应的数值

all_categories=['行人',
'乘用车',
'商用车',
'小障碍物',
'非机动车',
'抬杆',
'工业车辆',
'工厂设备',
'噪声',
'路沿']

#添加 数据中不存在，但是需要统计的类别，数量设置为0
for category in all_categories:
    if category not in all_categories:
        region0[category]=0
        region1[category]=0
        region2[category]=0
        region3[category]=0
        region4[category]=0
        region5[category]=0
        region6[category]=0
        region7[category]=0
        region8[category]=0


for k in region8.keys():
    print(k+'\t'+str(region8[k]))
    # print(str(region0[k]))
# # 创建柱状图
# plt.figure(figsize=(10, 6))  # 设置图形大小
# plt.barh(categories, values, color='skyblue')  # 水平柱状图
#
# # 设置标题和标签
# plt.title('Region0 类别数量柱状图', fontsize=16,fontproperties=zhfont1)
# plt.xlabel('数量', fontsize=12, fontproperties=zhfont1)
# plt.ylabel('类别', fontsize=12, fontproperties=zhfont1)
# # 显示图形
# plt.show()