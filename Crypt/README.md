# CTF:Crypt
## Cryptに良さげなPythonライブラリ
- https://pypi.org/project/pycrypto/
- pip install pycrypto

## シーザー暗号
- caesar.pyを使う

## RSA

```
暗号文y = 平文x ^ E % N
平文x = 暗号文y ^ D % N
NをN = pq (但しpとqは素数)
```
- が成り立つようにしたい
- 公開鍵が(E, N)，秘密鍵(D, N)
  - L = (p-1)と(q-1)の最小公倍数を求める(鍵ペアを作るための数)
  - Eは(p-1)(q-1)との最大公約数が1となるように適当にとる
  - EとLの最大公約数gcd(E, L)=1となるE(1 < E <L)を擬似乱数発生器で探す
  - ED % L = 1となるDを探す
    - ユークリッドの互除法でわかる
    - フェルマーの小定理よりx^(p-1) ≡1 (mod p)
- 素因数分解をするサイト: http://www.factordb.com/
- RSAについて:http://tsujimotter.hatenablog.com/entry/rsa
- 例えば以下が与えられたとき，Nは公開鍵のN，Eは平文をpowするE乗根，Cは暗号文

```
N = 97139961312384239075080721131188244842051515305572003521287545456189235939577
E = 65537
C = 77361455127455996572404451221401510145575776233122006907198858022042920987316
```

- 秘密鍵Dを手に入れ，暗号文をDecryptしたい．
  - まずNをhttp://www.factordb.com/で素因数分解し，pとq(但しp<q)とする
  - L = lcm((p-1)(q-1))を求める
  - あとはLを少しずつ足しながらDを探しておしまい
- pycryptoを使えば3ステップでできる

```
d = inverse(E, (p-1)*(q-1))
key = RSA.construct(map(int, (N, E, d)))
print(long_to_bytes(key.decrypt(C)))
```

# Misc
- 深瀬暗号ジェネレータ