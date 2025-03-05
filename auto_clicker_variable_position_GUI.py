import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
from pynput import mouse
import threading
import time

class AutoclickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Clicker")
        
        # 存储所有任务行
        self.task_rows = []
        
        # 顶部控制区域
        control_frame = ttk.Frame(root)
        control_frame.pack(pady=5)
        
        self.add_btn = ttk.Button(control_frame, text="+ 添加任务", command=self.add_row)
        self.add_btn.pack(side=tk.LEFT, padx=5)
        
        # 任务列表容器
        self.tasks_frame = ttk.Frame(root)
        self.tasks_frame.pack(pady=5, fill=tk.X)
        
        # 底部按钮
        bottom_frame = ttk.Frame(root)
        bottom_frame.pack(pady=10)
        
        self.run_btn = ttk.Button(bottom_frame, text="开始运行", command=self.start_autoclick)
        self.run_btn.pack(side=tk.LEFT, padx=5)
        
        self.placeholder_btn = ttk.Button(bottom_frame, text="待实现功能")
        self.placeholder_btn.pack(side=tk.LEFT, padx=5)
        
        # 初始添加一行
        self.add_row()
        
        # 鼠标监听控制
        self.mouse_listener = None
        self.current_position_entry = None
    
    def add_row(self):
        row_frame = ttk.Frame(self.tasks_frame)
        row_frame.pack(fill=tk.X, pady=2)
        
        # 位置获取
        pos_frame = ttk.Frame(row_frame)
        pos_frame.pack(side=tk.LEFT, padx=5)
        
        pos_entry = ttk.Entry(pos_frame, width=15)
        pos_entry.pack(side=tk.LEFT)
        
        get_pos_btn = ttk.Button(
            pos_frame,
            text="获取位置",
            command=lambda: self.start_get_position(pos_entry)
        )
        get_pos_btn.pack(side=tk.LEFT, padx=5)
        
        # 点击次数
        times_entry = ttk.Entry(row_frame, width=10)
        times_entry.pack(side=tk.LEFT, padx=5)
        times_entry.insert(0, "1")
        
        # 点击间隔
        interval_entry = ttk.Entry(row_frame, width=10)
        interval_entry.pack(side=tk.LEFT, padx=5)
        interval_entry.insert(0, "1")
        
        # 删除按钮
        remove_btn = ttk.Button(
            row_frame,
            text="-",
            command=lambda: self.remove_row(row_frame)
        )
        remove_btn.pack(side=tk.RIGHT, padx=5)
        
        self.task_rows.append({
            "frame": row_frame,
            "pos_entry": pos_entry,
            "times_entry": times_entry,
            "interval_entry": interval_entry
        })
    
    def remove_row(self, row_frame):
        for task in self.task_rows:
            if task["frame"] == row_frame:
                task["frame"].destroy()
                self.task_rows.remove(task)
                break
    
    def start_get_position(self, entry_widget):
        self.current_position_entry = entry_widget
        self.root.iconify()  # 最小化窗口方便点击
        
        def on_click(x, y, button, pressed):
            if pressed and button == mouse.Button.left:
                entry_widget.delete(0, tk.END)
                entry_widget.insert(0, f"{int(x)},{int(y)}")
                self.mouse_listener.stop()
                self.root.deiconify()  # 恢复窗口
        
        self.mouse_listener = mouse.Listener(on_click=on_click)
        self.mouse_listener.start()
    
    def validate_inputs(self):
        for task in self.task_rows:
            try:
                x, y = map(int, task["pos_entry"].get().split(','))
                times = int(task["times_entry"].get())
                interval = float(task["interval_entry"].get())
                if times < 1 or interval < 0:
                    raise ValueError
            except:
                messagebox.showerror("输入错误", "请检查输入的有效性")
                return False
        return True
    
    def start_autoclick(self):
        if not self.validate_inputs():
            return
        
        def autoclick_thread():
            for task in self.task_rows:
                try:
                    x, y = map(int, task["pos_entry"].get().split(','))
                    times = int(task["times_entry"].get())
                    interval = float(task["interval_entry"].get())
                except:
                    continue
                
                for _ in range(times):
                    if self.stop_flag:
                        return
                    pyautogui.click(x, y)
                    time.sleep(interval)
        
        self.stop_flag = False
        self.run_btn.config(text="停止运行", command=self.stop_autoclick)
        self.thread = threading.Thread(target=autoclick_thread)
        self.thread.start()
    
    def stop_autoclick(self):
        self.stop_flag = True
        self.run_btn.config(text="开始运行", command=self.start_autoclick)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoclickerApp(root)
    root.mainloop()