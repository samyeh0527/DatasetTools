#HC
import os 
import shutil
from tqdm import tqdm
from decimal import *
#setting default path and cls 0 ,1 
from ascllart import art
def cpfile(number,cls0,cls1,cls2,labels,pathfile,cls_numbs):
    allFileList = os.listdir(pathfile)
    loss_number = 0
    for file in tqdm(allFileList):
        new_pathfile = pathfile+'/'+file
        with open(new_pathfile,'r+') as f:
                line = f.readlines()
                #replac [''] to " " and split str to list next find first character 0 or 1  
                newline = str(line)
                replacecharacter=["'",'[',']']
                for _ in replacecharacter:
                    newline = newline.replace(str(_),'')
                newline = newline.split(',')
                newline = str(newline[0]).split(' ')
                number_cls = number / cls_numbs
                if  number >number_cls * cls_numbs :
                    loss_number= number - number_cls
                if newline[0] == '0' and cls0 < number_cls+loss_number : 
                    shutil.copyfile(new_pathfile,labels+'/'+file)
                    cls0+=1 
                elif newline[0] == '1' and cls1 < number_cls :
                    shutil.copyfile(new_pathfile,labels+'/'+file)
                    cls1+=1
                elif newline[0] == '2' and cls2 < number_cls :
                    shutil.copyfile(new_pathfile,labels+'/'+file)
                    cls2+=1
    return cls0,cls1,cls2
def checkcontent(path):
    print('***point path is =) ',path,'***  \n')
    print('\nRun check all txt content .. if txt file is None will show file name........  \n')
    allFileList = os.listdir(path)
    
    for file in tqdm(allFileList):
        newpathfile = str(path+'/'+file)
        with open(newpathfile,'r+') as f:
            content = f.readlines()
            if content is None : print('this file txt is None   "',newpathfile,'"  ' )


def cpimages(path,savepath,labels):
    AllimgList = os.listdir(path)
    pathList=[]
    replacecharacter=['.jpg',"'",'[',']']
    pathList.append(labels)
    for _ in replacecharacter:
        AllimgList = str(AllimgList).replace(_,'')
    AllimgList = AllimgList.split(',')
    AllimgList_int = list(map(int,AllimgList))
    print('\ncheck difference set ...')
    for _ in tqdm(range(len(pathList))):
        filelist = pathList[_]
        replacecharacter=['.txt',"'",'[',']']
        print('\nNow is '+ filelist +'... \n')  
        filelist = os.listdir(filelist)
        for _ in replacecharacter:
            filelist = str(filelist).replace(_,'')
        filelist = filelist.split(',')
        filelist2_format = filelist
        filelist = list(map(int,filelist))
        countSort = sorted(list(map(str,set(AllimgList_int)&set(filelist))))
        
        print('total .. ' ,len(countSort))
        if len(set(countSort)^set(filelist)) > 0 : 
            print('difference set  '+ set(countSort)^set(filelist))
        else:
            for format_ in tqdm(list(filelist2_format)):
                format_ = str(format_).replace(' ','')
                shutil.copy(path+'/'+str(format_)+'.jpg',savepath+'/'+str(format_)+'.jpg')


if __name__ == '__main__':
    art.hisnchun()
    #labels path
    pathfile = r'D:\DatasetBenchmark\DatasetTools\text\ProfileMask2\labels'
    #image path
    imgapthfile = r'D:\DatasetBenchmark\DatasetTools\text\ProfileMask2\images'
    allFileList = os.listdir(pathfile)
    cls0 ,cls1,cls2= 0,0,0
    #can change rannge number (X,Y+1,Z)
    dataset_length = 10
    dataset_splict = 1
    cls_numbs = 2
    for _ in range(dataset_length,dataset_length+5,dataset_splict):
        folderpath = './dataset'+str(_)
        if not os.path.isdir(folderpath):
            os.mkdir(folderpath)
            images = folderpath+'/images'
            labels = folderpath+'/labels'
            if not os.path.isdir(images):
                os.mkdir(images)
            if not os.path.isdir(labels):
                os.mkdir(labels)
            savepath = images
            cls0 ,cls1 ,cls2 = cpfile(_,cls0,cls1,cls2,labels,pathfile,cls_numbs)
            checkcontent(labels)
            cpimages(imgapthfile,savepath,labels)
        print(f'log : class 0  {cls0}.  class 1  {cls1}.  class 2  {cls2}. ')
    art.complete()
    # art.mario()


