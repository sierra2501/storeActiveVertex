
if (xshade.scene().active_shape().type == 7):

    # 頂点・コントロールポイントの番号のタプルの配列
    v_str = TARGET_V
    v_array = v_str.split(',')

    # 全ての頂点の選択を非選択にする
    xshade.scene().active_shape().select_all_control_points(False)

    # 頂点の選択を開始
    xshade.scene().active_shape().begin_selecting_control_points()

    # 頂点の選択のループ
    for v_num in v_array:

        try:
            int(v_num)
            xshade.scene().active_shape().set_active_control_point(int(v_num),True)
        except:
            print("Error : " + v_num)

    # 頂点の選択を終了
    xshade.scene().active_shape().end_selecting_control_points()