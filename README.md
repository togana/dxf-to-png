# dxf-to-png

dxf ファイルを png に変換する

# ビルド

```sh
docker build --rm -t dxf-to-png .
```

# 利用方法

1. 変換したいファイルを input ディレクトリに配置する。
2. 下記のコマンドを実行する。

```sh
docker run --rm -it -v $(pwd):/app dxf-to-png
```

3. output ディレクトリに出力される。
