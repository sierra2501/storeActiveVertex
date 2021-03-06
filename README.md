# storeActiveVertex.py / selectVertex.py
Shade3Dのスクリプト。選択した頂点を一時保存する。

## インストール（Windows）
1. 上記「Clone or download」からローカルに落とします。
2. 落としたフォルダを「Program Files」のShade3Dフォルダの中にある「widgets」に入れます。
3. Shade3Dを起動して、メニューバーの「スクリプト」に「選択した頂点を一時保存」があるか確認します。

## 使い方
### 1. 保存する
ポリゴンメッシュで選択された頂点の番号を右の（灰色の）テキストボックス内に書き込みます。その際、保存時の情報として、形状の名前と日時が表示されます。

### 2. 選択する
テキストボックス内の頂点の番号を選択します。なお、編集モードに関わらず実行（選択）されます。


### 3. クリア
テキストボックスと保存時の情報をクリアします。

## ※ 注意事項
1. スクリプトのウィンドウを落とすと、保存した情報も消えます。
2. 「保存」した後にポリゴンを編集した（特に頂点数が上下した）場合、「選択」しても前と同じ頂点を選択しない可能性があります。
3. 選択された形状または頂点数によって、数値の枠内の色が変わります。
   1. 緑色は正常値です。
   2. 黄色は頂点が選択されていない（テキストボックス内が空）状態です。
   3. 赤色はポリゴンメッシュ以外が選択された状態です。

## バージョン
-v 1.1.0

## ライセンス
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

## 作者
sierra  
- [Wordpress](http://tenteroring.luna.ddns.vc/sierra/)  
- [Twitter](https://twitter.com/sierra2501?lang=ja)
