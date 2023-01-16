#!/usr/bin/env python
# encoding: utf-8
'''
只适用于 一个 info, 对应一个 flv的b站视频
'''
import codecs
import json
import os.path


def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)

    arr = []
    for allDir in pathDir:
        child = os.path.join('%s\%s' % (filepath, allDir))
        if os.path.isfile(child):
            if check_contain_chinese:
                pass
            # readFile(child)
            if 'info' in str(child):
                new_path = ''
                # read the info file for name
                pa = str(child).split('\\')[:-1]
                path = "\\".join(map(str, pa))
                with codecs.open(child, 'r', 'utf-8') as f:
                    content = f.read()
                    con = json.loads(content)
                    new_path = path + '\\' + con["PartName"].replace('  ', '.') + '.flv'
                    arr.append(new_path)
            if 'flv' in str(child):
                os.rename(child, arr[len(arr) - 1])

            continue
        eachFile(child)


if __name__ == "__main__":
    # TODO 自动获取目录
    # TODO 已经改过的忽略
    filenames = 'D:\\bilibili\\45682252'  # refer root dir
    arr = []
    eachFile(filenames)
