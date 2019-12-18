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
