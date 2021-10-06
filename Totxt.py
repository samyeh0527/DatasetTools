#CoCoSTD

import os


def Conversion_Txt(Apath):
    Apath_filelist = os.listdir(Apath)
    Traintxt = './Traintxt.txt'
    if not os.path.isdir(Traintxt):
        for _ in Apath_filelist:
            with open(Traintxt,'a+') as f:
                f.write(Apath+'/'+_ +'\n')
    else:
        for _ in Apath_filelist:
            with open(Traintxt,'a+') as f:
                f.write(Apath+'/'+_ +'\n')






Apath = r'./exam/labels'
Conversion_Txt(Apath)
