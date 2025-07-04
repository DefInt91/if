from tkinter import CENTER, Tk, Label, StringVar, OptionMenu, Entry, Text, Scrollbar, RIGHT, Y, Listbox, YES, Button, \
    mainloop, END, Frame, messagebox, TclError, WORD, Menu, font, ttk, filedialog, Toplevel, PhotoImage
from tkcalendar import Calendar
import bitlyshortener
from bitlyshortener.exc import RequestError, ArgsError, ShortenerError
import re
from datetime import datetime
import klembord
import json
from jira import JIRA, JIRAError
import psutil
import textwrap
import base64
# import smtplib

# Updated History
# 2022/10/28 新增多系統百分比附加, 簡易計算百分比
# 2022/11/09 多import一個模組JIRAError
# 2022/11/09 修復Create Jira ticket. 新增顯示Jira 錯誤訊息
# 2023/03/31 修改Action Taken的內容可在json檔新增修改
# 2023/04/09 新增：Clik ID自動填入、時間日期帶入APP開啟時間、取得當下時間按鈕
# 2023/04/09 移除：持續顯示當下時間，降低佔用資源
# 2023/05/28 增加效能检查psutil
# 2023/06/02 增加倒计时按钮
# 2023/06/13 Bring to front when countdown ends + trigger PD(Hidden)
# 2024/07/25 新增判斷teams URL 可保留tinyurl
# 2025/06/30 
# 1.移除symptoms顯示，功能還在只是不顯示
# 2.標題可自行添加在json檔裡面用來下拉選擇
# 3.修正無法貼到純文字中
# 4.新增選擇ICU時自動填入End Time/Root Cause/Clik ID/Customer Ref
# 5.新增清除action taken按鈕
# 2025/07/01
# 重新建立佈局方式
# 2025/07/03
# 新增Icon
# 更改comms manager下拉選單模式
# 更改Get Time 按鈕


icon_b64 = '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'

# Main Window
master = Tk()
master.title('High Severity Escalation App --Version 8.7.1')

# --- 解碼並設定圖示 ---
try:
    icon_binary_data = base64.b64decode(icon_b64)
    icon_image = PhotoImage(data=icon_binary_data)
    # master.iconphoto(True, icon_image) 的 True 參數代表後續的子視窗(Toplevel)也會沿用此圖示
    master.iconphoto(True, icon_image)
except Exception as e:
    print(f"設定視窗圖示時發生錯誤: {e}")

# 建立左側和右側的主要框架
# padx 和 pady 是為了讓框架和視窗邊緣有一些間距，比較美觀
left_frame = Frame(master, padx=10, pady=10)
right_frame = Frame(master, padx=10, pady=10)

# 使用 pack 將左右框架並排。fill='both' 和 expand=True 是讓框架能跟隨視窗縮放的關鍵
left_frame.pack(side='left', fill='both', expand=True)
right_frame.pack(side='right', fill='both', expand=True)

