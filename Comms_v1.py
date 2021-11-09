from os import set_inheritable
from tkinter import *
import tkinter as tk
from tkinter import ttk
import datetime
from tkinter import font

win =Tk() #建立主視窗

win.title("Comms Draft") #視窗標題

win.geometry("500x500+800+400") #視窗大小,寬X高, 出現在銀幕的位置
win.resizable(0,0) #固定大小,不能縮放

win.iconbitmap("microgaming-logo.ico") #視窗icon,只支援副檔名.ico

win.config(background="#f1f1f1") #顏名or 16進制 000000

win.attributes("-alpha",0.9) #透明度1~0, 1=不透明

win.attributes("-topmost", 1) #置頂 
#=====================================================================
#Function
# en=tk.Entry() #輸入窗的物件
# en.pack()


# Image
# img=tk.PhotoImage(file="microgaming-logo.png")



# # 按鈕 btn=button
# btn=tk.Button(text="GET URL",command=GETURL)
# #btn.config(bg="skyblue")
# #btn.config(width=10, height=5)
# btn.config(image=img) #按鈕改成上面圖檔
# #btn.config(command=GETURL)
# btn.config(bg="#000000")
# btn.config(fg="red")
# btn.pack()

# gn=tk.Entry() #輸入窗的物件
# gn.pack()


# #Lable物件 
# lb=tk.Label(bg="#000000",fg="red",text="you have selected") #lb=lable
# #lb.config(bg="#000000")
# #lb.config(fg="red")
# #lb.config(text="change") 可以這樣改text裡面的值
# #lb.config(font="微軟正黑體 15") #輸入字體名稱 數字等於大小
# lb.pack()
# lb1=tk.Label(bg="#000000",fg="red",text="") #lb=lable
# #lb.config(bg="#000000")
# #lb.config(fg="red")
# #lb.confgi(text="change") 可以這樣改text裡面的值
# lb1.pack()

# chkvalue =tk.StringVar()
# chkvalue.set(False)#預設勾選or不勾選

#時間日期
def uptime():
    global TimeLabel
    TimeLabel.config(text= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    win.after(200,uptime)

textweight=font.Font(weight=font.BOLD)
TimeLabel = Label(text = "%s" %(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),),fg='red',font=textweight)
TimeLabel.place(x=340,y=20)
win.after(100,uptime)



def copy_value ():
    win.clipboard_append(msglabel.get())

# Status
stala=Label(win,text='Status:').place(x=0,y=0)
sraval=StringVar()
sraval.set('New') #預選值為New的選項
srabtn0=Radiobutton(win, text='New',variable=sraval,value='New').place(x=50,y=0)
srabtn1=Radiobutton(win, text='Resolved',variable=sraval,value='Resolved').place(x=100,y=0)
srabtn2=Radiobutton(win, text='On Hold',variable=sraval,value='On Hold').place(x=180,y=0)
srabtn3=Radiobutton(win, text='Re-occurring',variable=sraval,value='Re-occurring').place(x=260,y=0)

# Severity
sevl=Label(win,text='Severity:').place(x=0,y=20)
sevrad=StringVar()
sevrad.set('A')
sev_A=Radiobutton(win, text='A',variable=sevrad,value='A').place(x=50,y=20)
sev_B=Radiobutton(win, text='B',variable=sevrad,value='B').place(x=90,y=20)

# Systems
checkvalue=StringVar()
# for 迴圈寫法 https://www.dotblogs.com.tw/YiruAtStudio/2021/02/22/193206; https://selflearningsuccess.com/python-for-loop/
def ch_sys():
    global HO,sysall
    showmsg = "Affecting System: "
    for i in range(0,len(HO)):
        if(HO[i].get()==True):#勾選時
            showmsg=showmsg+chva[i]+", "
    
    msglabel.set(showmsg)

HO=[]
sysall=['TEG0','TEG1','TEG2','TEG3','TEG4','TEG5','TEG6','TEG7','TEG8','Sem','B2C','QF2','LD',]
chva=['TEG0','TEG1','TEG2','TEG3','TEG4','TEG5','TEG6','TEG7','TEG8','Sempris','TNGQuickfire','QF2','Live Dealer']
msglabel = StringVar()

mylabel = Label(win,text="Choice Affected System:").place(x=150,y=20)

