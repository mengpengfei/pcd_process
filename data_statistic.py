import sys

from pypcd import pypcd
import numpy as np
import os
from pathlib import Path

#标注数据中ID和类别的映射关系
labelmapping={0:"BARRIER_ARM", 1:"PEDESTRIAN", 2:"TWO_WHEELER", 3:"TRICYCLE",
              4:"CAR", 5:"BUS", 6:"TRUCK", 7:"FORKLIFT", 8:"TRAILER", 9:"DELIVERY_VEHICLE"
    , 10:"SMALL_OBSTACLE", 11:"POLE", 12:"TREE", 13:"EQUIPMENT"
    , 14:"GREEN_BELT", 15:"CURB", 16:"BUILDING", 17:"FENCE"
    , 18:"DISCRETE_POINT", 19:"ROAD", 20:"NOISE", 21:"MID_OBSTACLE", 22:"BJG_OBSTACLE"}

#需要统计的类别
effective_label=['PEDESTRIAN','CAR','BUS','TRUCK','SMALL_OBSTACLE','TWO_WHEELER','TRICYCLE','BARRIER_ARM'
    ,'FORKLIFT','TRAILER','DELIVERY_VEHICLE','EQUIPMENT','DISCRETE_POINT','NOISE','CURB']

#标注类别和最终统计结果类别的映射关系
res_label_dict={
    "PEDESTRIAN":"行人",
    "CAR":"乘用车",
    "BUS":"商用车",
    "TRUCK":"商用车",
    "SMALL_OBSTACLE":"小障碍物",
    "TWO_WHEELER":"非机动车",
    "TRICYCLE":"非机动车",
    "BARRIER_ARM":"抬杆",
    "FORKLIFT":"工业车辆",
    "TRAILER":"工业车辆",
    "DELIVERY_VEHICLE":"工业车辆",
    "EQUIPMENT":"工厂设备",
    "DISCRETE_POINT":"噪声",
    "NOISE":"噪声",
    "CURB":"路沿"
}

def get_label_count(pcd_path,min_x,max_x,min_y,max_y):
    # also can read from file handles.
    cloud = pypcd.PointCloud.from_path(pcd_path)
    # pc.pc_data has the data as a structured array
    # pc.fields, pc.count, etc have the metadata

    pc_data_new = cloud.pc_data.copy()
    pcds_total = np.array(pc_data_new.tolist())
    valid_mask = ~np.isnan(pcds_total.sum(axis=1))
    pcds_total = pcds_total[valid_mask]

    mask = np.where((pcds_total[:, 0] <= max_x) & (pcds_total[:, 0] >= min_x) & (pcds_total[:, 1] >= min_y) & (pcds_total[:, 1] <= max_y))

    data1=pcds_total[mask]
    # data2=pcds_total[0<pcds_total[:,1]<20]

    # pcds_total = pcds_total.astype(np.float32)
    labels, counts=np.unique(data1[:, 3], return_counts=True)
    label_count=dict()
    # 输出结果
    for label, count in zip(labels, counts):
        label_count[label]=count
        # print(f"Label {label} appears {count} times.")
    return label_count
def get_all_label_count(root_dir,min_x,max_x,min_y,max_y):
    res_dict=dict()
    count=0
    pcds=Path(root_dir).glob("**/*.pcd")
    for pcd in pcds:
        count += 1
        # if count >=10:
        #     break
        tmp_label_count=get_label_count(pcd,min_x,max_x,min_y,max_y)
        for tmp_key in tmp_label_count.keys():
            history_count=res_dict.get(tmp_key)
            if history_count is None:
                res_dict[tmp_key]=tmp_label_count[tmp_key]
            else:
                res_dict[tmp_key] += tmp_label_count[tmp_key]
        # print(res_dict)
        # print('-------------------------------')
    res_dict1=dict()
    for res_dict_key in res_dict.keys():
        res_dict1[labelmapping[res_dict_key]]=res_dict[res_dict_key]
    return res_dict1

