import datetime
import tkinter as tk
from tkinter import messagebox
from os import set_inheritable
from tkinter import *
from tkinter import font, ttk

from numpy.testing._private.utils import print_assert_equal

# from numpy.lib.function_base import place
# from numpy.testing._private.utils import print_assert_equal

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


#字型 控制 https://www.delftstack.com/zh-tw/howto/python-tkinter/how-to-change-the-tkinter-label-font-size/
text_weight=font.Font(weight=font.BOLD) # 粗體
text_size10=font.Font(size=10,weight=font.BOLD) #字體大小&粗體
text_size8=font.Font(size=8,weight=font.BOLD) #字體大小&粗體

#時間日期 https://www.codeprj.com/zh/blog/b7ac791.html
def uptime():
    global TimeLabel
    TimeLabel.config(text= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    win.after(200,uptime)


TimeLabel = Label(text = "%s" %(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),),fg='red',font=text_weight)
TimeLabel.place(x=340,y=20)
win.after(100,uptime)


def copy_value ():
    win.clipboard_append(msglabel.get())

# Status
status_lab=Label(win,text='Status:').place(x=0,y=0)
status_variable=StringVar()
status_variable.set('New') #預選值為New的選項
srabtn0=Radiobutton(win, text='New',variable=status_variable,value='New').place(x=50,y=0)
srabtn1=Radiobutton(win, text='Resolved',variable=status_variable,value='Resolved').place(x=100,y=0)
srabtn2=Radiobutton(win, text='On Hold',variable=status_variable,value='On Hold').place(x=180,y=0)
srabtn3=Radiobutton(win, text='Re-occurring',variable=status_variable,value='Re-occurring').place(x=260,y=0)

# Severity
sevl=Label(win,text='Severity:').place(x=0,y=20)
sev_variable=StringVar()
sev_variable.set('A')
sev_A=Radiobutton(win, text='A',variable=sev_variable,value='A').place(x=50,y=20)
sev_B=Radiobutton(win, text='B',variable=sev_variable,value='B').place(x=90,y=20)

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
sysall=['TEG0','TEG1','TEG2','TEG3','TEG4','TEG6','Sem','B2C','QF2','LD',]
chva=['TEG0','TEG1','TEG2','TEG3','TEG4','TEG6','Sempris','TNGQuickfire','QF2','Live Dealer']
msglabel = StringVar()

mylabel = Label(win,text="Choice Affected System:").place(x=150,y=20)

for i in range(0,6):
    num=IntVar()
    # print(num)
    HO.append(num)
    mychkbtn=Checkbutton(win,text=sysall[i],variable=HO[i],command=ch_sys,onvalue=1,offvalue=0).place(x=(i*60),y=40)
j=0

for i in range(6,10):
    num=IntVar()
    # print(num)
    HO.append(num)
    mychkbtn=Checkbutton(win,text=sysall[i],variable=HO[i],command=ch_sys,onvalue=1,offvalue=0).place(x=(j*60),y=60)
    j+=1
k=80


for k in range(80,340,20):
    ll0=Label(win,text='x=0, y='+ str(k)).place(x=0,y=k)
    k = k + 20
    

w1=win.winfo_width()
h1=win.winfo_height()
# print(str(w1)) 結果為500
mylabel=Label(win,textvariable=msglabel).place(x=w1/2-100,y=100)


#Root cause
cause_label=Label(win,font=text_size8,text='Root Cause:').place(x=0,y=320)
cause_varable=StringVar()
cause_list=ttk.Combobox(win,state='readonly',textvariable=cause_varable,values=(\
    'Unknown',\
    'Operator',\
    'Regular Maintenance',\
    'Infra',\
    'Network',\
    'Internal',\
    'Internal - 3rd Party',\
    'Internal - MG+',\
    'TBC',\
    'Drill')).place(x=105,y=320)
cause_varable.set('Unknown')

# Comms_Manager
Comms_lab=Label(win,font=text_size8,text='Comms Manager:').place(x=0,y=340)
comms_variable=StringVar()
comms_manager=ttk.Combobox(win,state='readonly',textvariable=comms_variable,values=(\
    'Pick one',\
    'Abri Liebenberg (+61 4 3282 3087)',\
    'Bartosz Lewandowski (+886 978 705 232)',\
    'Jeff Huang (+886 933 308 768)',\
    'Jill Shen (+886 903 438 345)',\
    'Matt Cheng (+886 932 075 280)',\
    'Matthew Geoghegan (+886 905 249 541)')).place(x=105,y=340)
comms_variable.set('Pick one')


        
# Crisis_Manager
crisis_lab=Label(win,font=text_size8,text='Crisis Manager: ').place(x=0,y=360)
crisis_variable=StringVar()
# crisis_lab2=Label(win,font=text_size8,textvariable=comms_variable).place(x=245,y=360)
crisis_entry=Entry(win,font=text_size8,textvariable=crisis_variable).place(x=105,y=360)
crisis_variable.set('Null or Fill in')

