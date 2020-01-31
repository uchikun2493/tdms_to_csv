# tdms_to_csv

## Overview

tdmsをcsvに保存し直す，確認用にpngも生成

## Requirement

- python3
- numpy
- matplotlib
- py_modules
- gitのアカウント

## Install

適宜cdしてからgitからcloneする
```
$ git clone https://github.com/uchikun2493/tdms_to_csv.git
```

カレントディレクトリにtdms_to_csvが生成される

## Usage

外部モジュールのpy_modulesを利用するため，scriptsまでcd

```
$ cd tdms_to_csv/scripts
$ git clone https://github.com/aist9/py_modules.git
```

プログラム中の22行目はデータがあるディレクトリへ変更しておく
```
data_dir = '../data'
```

必要があれば25行目の保存先も好きな場所へ変更
```
save_dir = '../output'
```

## Other

何かあれば質問してください

