import re
import calendar
import datetime
from posixpath import split
import tkinter as tk
from tkinter import messagebox
from os import read, set_inheritable
from tkinter import *
from tkinter import font, ttk


# from numpy.lib.function_base import place
# from numpy.testing._private.utils import print_assert_equal

win = Tk()  # 建立主視窗

win.title("Comms Draft")  # 視窗標題

win.geometry("500x500+800+400")  # 視窗大小,寬X高, 出現在銀幕的位置
win.resizable(0, 0)  # 固定大小,不能縮放

# win.iconbitmap("microgaming-logo.ico") #視窗icon,只支援副檔名.ico

win.config(background="#f1f1f1")  # 顏名or 16進制 #000000

win.attributes("-alpha", 1)  # 透明度1~0, 1=不透明

win.attributes("-topmost", 1)  # 置頂
# =====================================================================
# Function
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


# 字型 控制 https://www.delftstack.com/zh-tw/howto/python-tkinter/how-to-change-the-tkinter-label-font-size/
text_B = font.Font(family='Arial',weight=font.BOLD)  # 粗體
size10_B = font.Font(family='Arial',size=10, weight=font.BOLD)  # 字體大小&粗體
size8 = font.Font(family='Arial',size=8)
size8_B = font.Font(family='Arial',size=8, weight=font.BOLD)  # 字體大小&粗體
size10 = font.Font(family='Arial',size=10)
size12 = font.Font(family='Arial',size=12,weight=font.BOLD)

# 時間日期 https://www.codeprj.com/zh/blog/b7ac791.html
def uptime():
    global TimeLabel
    TimeLabel.config(font=size10_B, text=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    win.after(200, uptime)


TimeLabel = Label(text="%s" % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),), fg='red', font=text_B)
TimeLabel.place(x=200, y=20)
win.after(100, uptime)

# https://zhuanlan.zhihu.com/p/95919866
ima=datetime.datetime.now()
start_ima=datetime.datetime(ima.year, ima.month,1) # 每月第一天
end_ima=datetime.datetime(ima.year, ima.month, calendar.monthrange(ima.year, ima.month)[1]) # 每月最後一天
# print(start_ima.day,end_ima.day)
dd = datetime.timedelta(days=1, seconds=0)
hh = datetime.timedelta(hours=1, seconds=0)
mm = datetime.timedelta(minutes=1, seconds=0)
next_ima = end_ima+dd  # 下個月第一天
next_day = ima+(dd*7)

def copy_value():
    win.clipboard_append(msglabel.get())


# Status
status_lab = Label(win, font=size8_B, text='Status:').place(x=0, y=0)
status_variable = StringVar()
status_variable.set('New')  # 預選值為New的選項
srabtn0 = Radiobutton(win, text='New', variable=status_variable, value='New').place(x=50, y=0)
srabtn1 = Radiobutton(win, text='Resolved', variable=status_variable, value='Resolved').place(x=100, y=0)
srabtn2 = Radiobutton(win, text='On Hold', variable=status_variable, value='On Hold').place(x=180, y=0)
srabtn3 = Radiobutton(win, text='Re-occurring', variable=status_variable, value='Re-occurring').place(x=260, y=0)
srabtn4 = Radiobutton(win, text='New/Resolved', variable=status_variable, value='New / Resolved').place(x=360, y=0)


# Severity
sevl = Label(win, font=size8_B, text='Severity:').place(x=0, y=20)
sev_variable = StringVar()
sev_variable.set('A')
sev_A = Radiobutton(win, text='A', variable=sev_variable, value='A').place(x=50, y=20)
sev_B = Radiobutton(win, text='B', variable=sev_variable, value='B').place(x=90, y=20)

# Systems
# 用for迴圈的寫法 https://www.dotblogs.com.tw/YiruAtStudio/2021/02/22/193206; https://selflearningsuccess.com/python-for-loop/
def ch_sys():
    global HO, sysall
    showmsg = ""
    for i in range(0, len(HO)):
        if(HO[i].get() == True):  # 勾選時
            showmsg = showmsg+chva[i]+", "
    msglabel.set(showmsg)


