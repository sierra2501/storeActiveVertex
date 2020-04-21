import time
from datetime import datetime

# タイムスタンプ
time_stamp = time.time()
time_stamp = datetime.fromtimestamp(time_stamp)
time_stamp.strftime("%Y/%m/%d %H:%M:%S")

# 選択したポリゴンメッシュの形状名
polygon_n = xshade.scene().active_shape().name

# ポリゴンメッシュなら実行
if (xshade.scene().active_shape().type == 7):

    # 選択されている頂点・コントロールポイントの番号のタプル
    active_v = xshade.scene().active_shape().active_vertex_indices

    # 文字列化とカッコの削除
    active_v = str(active_v)
    active_v = active_v.replace("(", "")
    active_v = active_v.replace(")", "")

    # 色
    if (active_v == ""):
        color_flag= "Y"
    else:
        color_flag= "G"

    
    result = str(color_flag) + "," + str(time_stamp) + ", " + polygon_n + ", " + active_v

else:

    #s 色
    color_flag= "R"

    result = str(color_flag) + "," + str(time_stamp) + ", " + polygon_n + ", " + "Not Polygon Mesh"