def relabel_data(res_dict):
    relabel_dict=dict()
    for k in res_dict.keys():
        if k not in effective_label:
            continue
        else:
            tmp_value=relabel_dict.get(res_label_dict[k])
            if tmp_value is None:
                relabel_dict[res_label_dict[k]]=res_dict[k]
            else:
                relabel_dict[res_label_dict[k]]=res_dict[k]+tmp_value
    return relabel_dict

def get_final_data(root_dir,min_x,max_x,min_y,max_y):
    res_dict_all=get_all_label_count(root_dir,min_x,max_x,min_y,max_y)
    return relabel_data(res_dict_all)



#total
#{'PEDESTRIAN': 2381178, 'FORKLIFT': 1188286, 'TRAILER': 141249, 'EQUIPMENT': 9676894, 'BUILDING': 21099722, 'DISCRETE_POINT': 80719, 'ROAD': 57902361, 'NOISE': 414491, 'CAR': 17943598, 'POLE': 1395663, 'TREE': 15114855, 'GREEN_BELT': 7799672, 'BARRIER_ARM': 259009, 'SMALL_OBSTACLE': 1268834, 'CURB': 4324540, 'TRICYCLE': 121032, 'FENCE': 4611881, 'BUS': 8717008, 'TRUCK': 9886969, 'DELIVERY_VEHICLE': 7624, 'TWO_WHEELER': 336770, 'MID_OBSTACLE': 8827, 'BJG_OBSTACLE': 150191}
#second total res
#{'PEDESTRIAN': 3172308, 'BUS': 10300493, 'FORKLIFT': 1276081, 'TRAILER': 162603, 'POLE': 1721666, 'TREE': 20066700, 'EQUIPMENT': 11220801, 'GREEN_BELT': 9098049, 'CURB': 4625243, 'BUILDING': 26853294, 'DISCRETE_POINT': 108672, 'ROAD': 58218425, 'NOISE': 440082, 'CAR': 20678458, 'BARRIER_ARM': 313634, 'SMALL_OBSTACLE': 1369347, 'TRICYCLE': 179286, 'TRUCK': 12005523, 'FENCE': 5430707, 'DELIVERY_VEHICLE': 7979, 'TWO_WHEELER': 385244, 'MID_OBSTACLE': 11824, 'BJG_OBSTACLE': 168792}

if __name__=='__main__':
    # for k in res_label_dict.keys():
    #     print(res_label_dict[k])
    # sys.exit(-1)

    root_dir='/data/pcd_test/label_pcd_old'
    # root_dir='/data/pcd_test/test1'
    # pcds=Path(root_dir).glob("**/*.pcd")
    # set=set()
    # res_dict=dict()
    res_region0=get_final_data(root_dir,30,50,10,20)
    # print('--------res_region0--------')
    print(res_region0)
    # print('----------------------------')
    res_region1=get_final_data(root_dir,30,50,-10,10)
    # print('--------res_region1--------')
    print(res_region1)
    # print('----------------------------')
    res_region2=get_final_data(root_dir,30,50,-20,-10)
    # print('--------res_region2--------')
    print(res_region2)
    # print('----------------------------')
    res_region3=get_final_data(root_dir,0,30,10,20)
    # print('--------res_region3--------')
    print(res_region3)
    # print('----------------------------')
    res_region4=get_final_data(root_dir,0,30,-10,10)
    # print('--------res_region4--------')
    print(res_region4)
    # print('----------------------------')
    res_region5=get_final_data(root_dir,0,30,-20,-10)
    # print('--------res_region5--------')
    print(res_region5)
    # print('----------------------------')

    res_region6=get_final_data(root_dir,-20,0,10,20)
    # print('--------res_region6--------')
    print(res_region6)
    # print('----------------------------')
    res_region7=get_final_data(root_dir,-20,0,-10,10)
    # print('--------res_region7--------')
    print(res_region7)
    # print('----------------------------')
    res_region8=get_final_data(root_dir,-20,0,-20,-10)
    # print('--------res_region8--------')
    print(res_region8)
    # print('----------------------------')