HO = []
sysall = ['TEG0', 'TEG1', 'TEG2', 'TEG3', 'TEG4', 'TEG6', 'Sem', 'B2C', 'QF2', 'LD' ,'MGP SW']
chva = ['TEG0', 'TEG1', 'TEG2', 'TEG3', 'TEG4', 'TEG6', 'Sempris', 'TNGQuickfire', 'QF2', 'Live Dealer', 'MGPSW']
msglabel = StringVar()
for i in range(0, 6):
    num = IntVar()
    # print(num)
    HO.append(num)
    mychkbtn = Checkbutton(win, text=sysall[i], variable=HO[i],command=ch_sys, onvalue=1, offvalue=0).place(x=140+(i*60), y=40)

j = 0
for i in range(6, 11):
    num = IntVar()
    # print(num)
    HO.append(num)
    mychkbtn = Checkbutton(win, text=sysall[i], variable=HO[i],command=ch_sys, onvalue=1, offvalue=0).place(x=140+(j*60), y=60)
    j += 1


# k = 80
# for k in range(80, 340, 20):
#     ll0 = Label(win, text='x=0, y=' + str(k)).place(x=0, y=k)
#     k = k + 20


w1 = win.winfo_width()
h1 = win.winfo_height()
# print(str(w1)) 結果為500

Sys_label0 = Label(win, font=size8_B, text="Affected System:").place(x=0, y=40)
# Sys_label1 = Label(win, textvariable=msglabel, text="Choice Affected System:").place(x=w1/2-100, y=100)

# Name

# Tier
tier_lab=Label(win, font=size8_B, text='Tier:').place(x=0, y=120)
tier_variable = StringVar()
tier_variable.set('Tier_1')
tier1_rad=Radiobutton(win, text='Tier_1', variable=tier_variable, value='Tier_1').place(x=105, y=120)
tier2_rad=Radiobutton(win, text='Tier_2', variable=tier_variable, value='Tier_2').place(x=170, y=120)

# Operator 缺HO
operator_variable = StringVar()
operator_lab = Label(win, font=size8_B, text="Operator:").place(x=0, y=140)
operator_lab = Label(win, font=size8_B, textvariable=msglabel).place(x=0, y=160)





# Time Elapsed/ Start Time/ End Time/ Service Degradation /Symptoms
ti = []
title_all = ['Time Elapsed:', 'Start Time:',
             'End Time:', 'Service Degradation:', 'Symptoms:']
ti_lab = StringVar()
xx = 0
for h in range(180, 280, 20):
    tii = Label(win, font=size8_B, text=title_all[xx]).place(x=0, y=h)
    h = h + 20
    xx += 1



#只能輸入數字 https://shengyu7697.github.io/python-tkinter-entry-number-only/
def validate(P):
    # print(P)
    if str.isdigit(P):
        return True
    else:
        return False
vcmd = (win.register(validate), '%P')


dds = []  # 01-31 days
if ima.month == next_day.month:  # 今天月等於明天月
    print('等於')
    for ds in range(ima.day, int(end_ima.day)+1, 1):
        dds.append(ds)
        ds += 1
elif ima.month != next_day.month:  # 今天月不等於明天月
    print('不等於')
    for ds in range(ima.day, int(end_ima.day)+1, 1):
        dds.append(ds)
        ds += 1
    for ds in range(next_ima.day, int(next_day.day)+1, 1):
        dn = ds
        dds.append(dn)
        ds += 1

mms=[] # 00-59 mins
for ms in range(0,60,1):
    mms.append(ms)
    ms+=1
    # print(mms)

hhs=[] # 00-24 hrs
for hs in range(00,24,1):
    hhs.append(hs)
    hs+=1
    # print(hhs)

# # Start Time 缺計算時間
sTed = IntVar()
sTeh = IntVar()
sTem = IntVar()
start_lab = Label(win, font=size12, text=':').place(x=190, y=195)
GMT_lab = Label(win, font=size10, text='GMT+8').place(x=243, y=200)
start_Time_entry0=ttk.Combobox(win, values=dds,width=3,textvariable=sTed).place(x=105, y=200)
start_Time_entry1=ttk.Combobox(win, values=hhs,width=3,textvariable=sTeh).place(x=150, y=200)
start_Time_entry2=ttk.Combobox(win, values=mms,width=3,textvariable=sTem).place(x=203, y=200)

