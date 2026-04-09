import os
import argparse
import rospy
import tf
import tf.transformations as tft
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import Quaternion

from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Path, Odometry
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import TransformStamped, PoseStamped
from parser import parse_odometry, parse_fsm_info, parse_scan_on_base_link, parse_scan_on_camera_link, parse_path, parse_pose, parse_controller_info
from enum import Enum, auto
from collections import defaultdict
from std_msgs.msg import String
from datetime import datetime, timedelta, timezone
from geometry_msgs.msg import Point
from std_msgs.msg import ColorRGBA
from visualization_msgs.msg import Marker
import math
import matplotlib.pyplot as plt


class FileType(Enum):
    ODOMETRY = auto()
    DECISION_INFO = auto()
    PLANNER_INFO = auto()
    CONTROLLER_INFO = auto()
    DENSE_SCAN = auto()
    FRONT_STATIC_SCAN = auto()
    LEFT_STATIC_SCAN = auto()
    RIGHT_STATIC_SCAN = auto()
    FRONT_MOVE_SCAN = auto()
    LEFT_MOVE_SCAN = auto()
    RIGHT_MOVE_SCAN = auto()
    VIRTUAL_SCAN = auto()
    FOOTPRINT = auto()
    PATH = auto()
    POSE = auto()
    UNKNOWN = auto()
    
def get_file_type(filename):
    if 'odom' in filename:
        return FileType.ODOMETRY
    elif 'decisionInfo' in filename:
        return FileType.DECISION_INFO
    elif 'plannerInfo' in filename:
        return FileType.PLANNER_INFO
    elif 'controllerInfo' in filename:
        return FileType.CONTROLLER_INFO
    elif 'denseScan' in filename:
        return FileType.DENSE_SCAN
    elif 'frontStaticScan' in filename:
        return FileType.FRONT_STATIC_SCAN
    elif 'leftStaticScan' in filename:
        return FileType.LEFT_STATIC_SCAN
    elif 'rightStaticScan' in filename:
        return FileType.RIGHT_STATIC_SCAN
    elif 'frontMoveScan' in filename:
        return FileType.FRONT_MOVE_SCAN
    elif 'leftMoveScan' in filename:
        return FileType.LEFT_MOVE_SCAN
    elif 'rightMoveScan' in filename:
        return FileType.RIGHT_MOVE_SCAN
    elif 'virtualScan' in filename:
        return FileType.VIRTUAL_SCAN
    elif 'footprint' in filename:
        return FileType.FOOTPRINT
    elif 'path' in filename:
        return FileType.PATH
    # elif 'pose' in filename:
    #     return FileType.POSE
    else:
        return FileType.UNKNOWN
        
def process_files(directory):
    # 定义解析函数映射字典
    parse_function_map = {
        FileType.ODOMETRY: parse_odometry,
        FileType.DECISION_INFO: parse_fsm_info,
        FileType.PLANNER_INFO: parse_fsm_info,
        FileType.CONTROLLER_INFO: parse_controller_info,
        FileType.DENSE_SCAN: parse_scan_on_camera_link,
        FileType.FRONT_STATIC_SCAN: parse_scan_on_camera_link,
        FileType.LEFT_STATIC_SCAN: parse_scan_on_camera_link,
        FileType.RIGHT_STATIC_SCAN: parse_scan_on_camera_link,
        FileType.FRONT_MOVE_SCAN: parse_scan_on_camera_link,
        FileType.LEFT_MOVE_SCAN: parse_scan_on_camera_link,
        FileType.RIGHT_MOVE_SCAN: parse_scan_on_camera_link,
        FileType.VIRTUAL_SCAN: parse_scan_on_base_link,
        FileType.FOOTPRINT: parse_scan_on_base_link,
        FileType.PATH: parse_path,
        # FileType.POSE: parse_pose,
    }

    data_map = {ft.name: [] for ft in FileType}
    # 获取目录中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_type = get_file_type(filename)
            parse_function = parse_function_map.get(file_type, None)
            if parse_function:
                data_map[file_type.name].append(parse_function(file_path))
            else:
                print(f"Unknown file type: {filename}")
    return data_map
    
    
def get_min_timestamp(data_map):
    min_timestamp = None
    for data_list in data_map.values():
        for datas in data_list:
            for data in datas:  # 正常迭代其他可迭代的对象
                if isinstance(data,MarkerArray):
                    for marker in data.markers:
                        timestamp= marker.header.stamp
                        if min_timestamp is None or timestamp < min_timestamp:
                            min_timestamp = timestamp
                if isinstance(data, (Odometry, PoseStamped, LaserScan, Path)):
                    timestamp = data.header.stamp
                    if min_timestamp is None or timestamp < min_timestamp:
                        min_timestamp = timestamp
    return min_timestamp
    
