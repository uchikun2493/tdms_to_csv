# my default import modules
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# add path
sys.path.append(os.path.join('py_modules/'))

# import modules
from file_io import tdms_read

# **********************************************
# main
# **********************************************
def main():

    # -------------------------------------
    # init
    # -------------------------------------
    # データが保存されているディレクトリ(適宜変更)
    data_dir = '../data'

    # 出力先のディレクトリ(適宜変更)
    save_dir = '../output'

    # サブディレクトリ名
    save_sub_dir = ['csv', 'fig']

    # 出力先のディレクトリを生成
    for sub_dir in save_sub_dir:
        save_path = os.path.join(save_dir, sub_dir)
        os.makedirs(save_path, exist_ok=True)

    # -------------------------------------
    # data_dirからtdmsファイルのパスを取得
    # 自然順にソート
    # -------------------------------------
    file_paths = tdms_read.tdms_path_get(data_dir)

    # -------------------------------------
    # ファイルを順番に読み込み保存する
    # -------------------------------------
    for i, file_path in enumerate(file_paths):
        print('\rFile name: ' + file_path , end="")

        # tdmsデータの読み込み
        data = tdms_read.tdms_to_nparr(file_path)

        # ファイル名だけ抜き出し
        file_name = os.path.basename(file_path)

        # 'tdms'を'csv'へ置き換える
        save_name = file_name.replace('tdms', 'csv')

        # 保存パスを生成
        save_path = os.path.join(save_dir, save_sub_dir[0], save_name)
        
        # csvで保存
        np.savetxt(save_path, data, delimiter=',')

        # +++++++++++++++++++++++++
        # ついでにpngにして保存

        # 'tdms'を'csv'へ置き換える
        save_name = file_name.replace('tdms', 'png')
        # 保存パスを生成
        save_path = os.path.join(save_dir, save_sub_dir[1], save_name)

        # 保存処理
        plt.plot(data, c='k')
        plt.savefig(save_path)
        plt.close()

    print('\n --end--')
   
if __name__ == '__main__':
    main()

