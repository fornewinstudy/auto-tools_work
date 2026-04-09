import struct
import argparse
import numpy as np

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

            odometry_data = {
                'header': {
                    'stamp': {
                        'secs': sec,
                        'nsecs': nsec
                    }
                },
                'pose': {
                    'position': {
                        'x': pos[0],
                        'y': pos[1],
                        'z': pos[2]
                    },
                    'orientation': {
                        'x': orient[0],
                        'y': orient[1],
                        'z': orient[2],
                        'w': orient[3]
                    }
                },
                'twist': {
                    'linear': {
                        'x': lin_vel[0],
                        'y': lin_vel[1],
                        'z': lin_vel[2]
                    },
                    'angular': {
                        'x': ang_vel[0],
                        'y': ang_vel[1],
                        'z': ang_vel[2]
                    }
                }
            }

            odometry_data_list.append(odometry_data)

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
def parse_scan(file_path):
    scans = []
    with open(file_path, 'rb') as file:
        while True:
            # 尝试读取时间戳
            timestamp_data = file.read(8)
            if len(timestamp_data) < 8:
                break
            sec, nsec = struct.unpack('II', timestamp_data)
            timestamp = sec + nsec * 1e-9

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

            scan_data = {
                'timestamp': timestamp,
                'angle_min': angle_min,
                'angle_max': angle_max,
                'angle_increment': angle_increment,
                'time_increment': time_increment,
                'scan_time': scan_time,
                'range_min': range_min,
                'range_max': range_max,
                'ranges': ranges.tolist(),  # 转换为列表，便于显示
                'intensities': intensities.tolist(),  # 转换为列表，便于显示
            }

            scans.append(scan_data)

    return scans


def parse_path(file_path):
    paths = []
    with open(file_path, 'rb') as file:
        while True:
            # 读取路径的时间戳
            timestamp_data = file.read(8)
            if len(timestamp_data) < 8:
                break
            sec, nsec = struct.unpack('II', timestamp_data)
            timestamp = sec + nsec * 1e-9

            # 读取路径中的每个Pose
            poses_size_data = file.read(4)
            if len(poses_size_data) < 4:
                break
            poses_size = struct.unpack('I', poses_size_data)[0]

            poses = []
            for _ in range(poses_size):
                # 读取位姿
                position = struct.unpack('3d', file.read(3 * 8))
                orientation = struct.unpack('4d', file.read(4 * 8))

                pose = {
                    'position': {
                        'x': position[0],
                        'y': position[1],
                        'z': position[2],
                    },
                    'orientation': {
                        'x': orientation[0],
                        'y': orientation[1],
                        'z': orientation[2],
                        'w': orientation[3],
                    }
                }
                poses.append(pose)

            path_data = {
                'timestamp': timestamp,
                'poses': poses
            }
            paths.append(path_data)

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
            timestamp = sec + nsec * 1e-9

            # 读取位姿
            position = struct.unpack('3d', file.read(3 * 8))
            orientation = struct.unpack('4d', file.read(4 * 8))

            pose = {
                'timestamp': timestamp,
                'position': {
                    'x': position[0],
                    'y': position[1],
                    'z': position[2],
                },
                'orientation': {
                    'x': orientation[0],
                    'y': orientation[1],
                    'z': orientation[2],
                    'w': orientation[3],
                }
            }
            poses.append(pose)

    return poses

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse odometry data from a binary file.")
    parser.add_argument("file_path", type=str, help="The path to the binary file containing odometry data.")
    args = parser.parse_args()

    # odometry_data_list = parse_odometry(args.file_path)
    # for i, odometry_data in enumerate(odometry_data_list):
    #     print(f"Frame {i}: {odometry_data}")
    # info = parse_fsm_info(args.file_path)
    # for entry in info:
    #     print(f"Timestamp: {entry['timestamp']}, Info: {entry['info']}")
    # scans = parse_scan(args.file_path)
    # for i, scan in enumerate(scans):
    #     print(f"Scan {i}: {scan}")
    # path_data = parse_path(args.file_path)
    # for i, path in enumerate(path_data):
    #     print(f"Path {i}: Timestamp: {path['timestamp']}")
    #     for j, pose in enumerate(path['poses']):
    #         print(f"  Pose {j}: {pose}")
    poses_data = parse_pose(args.file_path)
    for i, pose in enumerate(poses_data):
        print(f"Pose {i}: {pose}")