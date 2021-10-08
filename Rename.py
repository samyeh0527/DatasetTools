#RenameImages
from genericpath import exists
import os 
from ascllart import art
class Rename():
    def renameImage(self,path,new_name,itemtype,path2=None):
        basenameFileList=[]
        basenameFileList2=[]
        type1,type2=None,None
        
        FileList = os.listdir(path)
       
        for fileimg in FileList:
            fileimg = fileimg.split(".")
            type1 = fileimg[1]
            fileimg = fileimg[0]
            basenameFileList.append(fileimg)
        number = 0
        if path2 != None :
            FileList2 = os.listdir(path2)
            for fileimg2 in FileList2:
                fileimg2 = fileimg2.split(".")
                type2 = fileimg2[1]
                fileimg2 = fileimg2[0]
                basenameFileList2.append(fileimg2)
            print('OK')
            existsFile = set(basenameFileList)&set(basenameFileList2)
            for _ in existsFile:
                    number+=1
                    print(path+'/'+_+'.'+type1, path+'/'+new_name+str(number)+'.'+type1)
                    print(path2+'/'+_+'.'+type2, path2+'/'+new_name+str(number)+'.'+type2)

                    os.rename( path+'/'+_+'.'+type1, path+'/'+new_name+str(number)+'.'+type1)
                    os.rename( path2+'/'+_+'.'+type2, path2+'/'+new_name+str(number)+'.'+type2)    
        else :
            for _ in FileList:
                number+=1
                os.rename( path+'/'+_, path+'/'+new_name+str(number)+itemtype)
                
            
        NewNameFileList = os.listdir(path)
        if path2 != None:
            NewNameFileList2= os.listdir(path2)
            NewNameFileList.extend(NewNameFileList2)
        return NewNameFileList
    def renameChr(self,name):
        Chr=['(',')']
        for i in range(len(Chr)):
            new_name = str(name).replace(Chr[i],'')
        return new_name


if __name__ == '__main__':
    #Testing fuction it's work 
    art().hisnchun
    # path = r'D:\DatasetBenchmark\DatasetTools\text\ProfileMask2\A'
    # # # path2 = r'D:\DatasetBenchmark\DatasetTools\text\ProfileMask2\B'
    # _rename_='C'
    # Selectitem = '.jpg'
    # Rename().renameImage(path,_rename_,Selectitem)