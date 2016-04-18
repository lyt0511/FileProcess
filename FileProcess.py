#-*- coding:utf-8 -*-
"""
一个简单的python文件处理小工具，可以对文件进行分子文件等处理

Author: lyt0511
Version: 0.0.1
Date: 2016-4-9
Language: Python2.7.11
Editor: Sublime Text 2
"""
import codecs 
import random

class FileProcess:
        """
        本类用于处理文本文件

        目前实现的功能有：分割文件（随机分配为k份）

        Attributes
        ----------

                'k': 用于设置待处理文件分成子文件的份数

        """

        def __init__(self,k=5):
            self.k = k
        
        def splitFile(self, path='BX-Book-Ratings.csv',filename='file',mode=1):
                """
                加载文本数据，分割后子文件名格式为：公共名称+数字

                Attributes
                ----------

                    'path': 待分割文件的目录名和文件名
                    'filename': 分割后文件名字的公共部分
                    'mode': 随机分割模式，1指每k行作为一组随机分割至k个子文件中
                                          2指对于整个文件随机分割至k个子文件中
                """
                i = 0
                cnt = 0
                #
                # 生成k个子文件,并加载其指针到字典
                #
                ch = filename
                dic = {}
                for j in range(self.k):
                        nfile = ch + str(j) + '.csv'
                        wf = codecs.open(nfile, 'w', 'utf8')
                        dic[j] = wf
                rf = codecs.open(path, 'r', 'utf8')
                if mode==1:
                #
                # 首先生成一个列表，按行读取文本文件，然后每读取k行就
                # 对列表进行一次洗牌。 根据列表每个元素对应字典的键值写入文件
                # 从而达到每k行随机写入子文件的效果
                #
                    item = range(self.k)
                    for line in rf:
                            if i%self.k == 0:
                                    random.shuffle(item)
                                    cnt = 0
                            i += 1
                            dic[item[cnt]].write(line)
                            cnt += 1
                elif mode==2:
                #
                # 首先生成一个字典，按行读取文本文件，然后将每行载入字典，并记录总行数
                # 然后生成一个以0到总行数作为值的列表，对其进行洗牌
                # 将洗牌后列表分割为k个子列表，再进行k次循环分别对每个子文件写入每个子列表顺序对应字典的键值
                # 从而达到将整个文件随机写入子文件的效果
                #
                    dic2 = {}
                    for line in rf:
                            dic2[i] = line
                            i += 1
                    item = range(i)
                    random.shuffle(item)
                    point = 0
                    offset = i/self.k
                    for j in range(self.k):
                        item2 = item[point:point+offset]
                        for l in range(offset):
                            dic[j].write(dic2[item2[l]])
                        point = point + offset
                #
                # 关闭读，写文件指针
                #
                rf.close()   
                for j in range(self.k):
                        dic[j].close()
                print '成功读取 %d 行文本记录'%i
