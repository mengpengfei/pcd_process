**一、简介：**

pcd_process 为点云数据处理工具，目前支持分别对多个网格进行类别数量统计

---

**二、使用方法：**

###### 1、安装依赖

分别执行下面命令
pip install -r requirement.txt
cd pypcd
python setup.py install

###### 2、使用

2.1、配置
配置data_statistic.py中的labelmapping、effective_label和res_label_dict 参数。

2.2、使用

调用data_statistic.py的get_final_data函数获取统计结果。

get_final_data(root_dir,min_x,max_x,min_y,max_y) 函数的参数说明：

root_dir：pcd文件所在目录

min_x：需要统计的点云区域的最小x坐标

max_x：需要统计的点云区域的最大x坐标

min_y：需要统计的点云区域的最小y坐标

max_y：需要统计的点云区域的最大y坐标

2.3、可视化

使用matplotlib 对统计结果绘图、可视化。可视化例子代码：graphdata.py。