sTed.set(ima.day)
sTeh.set(ima.hour)
sTem.set(ima.minute)


# # End Time 缺計算時間
eTed = IntVar()
eTeh = IntVar()
eTem = IntVar()
end_lab = Label(win, font=size12, text=':').place(x=190, y=215)
GMT_lab = Label(win, font=size10, text='GMT+8').place(x=243, y=220)
# end_Time_entry0 = Entry(win, font=size10, textvariable=eTed, width=3, validate='key', validatecommand=vcmd).place(x=105, y=220)
# end_Time_entry1 = Entry(win, font=size10, textvariable=eTeh, width=3, validate='key', validatecommand=vcmd).place(x=135, y=220)
# end_Time_entry2 = Entry(win, font=size10, textvariable=eTem, width=3, validate='key', validatecommand=vcmd).place(x=175, y=220)
end_Time_entry0=ttk.Combobox(win, values=dds,width=3,textvariable=eTed).place(x=105, y=220)
end_Time_entry1=ttk.Combobox(win, values=hhs,width=3,textvariable=eTeh).place(x=150, y=220)
end_Time_entry2=ttk.Combobox(win, values=mms,width=3,textvariable=eTem).place(x=203, y=220)
eTed.set(ima.day)
eTeh.set(ima.hour)
eTem.set(ima.minute)


before_split = StringVar()
elapsed_variable = StringVar()

# 時間格式參考https://blog.jaycetyle.com/2018/01/python-format-string/

