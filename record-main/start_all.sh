#!/bin/bash

# 检查 roscore 是否已启动
if ! pgrep -x "roscore" > /dev/null; then
  echo "启动 roscore..."
  roscore &  # 后台启动 roscore
  sleep 3    # 等待 roscore 启动
else
  echo "roscore 已经运行。"
fi

# 打开 record.rviz
echo "启动 RViz 并加载 record.rviz..."
rviz -d record.rviz &  # 替换为 record.rviz 的实际路径
sleep 2  # 等待 RViz 稳定启动

# 运行 Python 文件
echo "运行 Python 脚本..."
python3 ./src/ros_test/scripts/test.py  # 替换为实际的 Python 文件路径
rosrun tf2_ros static_transform_publisher 0.0 0.0 0.0 0.0 0.0 0.872664625997164 odom map

echo "所有任务已完成！"

