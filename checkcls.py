#HC
#checkcls
import os
from collections import Counter
from tqdm import tqdm
import gc
from ascllart import art
gc.enable()
class check():
    def checkcls(self, floderpath , didnt_need_cls , need_cls):
        cls3=[]
        labelspath = os.listdir(floderpath)
        print(labelspath)
        for file in tqdm(labelspath):
            content=[]
            new_pathfile = floderpath+'/'+file
            with open(new_pathfile,'r+') as f:
                line = f.readlines()
                newline = str(line)
                replacecharacter=["'",'[',']']
                for _ in replacecharacter:
                    newline = newline.replace(_,'')
                newline = newline.split(',')
                #Run each line in the file
                for _ in range(0,len(newline)):
                    # print(newline[_],'\n')
                    cls = str(newline[_])[0]
                    if cls ==didnt_need_cls  or str(newline[_])[1] ==didnt_need_cls:
                        #save file name
                        cls3.append(new_pathfile) 
                        #sace content
                        content.append(newline)
                #Check again that there will be duplicate file names inside cls3
                reduce_repeat = dict(Counter(cls3))
                cls3 = [key for key,value in reduce_repeat.items() if value >= 1 ]
            #Unwanted category txt file
            if not cls3:
                continue
            else:
                # print(f'The  txt path is { cls3 } ')
                _ = cls3.pop()
                with open(_,'w+') as f:
                #read content
                    replacecharacter=['\\n',"'",'[',']','\\']
                    for ch in replacecharacter:
                        content[0] = str(content[0]).replace(ch,'') 
                    content = content[0].split(',')
                    if content[-1] == '  ' :
                        content = content[:-1]
                    for contentline in range(len(content)):
                        if str(content[contentline])[0] == ' ':
                            content[contentline] = str(content[contentline])[2:]
                        if content[contentline][0] == didnt_need_cls:
                            tmp = content[contentline] 
                            content[contentline]  = self.sub(str(tmp),0,need_cls)
                            content[contentline] = str(content[contentline] )+'\n'
                            f.write(content[contentline])
                        else:
                            content[contentline] = str(content[contentline] )+'\n'
                            f.write(content[contentline])


    def sub(self,string,p,c):
            new = []
            for s in string:
                new.append(s)
            new[p] = str(c)
            return "".join(new)
                    

if __name__ == '__main__':
    art.hisnchun()
    floderpath =r'D:\DatasetBenchmark\DatasetTools\text'
    
    didnt_need_cls ='2'
    need_cls='3'    
    check().checkcls(floderpath,didnt_need_cls,need_cls)
    art.complete()
