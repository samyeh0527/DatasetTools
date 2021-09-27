#HC
import os 
import shutil
from tqdm import tqdm, trange
#setting default path and cls 0 ,1 
from ascllart import art
def cpfile(number,cls0,cls1_2,labels):
    for file in tqdm(allFileList):
        new_pathfile = pathfile+'/'+file
        #if file != 'cls0' or file != 'cls1_2':
        with open(new_pathfile,'r+') as f:
                line = f.readlines()
                #replac [''] to " " and split str to list next find first character 0 or 1  
                newline = str(line)
                replacecharacter=["'",'[',']']
                for _ in replacecharacter:
                    newline = newline.replace(str(_),'')
                newline = newline.split(',')
                newline = str(newline[0]).split(' ')
                if newline[0] == '0' and cls0 < number/2:
                    shutil.copyfile(new_pathfile,labels+'/'+file)
                    cls0+=1 
                elif newline[0] != '0' and cls1_2 < number/2 :
                    shutil.copyfile(new_pathfile,labels+'/'+file)
                    cls1_2+=1
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
        countSort = sorted(list(map(int,set(AllimgList_int)&set(filelist))))
        
        print('total .. ' ,len(countSort))
        if len(set(countSort)^set(filelist)) > 0 : 
            print('difference set  '+ set(countSort)^set(filelist))
        else:
            for format_ in tqdm(list(filelist2_format)):
                format_ = str(format_).replace(' ','')
                shutil.copy(imgapthfile+'/'+str(format_)+'.jpg',savepath+'/'+str(format_)+'.jpg')


if __name__ == '__main__':
    art.hisnchun()
    pathfile = r'./PWMFD_Train/labels'
    imgapthfile = r'./PWMFD_Train/images'
    allFileList = os.listdir(pathfile)
    cls0 ,cls1_2= 0,0
    for _ in range(500,1001,500):
        folderpath = './PWMFD_Train/dataset'+str(_)
        if not os.path.isdir(folderpath):
            os.mkdir(folderpath)
            images = folderpath+'/images'
            labels = folderpath+'/labels'
            if not os.path.isdir(images):
                os.mkdir(images)
            if not os.path.isdir(labels):
                os.mkdir(labels)
            savepath = images
            cpfile(_,cls0,cls1_2,labels)
            checkcontent(labels)
            cpimages(imgapthfile,savepath,labels)
    art.complete()
    art.mario()


