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

        目前实现的功能有：分子文件（随机分配为k份）

        Attributes
        ----------

                'filename': 用于设置待处理文件的所在目录和文件名
                'k': 用于设置待处理文件分成子文件的份数

        """

        def __init__(self,filename,k=5):
            self.filename = filename
            self.k = k
        
        def loadFile(self, path=''):
                """加载文本数据，path是文本所在目录和其文件名"""
                i = 0
                cnt = 0
                path = self.filename
                #
                # 生成k个子文件,并加载其指针到字典
                #
                ch = 'file'
                dic = {}
                for j in range(self.k):
                        nfile = ch + str(j) + '.csv'
                        wf = codecs.open(nfile, 'w', 'utf8')
                        dic[j] = wf
                #
                # 首先生成一个列表，按行读取文本文件，然后每读取k行就
                # 对列表进行一次洗牌。 根据列表每个元素对应字典的键值写入文件
                # 从而达到随机写入子文件的效果
                #
                rf = codecs.open(path, 'r', 'utf8')
                item = [0,1,2,3,4]
                for line in rf:
                        if i%self.k == 0:
                                random.shuffle(item)
                                cnt = 0
                        i += 1
                        dic[item[cnt]].write(line)
                        cnt += 1
                #
                # 关闭读，写文件指针
                #
                rf.close()   
                for j in range(self.k):
                        dic[j].close()
                print '成功读取 %d 行文本记录'%i
