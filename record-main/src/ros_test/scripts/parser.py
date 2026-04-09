import struct
import argparse
import numpy as np
import rospy
from nav_msgs.msg import Odometry, Path
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA
from datetime import datetime, timedelta

def parse_odometry(file_path):
    odometry_data_list = []
    frame_size = 8 + 3*8 + 4*8 + 3*8 + 3*8  # 每个frame的大小: 时间戳(8) + 位姿(3*8 + 4*8) + 速度(3*8 + 3*8)

    with open(file_path, 'rb') as file:
        while True:
            # 读取一个frame的数据
            data = file.read(frame_size)
            if len(data) < frame_size:
                break  # 文件结尾

            # 解析frame的数据
            sec, nsec = struct.unpack('II', data[0:8])
            pos = struct.unpack('3d', data[8:8 + 3*8])
            orient = struct.unpack('4d', data[8 + 3*8:8 + 3*8 + 4*8])
            lin_vel = struct.unpack('3d', data[8 + 3*8 + 4*8:8 + 3*8 + 4*8 + 3*8])
            ang_vel = struct.unpack('3d', data[8 + 3*8 + 4*8 + 3*8:])

            odometry_msg = Odometry()
            odometry_msg.header.stamp.secs = sec
            odometry_msg.header.stamp.nsecs = nsec
            odometry_msg.header.frame_id = "odom"
            odometry_msg.pose.pose.position.x = pos[0]
            odometry_msg.pose.pose.position.y = pos[1]
            odometry_msg.pose.pose.position.z = pos[2]
            odometry_msg.pose.pose.orientation.x = orient[0]
            odometry_msg.pose.pose.orientation.y = orient[1]
            odometry_msg.pose.pose.orientation.z = orient[2]
            odometry_msg.pose.pose.orientation.w = orient[3]
            odometry_msg.twist.twist.linear.x = lin_vel[0]
            odometry_msg.twist.twist.linear.y = lin_vel[1]
            odometry_msg.twist.twist.linear.z = lin_vel[2]
            odometry_msg.twist.twist.angular.x = ang_vel[0]
            odometry_msg.twist.twist.angular.y = ang_vel[1]
            odometry_msg.twist.twist.angular.z = ang_vel[2]

            odometry_data_list.append(odometry_msg)

    return odometry_data_list

def parse_fsm_info(file_path):
    with open(file_path, 'rb') as file:
        while True:
            # 读取时间戳
            sec_data = file.read(4)
            nsec_data = file.read(4)
            if not sec_data or not nsec_data:
                break
            sec = struct.unpack('I', sec_data)[0]
            nsec = struct.unpack('I', nsec_data)[0]
            
            # 读取info大小
            info_size_data = file.read(4)
            if not info_size_data:
                break
            info_size = struct.unpack('I', info_size_data)[0]
            
            # 读取info
            info_data = file.read(info_size)
            if not info_data:
                break
            info = info_data.decode('utf-8')
            
            yield {
                'timestamp': f"{sec}.{nsec}",
                'info': info
            }

def parse_controller_info(file_path):
    marker_arraylist = []
    with open(file_path, 'rb') as file:
        marker_id = 0  # 用于唯一标识每个Marker
        while True:
            # 尝试读取时间戳
            timestamp_data = file.read(8)  # 读取 sec 和 nsec (4 bytes each)
            if len(timestamp_data) < 8:
                break  # 文件结束或读取失败，退出循环
            sec, nsec = struct.unpack('II', timestamp_data)
            timestamp = rospy.Time(sec, nsec)

            # 读取info字符串大小
            info_size_data = file.read(4)  # 读取info的大小 (uint32)
            if len(info_size_data) < 4:
                break  # 文件结束或读取失败，退出循环
            info_size = struct.unpack('I', info_size_data)[0]

            # 读取info字符串内容
            info_data = file.read(info_size)  # 读取实际info内容
            if len(info_data) < info_size:
                break  # 文件结束或读取失败，退出循环
            info = info_data.decode('utf-8')  # 将二进制数据解码为字符串

            # 创建Marker并填充数据
            marker_array = MarkerArray()
            marker = Marker()
            marker.header.frame_id = "odom"
            marker.header.stamp = timestamp
            marker.ns = "controller_info"
            marker.id = 0
            marker.type = Marker.TEXT_VIEW_FACING  # 选择显示文本
            marker.action = Marker.ADD
            marker.pose.position.x = 0  # 位置可以根据需求调整
            marker.pose.position.y = 0.0
            marker.pose.position.z = 1.0  # 在Z轴上提升，以便更好显示
            marker.pose.orientation.w = 1.0

            # Marker 大小和颜色
            marker.scale.z = 1  # 字体大小
            marker.color = ColorRGBA(1.0, 0.0, 0.0, 1.0)  # 红色字体

            # 设置文本为info内容
            timestamp_str = f"{timestamp.secs}.{timestamp.nsecs:09d}"
            utc_time = datetime.utcfromtimestamp(timestamp.to_sec())

            # 将UTC时间转换为北京时间（UTC+8）
            beijing_time = utc_time + timedelta(hours=8)
            beijing_time_str = beijing_time.strftime('%Y-%m-%d %H:%M:%S')
            marker.text = beijing_time_str

            # 添加到MarkerArray
            marker_array.markers.append(marker)

            marker_arraylist.append(marker_array)
            marker_id += 1  # 增加marker id，以确保每个Marker唯一

    return marker_arraylist

