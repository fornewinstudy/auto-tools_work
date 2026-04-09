# record

## 修改ROS主机
sudo vim ~/.bashrc

## 添加以下内容
export ROS_HOSTNAME=localhost
export ROS_MASTER_URI=http://localhost:11311

## 给脚本添加执行权限
chmod +x start_all.sh

## 执行脚本
./start_all.sh

## 输入record文件路径
请输入路径：/home/mimeng/logspace/1227gan/userdata/logs/record/1538

## 输入record跳转时间（s）
请输入跳转时间：0

