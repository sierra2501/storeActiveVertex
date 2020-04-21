// ブラウザがIEか判定.
function checkBrowserIE() {
    var userAgent  = window.navigator.userAgent.toLowerCase();

    if (userAgent.indexOf('msie') != -1) {
        return true;
    } else if (userAgent.indexOf('trident/7') != -1) {
        return true;
    }
    return false;
    }

  // 外部のテキストファイルを読み込み.
function readFileToString(fileName) {
    // XMLHttpRequestを取得.
    var xmlHttp = null;
    if (checkBrowserIE()) {
        xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
    } else if (window.XMLHttpRequest) {
        xmlHttp = new XMLHttpRequest();
    }
    if (xmlHttp == null) return "";

    var str = "";
    try {
      // 第三引数をfalseにすると、同期読み込み。
      // 読み込みが完了するまで待つ（実際は非推奨）.
        xmlHttp.open("GET", fileName, false);
        xmlHttp.send(null);          // ここで読み込みが行われる.
        str = xmlHttp.responseText;  // 結果をテキストで取得.
    } catch(e) {
        window.alert(e);
    }
    return str;
}