def elapsed():
    global elapsed_lab
    elapsed_lab.config(text= '%s' % elapsed_variable.get())
    dd=datetime.timedelta(days=1)
    hh=datetime.timedelta(hours=1)
    mm=datetime.timedelta(minutes=1)

    # -------------------------------------------------------------------------------------- 時間運算OK 
    # Time_format
    format_ima = ima.strftime('%Y-%m-%d %H:%M') # 轉換為指定日期格式字串格式
    # print(format_ima)
    format_start_ima = ima.strftime('%Y-%m-' + '%d %d:%d'%(int(sTed.get()),int(sTeh.get()),int(sTem.get())))
    format_end_ima = ima.strftime('%Y-%m-' + '%d %d:%d'%(int(eTed.get()),int(eTeh.get()),int(eTem.get()))) #取得指定時間,字串格式
    # print(format_end_ima)
    # print(type(format_end_ima)) # str格式

    start_ima=datetime.datetime.strptime(format_start_ima,'%Y-%m-%d %H:%M')
    end_ima=datetime.datetime.strptime(format_end_ima,'%Y-%m-%d %H:%M') # 轉換為時間陣列格式
    # print(str(start_ima)+'      '+str(end_ima))
    # print(type(end_ima)) # 時間陣列格式

    # 時間運算
    final_elapsed_real=(end_ima-start_ima) # 結束減去開始時間
    before_split.set(final_elapsed_real) # 最終結果
    elapsed_split_sec_float=str(before_split.get()).rsplit(':',1) # 切割到數第一個':'(秒跟小數點之後) elapsed_split_float[0]-->日時分, elapsed_split_float[1]-->秒 & 微秒
    elapsed_split_hm=elapsed_split_sec_float[0].split(':',1) # 切割時分, elapsed_final[0]-->日 & 時, elapsed_final[1]-->分
    elapsed_variable.set(elapsed_split_hm[0]+ ':' + elapsed_split_hm[1]) # 設定最後值
    # elapsed_variable.set(elapsed_split_sec_float[0]) # 設定最後值
    # print(elapsed_split_hm[0]+ ':' + elapsed_split_hm[1])
    # --------------------------------------------------------------------------------------
    
    if '-' in str(elapsed_split_hm[0]):
        elapsed_variable.set('Time cannot be negative!')
    else:
        if 'day' not in str(elapsed_split_hm[0]): # 不到一天
            if all(c in "01" for c in str(elapsed_split_hm[0])): # 日時的字串中有0 1
                if int(elapsed_split_hm[0]) < 1: # 日時的字串小於1
                    if int(elapsed_split_hm[1]) <= 1:
                        elapsed_variable.set(str(elapsed_split_hm[1]) + ' min ') # 0天 0小 0-1分
                    elif int(elapsed_split_hm[1]) > 1:
                        elapsed_variable.set(str(elapsed_split_hm[1]) + ' mins ') # 0天 0-1小 > 1分
                elif int(elapsed_split_hm[0]) == 1: # 日時的字串等於1
                    if int(elapsed_split_hm[1]) <= 1:
                        elapsed_variable.set(str(elapsed_split_hm[0]) + ' hr ' + str(elapsed_split_hm[1]) + ' min ') # 0天 0-1小 0-1分
                    elif int(elapsed_split_hm[1]) > 1:
                        elapsed_variable.set(str(elapsed_split_hm[0]) + ' hr ' + str(elapsed_split_hm[1]) + ' mins ') # 0天 0-1小 > 1分
                elif int(elapsed_split_hm[0]) > 1: # 日時的字串大於1
                    if int(elapsed_split_hm[1]) <= 1:
                        elapsed_variable.set(str(elapsed_split_hm[0]) + ' hrs ' + str(elapsed_split_hm[1]) + ' min ') # 0天 0-1小 0-1分
                    elif int(elapsed_split_hm[1]) > 1:
                        elapsed_variable.set(str(elapsed_split_hm[0]) + ' hrs ' + str(elapsed_split_hm[1]) + ' mins ') # 0天 0-1小 > 1分
            elif all(c in "23456789" for c in str(elapsed_split_hm[0])): # 日時的字串中有2-9
                if int(elapsed_split_hm[0]) < 1: # 日時的字串小於1
                    if int(elapsed_split_hm[1]) <= 1:
                        elapsed_variable.set(str(elapsed_split_hm[1]) + ' min ') # 0天 0小 0-1分
                    elif int(elapsed_split_hm[1]) > 1:
                        elapsed_variable.set(str(elapsed_split_hm[1]) + ' mins ') # 0天 0-1小 > 1分
                elif int(elapsed_split_hm[0]) == 1: # 日時的字串等於1
                    if int(elapsed_split_hm[1]) <= 1:
                        elapsed_variable.set(str(elapsed_split_hm[0]) + ' hr ' + str(elapsed_split_hm[1]) + ' min ') # 0天 0-1小 0-1分
                    elif int(elapsed_split_hm[1]) > 1:
                        elapsed_variable.set(str(elapsed_split_hm[0]) + ' hr ' + str(elapsed_split_hm[1]) + ' mins ') # 0天 0-1小 > 1分
                elif int(elapsed_split_hm[0]) > 1: # 日時的字串大於1
                    if int(elapsed_split_hm[1]) <= 1:
                        elapsed_variable.set(str(elapsed_split_hm[0]) + ' hrs ' + str(elapsed_split_hm[1]) + ' min ') # 0天 0-1小 0-1分
                    elif int(elapsed_split_hm[1]) > 1:
                        elapsed_variable.set(str(elapsed_split_hm[0]) + ' hrs ' + str(elapsed_split_hm[1]) + ' mins ') # 0天 0-1小 > 1分
        elif 'day' in str(elapsed_split_hm[0]): # 大於一天
            elapsed_split_dh=elapsed_split_hm[0].split(', ',1) # 分割日時字串中大於一天
            print(elapsed_split_dh[0], '-' ,elapsed_split_dh[1], '-' ,elapsed_split_hm[0], '-' ,elapsed_split_hm[1])
            if all(c in "01" for c in str(elapsed_split_dh[1])): # 時的字串中有0 1
                if int(elapsed_split_dh[1]) < 1: # 時的字串小於1
                    if int(elapsed_split_hm[1]) < 1:
                        elapsed_variable.set(str(elapsed_split_dh[0]) + ' ' + str(elapsed_split_hm[1]) + ' min ') # 1天 0-1小 0-1分
                    elif int(elapsed_split_hm[1]) > 1:
                        elapsed_variable.set(str(elapsed_split_dh[0]) + ' ' + str(elapsed_split_dh[1]) + ' hr ' + str(elapsed_split_hm[1]) + ' mins ') # 0天 0-1小 > 1分
                elif int(elapsed_split_dh[1]) == 1: # 時的字串等於1
                    if int(elapsed_split_hm[1]) < 1:
                        elapsed_variable.set(str(elapsed_split_dh[0]) + ' ' + str(elapsed_split_dh[1]) + ' hr ' + str(elapsed_split_hm[1]) + ' min ') # 1天 0-1小 0-1分
                    elif int(elapsed_split_hm[1]) > 1: 
                        elapsed_variable.set(str(elapsed_split_dh[0]) + ' ' + str(elapsed_split_dh[1]) + ' hr ' + str(elapsed_split_hm[1]) + ' mins ') # 0天 0-1小 > 1分
                elif int(elapsed_split_dh[1]) > 1: # 時的字串大於1
                    if int(elapsed_split_hm[1]) <= 1:
                        elapsed_variable.set(str(elapsed_split_dh[0]) + ' ' + str(elapsed_split_dh[1]) + ' hrs ' + str(elapsed_split_hm[1]) + ' min ') # 1天 0-1小 0-1分
                    elif int(elapsed_split_hm[1]) > 1:
                        elapsed_variable.set(str(elapsed_split_dh[0]) + ' ' + str(elapsed_split_dh[1]) + ' hrs' + str(elapsed_split_hm[1]) + ' mins ') # 0天 0-1小 > 1分
            elif all(c in "23456789" for c in str(elapsed_split_dh[1])): # 時的字串中有2-9
                if int(elapsed_split_dh[1]) < 1:
                    if int(elapsed_split_hm[1]) < 1: # 時的字小於1
                        elapsed_variable.set(str(elapsed_split_dh[0]) + ' ' + str(elapsed_split_hm[1]) + ' min ') # 1天 0-1小 0-1分
                    elif int(elapsed_split_hm[1]) > 1:
                        elapsed_variable.set(str(elapsed_split_dh[0]) + ' ' + str(elapsed_split_dh[1]) + ' hr ' + str(elapsed_split_hm[1]) + ' mins ') # 0天 0-1小 > 1分
                elif int(elapsed_split_dh[1]) == 1: # 時的字串等於1
                    if int(elapsed_split_hm[1]) <= 1:
                        elapsed_variable.set(str(elapsed_split_dh[0]) + ' ' + str(elapsed_split_dh[1]) + ' hr ' + str(elapsed_split_hm[1]) + ' min ') # >1小0-1分
                    elif int(elapsed_split_hm[1]) > 1:
                        elapsed_variable.set(str(elapsed_split_dh[0]) + ' ' + str(elapsed_split_dh[1]) + ' hr ' + str(elapsed_split_hm[1]) + ' mins ') # >1小>1分
                elif int(elapsed_split_dh[1]) > 1: # 時的字串大於1
                    if int(elapsed_split_hm[1]) <= 1:
                        elapsed_variable.set(str(elapsed_split_dh[0]) + ' ' + str(elapsed_split_dh[1]) + ' hrs ' + str(elapsed_split_hm[1]) + ' min ') # >1小0-1分
                    elif int(elapsed_split_hm[1]) > 1:
                        elapsed_variable.set(str(elapsed_split_dh[0]) + ' ' + str(elapsed_split_dh[1]) + ' hrs ' + str(elapsed_split_hm[1]) + ' mins ') # >1小>1分


    # if all(str(elapsed_split_hm[0]) in "01:" for elapsed_split_hm[0] in str(elapsed_split_hm[0])):
    #     print('字串沒有 0: 1:')
    # elif all(str(elapsed_split_hm[0]) in "2" for elapsed_split_hm[0] in str(elapsed_split_hm[0])):
    #     print('字串有 0: 1:')


    win.after(200, elapsed)

