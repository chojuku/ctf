# Reversing
## まずやるべきコマンド
- file hoge
  - ELF 64-bit LSB executable
    - インテル64bitCPU用実行バイナリ
  - ELF：Executable and Linking Format
  - LSB：Least Significant Byte，つまりリトルエンディアン
- readelf -h hogeでELFヘッダ読める
- dynamically linked
- ldd hogeでどの共有ライブラリが呼び出されるか表示
- not stripped
  - シンボルテーブルが付属されて居る->読みやすい
  - ちなみにstrip hogeでシンボルテーブルを削除してファイルサイズを小さくすることができる
- strings hoge
  - バイナリファイルの可読文字列を抽出する．CTF的にはgrepと組み合わせてFlagを探す．

- strace -f ./hoge
  - システムコールとシグナルを追跡しながら実行するコマンド
  - システムコールはOSさんによろしく頼むやつ．
- ltrace -f ./hoge
  - ダイナミックリンクライブラリ呼び出しを追跡しながら実行するコマンド
  - fオプションはマルチプロセスなプログラムの子プロセスのみを選択するために必要

## インストールツール
- sudo yum install ltrace strace
- gdb-peda

## gdb-peda使い方
- startしたあとにsi(関数の中に入る)やni(関数の中に入らない)をして1行ずつみていくと，その時のregisters,code,stackが表示
  - http://inaz2.hatenablog.com/entry/2014/05/03/044943
  - http://uguisu.skr.jp/Windows/gdb.html
  - http://d.hatena.ne.jp/pyopyopyo/20100406/p1
  - http://d.hatena.ne.jp/shibason/20090624/1245840061
