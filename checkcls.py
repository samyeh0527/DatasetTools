#HC
#checkcls
import os
from collections import Counter
from tqdm import tqdm
import gc
gc.enable()



def cpfile():
    cls3=[]
    for file in labelspath:
        
        content=[]
        new_pathfile = floderpath+'/'+file
        with open(new_pathfile,'r+') as f:
            line = f.readlines()
            newline = str(line)
            replacecharacter=["'",'[',']']
            for _ in replacecharacter:
                newline = newline.replace(_,'')
            newline = newline.split(',')

            #跑檔案裡面每行
            for _ in range(0,len(newline)):
                # print(newline[_],'\n')
                cls = str(newline[_])[0]
                if cls =='3'  or str(newline[_])[1] =='3':
                    #存檔名 
                    cls3.append(new_pathfile) 
                    reduce_repeat = dict(Counter(cls3))
                    cls3 = [key for key,value in reduce_repeat.items() if value >= 1 ]
                    #存內容
                    content.append(newline)
        
        #不要的類別txt檔
        if  not cls3:
            continue
        else:
            print(f'The  txt path is { cls3 } there are unneeded cls => { didnt_need_cls } replace to {need_cls}')
            _ = cls3.pop()
            with open(_,'w+') as f:
            #讀內容
                replacecharacter=['\\n',"'",'[',']','\\']
                for ch in replacecharacter:
                    content[0] = str(content[0]).replace(ch,'')
                    # content[contentline] = str(content[contentline])+'\n'
                content = content[0].split(',')
                if content[-1] == '  ' :
                    content = content[:-1]
                for contentline in range(len(content)):
                    
                    if str(content[contentline])[0] == ' ':
                        content[contentline] = str(content[contentline])[2:]
                    if content[contentline][0] == didnt_need_cls:
                        tmp = content[contentline] 
                        content[contentline]  = sub(str(tmp),0,need_cls)
                        content[contentline] = str(content[contentline] )+'\n'
                        f.write(content[contentline])
                    else:
                        content[contentline] = str(content[contentline] )+'\n'
                        f.write(content[contentline])


def sub(string,p,c):
        new = []
        for s in string:
            new.append(s)
        new[p] = str(c)
        return "".join(new)
                

if __name__ == '__main__':
    floderpath =r'./labels'
    labelspath = os.listdir(floderpath)
    didnt_need_cls ='3'
    need_cls='2'    
    cpfile()
    print('Complete!')