def adjust_timestamps(data_map, time_difference):
    adjusted_data_map = defaultdict(list)
    for key, data_list in data_map.items():
        for datas in data_list:
            for data in datas:  # 正常迭代其他可迭代的对象
                if isinstance(data,MarkerArray):
                    for marker in data.markers:
                        marker.header.stamp += time_difference
                        adjusted_data_map[key].append(data)
                if isinstance(data, (Odometry, PoseStamped, LaserScan, Path)):
                    data.header.stamp += time_difference
                    adjusted_data_map[key].append(data)
    return adjusted_data_map

def publish_footprint():
    marker_pub = rospy.Publisher('robot_footprint', Marker, queue_size=10)
    rate = rospy.Rate(10)
    footprint = [
        Point(0.85, 0.33, 0),   # 右前角
        Point(0.85, -0.33, 0),  # 右后角
        Point(-0.2, -0.33, 0), # 左后角
        Point(-0.2, 0.33, 0)   # 左前角
    ]
    marker = Marker()
    marker.header.frame_id = "base_link"  # 使用机器人坐标系
    marker.header.stamp = rospy.Time.now()
    marker.ns = "robot_footprint"
    marker.id = 0
    marker.type = Marker.LINE_STRIP  # 使用LINE_STRIP来绘制多边形边界
    marker.action = Marker.ADD

    # 设置颜色
    marker.color = ColorRGBA(1.0, 1.0, 1.0, 1.0)
    marker.scale.x = 0.02  # 设置线条宽度
    # 将足迹的顶点添加到Marker消息中
    for point in footprint:
        marker.points.append(point)
    marker.points.append(footprint[0])   
    
    # 在base_link前0.3m处画一个半径为0.25m的圆
    circle_center = Point(0.3, 0, 0)  # 圆心位置在base_link前0.3m
    circle_radius = 0.25  # 半径0.25米
    num_points = 100  # 圆上点的数量，越多圆越光滑

    # 计算圆上每个点的坐标
    for i in range(num_points + 1):  # 多加一个点来闭合圆
        angle = 2 * math.pi * i / num_points  # 均匀分布的角度
        x = circle_center.x + circle_radius * math.cos(angle)
        y = circle_center.y + circle_radius * math.sin(angle)
        circle_point = Point(x, y, 0)
        marker.points.append(circle_point)
    
    marker_pub.publish(marker)

    