# Time Elapsed 缺計算時間

elapsed_lab = Label(win, text='%s' % elapsed_variable.get())
elapsed_lab.place(x=105, y=179)
win.after(100,elapsed)


# Service Degradation
def to_uppercase(*args):
    service_variable.set(service_variable.get().upper())
service_variable = StringVar()
service_lab = Label(win, text=' %').place(x=150, y=241)
service_entry = Entry(win, font=size8_B, textvariable=service_variable, width=4).place(x=125, y=242)
service_variable.set('N/A')
service_variable.trace_add('write', to_uppercase)

# Symptoms
symptoms_variable = StringVar()
symptoms_entry = Entry(win, font=size8_B, width=64).place(x=105, y=260)

# Action Taken 
action_lab = Label(win, font=size8_B, text='Action Taken:').place(x=0, y=280)
action_variable = StringVar()
action_text = Text(win, font=size8_B).place(x=105, y=280, width=390, height=20)
action_list = ttk.Combobox(win, width=50, textvariable=action_variable, values=('ITOC is contacting relevant teams.', 'ITOC is checking with client.', 'Engineers are investigating.')).place(x=105, y=300, height=20)
action_variable.set('How is it now?')

# Root cause
cause_label = Label(win, font=size8_B, text='Root Cause:').place(x=0, y=320)
cause_variable = StringVar()
cause_list = ttk.Combobox(win, state='readonly', textvariable=cause_variable, values=(
    'Unknown',
    'Operator',
    'Regular Maintenance',
    'Infra',
    'Network',
    'Internal',
    'Internal - 3rd Party',
    'Internal - MG+',
    'TBC',
    'Drill')).place(x=105, y=320)
