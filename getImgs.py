# -*- coding=utf-8 -*-
import os,sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

class getImgs:
    def __init__(self, Path, Topath):
        # 得到两个路径
        self.path = self.Path2Std(Path)
        self.toPath = self.Path2Std(Topath)

    def start(self):
        # 举出html存放路径下所有文件
        all_file = os.listdir(self.path)
        exists_file = os.listdir(self.toPath)
        # print all_file
        for each in all_file:
            print each + ' is start to convert.'
            if not each.endswith('.html') or each in exists_file:
                continue
            name = each.decode('utf-8')
            FilePath = self.path + name
            soup = BeautifulSoup(open(FilePath),'lxml')
            imgs =  soup.findAll('img')
            for img in imgs:
                if img['src'].endswith('jpg' or 'png'):
                    img['src'] = 'https://pic4.zhimg.com/' + img['src'][:-4] + '_b.jpg'
                else:
                    img['src'] = 'https://pic4.zhimg.com/' + img['src'] + '_b.jpg'

            filename = self.toPath + each
            f = file(filename,'w')
            f.write(str(soup))
            f.close
            print name +  ' was successfully converted.'


    def Path2Std(self, Path):
        Path = Path.decode('utf-8')
        Path = Path.replace('\\', '/')
        if Path.endswith('/'):
            pass
        else:
            Path += '/'
        # print Path
        return Path

if __name__ == '__main__':
        path = 'papers'
        ToPath = path + '_img'
        zh = getImgs(path, ToPath)
        zh.start()

