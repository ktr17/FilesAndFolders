import os, os.path
from Config import Config

"""
探索対象のフォルダを指定する
"""
path = './'
varsions = []
url = ''

if __name__=='__main__':
    version = input("バージョンを入力してください： ")
    files = []

    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            files.append(filename)

    print(files)
