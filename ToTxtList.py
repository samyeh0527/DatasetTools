import os


def Conversion_Txt(Apath,Traintxt):
    Apath_filelist = os.listdir(Apath)
    if not os.path.isdir(Traintxt):
        for _ in Apath_filelist:
            with open(Traintxt,'a+') as f:
                f.write(Apath+'/'+_ +'\n')
    else:
        with open(Traintxt,'W+') as f:
                pass
        for _ in Apath_filelist:
            with open(Traintxt,'a+') as f:
                f.write(Apath+'/'+_ +'\n')



if __name__ == "__main__":
    Apath = r'./exam/labels'
    Traintxt = './Traintxt.txt'
    # Conversion_Txt(Apath,Traintxt)