from pip import main as I
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *


def install():     
    print('================AM PIP FOR ALL ====================')
    x=module_name.get()
    I(['install' ,x])
    showinfo("SUCCESSFUL","Installation successful")



"""
____________________________________________________________
Oi tuklu ekta GUI design kor niche ar Tate button er command 
Ta oi install function ta call koris thhik achhe 
Hello oi............
Ar eita hobe ekta GUI pip installer chol suru 
Kor kaj joldi plsss 
🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏🙏
____________________________________________________________
"""
root=Tk()
root.title('GUI PIP')
root.geometry("700x700")
module_name = Entry(root,font=('verdana',24))
module_name.pack(side=TOP, padx=10)
btn=Button(root, font=('verdana',24) , text='Install', command=install)
btn.pack(side=TOP, pady=10)

root.mainloop()










