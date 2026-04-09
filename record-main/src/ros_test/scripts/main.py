import os
import argparse
import rospy
import tf
import tf.transformations as tft
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Path, Odometry
from geometry_msgs.msg import TransformStamped, PoseStamped
from visualization_msgs.msg import Marker, MarkerArray
from parser import parse_odometry, parse_fsm_info, parse_scan_on_base_link, parse_scan_on_camera_link, parse_path, parse_pose, parse_controller_info
from enum import Enum, auto
from collections import defaultdict
from std_msgs.msg import String

class FileType(Enum):
    ODOMETRY = auto()
    DECISION_INFO = auto()
    PLANNER_INFO = auto()
    CONTROLLER_INFO = auto()
    DENSE_SCAN = auto()
    FRONT_STATIC_SCAN = auto()
    LEFT_STATIC_SCAN = auto()
    RIGHT_STATIC_SCAN = auto()
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
    elif 'virtualScan' in filename:
        return FileType.VIRTUAL_SCAN
    elif 'footprint' in filename:
        return FileType.FOOTPRINT
    # elif 'path' in filename:
    #     return FileType.PATH
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
        FileType.VIRTUAL_SCAN: parse_scan_on_base_link,
        FileType.FOOTPRINT: parse_scan_on_base_link,
        # FileType.PATH: parse_path,
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
            for data in datas:
                if isinstance(data, (Odometry, PoseStamped, LaserScan, Path)):
                    timestamp = data.header.stamp
                    if min_timestamp is None or timestamp < min_timestamp:
                        min_timestamp = timestamp
    return min_timestamp

def adjust_timestamps(data_map, time_difference):
    adjusted_data_map = defaultdict(list)
    for key, data_list in data_map.items():
        for datas in data_list:
            for data in datas:
                if isinstance(data, (Odometry, PoseStamped, LaserScan, Path)):
                    data.header.stamp += time_difference
                    adjusted_data_map[key].append(data)
    return adjusted_data_map

class DataPublisher:
    def __init__(self):
        self.publishers = {
            FileType.ODOMETRY: rospy.Publisher('/odom', Odometry, queue_size=10),
            FileType.DECISION_INFO: rospy.Publisher('/decision_info', String, queue_size=10),
            FileType.CONTROLLER_INFO: rospy.Publisher('/controller_info', String, queue_size=10),
            FileType.DENSE_SCAN: rospy.Publisher('/dense_scan', LaserScan, queue_size=10),
            FileType.FRONT_STATIC_SCAN: rospy.Publisher('/front_static_scan', LaserScan, queue_size=10),
            FileType.LEFT_STATIC_SCAN: rospy.Publisher('/left_static_scan', LaserScan, queue_size=10),
            FileType.RIGHT_STATIC_SCAN: rospy.Publisher('/right_static_scan', LaserScan, queue_size=10),
            FileType.VIRTUAL_SCAN: rospy.Publisher('/virtual_scan', LaserScan, queue_size=10),
            FileType.FOOTPRINT: rospy.Publisher('/footprint', LaserScan, queue_size=10),
            FileType.PATH: rospy.Publisher('/path', Path, queue_size=10),
            FileType.POSE: rospy.Publisher('/pose', PoseStamped, queue_size=10),
        }
        self.br = tf.TransformBroadcaster()

    def publish(self, file_type, data):
        if file_type == FileType.ODOMETRY:
            self.publish_odometry(data)
        elif file_type == FileType.DECISION_INFO:
            self.publish_decision_info(data)
        elif file_type == FileType.CONTROLLER_INFO:
            self.publish_controller_info(data)
        elif file_type == FileType.DENSE_SCAN:
            self.publish_scan(data)
        elif file_type == FileType.FRONT_STATIC_SCAN:
            self.publish_scan(data)
        elif file_type == FileType.LEFT_STATIC_SCAN:
            self.publish_scan(data)
        elif file_type == FileType.RIGHT_STATIC_SCAN:
            self.publish_scan(data)
        elif file_type == FileType.VIRTUAL_SCAN:
            self.publish_scan(data)
        elif file_type == FileType.FOOTPRINT:
            self.publish_scan(data)
        elif file_type == FileType.PATH:
            self.publish_path(data)
        elif file_type == FileType.POSE:
            self.publish_pose(data)

    def publish_odometry(self, data):
        position = data.pose.pose.position
        orientation = data.pose.pose.orientation
        self.br.sendTransform((position.x, position.y, position.z),
                              (orientation.x, orientation.y, orientation.z, orientation.w),
                              data.header.stamp,
                              "base_link",
                              "odom")
        self.publishers[FileType.ODOMETRY].publish(data)

    def publish_decision_info(self, data):
        self.publishers[FileType.DECISION_INFO].publish(data)

    def publish_controller_info(self, data):
        self.publishers[FileType.CONTROLLER_INFO].publish(data)

    def publish_scan(self, data):
        self.publishers[FileType.DENSE_SCAN].publish(data)

    def publish_path(self, data):
        self.publishers[FileType.PATH].publish(data)

    def publish_pose(self, data):
        self.publishers[FileType.POSE].publish(data)

if __name__ == '__main__':
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='Process some binary data files.')
    parser.add_argument('directory', type=str, help='Directory containing the data files')
    args = parser.parse_args()

    # 调用处理文件的函数
    process_files(args.directory)