cause_variable.set('Unknown')

# Comms_Manager
Comms_lab = Label(win, font=size8_B,text='Comms Manager:',fg='red').place(x=0, y=340)
comms_variable = StringVar()
comms_manager = ttk.Combobox(win, state='readonly', textvariable=comms_variable, values=(
    'Abri Liebenberg (+61 4 3282 3087)',
    'Bartosz Lewandowski (+886 978 705 232)',
    'Jeff Huang (+886 933 308 768)',
    'Jill Shen (+886 903 438 345)',
    'Matt Cheng (+886 932 075 280)',
    'Matthew Geoghegan (+886 905 249 541)')).place(x=105, y=340)
comms_variable.set('Pick one')


# Crisis_Manager
crisis_lab = Label(win, font=size8_B,text='Crisis Manager: ').place(x=0, y=360)
crisis_variable = StringVar()
# crisis_lab2=Label(win,font=size8_B,textvariable=comms_variable).place(x=245,y=360)
crisis_entry = Entry(win, font=size8_B, textvariable=crisis_variable).place(x=105, y=361)
crisis_variable.set('Null or Fill in')

# ITOC member
ITOC_lab = Label(win, font=size10_B, text='Escalated by:',fg='red').place(x=0, y=380)
ITOC_variable = StringVar()
ITOC_manager = ttk.Combobox(win, textvariable=ITOC_variable, values=(
    'Acise Lee',
    'Christopher Lia',
    'Da Wu',
    'Jackie Xu',
    'Jiajin Kang',
    'Jin Yang',
    'Joy Huang',
    'Ray Duan')).place(x=105, y=380)
ITOC_variable.set('Pick or Input')

# clik Number
# 輸入字母強制轉大寫 https://www.codenong.com/44105484/
def to_uppercase(*args):
    clik_variable.set(clik_variable.get().upper())
clik_variable = StringVar()
clik_lab = Label(win, font=size8_B, text='Clik ID:').place(x=0, y=400)
# 輸入框 https://jennaweng0621.pixnet.net/blog/post/403560362-%5Bpython%5D-tkinter-%E6%96%87%E5%AD%97%E6%A1%86%28entry%29
clik_entry = Entry(win, textvariable=clik_variable).place(x=105, y=400)
clik_variable.trace_add('write', to_uppercase)


# SUPL Number
def to_uppercase(*args):
    ref_variable.set(ref_variable.get().upper())
ref_variable = StringVar()
ref_lab = Label(win, font=size8_B, text='Ref#').place(x=0, y=420)
ref_entry = Entry(win, textvariable=ref_variable).place(x=105, y=420)
ref_variable.trace_add('write', to_uppercase)

# Teams URL
teams_variable = StringVar()
teams_lab = Label(win, font=size8_B, text='Teams Chat: ').place(x=0, y=440)
teams_entry = Entry(win, textvariable=teams_variable).place(x=105, y=440)
teams_variable.set('N/A')


