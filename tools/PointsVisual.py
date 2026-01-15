import open3d as o3d
import numpy as np
# import torch

# from utils.mogo_color_map import get_colormap

import yaml
from pypcd import pypcd

classname_to_color = {  # RGB.
    "BARRIER_ARM": "#CFCFCF",
    "PEDESTRIAN": "#FAFFF5",
    "TWO_WHEELER": "#FFFF00",
    "TRICYCLE": "#FF5B8E",
    "CAR": "#799024",
    "BUS": "#785C6F",
    "TRUCK": "#DDCDFF",
    "FORKLIFT": "#FFA859",
    "TRAILER": "#FF6D67",
    "DELIVERY_VEHICLE": "#C0AE89",
    "SMALL_OBSTACLE": "#7BC32B",
    "POLE": "#FBB577",
    "TREE": "#FF7FC3",
    "EQUIPMENT": "#827E67",
    "GREEN_BELT": "#FFDB62",
    "CURB": "#4D3D48",
    "BUILDING": "#9E9BFF",
    "FENCE": "#87D8FF",
    "DISCRETE_POINT": "#FF8800",
    "ROAD": "#119599",
    "NOISE": "#F1F1EF",
    "MID_OBSTACLE": "#FF6FA2",
    "BJG_OBSTACLE": "#4EAB93"
}

# npz_file = np.load('/hdm/mengpengfei/data_3d/mogo/val/train_hy_taxi_2d3d_4725_20221110_21/1668048147.550318003.npz')
# cloud = pypcd.PointCloud.from_path('/workspace/data1/turbo_data/mengpengfei/data_3d/mogo/rbs_ori/train_dali_010099_jira_20230815/json/20230804162031-2392729728-full-PA010099_6/3d_url/pcd/1691137223.430028915.pcd')
# cloud = pypcd.PointCloud.from_path('/workspace/data1/turbo_data/HDMap/Mapping/pre_mark/pcd/seg/test_result/1684913676.099830151.pcd')
# cloud = pypcd.PointCloud.from_path('/workspace/data1/turbo_data/HDMap/Mapping/pre_mark/pcd/seg/test_pcd/1684913675.899829865.pcd')
# cloud = pypcd.PointCloud.from_path('/workspace/data1/turbo_data/mengpengfei/data_3d/mogo/demo_label/3d_url_res/1684913675.899829865.pcd')
cloud = pypcd.PointCloud.from_path('/data/pcd_test/label_pcd_old/000000.pcd')
new2 = cloud.pc_data.copy()
# print(new2)
npz_file = np.array(new2.tolist())

pcds = npz_file[:,:3]
print(pcds)
pcds_label_use = npz_file[:,-1]


# pcds_label_use[pcds_label_use!=0]=12
# # pcds_color = (pcds_color-np.min(pcds_color))/(np.max(pcds_color)-np.min(pcds_color))
# #pcds_color=np.expand_dims(pcds_color,axis=1).repeat(3,axis=1)/255
# # pcds_color=np.asarray(pcds_color,dtype=np.long)
# pcds_label_use = npz_file['pcd_label']
# print("->正在加载点云... ")
# classname_to_color=get_colormap()


# with open(r'/hdm/mengpengfei/semantic-segmentation/mm3d/CPGNet_1/datasets/mogo_v1.yaml', 'r') as f:
#     task_cfg = yaml.load(f)
# learning_map=task_cfg['label_map']
# for k,v in learning_map:
#     print(v)
# # label_map_inv=task_cfg['label_map_inv']
# pcds_label_use_map=[learning_map[la] for la in pcds_label_use]
# pcds_label_use_color=[classname_to_color[label_map_inv[ca_n]] for ca_n in pcds_label_use_map]


# pcds_label_use_color=np.asarray(pcds_label_use_color,dtype=np.long)/255

# pcds_label_use_color=np.zeros_like(pcds_label_use_color)
# pcds_label_use_color[:,2]=1

vis = o3d.visualization.Visualizer()
vis.create_window()
vis.get_render_option().point_size=0.5
vis.get_render_option().background_color=np.zeros(3)

pd=o3d.geometry.PointCloud()

pd.points=o3d.utility.Vector3dVector(pcds)
#coordinate axis
coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=10)

vis.add_geometry(pd)
vis.add_geometry(coordinate_frame)

# view_control = vis.get_view_control()
# view_control.set_lookat([0, 0, 0])  # 设置视角中心
# view_control.set_up([0, 1, 0])  # 设置“上”方向
# view_control.set_front([0, 0, -1])  # 设置前方方向

vis.run()
vis.destroy_window()
# o3d.visualization.draw_geometries([pd])

# pcd = o3d.io.read_point_cloud("/hdm/mengpengfei/software/PCDViewer-4.8.0-Ubuntu18.04/test_data/2.pcd")
# pcd = o3d.io.read_point_cloud(pcds)
# pcd = o3d.io.rea
# print(pcd.points)
# pcds=np.fromfile("/hdm/mengpengfei/software/PCDViewer-4.8.0-Ubuntu18.04/test_data/2.pcd")
# print()
# print("->正在可视化点云")
# o3d.visualization.draw_geometries([pcd])
