from os import path
from tkinter import *
from tkinter.filedialog import askdirectory
class selectPath():
    def __init__(self) :
        root = Tk()
        path = StringVar()
        Label(root,text='path: ').grid(row =0 ,column =0 )
        Entry(root,textvariable = path ).grid(row =0 ,column =1 )
        Button(root,text= 'select_path',command=selectPath).grid(row =0 ,column =2 )

    def selectPath(self):
        path_ =askdirectory()
        path.set(path_)
        print(path_)

if __name__ == "__main__":
    selectPath.root.mainloop()