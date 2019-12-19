# coding: UTF-8
# 講習名： ドローンソフトウェアエンジニア
# 記載日：　2019/12/28
# 作成者：　宮田浩和
# ファイル名：　flyght_test_hm_03.py
# 内容　：　絶対座標で移動する

# 使用する関数、クラスを宣言する
from dronekit import connect, VehicleMode
# 標準ライブラリのtimeを使う宣言
import time

# 機体に接続する
# シミュレータに接続
vehicle = connect('127.0.0.1:14550', wait_ready=True)

# アーミング可能かチェック
while not vehicle.is_armable:
    print "Waiting for vehicle to initializ)e…"
    time.sleep(1)    

# vehicle.home_locationに値がセットされるまで
# downloadを繰り返し実行する
while not vehicle.home_location:
    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()

    if not vehicle.home_location:
        print "Waiting for home location ..."

# ホームロケーションの取得完了
print "\n Home location: %s " % vehicle.home_location

# vehicle is an instance of the Vehicle class
print "Autopilot Firmware version: %s" % vehicle.version
# print "Autopilot capabilities (supports ftp): %s" % vehicle.capabilities.ftp
print "Global Location: %s" % vehicle.location.global_frame
print "Global Location (relative altitude): %s" % vehicle.location.global_relative_frame
print "Local Location: %s" % vehicle.location.local_frame    #NED
print "Attitude: %s" % vehicle.attitude
print "Velocity: %s" % vehicle.velocity
print "GPS: %s" % vehicle.gps_0
print "Groundspeed: %s" % vehicle.groundspeed
print "Airspeed: %s" % vehicle.airspeed
print "Gimbal status: %s" % vehicle.gimbal
print "Battery: %s" % vehicle.battery
print "EKF OK?: %s" % vehicle.ekf_ok
print "Last Heartbeat: %s" % vehicle.last_heartbeat
print "Rangefinder: %s" % vehicle.rangefinder
print "Rangefinder distance: %s" % vehicle.rangefinder.distance
print "Rangefinder voltage: %s" % vehicle.rangefinder.voltage
print "Heading: %s" % vehicle.heading
print "Is Armable?: %s" % vehicle.is_armable
print "System status: %s" % vehicle.system_status.state
print "Mode: %s" % vehicle.mode.name    # settable
print "Armed: %s" % vehicle.armed    # settable

# 
print "\n Class key and Value."
for key, value in vehicle.location.global_frame.__dict__.items():
	print(key, value)


print(vehicle.location.global_frame.lat)

# プログラム終わり
