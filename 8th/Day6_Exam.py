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
URL = 'https://www.tajisoft.jp/mission_8th.waypoints'
#print(URL)

res = requests.get(URL, stream = True)
#print(res.text)

waypoint_line = res.text.split("\n")
#print(waypoint_line)
#waypoint_line = res.text.split("\n")

#print(len(waypoint_line))
#print(type(waypoint_line))

for i in range(2, len(waypoint_line)):
#    print(type(waypoint_line[i]))
#    print(waypoint_line[i])
    waypoint_text = waypoint_line[i].split("\t")
    print(waypoint_text)
#    for j in range(len(waypoint_text)):
#       print(j)

#    print("\n")

#waypoint_text = waypoint_line.
