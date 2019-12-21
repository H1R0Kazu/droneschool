# coding: UTF-8
# 講習名： ドローンソフトウェアエンジニア
# 記載日：　2019/12/21
# 作成者：　チームC
# ファイル名：　Day6_exam.py
# 内容　：　

# 使用する関数、クラスを宣言する
# from dronekit import connect, VehicleMode, LocationGlobalRelative
# 標準ライブラリのtimeを使う宣言
import time

# 該当箇所から waypoint 情報を取得する
import sys
import shutil
import requests
args = sys.argv
id = args[1]
URL = 'https://www.tajisoft.jp/mission_8th.waypoints' + id + '.md'
print(URL)

filepath = id + '.md'
print(filepath)
res = requests.get(URL, stream = True)
with open(filepath, 'wb') as fp:
    shutil.copyfileobj(res.raw, fp)


