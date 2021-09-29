#RenameImages
import os 
from ascllart import art
class Rename():
    def renameImage(self,Image_path,new_name,itemtype):
        AllFileList = os.listdir(Image_path)
        number = 0
        
        for _ in AllFileList:
            number+=1
            os.rename( Image_path+'/'+_, Image_path+'/'+new_name+str(number)+itemtype) 
            pass
        NewNameFileList = os.listdir(Image_path)
        return NewNameFileList
    def renameChr(self,name):
        Chr=['(',')']
        for i in range(len(Chr)):
            new_name = str(name).replace(Chr[i],'')
        return new_name


if __name__ == '__main__':
    art().hisnchun
    image_path = r'./Profile2'
    newname='profile'
    Rename().renameImage(image_path,newname)