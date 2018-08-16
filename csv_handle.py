# -*- coding:utf-8 -*-
"""
    @File    CSV file, read and write. [python3.5]
    @Author  tx
    @Created On 2018-08-16
    @Updated On 2018-08-16
"""

__all__ = ['CsvHandle']

import os
import csv
from collections import Iterable
from pprint import pprint


class CsvHandle(object):
    @staticmethod
    def read_data(f_path, f_name, mode='r'):
        """
        读csv文件
        :param f_path: 文件路径
        :param f_name: 文件名
        :param mode: 文件打开模式
        :return: 数据列表
        """
        csv_file = os.path.join(f_path, f_name)
        with open(csv_file, mode) as fp:
            rows = csv.reader(fp)
            data_header = next(rows)  # 读取第一行的标题
            data = [row for row in rows]
        return data

    @staticmethod
    def write_data(data, f_path, f_name, mode='a'):
        """
        写csv文件
        :param data: 要写入的数据, 列表类型
        :param f_path: 文件路径
        :param f_name: 文件名
        :param mode: 文件打开模式, 默认'a'以追加方式打开
        :return: 文件全路径, 写入状态
        """
        csv_file = os.path.join(f_path, f_name)
        try:
            with open(csv_file, mode, newline='') as fp:
                writer = csv.writer(fp, dialect='excel')
                for item in data:
                    writer.writerow(item)
            return csv_file, True
        except Exception as e:
            print(e)
            os.remove(csv_file)
            return csv_file, False

    @staticmethod
    def format_data(head, values, keys):
        """
        格式化数据
        :param head: 头部数据
        :param values: 需要格式化的数据， 其中每一条数据要求为字典格式
        :param keys: 需要格式化数据的键值
        :return: 组合后的列表数据
        """
        f_data = list()
        if head:
            f_data.append(list(head))
        if not keys or not values or not isinstance(values, Iterable):
            return f_data
        data = [[item.get(key) for key in keys] for item in values]
        f_data.extend(data)
        return f_data


def test_read_file():
    print('### test read csv file: ')
    f_path = './'
    f_name = 'demo.csv'
    data = CsvHandle.read_data(f_path, f_name)
    pprint(data)
    print('\n')


def test_write_file():
    print('### test write csv file: ')
    f_path = './'
    f_name = 'demo1.csv'
    head = [u'id', u'地址', u'资产名称', u'添加/发现时间', u'管理员', u'安全状态', u'可用性', u'备注']
    data = [{'id': '1', 'address': '127.0.0.1', 'name': 'bbb', 'found_time': '2018/08/16',
             'admin': 'admin', 'safe_state': '安全', 'available': True, 'comment': '1fegweg'},
            {'id': '2', 'address': '127.0.0.2', 'name': 'cc', 'found_time': '2018/08/16',
             'admin': 'test', 'safe_state': '高危', 'available': False, 'comment': 1, 'aa': 'nihadfado'}]

    keys = ('id', 'address', 'name', 'found_time', 'admin', 'safe_state', 'available', 'comment')

    f_data = CsvHandle.format_data(head, data, keys=keys)  # 1.格式化数据
    ret = CsvHandle.write_data(f_data, f_path, f_name, 'w')  # 2.写入文件
    if not ret[1]:
        print("### save csv file[{}] failed!".format(ret[0]))
    else:
        print("### save csv file[{}] success!".format(ret[0]))


if __name__ == "__main__":
    test_read_file()
    test_write_file()