def parse_scan(file_path, frame_id):
    scans = []
    with open(file_path, 'rb') as file:
        while True:
            # 尝试读取时间戳
            timestamp_data = file.read(8)
            if len(timestamp_data) < 8:
                break
            sec, nsec = struct.unpack('II', timestamp_data)
            timestamp = rospy.Time(sec, nsec)

            # 读取LaserScan参数
            params_data = file.read(7 * 4)
            if len(params_data) < 7 * 4:
                break
            angle_min, angle_max, angle_increment, time_increment, scan_time, range_min, range_max = struct.unpack('7f', params_data)

            # 读取ranges数组
            ranges_size_data = file.read(4)
            if len(ranges_size_data) < 4:
                break
            ranges_size = struct.unpack('I', ranges_size_data)[0]
            ranges_data = file.read(ranges_size * 4)
            if len(ranges_data) < ranges_size * 4:
                break
            ranges = np.frombuffer(ranges_data, dtype=np.float32)

            # 读取intensities数组
            intensities_size_data = file.read(4)
            if len(intensities_size_data) < 4:
                break
            intensities_size = struct.unpack('I', intensities_size_data)[0]
            intensities_data = file.read(intensities_size * 4)
            if len(intensities_data) < intensities_size * 4:
                break
            intensities = np.frombuffer(intensities_data, dtype=np.float32)

            scan_msg = LaserScan()
            scan_msg.header.stamp = timestamp
            scan_msg.header.frame_id = frame_id
            scan_msg.angle_min = angle_min
            scan_msg.angle_max = angle_max
            scan_msg.angle_increment = angle_increment
            scan_msg.time_increment = time_increment
            scan_msg.scan_time = scan_time
            scan_msg.range_min = range_min
            scan_msg.range_max = range_max
            scan_msg.ranges = ranges.tolist()
            scan_msg.intensities = intensities.tolist()

            scans.append(scan_msg)

    return scans

def parse_scan_on_base_link(file_path):
    return parse_scan(file_path, "base_link")

def parse_scan_on_camera_link(file_path):
    return parse_scan(file_path, "camera_link")

def parse_path(file_path):
    paths = []
    with open(file_path, 'rb') as file:
        while True:
            # 读取路径的时间戳
            timestamp_data = file.read(8)
            if len(timestamp_data) < 8:
                break
            sec, nsec = struct.unpack('II', timestamp_data)
            timestamp = rospy.Time(sec, nsec)

            # 读取路径中的每个Pose
            poses_size_data = file.read(4)
            if len(poses_size_data) < 4:
                break
            poses_size = struct.unpack('I', poses_size_data)[0]

            poses = []
            for _ in range(poses_size):
                # 读取位姿
                # position = struct.unpack('3d', file.read(3 * 8))
                data = file.read(3 * 8)
                if len(data) == 24:
                    position = struct.unpack('3d', data)
                # orientation = struct.unpack('4d', file.read(4 * 8))
                data = file.read(4 * 8)
                if len(data) == 32:
                    orientation = struct.unpack('4d', data)

                pose = PoseStamped()
                pose.header.frame_id = "map"
                pose.header.stamp = timestamp
                pose.pose.position.x = position[0]
                pose.pose.position.y = position[1]
                pose.pose.position.z = position[2]
                pose.pose.orientation.x = orientation[0]
                pose.pose.orientation.y = orientation[1]
                pose.pose.orientation.z = orientation[2]
                pose.pose.orientation.w = orientation[3]
                poses.append(pose)

            path_msg = Path()
            path_msg.header.frame_id = "map"
            path_msg.header.stamp = timestamp
            path_msg.poses = poses
            paths.append(path_msg)

    return paths

def parse_pose(file_path):
    poses = []
    with open(file_path, 'rb') as file:
        while True:
            # 读取时间戳
            timestamp_data = file.read(8)
            if len(timestamp_data) < 8:
                break
            sec, nsec = struct.unpack('II', timestamp_data)
            timestamp = rospy.Time(sec, nsec)

            # 读取位姿
            position = struct.unpack('3d', file.read(3 * 8))
            # orientation = struct.unpack('4d', file.read(4 * 8))

            pose_msg = PoseStamped()
            pose_msg.header.stamp = timestamp
            pose_msg.pose.position.x = position[0]
            pose_msg.pose.position.y = position[1]
            pose_msg.pose.position.z = position[2]
            pose_msg.pose.orientation.x = orientation[0]
            pose_msg.pose.orientation.y = orientation[1]
            pose_msg.pose.orientation.z = orientation[2]
            pose_msg.pose.orientation.w = orientation[3]

            poses.append(pose_msg)

    return poses