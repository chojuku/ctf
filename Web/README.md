# CTF:Web

## Cookieを変更してGETしたいとき
- curl -b name=admin hoge | grep flag
- Edit this cookieで差し込み，再読み込み

## SQLインジェクション
$' UNION SELECT null, null, null, null; #$
## OSコマンドインジェクション
## ディレクトリトラバーサル
## XSS