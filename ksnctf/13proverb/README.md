# 13proverb

よくよく考えると怖い現象なのかも.
権限上見れないはずのものでもシンボリックリンクを貼ればみれてしまう事案
今回、実行ファイルのproverbはproverb.txtを読み込んでいた。
flag.txtをproverb.txtと思い込ませれば良い。
tmp/sub/で行える
ln -s ~/flag.txt(root) proverb.txt
ln -s ~/proverb proverb
読めてしまうロリポップ.

一応proverb中身

```
All's well that ends well.
A good beginning makes a good ending.
Many a true word is spoken in jest.
Fear is often greater than the danger.
Go for broke!
Fire is a good servant but a bad master.
The wolf knows what the ill beast thinks.
There is always a next time.
Spare the rod and spoil the child.
The calm before the storm.
The die is cast.
Take heed of the snake in the grass.
Confidence is a plant of slow growth.
Love is blind.
The sky's the limit...
Truth lies at the bottom of a well.
Blood is thicker than water.
Ignorance is bliss.
There's no way out.
Full of courtesy, full of craft.
Heaven helps those who help themselves.
Bad luck often brings good luck.
Misfortunes never come singly.
Nothing ventured, nothing gained.
Eternal Immortality.
```