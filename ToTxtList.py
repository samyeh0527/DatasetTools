import os
import csv

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
def Conversion_v3Text(Apath):
    line = None
    Apath_filelist = os.listdir(Apath)
    with open('train_info.csv', 'w+', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['img_id', 'xmin', 'ymin','xmax','ymax','class_id'])
    for labeltxt in Apath_filelist:
        with open(Apath+'/'+labeltxt,'r+') as f:
            line = f.read().splitlines()
            with open('train_info.csv', 'a+', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for _ in range (0,len(line)):
                    single = line[_].split(' ')
                    writer.writerow([labeltxt,single[1],single[2],single[3],single[4],single[0]])

                            
    



if __name__ == "__main__":
    Apath = r'./exam/labels'
    Traintxt = './Traintxt.txt'
    ans = Conversion_v3Text(Apath)
    