def publish_data(data_map, time_difference, jump_time):
    publishers = {
        FileType.DECISION_INFO: rospy.Publisher('/decision_info', String, queue_size=10),
        FileType.ODOMETRY: rospy.Publisher('/odom', Odometry, queue_size=10),
        FileType.CONTROLLER_INFO: rospy.Publisher('/controller_info', MarkerArray, queue_size=10),  # MarkerArray publisher
        FileType.DENSE_SCAN: rospy.Publisher('/dense_scan', LaserScan, queue_size=10),
        FileType.FRONT_STATIC_SCAN: rospy.Publisher('/front_static_scan', LaserScan, queue_size=10),
        FileType.LEFT_STATIC_SCAN: rospy.Publisher('/left_static_scan', LaserScan, queue_size=10),
        FileType.RIGHT_STATIC_SCAN: rospy.Publisher('/right_static_scan', LaserScan, queue_size=10),
        FileType.FRONT_MOVE_SCAN: rospy.Publisher('/front_move_scan', LaserScan, queue_size=10),
        FileType.LEFT_MOVE_SCAN: rospy.Publisher('/left_move_scan', LaserScan, queue_size=10),
        FileType.RIGHT_MOVE_SCAN: rospy.Publisher('/right_move_scan', LaserScan, queue_size=10),
        FileType.VIRTUAL_SCAN: rospy.Publisher('/virtual_scan', LaserScan, queue_size=10),
        FileType.FOOTPRINT: rospy.Publisher('/footprint', LaserScan, queue_size=10),
        FileType.PATH: rospy.Publisher('/path', Path, queue_size=10),
    }
    timestamp_publisher = rospy.Publisher('/timestamp', MarkerArray, queue_size=10)
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(100)  # 100 Hz
    print(f"record publish sucess!")
    while not rospy.is_shutdown():
        current_time = rospy.Time.now()
        current_time = rospy.Time(current_time.secs + jump_time, current_time.nsecs)
        for key, data_list in data_map.items():
            publisher = publishers.get(FileType[key])
            if not publisher:
                continue
            if key == FileType.CONTROLLER_INFO.name:
                for data in data_list:
                    for marker in data.markers:
                        if marker.header.stamp <= current_time:
                            publisher.publish(data)
                            data_list.remove(data)

            if key != FileType.CONTROLLER_INFO.name:
                for data in data_list:
                    if data.header.stamp <= current_time:
                        publisher.publish(data)  # 发布其他消息类型
                        if key == FileType.ODOMETRY.name:
                            #print("tf")
                            publish_footprint()
                            position = data.pose.pose.position
                            orientation = data.pose.pose.orientation
                            # quaternion = tft.quaternion_from_euler(0, 0, 0.8726646259971648)
    
                            # # 创建 tf2 的 Quaternion 对象（四元数）
                            # quat = Quaternion()
                            # quat.x = quaternion[0]
                            # quat.y = quaternion[1]
                            # quat.z = quaternion[2]
                            # quat.w = quaternion[3]
                            br.sendTransform((position.x, position.y, position.z),
                                             (orientation.x, orientation.y, orientation.z, orientation.w),
                                             data.header.stamp,
                                             "base_link",
                                             "odom")
                            br.sendTransform((0.7202149 , 0.05873897, 0.39943391),
                                             (0.0, 0.0,  0.0, 1.0),
                                             data.header.stamp,
                                             "camera_link",
                                             "base_link")
                            br.sendTransform((0, 0, 0),  # 假设 odom 相对于 map 没有位移
                                            (0.000, 0.000, 0.0, 1.0),  # 假设 odom 和 map 之间没有旋转
                                            data.header.stamp,
                                            "map",  # 子坐标系
                                            "odom"    # 父坐标系
                                            )
                            
                            # 计算 UTC 时间
                            utc_time = datetime.utcfromtimestamp((data.header.stamp - time_difference).to_sec())
                            # 转换为北京时间（UTC+8）
                            beijing_time = utc_time + timedelta(hours=8)
                            # 格式化时间字符串，手动添加小数秒
                            beijing_time_str = f"{beijing_time.strftime('%Y-%m-%d %H:%M:%S')}.{beijing_time.microsecond:06d}"
                            # 创建 Marker
                            marker = Marker()
                            marker.header.frame_id = "odom"  # 替换为你的坐标系
                            marker.header.stamp = rospy.Time.now()
                            marker.ns = "timestamp"
                            marker.id = 0
                            marker.type = Marker.TEXT_VIEW_FACING
                            marker.action = Marker.ADD
                            marker.pose.position.x = 0.0
                            marker.pose.position.y = 0.0
                            marker.pose.position.z = 1.0
                            marker.pose.orientation.x = 0.0
                            marker.pose.orientation.y = 0.0
                            marker.pose.orientation.z = 0.0
                            marker.pose.orientation.w = 1.0
                            marker.scale.z = 1.0  # 文本大小
                            marker.color.a = 1.0
                            marker.color.r = 0.0
                            marker.color.g = 1.0
                            marker.color.b = 0.0
                            marker.text = beijing_time_str  # 时间字符串作为文本内容
                    
                            # 将 Marker 添加到 MarkerArray
                            marker_array = MarkerArray()
                            marker_array.markers.append(marker)
                    
                            # 发布 MarkerArray
                            timestamp_publisher.publish(marker_array)
                        
                        data_list.remove(data)
            rate.sleep() 
            

directory = input("请输入路径：")
speeduptime = int(input("请输入跳转时间："))
data_map = process_files(directory)
dense_scan = data_map['ODOMETRY']

records = dense_scan[0]  # 假设 dense_scan 是一个包含多条 LaserScan 数据的列表
# 提取时间戳（转换为浮点秒数）
timestamps = [
    rec.header.stamp.secs + rec.header.stamp.nsecs / 1e9
    for rec in records
]

# timestamps为绝对时间戳列表
differences = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
plt.figure(figsize=(10,5))
plt.plot(differences, 'o-')
plt.title("Time Differences Between Consecutive Frames")
plt.xlabel("Frame index (i means interval between frame i and i+1)")
plt.ylabel("Time difference (seconds)")
# plt.grid(True)
# plt.show()
# plt.pause(0.001)

rospy.init_node('record_publisher')
odom_pub = rospy.Publisher('/odom', Odometry, queue_size=10)

# 解析文件
data_map = process_files(directory)
min_timestamp = get_min_timestamp(data_map)
current_time = rospy.Time.now()
time_difference = current_time - min_timestamp    
adjusted_data_map = adjust_timestamps(data_map, time_difference)
publish_data(adjusted_data_map, time_difference, speeduptime)
    