for i in range(0,7):
    num=IntVar()
    # print(num)
    HO.append(num)
    mychkbtn=Checkbutton(win,text=sysall[i],variable=HO[i],command=ch_sys,onvalue=1,offvalue=0).place(x=(i*60),y=40)
j=0
k=0
for i in range(7,13):
    num=IntVar()
    # print(num)
    HO.append(num)
    mychkbtn=Checkbutton(win,text=sysall[i],variable=HO[i],command=ch_sys,onvalue=1,offvalue=0).place(x=(j*60),y=60)
    j+=1


w1=win.winfo_width()
h1=win.winfo_height()
# print(str(w1)) 結果為500
mylabel=Label(win,textvariable=msglabel).place(x=w1/2-100,y=100)

# Comms_Manager
Comms_lab=Label(win,text='Comms Manager:').place(x=0,y=400)
comms_variable=StringVar()
comms_manager=ttk.Combobox(win,textvariable=comms_variable,values=(\
    'Pick one',\
    'Abri Liebenberg (+61 4 3282 3087)',\
    'Bartosz Lewandowski (+886 978 705 232)',\
    'Jeff Huang (+886 933 308 768)',\
    'Jill Shen (+886 903 438 345)',\
    'Matt Cheng (+886 932 075 280)',\
    'Matthew Geoghegan (+886 905 249 541)')).place(x=100,y=400)
comms_variable.set('Pick one')

# ITOC member
Comms_lab=Label(win,text='Escalated by:').place(x=0,y=420)
ITOC_variable=StringVar()
ITOC_manager=ttk.Combobox(win,textvariable=ITOC_variable,values=(\
    'Who are you?',\
    'Acise Lee',\
    'Christopher Lia',\
    'Da Wu',\
    'Jackie Xu',\
    'Jiajin Kang',\
    'Jin Yang',\
    'Joy Huang',\
    'Ray Duan')).place(x=100,y=420)
ITOC_variable.set('Who are you?')





#TEXT物件
# mes=tk.Text(win, width=50, height=3)
# mes.insert("insert", "未選擇")
# mes.pack()
def copy_comms ():
    all_sen= \
        "Status: "+ sraval.get() + \
        "\nSeverity: "+ sevrad.get() + \
        "\nName: "+"\n"+ str(msglabel.get()) + \
        "\nTier: Tier_1" + \
        "\nOperator: Power_Asia, FCM88, TOP_USD2, Asia888, Poseidon, TH1GAMES, TOP_USD(GAMA), MaxPro, Metaltex" + \
        "\nTime Elapsed: 10 mins " + \
        "\nStart Time: " + datetime.datetime.now().strftime('%Y-%m-%d') + " (GMT+8)"\
        "\nEnd Time: " + \
        "\nService Degradation: 25% " + \
        "\nSymptoms: GPM degradation on TEG0 " + \
        "\nAction Taken: ITOC is checking with client. " + \
        "\nRoot Cause: "+ \
        "\nComms Manager: " + comms_variable.get() + \
        "\nCrisis Manager: " + comms_variable.get() +  \
        "\nEscalated by: "+ ITOC_variable.get() + "(+886 226 560 700 ext 207) "+ \
        "\n" + \
        "\nClik ID: INC-A37436 "+ \
        "\nCustomer Ref#: "+ \
        "\n" + \
        "\nJoin Microsoft Teams Chat: "
        

    win.clipboard_append (all_sen) # This is the process of copying to the clipboard

def clear_All(): #https://stackoom.com/question/3mvSR https://stackoverflow.com/questions/37171478/how-to-deselect-checkboxes-using-a-button-in-python
    i=0
    for i in range(0,len(HO)):
        HO[i].set(0)
    
    sraval.set('New')
    sevrad.set('A')
    comms_variable.set('Pick one')


# 放置參考https://pythonhi.pixnet.net/blog/post/322521486; http://yhhuang1966.blogspot.com/2018/10/python-gui-tkinter_12.html
copybtn = Button ( win, text = "Copy" , padx = 50 , pady = 5 , command = copy_comms ) . pack ( side = 'left' , padx = 50 , anchor= S )
clearbtn = Button ( win, text = "Clear" , padx = 50 , pady = 5 ,command = clear_All ) . pack ( side = 'right' , padx = 50 , anchor= S)

win.mainloop() #常駐主視窗,不然執行後會關閉視窗