# ITOC member
ITOC_lab=Label(win,font=text_size10,text='Escalated by:').place(x=0,y=380)
ITOC_variable=StringVar()
ITOC_manager=ttk.Combobox(win,textvariable=ITOC_variable,values=(\
    'Acise Lee',\
    'Christopher Lia',\
    'Da Wu',\
    'Jackie Xu',\
    'Jiajin Kang',\
    'Jin Yang',\
    'Joy Huang',\
    'Ray Duan')).place(x=105,y=380)
ITOC_variable.set('Pick or Input')

# clik Number
# 輸入字母強制轉大寫 https://www.codenong.com/44105484/
def to_uppercase(*args):
    clik_variable.set(clik_variable.get().upper())
clik_variable=StringVar()
clik_lab=Label(win,font=text_size10,text='Clik ID:').place(x=0,y=400)
# 輸入框 https://jennaweng0621.pixnet.net/blog/post/403560362-%5Bpython%5D-tkinter-%E6%96%87%E5%AD%97%E6%A1%86%28entry%29
clik_entry=Entry(win,textvariable=clik_variable).place(x=105,y=400)
clik_variable.trace_add('write', to_uppercase)


# SUPL Number
def to_uppercase(*args):
    ref_variable.set(ref_variable.get().upper())
ref_variable=StringVar()
ref_lab=Label(win,font=text_size10,text='Ref#').place(x=0,y=420)
ref_entry=Entry(win,textvariable=ref_variable).place(x=105,y=420)
ref_variable.trace_add('write', to_uppercase)

# Teams URL
teams_variable=StringVar()
teams_lab=Label(win,font=text_size10,text='Teams Chat: ').place(x=0,y=440)
teams_entry=Entry(win,textvariable=teams_variable).place(x=105,y=440)

#TEXT物件
# mes=tk.Text(win, width=50, height=3)
# mes.insert("insert", "未選擇")
# mes.pack()
def copy_comms ():
    win.clipboard_clear()
    if comms_variable.get() == 'Pick one':
        messagebox.showerror('Pick one please!','Choice a Manager')

    if crisis_variable.get() == 'Null or Fill in':
        crisis_variable_X=comms_variable.get()
        crisis_variable.set(crisis_variable_X)
        

    if ITOC_variable.get() == 'Pick or Input':
        messagebox.showerror('Hey! ITOC','Who you are?')

    

    all_sen= \
        "Status: "+ status_variable.get() + \
        "\nSeverity: "+ sev_variable.get() + \
        "\nName: "+"\n"+ msglabel.get() + \
        "\nTier: Tier_1" + \
        "\nOperator: Power_Asia, FCM88, TOP_USD2, Asia888, Poseidon, TH1GAMES, TOP_USD(GAMA), MaxPro, Metaltex" + \
        "\nTime Elapsed: 10 mins " + \
        "\nStart Time: " + datetime.datetime.now().strftime('%Y-%m-%d') + " (GMT+8)"\
        "\nEnd Time: " + \
        "\nService Degradation: 25% " + \
        "\nSymptoms: GPM degradation on TEG0 " + \
        "\nAction Taken: ITOC is checking with client. " + \
        "\nRoot Cause: "+ cause_varable.get() + \
        "\nComms Manager: " + comms_variable.get() + \
        "\nCrisis Manager: " + crisis_variable.get() +  \
        "\nEscalated by: "+ ITOC_variable.get() + " (+886 226 560 700 ext 207) "+ \
        "\n" + \
        "\nClik ID: "+ clik_variable.get() + \
        "\nCustomer Ref#: " + ref_variable.get() + \
        "\n" + \
        "\nJoin Microsoft Teams Chat: " + teams_variable.get()
    win.clipboard_append (all_sen) # This is the process of copying to the clipboard

def clear_All(): #https://stackoom.com/question/3mvSR https://stackoverflow.com/questions/37171478/how-to-deselect-checkboxes-using-a-button-in-python
    i=0
    for i in range(0,len(HO)):
        HO[i].set(0)
    
    status_variable.set('New')
    sev_variable.set('A')
    cause_varable.set('Unknown')
    comms_variable.set('Pick one')
    crisis_variable.set('Null or Fill in')
    clik_variable.set('')
    ref_variable.set('')
    teams_variable.set('')
    win.quit


# 放置參考https://pythonhi.pixnet.net/blog/post/322521486; http://yhhuang1966.blogspot.com/2018/10/python-gui-tkinter_12.html
copybtn = Button ( win, text = "Copy" , padx = 50 , pady = 5 , command = copy_comms ) . pack ( side = 'left' , padx = 50 , anchor= S )
clearbtn = Button ( win, text = "Clear" , padx = 50 , pady = 5 ,command = clear_All ) . pack ( side = 'right' , padx = 50 , anchor= S)

win.mainloop() #常駐主視窗,不然執行後會關閉視窗