# TEXT物件
# mes=tk.Text(win, width=50, height=3)
# mes.insert("insert", "未選擇")
# mes.pack()
def copy_comms():
    win.clipboard_clear()

    sv=service_variable.get()
    if sv.isdigit() :
        service_variable.set(service_variable.get()+' %')
        

    if cause_variable.get() == 'Regular Maintenance':
        teams_variable.set('N/A')

    if comms_variable.get() == 'Pick one':
        messagebox.showerror('Pick one please!', 'Chooce a Manager')

    if crisis_variable.get() == 'Null or Fill in':
        crisis_variable_X = comms_variable.get()
        crisis_variable.set(crisis_variable_X)

    if ITOC_variable.get() == 'Pick or Input':
        messagebox.showerror('Hey! ITOC', 'Who are you?')
    



# https://pyformat.info/ 數字補零格式化
    all_sen = \
        "Status: " + status_variable.get() +\
        "\nSeverity: " + sev_variable.get() +\
        "\nName: " + msglabel.get() +\
        "\nTier: " + tier_variable.get() +\
        "\nOperator: Power_Asia, FCM88, TOP_USD2, Asia888, Poseidon, TH1GAMES, TOP_USD(GAMA), MaxPro, Metaltex" +\
        "\nTime Elapsed: " + elapsed_variable.get() +\
        "\nStart Time: " + datetime.datetime.now().strftime('%Y-%m-') + '{:02d}'.format(sTed.get()) + ' ' + '{:02d}'.format(sTeh.get()) + ':' + '{:02d}'.format(sTem.get()) + " (GMT+8)" +\
        "\nEnd Time: " + datetime.datetime.now().strftime('%Y-%m-') + '{:02d}'.format(eTed.get()) + ' ' + '{:02d}'.format(eTeh.get()) + ':' + '{:02d}'.format(eTem.get()) + " (GMT+8)" +\
        "\nService Degradation: " + service_variable.get() +\
        "\nSymptoms: GPM degradation on TEG0 " +\
        "\nAction Taken: " + action_variable.get() +\
        "\nRoot Cause: " + cause_variable.get() +\
        "\nComms Manager: " + comms_variable.get() +\
        "\nCrisis Manager: " + crisis_variable.get() +\
        "\nEscalated by: " + ITOC_variable.get() + " (+886 226 560 700 ext 207)" +\
        "\n" +\
        "\nClik ID: " + clik_variable.get() +\
        "\nCustomer Ref#: " + ref_variable.get() +\
        "\n" +\
        "\nJoin Microsoft Teams Chat: " + teams_variable.get()
    win.clipboard_append(all_sen) # This is the process of copying to the clipboard
    


def clear_All():  # https://stackoom.com/question/3mvSR https://stackoverflow.com/questions/37171478/how-to-deselect-checkboxes-using-a-button-in-python
    i = 0
    for i in range(0, len(HO)):
        HO[i].set(0)
    
    status_variable.set('New')
    sev_variable.set('A')
    # name
    tier_variable.set('Tier_1')
    # operator
    # elapsed
    sTed.set(ima.day)
    sTeh.set(ima.hour)
    sTem.set(ima.minute)
    eTed.set(ima.day)
    eTeh.set(ima.hour)
    eTem.set(ima.minute)
    service_variable.set('N/A')
    # symptoms
    action_variable.set('How is it now?')
    cause_variable.set('Unknown')
    comms_variable.set('Pick one')
    crisis_variable.set('Null or Fill in')
    clik_variable.set('')
    ref_variable.set('')
    teams_variable.set('N/A')
    win.quit


# 放置參考https://pythonhi.pixnet.net/blog/post/322521486; http://yhhuang1966.blogspot.com/2018/10/python-gui-tkinter_12.html
copybtn = Button(win, text="Copy", padx=50, pady=5, command=copy_comms) . pack(side='left', padx=50, anchor=S)
clearbtn = Button(win, text="Clear", padx=50, pady=5, command=clear_All) . pack(side='right', padx=50, anchor=S)

win.mainloop()  # 常駐主視窗,不然執行後會關閉視窗