def center_window(window, width, height):
    """計算並設定視窗在螢幕正中央的位置。"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

# File Menu
def help():
    splash_window = Toplevel(master)
    splash_window.title("Help") 
    center_window(splash_window, 300, 300)
    yscrollbar = Scrollbar(splash_window)
    yscrollbar.pack(side=RIGHT, fill=Y)
    help_box = Text(splash_window, height=120, width=300, undo=True, wrap=WORD)
    help_box.insert("end", "Help\n\n"
                           "1. Time Elapsed is automatically calculated. You just need to fill in the 'Now' time. "
                           "Only resolved/ICU escalations will have End Time printed. Time Elapsed 是自動計算的. "
                           "只需要填寫“現在”時間. 只有Resolved/ICU才會打印 End Time\n\n"
                           "2. 有建議可以提出，但不一定會有用")
    help_box.pack()


menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
menu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Help", command=help)
menubar.add_cascade(label="File", menu=filemenu)
master.config(menu=menubar)

# 將這個函式放在您所有 UI 元件建立之前，例如放在 `menubar` 設定的後面

status_options = None
severity_options = None
tier_options = None
root_cause_options  = None
comms_manager_options  = None
Presult = None 
pp = None

def lst_generator(lst1, lst2):
    for x in lst1:
        for y in x:
            lst2.append(y)

def load_and_update_config(filepath):
    """從指定的路徑載入 JSON 檔案，並更新所有相關的變數和 UI 元件。"""
    global status2, severity2, affecting_system2, tier2, operator2, service_degradation2, root_cause2, comms_manager2
    global action_taken_text, escalation_names, user, apikey, server, escalated_by_value, action_taken_options

    try:
        with open(filepath, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # --- 1. 重新載入所有資料到變數 ---
        # 使用 .get(key, default_value) 的方式讀取，這樣即使 json 缺少某個 key 也不會出錯
        status_data = data.get('status', [])
        severity_data = data.get('severity', [])
        affecting_system_data = data.get('affecting_system', [])
        tier_data = data.get('tier', [])
        operator_data = data.get('operator', [])
        service_degradation_data = data.get('service_degradation', [])
        root_cause_data = data.get('root_cause', [])
        comms_manager_data = data.get('comms_manager', [])
        
        escalation_names = data.get('escalation_names', [])
        action_taken_options = data.get('action_taken', [])

        user = data.get('user', '')
        apikey = data.get('apikey', '')
        server = data.get('server', '')
        escalated_by_value = data.get('escalated_by', 'N/A')

        # --- 2. 清空並重新填滿給 OptionMenu 用的列表 ---
        status2, severity2, affecting_system2, tier2, operator2, service_degradation2, root_cause2, comms_manager2 = [],[],[],[],[],[],[],[]
        lst_generator([status_data], status2)
        lst_generator([severity_data], severity2)
        lst_generator([affecting_system_data], affecting_system2)
        lst_generator([tier_data], tier2)
        lst_generator([operator_data], operator2)
        lst_generator([service_degradation_data], service_degradation2)
        lst_generator([root_cause_data], root_cause2)
        lst_generator([comms_manager_data], comms_manager2)

        # --- 3. 更新 UI 介面 ---
        refresh_ui_elements()
        
        # messagebox.showinfo("成功", f"已成功從 {filepath} 載入設定！")

    except FileNotFoundError:
        messagebox.showerror("錯誤", f"找不到檔案：{filepath}")
    except json.JSONDecodeError:
        messagebox.showerror("錯誤", f"檔案 {filepath} 不是一個有效的 JSON 格式。")
    except Exception as e:
        messagebox.showerror("錯誤", f"讀取設定時發生未知錯誤：{e}")

def refresh_ui_elements():
    """專門用來刷新介面所有元件內容的函式 (已更新為 Grid 佈局)。"""
    # 確保這些元件變數是全域的，以便函式存取
    global status_options, severity_options, tier_options, root_cause_options, comms_manager_options, action_taken_combobox, action_taken_text_area

    # --- 更新左側框架 (Left Frame) ---
    
    # 更新 Escalation Name Combobox
    name_combobox['values'] = escalation_names
    if escalation_names:
        name_combobox.set(escalation_names[0])
    else:
        name_combobox.set("GPM degradation by XX% affecting <xxx>")

    # 更新 Escalated by 輸入框
    escalated_by.set(escalated_by_value)

    # 1. 刪除所有舊的 OptionMenu
    if 'status_options' in globals() and status_options.winfo_exists(): status_options.destroy()
    if 'severity_options' in globals() and severity_options.winfo_exists(): severity_options.destroy()
    if 'tier_options' in globals() and tier_options.winfo_exists(): tier_options.destroy()
    if 'root_cause_options' in globals() and root_cause_options.winfo_exists(): root_cause_options.destroy()
    
    # 2. 依序重建所有 OptionMenu (使用 .grid() 放回原位)
    # 重建 Status
    status_variable.set(status2[0] if status2 else "N/A")
    status_options = OptionMenu(left_frame, status_variable, *(status2 if status2 else ["N/A"]))
    status_options.grid(row=1, column=0, sticky="w")

    # 重建 Severity
    severity_variable.set(severity2[0] if severity2 else "N/A")
    severity_options = OptionMenu(left_frame, severity_variable, *(severity2 if severity2 else ["N/A"]))
    severity_options.grid(row=1, column=1, sticky="w", padx=5)

    # 重建 Tier
    tier_variable.set(tier2[0] if tier2 else "N/A")
    tier_options = OptionMenu(left_frame, tier_variable, *(tier2 if tier2 else ["N/A"]))
    tier_options.grid(row=1, column=2, sticky="w", padx=5)

    # 重建 Root Cause
    root_cause_variable.set(root_cause2[0] if root_cause2 else "N/A")
    root_cause_options = OptionMenu(left_frame, root_cause_variable, *(root_cause2 if root_cause2 else ["N/A"]))
    root_cause_options.grid(row=3, column=0, sticky="w")

    # --- 更新右側框架 (Right Frame) ---
    
    # 更新 Comms Manager (也在右側)
    comms_manager_options['values'] = comms_manager2
    if comms_manager2:
        comms_manager_variable.set(comms_manager2[0])
    else:
        comms_manager_variable.set("N/A")

    # 更新 Action Taken 區域
    action_taken_combobox['values'] = action_taken_options
    action_taken_combobox.set("Choose a template...")
    action_taken_text_area.delete("1.0", END)
    if action_taken_options:
        action_taken_text_area.insert("1.0", action_taken_options[0])

# 這是一個點擊按鈕後會觸發的函式
def open_file_and_reload():
    # 彈出檔案選擇視窗，限定只能選 .json 檔
    filepath = filedialog.askopenfilename(
        title="請選擇一個設定檔",
        filetypes=(("JSON files", "*.json"), ("All files", "*.*"))
    )
    if not filepath:  # 如果使用者取消選擇，filepath 會是空字串
        return
    
    # 呼叫我們的核心函式來載入並更新
    load_and_update_config(filepath)



# ==================== LEFT FRAME WIDGETS ====================
# 全選點擊文字框
def select_all(event):
    """一個通用的事件處理函式，會選取觸發此事件的元件內的所有文字。"""
    # event.widget 指的就是觸發這個<FocusIn>事件的那個元件(輸入框)本身
    event.widget.select_range(0, 'end')
    return 'break'


# --- 第 0-1 行: Status, Severity, Tier ---
Label(left_frame, text="Status", font=("Ariel", 10, "bold")).grid(row=0, column=0, sticky="w")
status_variable = StringVar(master)
status_variable.set("---")
status_options = OptionMenu(left_frame, status_variable, "---")
status_options.grid(row=1, column=0, sticky="ew") # sticky='ew' 讓元件水平填滿格子

Label(left_frame, text="Severity", font=("Ariel", 10, "bold")).grid(row=0, column=1, sticky="w", padx=5)
severity_variable = StringVar(master)
severity_variable.set("---")
severity_options = OptionMenu(left_frame, severity_variable, "---")
severity_options.grid(row=1, column=1, sticky="ew", padx=5)

Label(left_frame, text="Tier", font=("Ariel", 10, "bold")).grid(row=0, column=2, sticky="w", padx=5)
tier_variable = StringVar(master)
tier_variable.set("---")
tier_options = OptionMenu(left_frame, tier_variable, "---")
tier_options.grid(row=1, column=2, sticky="ew", padx=5)

# --- 第 2-3 行: Root Cause, Service Degradation ---
Label(left_frame, text="Root Cause", font=("Ariel", 10, "bold")).grid(row=2, column=0, sticky="w", pady=(10,0))
root_cause_variable = StringVar(master)
root_cause_variable.set("---")
root_cause_options = OptionMenu(left_frame, root_cause_variable, "---")
root_cause_options.grid(row=3, column=0, sticky="ew")

Label(left_frame, text="Service Degradation", font=("Ariel", 10, "bold")).grid(row=2, column=1, columnspan=2, sticky="w", padx=5, pady=(10,0))
# Service Degradation 的12個格子，我們用一個新的Frame包起來再用grid管理
degradation_frame = Frame(left_frame)
degradation_frame.grid(row=3, column=1, columnspan=2, sticky="w", padx=5)
s1 = Entry(degradation_frame, width=4, justify='center'); s1.grid(row=0, column=0); s1.bind('<FocusIn>', select_all)
s2 = Entry(degradation_frame, width=4, justify='center'); s2.grid(row=0, column=1); s2.bind('<FocusIn>', select_all)
s3 = Entry(degradation_frame, width=4, justify='center'); s3.grid(row=0, column=2); s3.bind('<FocusIn>', select_all)
s4 = Entry(degradation_frame, width=4, justify='center'); s4.grid(row=0, column=3); s4.bind('<FocusIn>', select_all)
s5 = Entry(degradation_frame, width=4, justify='center'); s5.grid(row=0, column=4); s5.bind('<FocusIn>', select_all)
s6 = Entry(degradation_frame, width=4, justify='center'); s6.grid(row=0, column=5); s6.bind('<FocusIn>', select_all)
s7 = Entry(degradation_frame, width=4, justify='center'); s7.grid(row=1, column=0); s7.bind('<FocusIn>', select_all)
s8 = Entry(degradation_frame, width=4, justify='center'); s8.grid(row=1, column=1); s8.bind('<FocusIn>', select_all)
s9 = Entry(degradation_frame, width=4, justify='center'); s9.grid(row=1, column=2); s9.bind('<FocusIn>', select_all)
s10 = Entry(degradation_frame, width=4, justify='center'); s10.grid(row=1, column=3); s10.bind('<FocusIn>', select_all)
s11 = Entry(degradation_frame, width=4, justify='center'); s11.grid(row=1, column=4); s11.bind('<FocusIn>', select_all)
s12 = Entry(degradation_frame, width=4, justify='center'); s12.grid(row=1, column=5); s12.bind('<FocusIn>', select_all)


# --- 第 4-5 行: Escalation Name ---
Label(left_frame, text="Escalation Name", font=("Ariel", 10, "bold")).grid(row=4, column=0, columnspan=3, sticky="w", pady=(10,0))
name = StringVar()
name_combobox = ttk.Combobox(left_frame, textvariable=name, width=60, values=[])
name_combobox.grid(row=5, column=0, columnspan=3, sticky="ew") # sticky='ew' 讓它水平填滿

# --- 第 6-7 行: Affecting System, Operators ---
# # 1. 建立一個新的容器 Frame，用來裝這兩個按鈕區塊
selection_buttons_frame = Frame(left_frame)
selection_buttons_frame.grid(row=6, column=0, columnspan=3, sticky="w", pady=(10,0))

# 2. 將 Affecting System 的區塊放進新的容器中，並靠左排列
system_frame = Frame(selection_buttons_frame)
system_frame.pack(side='left') # 使用 pack 讓它靠左
af_button = Button(system_frame, text="Affecting System:", command=lambda: select_affecting_system())
af_button.pack()
af_frame = Frame(system_frame)
af_frame.pack()

# 3. 將 Operators 的區塊也放進新的容器中，同樣靠左排列
#    padx=20 是為了在兩個按鈕之間創造出適當的間距，您可以自行調整這個數字
op_frame_container = Frame(selection_buttons_frame)
op_frame_container.pack(side='left', padx=20) # 使用 pack 讓它靠左
operator_button = Button(op_frame_container, text="Operators:",command=lambda: select_operators())
operator_button.pack()
op_frame = Frame(op_frame_container)
op_frame.pack()

# Percent Calculation
def degradationP():
    """計算百分比，並更新預先建立好的 Label 元件。"""
    global Presult, pp # 告訴函式我們要修改的是全域的 Label

    try:
        # 1. 取得數值
        num1 = float(cal_degradation1.get())
        num2 = float(cal_degradation2.get())

        # 2. 計算百分比
        if num1 == 0 and num2 == 0: # 避免除以零的錯誤
            percent_result = 0
        elif num1 >= num2:
            percent_result = ((num1 - num2) / num1) * 100
        else:
            percent_result = ((num2 - num1) / num2) * 100
        
        # 3. 決定顏色 (只有一個判斷區塊)
        percent_int = int(percent_result)
        if percent_int > 49:
            color = "red"
        elif 25 <= percent_int <= 49:
            color = "orange"
        else:
            color = "black"

        # 4. 更新預先建立好的 Label 的文字和顏色
        #    使用 .config() 來修改屬性，而不是建立新元件
        if 'Presult' in globals() and Presult.winfo_exists():
            Presult.config(text=str(percent_int), fg=color)
        if 'pp' in globals() and pp.winfo_exists():
            pp.config(text="%", fg=color)

    except (ValueError, ZeroDivisionError):
        # 如果使用者輸入的不是數字，或發生除以零的狀況，跳出提示
        messagebox.showerror("輸入錯誤", "請在百分比計算欄位中輸入有效的數字。")
        # 清空顯示結果
        if 'Presult' in globals() and Presult.winfo_exists():
            Presult.config(text="")
        if 'pp' in globals() and pp.winfo_exists():
            pp.config(text="")
            
calc_frame = Frame(left_frame)
calc_frame.grid(row=7, column=0, columnspan=3, pady=(20,0), sticky='w')
Label(calc_frame, text="Percent Calculation %", font=("Ariel", 10, "bold")).grid(row=0, column=0, columnspan=3, sticky='w')
cal_degradation1 = StringVar(value="NN")
cal_degradation_entry_box1 = Entry(calc_frame, textvariable=cal_degradation1, width=4, justify='center')
cal_degradation_entry_box1.grid(row=1, column=0)
cal_degradation_entry_box1.bind('<FocusIn>', select_all)
# ... Percent Calc 的其他元件也放在 calc_frame 裡面 ...
cal_degradation2 = StringVar(value="NN")
cal_degradation_entry_box2 = Entry(calc_frame, textvariable=cal_degradation2, width=4, justify='center')
cal_degradation_entry_box2.grid(row=1, column=1, padx=5)
cal_degradation_entry_box2.bind('<FocusIn>', select_all)

cal_P = Button(calc_frame, text="Calculator", command=degradationP)
cal_P.grid(row=1, column=2, padx=5)

# vvvv 新增這兩行，預先建立用來顯示結果的 Label vvvv
Presult = Label(calc_frame, text="", font=("Ariel", 10, "bold"))
Presult.grid(row=1, column=3, padx=(10, 0)) # 放在計算機按鈕右邊

pp = Label(calc_frame, text="", font=("Ariel", 10, "bold"))
pp.grid(row=1, column=4, sticky='w')

def click_clear_entry1(event):
    start_time_entry_box1.delete(0, "end")
    return None


def click_clear_entry2(event):
    start_time_entry_box2.delete(0, "end")
    return None


def click_clear_entry3(event):
    end_time_entry_box1.delete(0, "end")
    return None


def click_clear_entry4(event):
    end_time_entry_box2.delete(0, "end")
    return None

# Get Current Time


sel_date1 = datetime.now().date().strftime("%Y-%m-%d")

sel_date2 = datetime.now().date().strftime("%Y-%m-%d")


def update_time():
    # E_now = datetime.now()
    # E_hour = E_now.hour
    # E_minute = E_now.minute
    end_time1.set("{:02d}".format(datetime.now().hour))
    end_time2.set("{:02d}".format(datetime.now().minute))
    global sel_date2
    sel_date2 = datetime.now().date().strftime("%Y-%m-%d")
    cal_label2.config(text=sel_date2)



# Time Elapsed
def time_elapsed(year1, month1, day1, hour1, min1, year2, month2, day2, hour2, min2):
    start_time = datetime(int(year1), int(
        month1), int(day1), int(hour1), int(min1))
    end_time = datetime(int(year2), int(month2),
                        int(day2), int(hour2), int(min2))

    c = end_time - start_time
    txt = str(c)[:-3]  # string can change if days are included or not
    z = re.split("\\s", txt)  # splits into "###, days, hh:mm"
    # splits only hh:mm and removes a set of brackets on the hh:mm
    a = re.split(":", ", ".join(z))
    if "-" in txt:
        return 'date error'
    # z length of 3 is equal to "###, days, hh:mm"
    elif len(z) == 3 and z[2] and z[2][-2:] == "00" and z[2][:-3] == "0":
        return z[0] + "d"  # gives #d only
    elif len(z) == 3 and z[2] and z[2][:-3] == "0":
        # gives #d and #m int function removes leading zero
        return z[0] + "d" + " " + str(int(z[2][-2:])) + "m"
    elif len(z) == 3 and z[2] and z[2][-2:] == "0":
        return z[0] + "d" + " " + z[2][:-3] + "h"  # gives #d #h
    elif len(z) == 3 and z[2]:
        return z[0] + "d" + " " + z[2][:-3] + "h" + " " + str(
            int(z[2][-2:])) + "m"  # gives #d #h #m int func removes leading zero

    # z length of 1 is equal to "hh:mm"
    elif len(z) == 1 and a[1] == "00":
        return a[0] + "h"  # gives #h
    elif len(z) == 1 and a[0] == "0":
        # gives #m int function removes leading zero
        return str(int(a[1])) + "m"
    elif len(z) == 1:
        # gives #H #m int function removes leading zero
        return a[0] + "h" + " " + str(int(a[1])) + "m"
    else:
        print('no match')


# Checks if resolved comms is sent
def resolved_checker():
    if status_variable.get() == "Resolved" or status_variable.get() == "New/Resolved" or \
            status_variable.get() == "Re-occurring/Resolved":
        return str(sel_date2[0:4]) + "-" + str(sel_date2[5:7]) + "-" + str(sel_date2[8:10]) + " " + \
            str((end_time1.get().rjust(2, '0'))) + ":" + \
            str((end_time2.get().rjust(2, '0'))) + " (GMT+8)"
    elif status_variable.get() == "ICU":
        root_cause_variable.set("Not Applicable")
        clik_id.set("Not Applicable")
        customer_ref.set("Not Applicable")
        return str(sel_date2[0:4]) + "-" + str(sel_date2[5:7]) + "-" + str(sel_date2[8:10]) + " " + \
            str((end_time1.get().rjust(2, '0'))) + ":" + \
            str((end_time2.get().rjust(2, '0'))) + " (GMT+8)"
    else:
        return "N/A"


# Start/End Time and Date
time_frame = Frame(left_frame)
time_frame.grid(row=8, column=0, columnspan=3, pady=(10,0), sticky='w')
Button(time_frame, text="Start Date", command=lambda: get_date1()).grid(row=0, column=0, sticky='w')
cal_label1 = Label(time_frame, text=sel_date1); cal_label1.grid(row=1, column=0, sticky='w')
Label(time_frame, text="Start Time (GMT+8):", font=("Ariel", 10, "bold")).grid(row=0, column=1, padx=10, sticky='w')
# 建立一個專門放 Start Time 輸入框的小框架
start_time_entries_frame = Frame(time_frame)
start_time_entries_frame.grid(row=1, column=1, padx=10, sticky='w')
# ... Start/End Time 的其他元件也放在 time_frame 裡面 ...
# 2. 將兩個 Entry 元件用 pack 放進這個小框架，它們就會緊鄰
start_time1 = StringVar(value=f"{datetime.now().hour:02d}")
start_time2 = StringVar(value=f"{datetime.now().minute:02d}")
start_time_entry_box1 = Entry(start_time_entries_frame, textvariable=start_time1, width=4, justify='center')
start_time_entry_box1.pack(side='left')
start_time_entry_box2 = Entry(start_time_entries_frame, textvariable=start_time2, width=4, justify='center')
start_time_entry_box2.pack(side='left', padx=5)

Button(time_frame, text="End Date", command=lambda: get_date2()).grid(row=2, column=0, sticky='w', pady=(10,0))
cal_label2 = Label(time_frame, text=sel_date2); cal_label2.grid(row=3, column=0, sticky='w')
Label(time_frame, text="Now/End Time (GMT+8):", font=("Ariel", 10, "bold")).grid(row=2, column=1, padx=10, sticky='w', pady=(10,0))

end_time_entries_frame = Frame(time_frame)
end_time_entries_frame.grid(row=3, column=1, padx=10, sticky='w')
end_time1 = StringVar(value=f"{datetime.now().hour:02d}")
end_time2 = StringVar(value=f"{datetime.now().minute:02d}")
end_time_entry_box1 = Entry(end_time_entries_frame, textvariable=end_time1, width=4, justify='center')
end_time_entry_box1.pack(side='left')
end_time_entry_box2 = Entry(end_time_entries_frame, textvariable=end_time2, width=4, justify='center')
end_time_entry_box2.pack(side='left', padx=5)
# Get Current Time Button
gettime_button = Button(end_time_entries_frame, text="Get Time", command=lambda: update_time())
gettime_button.pack(side='left', padx=5)
# gettime_button_font = font.Font(size=0, weight='bold')
# gettime_button['font'] = gettime_button_font

# Calendar1
def get_date1():
    splash_window = Tk()
    splash_window.title("Select Start Date")
    splash_window.winfo_screenwidth()
    splash_window.winfo_screenheight()
    center_window(splash_window, 300, 300)
    cal = Calendar(splash_window, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=20)
    Button(splash_window, text="Select", command=lambda: select_date1()).pack()

    # Select Date Within Calendar
    def select_date1():
        global sel_date1
        cal_label1.config(text=cal.get_date())
        sel_date1 = cal.get_date()
        splash_window.destroy()
        return sel_date1



# Calendar2
def get_date2():
    splash_window = Tk()
    splash_window.title("Select End Date")
    splash_window.winfo_screenwidth()
    splash_window.winfo_screenheight()
    center_window(splash_window, 300, 300)
    cal = Calendar(splash_window, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=20)
    Button(splash_window, text="Select", command=lambda: select_date2()).pack()

    # Select Date Within Calendar
    def select_date2():
        global sel_date2
        cal_label2.config(text=cal.get_date())
        sel_date2 = cal.get_date()
        splash_window.destroy()
        return sel_date2


# --- 底部的按鈕 ---
bottom_button_frame = Frame(left_frame)
bottom_button_frame.grid(row=9, column=0, columnspan=3, pady=(20,0))
load_button = Button(bottom_button_frame, text="Import\nConfig", command=open_file_and_reload, height=2, width=10)
load_button.grid(row=0, column=0, padx=5)
countdown_button = Button(bottom_button_frame, text="Countdown", command=lambda: countdown2(), height=2, width=10)
countdown_button.grid(row=0, column=1, padx=5)
print_button = Button(bottom_button_frame, text="Print", command=lambda: printandcount(), height=2, width=10)
print_button.grid(row=0, column=2, padx=5)


all_degradation = []

# Degradation Calculation %
def showPercent():
    global all_degradation
    all_degradation = []
    service_degradation_variable = [s1.get(), s2.get(), s3.get(), s4.get(), s5.get(
    ), s6.get(), s7.get(), s8.get(), s9.get(), s10.get(), s11.get(), s12.get()]
    try:
        for i in range(0, len(service_degradation_variable)):
            if not service_degradation_variable[0]:
                all_degradation.append("N/A")
                all_degradation[1:] = []
            elif int(service_degradation_variable[i]) > 0:
                all_degradation.append(service_degradation_variable[i] + "%")
    except ValueError:
        print("not number")



PercentE = StringVar()





# Symptoms
# symptoms_label = Label(master, text="Symptoms", font=("Ariel", 10, "bold"))
# symptoms_label.place(x=0, y=450)
# symptoms = Text(master, undo=True, wrap=WORD)
# symptoms.insert("3.0", "")
# symptoms.place(x=0, y=470, height=100, width=390)


# 2. 建立一個 StringVar 來控制下拉選單
action_taken_template_var = StringVar()

# 3. 建立一個函式，當下拉選單被選擇時，會將內容填入下方的文字框
def on_template_select(event):
    """當使用者從下拉選單選擇模板時，將內容附加到文字框後方。"""
    # 1. 取得從下拉選單中選擇的模板文字
    selected_template = action_taken_template_var.get()

    # 如果沒有選擇任何東西，就直接結束
    if not selected_template:
        return

    # 2. 取得文字框中「現有」的內容
    #    使用 "end-1c" 是為了去除 Text 元件在結尾會自動加入的隱形換行符
    current_text = action_taken_text_area.get("1.0", "end-1c").strip()

    # 3. 判斷文字框是否為空
    if not current_text:
        # 如果現有內容是空的，就直接插入新選擇的模板
        action_taken_text_area.insert("1.0", selected_template)
    else:
        # 如果已有內容，則在後面附加 ". " 和新選擇的模板
        text_to_add = f" {selected_template}"
        action_taken_text_area.insert(END, text_to_add)

# ==================== RIGHT FRAME WIDGETS ====================
def clear_action_taken():
    """僅清除 Action Taken 文字框，並將其重設為預設模板。"""
    # vvvv 加上這一行，告訴函式要去全域作用域找這兩個變數 vvvv
    global action_taken_text_area, action_taken_options

    # 1. 刪除從頭到尾的所有文字
    action_taken_text_area.delete("1.0", END)

    # 2. 檢查是否有預設的模板選項列表
    # if action_taken_options:
    #     # 3. 如果有，則將第一個模板 (template1) 重新插入
    #     default_template = action_taken_options[0]
    #     action_taken_text_area.insert("1.0", default_template)


# --- Action Taken Section (New Layout) ---

# 1. 建立一個總容器 Frame
action_taken_section_frame = Frame(right_frame)
action_taken_section_frame.grid(row=0, column=0, columnspan=2, sticky="new", pady=(0, 10)) # sticky='new' 讓它填滿寬度
# 讓容器的第二欄(column=1)可以拉伸，這樣清除按鈕就會被推到最右邊
action_taken_section_frame.columnconfigure(1, weight=1)

# 2. 將所有相關元件都放進這個新容器中
#    注意它們的父容器都是 action_taken_section_frame

# Action Taken 標籤 (放在容器的第0行、第0欄)
Label(action_taken_section_frame, text="Action Taken", font=("Ariel", 10, "bold")).grid(row=0, column=0, sticky="w")

# Clear Action Taken 按鈕 (放在容器的第0行、第1欄，並靠右對齊)
clear_action_button = Button(action_taken_section_frame, text="Clear Action Taken", command=clear_action_taken)
clear_action_button.grid(row=0, column=1, sticky="e")

# 模板選擇 Combobox (放在第1行，橫跨2欄)
action_taken_template_var = StringVar()
action_taken_combobox = ttk.Combobox(action_taken_section_frame, textvariable=action_taken_template_var, width=60, values=[], state='readonly')
action_taken_combobox.set("Choose a template...")
action_taken_combobox.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(5,0))
action_taken_combobox.bind("<<ComboboxSelected>>", on_template_select)

# 多行文字輸入框 (放在第2行，橫跨2欄)
action_taken_text_area = Text(action_taken_section_frame, undo=True, wrap=WORD, height=6, width=50)
action_taken_text_area.grid(row=2, column=0, columnspan=2, sticky="ew")


# Comms Manager
comms_manager_frame = Frame(right_frame)
comms_manager_frame.grid(row=3, column=0, columnspan=2, sticky="w", pady=(10,0))
# 讓容器的第二欄(column=1)可以拉伸，以填滿空間
comms_manager_frame.columnconfigure(1, weight=1)

# 2. 建立 Label 和 Combobox，並放入容器中
Label(comms_manager_frame, text="Comms Manager", font=("Ariel", 10, "bold")).grid(row=0, column=0, sticky="w")
comms_manager_variable = StringVar()
comms_manager_options = ttk.Combobox(comms_manager_frame, textvariable=comms_manager_variable, state='readonly', values=[], width=37)
comms_manager_options.grid(row=1, column=0, sticky="ew")



# Crisis Manager 
crisis_manager_frame = Frame(right_frame)
crisis_manager_frame.grid(row=5, column=0, columnspan=2, sticky="w", pady=(10,0))
Label(crisis_manager_frame, text="Crisis Manager", font=("Ariel", 10, "bold")).grid(row=0, column=0, sticky="w")
crisis_manager_variable = StringVar(value="Comms Manager")
crisis_manager_entry_box = Entry(crisis_manager_frame, textvariable=crisis_manager_variable, width=40) # 您可以設定 width
crisis_manager_entry_box.grid(row=1, column=0, sticky="ew") # sticky="ew" 讓它填滿容器寬度


def crisis_man_checker():
    if crisis_manager_variable.get().lower() == "comms manager" or crisis_manager_variable.get().lower() == "comms" \
            or crisis_manager_variable.get() == "communication manager" or crisis_manager_variable.get() == "":
        return comms_manager_variable.get()
    else:
        return crisis_manager_variable.get()


# Escalated by
escalated_by_frame = Frame(right_frame)
escalated_by_frame.grid(row=7, column=0, columnspan=2, sticky="w", pady=(10,0))
Label(escalated_by_frame, text="Escalated by", font=("Ariel", 10, "bold")).grid(row=0, column=0, sticky="w")
escalated_by = StringVar()
escalated_by_entry_box = Entry(escalated_by_frame, textvariable=escalated_by, width=40, state='readonly') # 您可以設定 width
escalated_by_entry_box.grid(row=1, column=0, sticky="ew") # sticky="ew" 讓它填滿容器寬度

# --- Clik ID and SUPL Button Section ---

# 1. 建立一個專門的容器 Frame 來包裹這三個元件
clik_id_section_frame = Frame(right_frame)
# 將這個容器放置到 right_frame 的第9行，讓它橫跨2欄
clik_id_section_frame.grid(row=9, column=0, columnspan=2, pady=(10,0), sticky='w')

# 2. 接下來，將所有三個元件都放進這個新的容器 clik_id_section_frame 中
#    注意：父容器都是 clik_id_section_frame，且 grid 的 row/column 是相對於這個新容器的

# Create SUPL 按鈕 (放在容器的第0行、第0欄，佔2列高)
supl_button = Button(clik_id_section_frame, text="Create\nSUPL", command=lambda: jira_generator())
supl_button.grid(row=0, column=0, rowspan=2, sticky='ns', padx=(0, 10)) # sticky='ns' 讓它垂直填滿

# Clik ID 標籤 (放在容器的第0行、第1欄)
Label(clik_id_section_frame, text="SUPL-XXXX", font=("Ariel", 10, "bold")).grid(row=0, column=1, sticky="w")

# Clik ID 輸入框 (放在容器的第1行、第1欄)
clik_id = StringVar(value="N/A")
# 您可以為 Entry 設定一個 width 來控制其寬度
clik_id_entry_box = Entry(clik_id_section_frame, textvariable=clik_id, width=31) 
clik_id_entry_box.grid(row=1, column=1, sticky="ew")



def jira_generator():
    showPercent()
    global single_issue
    
    try:
        options = {'server': server}
        jira = JIRA(options, basic_auth=(user, apikey))
    except Exception as e:
        messagebox.showerror("Jira 連線錯誤", f"無法初始化 Jira 連線，請檢查設定檔中的 server, user, apikey。\n\n錯誤：{e}")
        return

    try:
        if shortener(bitly_url) == "Invalid URL":
            messagebox.showinfo('Bitly Error', 'Invalid URL\n無效URL')
        elif sel_date1 is None or sel_date2 is None:
            messagebox.showinfo('Error',
                                'There was an error! Please check the minimum required fields for an escalation!\n'
                                '發生錯誤! 請確認各欄位!')
        elif time_elapsed(int(sel_date1[0:4]), int(sel_date1[5:7]), int(sel_date1[8:10]),
                          int(start_time1.get()), int(
                start_time2.get()), int(sel_date2[0:4]),
                int(sel_date2[5:7]), int(
                sel_date2[8:10]), int(end_time1.get()),
                int(end_time2.get())) == 'date error':
            messagebox.showinfo('Date Error', 'Check the date! \n'
                                              '     確認日期')
        elif items is None or op_items is None or items == [] or op_items == []:
            messagebox.showinfo('Error',
                                'There was an error! Please check the minimum required fields for an escalation!\n'
                                '發生錯誤! 請確認各欄位!')
        else:
            issue_dict = {
                'project': {'id': 10002},  # TSB project ID
                'summary': name.get(),
                'description': f'Status: {status_variable.get()}\n'
                               f'Severity: {severity_variable.get()}\n'
                               f'Name: {name.get()}\n'
                               f'Affecting System: {", ".join(items)}\n'
                               f'Tier: {tier_variable.get()}\n'
                               f'Operator: {", ".join(op_items)}\n'
                               f"""Time Elapsed: {time_elapsed(int(sel_date1[0:4]), int(sel_date1[5:7]), int(sel_date1[8:10]), int(start_time1.get()), int(start_time2.get()), int(sel_date2[0:4]), int(sel_date2[5:7]), int(sel_date2[8:10]), int(end_time1.get()), int(end_time2.get()))}\n"""
                               f'Start Time: '
                               f"""{sel_date1[0:4]}-{sel_date1[5:7]}-{sel_date1[8:10]} {(start_time1.get().rjust(2, '0'))}:{(start_time2.get().rjust(2, '0'))} (GMT+8)\n"""
                               f'End Time: {resolved_checker()}\n'
                               f'Service Degradation: {", ".join(all_degradation)}\n'
                               f'Symptoms: {name.get()}\n'
                               f'Action Taken: {action_taken_text_area.get("1.0", "end-1c")}\n'
                               f'Root Cause: {root_cause_variable.get()}\n'
                               f'Comms Manager: {comms_manager_variable.get()}\n'
                               f'Crisis Manager: {crisis_man_checker()}\n'
                               f'Escalated by: {escalated_by.get()}\n'
                               f'\n\n'
                               f'Clik ID: {clik_id.get()}\n'
                               f'Customer Ref#: {customer_ref.get()}\n'
                               f'\n\n'
                               f'Join Microsoft Teams Chat: {shortener(bitly_url)}',
                'issuetype': {'name': 'MG+ Support Ticket'},
                'customfield_10053': {'value': 'Alert'},  # Call Type
                'components': [{"name": "General Failure"}],  # Components
                'customfield_10051': {'value': 'K2'},  # Provider
                'customfield_10037': {'value': 'K2'},  # Head Office
            }
            new_issue = jira.create_issue(fields=issue_dict)
            single_issue = jira.issue(new_issue.key)
            clik_id.set(str(single_issue))
            root = Tk()
            T = Text(root, font='Ariel 10', height=15,
                     width=35, undo=True, wrap=WORD)
            T.pack()
            T.insert("end", "Ticket created successfully!\n\n" + str(single_issue) +
                     "\n\nhttps://asiasupport247.atlassian.net/browse/" + str(single_issue))
            return f'{single_issue}'
    except TypeError:
        messagebox.showinfo('Error', 'Please fill out the escalation fields first.\n'
                                     '發生錯誤! 請確認各欄位.')
    except ValueError:
        messagebox.showinfo('Error', 'Please fill out the escalation fields first.\n'
                                     '發生錯誤! 請確認各欄位.')
    except JIRAError as eM:
        print(eM.status_code, eM.text)
        if eM.status_code == 401:
            messagebox.showinfo('Error', 'Your API key might be expired. Please get a New API key for Atlassian via https://id.atlassian.com/manage-profile/security/api-tokens.\n\n'
                                'API Key可能已過期,請獲取新的API Key.\n\nError code: ' + str(eM.status_code) + '\n' + str(eM.text))
        else:
            messagebox.showinfo('Error', str(
                eM.status_code) + '\n' + str(eM.text))


# Customer Ref#
customer_ref_frame = Frame(right_frame)
customer_ref_frame.grid(row=11, column=0, columnspan=2, sticky="w", pady=(10,0))
Label(customer_ref_frame, text="Customer Ref# SUPL-XXXX", font=("Ariel", 10, "bold")).grid(row=0, column=0, sticky="w")
customer_ref = StringVar(value="N/A")
customer_ref_entry_box = Entry(customer_ref_frame, textvariable=customer_ref, width=40) # 您可以設定 width
customer_ref_entry_box.grid(row=1, column=0, sticky="ew") # sticky="ew" 讓它填滿容器寬度

# Teams Chat
bitly_url_frame = Frame(right_frame)
bitly_url_frame.grid(row=13, column=0, columnspan=3, sticky="w", pady=(10,0))
Label(bitly_url_frame, text='Shorten to Bitly URL (needs "https://"):', font=("Ariel", 10, "bold"), justify="left").grid(row=0, column=0, columnspan=2, sticky="w")
Label(bitly_url_frame, text='Join Microsoft Teams Chat', justify="left").grid(row=1, column=0, columnspan=2, sticky="w")
bitly_url = StringVar(value="N/A")
teams_chat_entry_box = Entry(bitly_url_frame, textvariable=bitly_url, width=40) # 您可以設定 width
teams_chat_entry_box.grid(row=2, column=0, sticky="ew") # sticky="ew" 讓它填滿容器寬度



# Bitly Setup
def shortener(url):
    bitly_url_fix = []
    bitly_url_fix = str(bitly_url.get()).split("/", 3)
    url = bitly_url.get()
    # Use your own API key
    tokens_pool = ['d2375064d1ef535690914f2d2d96d7390b41fb10']
    shortener = bitlyshortener.Shortener(
        tokens=tokens_pool, max_cache_size=256)

    if url == "N/A" or bitly_url_fix[2] == "bit.ly" or bitly_url_fix[2] == "tinyurl.com" :
        return url
    elif url != "":
        try:
            return str(','.join(shortener.shorten_urls([bitly_url.get()])))
        except RequestError:
            return str("Invalid URL")
        except ArgsError:
            return str("Invalid URL")
        except ShortenerError:
            return str("Invalid URL")
    else:
        return str("N/A")


# Setup error statement in print function
items = None


# Select Affecting System from listbox
def select_affecting_system():
    splash_window = Tk()
    splash_window.title("Select Affecting System")
    splash_window.winfo_screenwidth()
    splash_window.winfo_screenheight()
    center_window(splash_window, 300, 300)
    yscrollbar = Scrollbar(splash_window)
    yscrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(splash_window, height=10,
                      selectmode='multiple', yscrollcommand=yscrollbar.set)
    yscrollbar.config(command=listbox.yview)

    for item in affecting_system2:
        listbox.insert(affecting_system2.index(item), item)

    # Creates the list and label inside the window
    def listbox_used(event):
        global items
        items = []
        curselection = listbox.curselection()
        for index in curselection:
            # Gets current selection from listbox
            items.append(listbox.get(index))

    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.pack(padx=10, pady=10, expand=YES, fill="both")

    # Displays current selection
    def select():
        global af_label
        af_label = Label(af_frame, text=(', '.join(items)),
                         wraplength=100, justify="center")
        af_label.pack()
        splash_window.destroy()

    Button(splash_window, text="Select", command=lambda: select()).pack(pady=0)
    items.clear()
    af_label.destroy()

    splash_window.mainloop()



# Setup error statement in print function
op_items = None


# Select Operators from listbox
def select_operators():
    splash_window = Tk()
    splash_window.title("Select Operators")
    splash_window.winfo_screenwidth()
    splash_window.winfo_screenheight()
    center_window(splash_window, 300, 300)
    yscrollbar = Scrollbar(splash_window)
    yscrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(splash_window, height=10,
                      selectmode='multiple', yscrollcommand=yscrollbar.set)
    yscrollbar.config(command=listbox.yview)

    for item in operator2:
        listbox.insert(operator2.index(item), item)

    # Creates the list and label inside the window
    def listbox_used(event):
        global op_items
        op_items = []
        curselection = listbox.curselection()
        for index in curselection:
            # Gets current selection from listbox
            op_items.append(listbox.get(index))

    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.pack(padx=10, pady=10, expand=YES, fill="both")

    def select():
        global op_label
        op_label = Label(op_frame, text=(', '.join(op_items)), wraplength=120)
        op_label.pack()
        splash_window.destroy()

    Button(splash_window, text="Select", command=lambda: select()).pack(pady=0)
    op_items.clear()
    op_label.destroy()

    splash_window.mainloop()


# Prints the fully sent escalation comms
def print_template():
    showPercent()
    global T
    klembord.set_text('Nothing to copy!')
    try:
        if shortener(bitly_url) == "Invalid URL":
            messagebox.showinfo('Bitly Error', 'Invalid URL\n無效URL')
        elif sel_date1 is None or sel_date2 is None:
            messagebox.showinfo('Error',
                                'There was an error! Please check the minimum required fields for an escalation!\n'
                                '發生錯誤! 請確認各欄位!')
        elif time_elapsed(int(sel_date1[0:4]), int(sel_date1[5:7]), int(sel_date1[8:10]),
                          int(start_time1.get()), int(
                              start_time2.get()), int(sel_date2[0:4]),
                          int(sel_date2[5:7]), int(
                              sel_date2[8:10]), int(end_time1.get()),
                          int(end_time2.get())) == 'date error':
            messagebox.showinfo('Date Error', 'Check the date! \n'
                                              '     確認日期')
        elif items is None or op_items is None or items == [] or op_items == []:
            messagebox.showinfo('Error',
                                'There was an error! Please check the minimum required fields for an escalation!\n'
                                '發生錯誤! 請確認各欄位!')
        else:
            root = Tk()
            root.title("High Sev Escalation")
            T = Text(root, font='Ariel 10', height=25, width=80, undo=True)
            l = Label(root, text="Template")
            note = Label(
                root, text="Note: Can only copy bold text to an HTML editor.")
            l.config(font=("Courier", 14))
            b2 = Button(root, text="Exit",command=root.destroy )
            clipboard_button = Button(
                root, text="Copy Text", command=lambda: copy())
            l.pack()
            T.pack()
            note.pack()
            clipboard_button.pack(ipadx=20)
            b2.pack()

            T.tag_configure('bold', font='Ariel 10 bold')
            TAG_TO_HTML = {
                ('tagon', 'bold'): '<b>',
                ('tagoff', 'bold'): '</b>',
            }

            # Lets you copy and paste bold to HTML editors
            def copy():
                plain_text = textwrap.dedent(f"""
                Status: {status_variable.get()}
                Severity: {severity_variable.get()}
                Name: {name.get()}
                Affecting System: {", ".join(items)}
                Tier: {tier_variable.get()}
                Operator: {", ".join(op_items)}
                Time Elapsed: {time_elapsed(int(sel_date1[0:4]), int(sel_date1[5:7]), int(sel_date1[8:10]), int(start_time1.get()), int(start_time2.get()), int(sel_date2[0:4]), int(sel_date2[5:7]), int(sel_date2[8:10]), int(end_time1.get()), int(end_time2.get()))}
                Start Time: {sel_date1[0:4]}-{sel_date1[5:7]}-{sel_date1[8:10]} {(start_time1.get().rjust(2, '0'))}:{(start_time2.get().rjust(2, '0'))} (GMT+8)
                End Time: {resolved_checker()}
                Service Degradation: {", ".join(all_degradation)}
                Symptoms: {name.get()}
                Action Taken: {action_taken_text_area.get("1.0", "end-1c")}
                Root Cause: {root_cause_variable.get()}
                Comms Manager: {comms_manager_variable.get()}
                Crisis Manager: {crisis_man_checker()}
                Escalated by: {escalated_by.get()}

                Clik ID: {clik_id.get()}
                Customer Ref#: {customer_ref.get()}

                Join Microsoft Teams Chat: {shortener(bitly_url)}
                """).strip()

                rich_text = textwrap.dedent(f"""
                <b>Status: </b>{status_variable.get()}
                <br><b>Severity: </b>{severity_variable.get()}
                <br><b>Name: </b>{name.get()}
                <br><b>Affecting System: </b>{", ".join(items)}
                <br><b>Tier: </b>{tier_variable.get()}
                <br><b>Operator: </b>{", ".join(op_items)}
                <br><b>Time Elapsed:</b> {time_elapsed(int(sel_date1[0:4]), int(sel_date1[5:7]), int(sel_date1[8:10]), int(start_time1.get()), int(start_time2.get()), int(sel_date2[0:4]), int(sel_date2[5:7]), int(sel_date2[8:10]), int(end_time1.get()), int(end_time2.get()))}
                <br><b>Start Time: </b>{sel_date1[0:4]}-{sel_date1[5:7]}-{sel_date1[8:10]} {(start_time1.get().rjust(2, '0'))}:{(start_time2.get().rjust(2, '0'))} (GMT+8)
                <br><b>End Time: </b>{resolved_checker()}
                <br><b>Service Degradation: </b>{", ".join(all_degradation)}
                <br><b>Symptoms: </b>{name.get()}
                <br><b>Action Taken: </b>{action_taken_text_area.get("1.0", "end-1c")}
                <br><b>Root Cause: </b>{root_cause_variable.get()}
                <br><b>Comms Manager: </b>{comms_manager_variable.get()}
                <br><b>Crisis Manager: </b>{crisis_man_checker()}
                <br><b>Escalated by: </b>{escalated_by.get()}
                <br>
                <br><b>Clik ID: </b>{clik_id.get()}
                <br><b>Customer Ref#: </b>{customer_ref.get()}
                <br>
                <br><b>Join Microsoft Teams Chat: </b>{shortener(bitly_url)}
                """).strip()

                klembord.set_with_rich_text(plain_text, rich_text)


            T.insert("end", "Status: ", "bold")
            T.insert("end", f"{status_variable.get()}\n")
            T.insert("end", "Severity: ", "bold")
            T.insert("end", f"{severity_variable.get()}\n")
            T.insert("end", "Name: ", "bold")
            T.insert("end", f"{name.get()}\n")
            T.insert("end", "Affecting System: ", "bold")
            T.insert("end", f"{', '.join(items)}\n")
            T.insert("end", "Tier: ", "bold")
            T.insert("end", f"{tier_variable.get()}\n")
            T.insert("end", "Operator: ", "bold")
            T.insert("end", f"{', '.join(op_items)}\n")
            T.insert("end", "Time Elapsed: ", "bold")
            T.insert("end",
                     f"""{time_elapsed(int(sel_date1[0:4]), int(sel_date1[5:7]), int(sel_date1[8:10]),
                                       int(start_time1.get()), int(
                                           start_time2.get()), int(sel_date2[0:4]),
                                       int(sel_date2[5:7]), int(
                                           sel_date2[8:10]), int(end_time1.get()),
                                       int(end_time2.get()))}\n""")
            T.insert("end", "Start Time: ", "bold")
            T.insert("end",
                     f"{sel_date1[0:4]}-{sel_date1[5:7]}-{sel_date1[8:10]} {(start_time1.get().rjust(2, '0'))}:{(start_time2.get().rjust(2, '0'))} (GMT+8)\n")
            T.insert("end", "End Time: ", "bold")
            T.insert("end", f"{resolved_checker()}\n")
            T.insert("end", "Service Degradation: ", "bold")
            T.insert("end", f"{', '.join(all_degradation)}\n")
            T.insert("end", "Symptoms: ", "bold")
            T.insert("end", f"{name.get()}\n")
            T.insert("end", "Action Taken: ", "bold")
            T.insert("end", f"{action_taken_text_area.get("1.0", "end-1c")}\n")
            T.insert("end", "Root Cause: ", "bold")
            T.insert("end", f"{root_cause_variable.get()}\n")
            T.insert("end", "Comms Manager: ", "bold")
            T.insert("end", f"{comms_manager_variable.get()}\n")
            T.insert("end", "Crisis Manager: ", "bold")
            T.insert("end", f"{crisis_man_checker()}\n")
            T.insert("end", "Escalated by: ", "bold")
            T.insert("end", f"{escalated_by.get()}\n\n")
            T.insert("end", "Clik ID: ", "bold")
            T.insert("end", f"{clik_id.get()}\n")
            T.insert("end", "Customer Ref#: ", "bold")
            T.insert("end", f"{customer_ref.get()}\n\n")
            T.insert("end", "Join Microsoft Teams Chat: ", "bold")
            T.insert("end", f"{shortener(bitly_url)}")

    # Backup Errors
    except NameError:
        messagebox.showinfo('Error', 'Please fill out the escalation fields first.\n'
                                     '發生錯誤! 請確認各欄位.')
        pass
    except ValueError:
        messagebox.showinfo('Error', 'Please fill out the escalation fields first.\n'
                                     '發生錯誤! 請確認各欄位.')

    mainloop()






current_job = None
def countdown2():
    global current_job

    if current_job: #check if theres a running countdown
        master.after_cancel(current_job) #reset status
    if severity_variable.get() == "A":
        seconds = 30 * 60
    else:
        seconds = 60 * 60

    def decrement_time():
        global current_job
        nonlocal seconds
        if seconds > 0:
            minutes, secs = divmod(seconds, 60)
            time_string = "{:02d}:{:02d}".format(minutes, secs)
            countdown_button.config(text=time_string)
            seconds -= 1
            current_job = master.after(1000, decrement_time)
        else:
            # send_email()
            master.attributes("-topmost", True)
            master.attributes("-topmost", False)
            messagebox.showinfo("Time's Up!", "Please draft a updated comms")

    decrement_time()

def printandcount():
    global current_job
    countdown2()
    print_template()
    current_job = None

# def send_email():
#     # Set up the SMTP connection
#     try:
#         smtp = smtplib.SMTP("smtp.gmail.com", 587)  # Replace with your SMTP server and port
#         smtp.starttls()
#         smtp.login("itoperationcentre247@gmail.com","muxzrtysritzoiit")  # Replace with your email and password
#     except smtplib.SMTPException as e:
#         messagebox.showerror("Error", f"Failed to establish SMTP connection: {e}")
#         return
#
#     # Create the email message
#     recipient = "it-operations-centre-email@bigasia.pagerduty.com"  # Replace with the recipient's email address
#     subject = "Please prepare a updated comms for " + clik_id.get()
#     message = name.get()
#
#     email_message = f"Subject: {subject}\n\n{message}"
#
#     # Send the email
#     try:
#         smtp.sendmail("itoperationcentre247@gmail.com", recipient, email_message)  # Replace with your email
#         messagebox.showinfo("Success", "Email sent successfully!")
#     except smtplib.SMTPException as e:
#         messagebox.showerror("Error", f"Failed to send email: {e}")
#
#     # Close the SMTP connection
#     smtp.quit()


#Monitor memory usage
def update_memory_usage():
    pid = psutil.Process().pid
    process = psutil.Process(pid)
    memory_info = process.memory_info()
    memory_usage = memory_info.rss
    memory_usage_readable = psutil._common.bytes2human(memory_usage)
    update_memory_usage_label = Label(right_frame, text="Memory usage: {memory_usage_readable} ", font=("Ariel", 10, "bold"))
    update_memory_usage_label.grid(row=16, column=0, columnspan=2, sticky="e", pady=(20,0))
    update_memory_usage_label.config(text=f"Memory usage: {memory_usage_readable} ")
    update_memory_usage_label.after(60000, update_memory_usage)

update_memory_usage()

load_and_update_config('config.json')
mainloop()