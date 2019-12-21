# coding: UTF-8
# 講習名： ドローンソフトウェアエンジニア
# 記載日：　2019/12/20
# 作成者：　宮田浩和
# ファイル名：　flyght_test_hm_03.py
# 内容　：　絶対座標で移動する

# 使用する関数、クラスを宣言する
from dronekit import connect, VehicleMode, LocationGlobalRelative
# 標準ライブラリのtimeを使う宣言
import time

### ←これ以降これは川村フィードバックコメントという印です。

### ここで、lat, lon, altを引数にして指定した場所まで飛ぶ関数を定義するとコードがすっきりしますね。
### 到達チェック関数も引数に入れてあげるともっと便利になります。下記は例です。
def myGoto(lat, lon, alt, reachedCheackFn):
    ### 座標オブジェクトへ変換して飛行指示
    ### チェック関数を呼び出す。ここの関数を切り替えることで将来的に到達判定ができるようになったら一定時間待つバージョンからすぐ切り替えられますね。
    reachedCheackFn()

### このようなリスナーコールバック関数を活用するとコードがすっきりしてきます。
def location_callback(self, attr_name, msg):
    pass

# 機体に接続する
# シミュレータに接続
vehicle = connect('127.0.0.1:14550', wait_ready=True)

# アーミング可能かチェック
while not vehicle.is_armable:
    print "Waiting for vehicle to initialize"
    time.sleep(1)

# vehicle.home_locationに値がセットされるまで
# downloadを繰り返し実行する
while not vehicle.home_location:
    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()

    if not vehicle.home_location:
        print "Waiting for home location ..."

# ホームロケーションの取得結果表示
print "\n Home location: %s " % vehicle.home_location

# アーミング実行
# フライトモードを”GUIDED”に変更し、armedにTrueを設定する。
print "Arming Moters"
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True

while not vehicle.armed:
    print "Waiting for arming..."
    time.sleep(1)

# 目標高度を設定
targetAltitude = 20

# テイクオフの実行
# 20mの高さまで離陸する
print "Take Off!!"
vehicle.simple_takeoff(targetAltitude)

# 目標の高度に達するまで待つ
while True:
    print "Altitude: ", vehicle.location.global_relative_frame.alt 

    if vehicle.location.global_relative_frame.alt >= targetAltitude * 0.95:
        print "Reached target altitude"
        break

    time.sleep(1)
    

# 座標指定で移動1　北
# 目標ロケーションの設定 
target1_location_lat = vehicle.location.global_relative_frame.lat + 0.002
target1_location_lon = vehicle.location.global_relative_frame.lon
target1_location_alt = 30

aLocation = LocationGlobalRelative(target1_location_lat, target1_location_lon, target1_location_alt)

vehicle.simple_goto(aLocation)

# 目標のロケーションに達するまで待つ
# 場所検知がうまくいかないため、時間指定(60秒)待つ
#while True:
for i in range(60):
    # ロケーション情報の表示
    ### このように常にモニタリングしておきたい属性がある場合はリスナー関数を作って登録しておくとすっきりします。
    ### https://dronekit-python.readthedocs.io/en/latest/automodule.html#dronekit.Vehicle.add_attribute_listener
    print "\n Current location: %s " % vehicle.location.global_relative_frame
    print "\n Traget location: %s " % aLocation

#    if vehicle.location.global_relative_frame.lat >= target1_location_lat  * 0.9:
#        print "Reached target lat"
#        break

    time.sleep(1)

# 座標指定で移動2 東
# 目標ロケーションの設定 
target2_location_lat = vehicle.location.global_relative_frame.lat
target2_location_lon = vehicle.location.global_relative_frame.lon + 0.002
target2_location_alt = 40

aLocation = LocationGlobalRelative(target2_location_lat, target2_location_lon, target2_location_alt)

vehicle.simple_goto(aLocation)

# 目標のロケーションに達するまで待つ
# 場所検知がうまくいかないため、時間指定(60秒)待つ
#while True:
for i in range(60):
    # ロケーション情報の表示
    print "\n Current location: %s " % vehicle.location.global_relative_frame
    print "\n Traget location: %s " % aLocation

#    if vehicle.location.global_relative_frame.lon >= target2_location_lon  * 0.9:
#       print "Reached target lon"
#        break

    time.sleep(1)

# 座標指定で移動3 南
# 目標ロケーションの設定 
target3_location_lat = vehicle.location.global_relative_frame.lat - 0.002
target3_location_lon = vehicle.location.global_relative_frame.lon
target3_location_alt = 50

aLocation = LocationGlobalRelative(target3_location_lat, target3_location_lon, target3_location_alt)

vehicle.simple_goto(aLocation)

# 目標のロケーションに達するまで待つ
# 場所検知がうまくいかないため、時間指定(60秒)待つ
#while True:
for i in range(60):
    # ロケーション情報の表示
    print "\n Current location: %s " % vehicle.location.global_relative_frame
    print "\n Traget location: %s " % aLocation

#    if vehicle.location.global_relative_frame.lat <= target3_location_lat  * 0.9:
#        print "Reached target lat"
#        break

    time.sleep(1)


# 座標指定で移動4 西
# 目標ロケーションの設定
target4_location_lat = vehicle.location.global_relative_frame.lat
target4_location_lon = vehicle.location.global_relative_frame.lon - 0.002
target4_location_alt = 60

aLocation = LocationGlobalRelative(target4_location_lat, target4_location_lon, target4_location_alt)

vehicle.simple_goto(aLocation)

# 目標のロケーションに達するまで待つ
# 場所検知がうまくいかないため、時間指定(60秒)待つ
#while True:
for i in range(60):
    # ロケーション情報の表示
    print "\n Current location: %s " % vehicle.location.global_relative_frame
    print "\n Traget location: %s " % aLocation

#    if vehicle.location.global_relative_frame.lat <= target4_location_lat  * 0.9:
#       print "Reached target lat"
#        break

### ここはtime.sleep(1)が抜けてる？

# Return To Launch　
vehicle.mode = VehicleMode("RTL")


# プログラム終わり
