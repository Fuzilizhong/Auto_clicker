import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import pyautogui
import time

class AutoClickerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("鼠标自动点击程序")
        self.root.geometry("400x400")

        # 用于存储位置信息
        self.positions = []

        # 创建 GUI 元素
        self.label = tk.Label(root, text="请输入点击位置数量:")
        self.label.pack(pady=10)

        self.click_count_entry = tk.Entry(root)
        self.click_count_entry.pack()

        self.start_button = tk.Button(root, text="开始设置位置", command=self.setup_positions)
        self.start_button.pack(pady=10)

        self.execute_button = tk.Button(root, text="开始执行点击任务", command=self.execute_clicks, state=tk.DISABLED)
        self.execute_button.pack(pady=10)

        self.status_label = tk.Label(root, text="", fg="green")
        self.status_label.pack(pady=10)

    def setup_positions(self):
        try:
            click_position_counts = int(self.click_count_entry.get())
            if click_position_counts <= 0:
                messagebox.showerror("错误", "请输入一个大于0的整数！")
                return
        except ValueError:
            messagebox.showerror("错误", "输入无效，请输入一个整数！")
            return

        self.positions = []
        for i in range(click_position_counts):
            position_info = self.get_position_info(i + 1)
            if position_info is None:
                messagebox.showerror("错误", "无法获取鼠标位置，程序退出。")
                return
            self.positions.append(position_info)

        self.execute_button.config(state=tk.NORMAL)
        self.status_label.config(text="所有位置信息已设置完成，可以开始执行点击任务。")

    def get_position_info(self, position_index):
    # 提示用户将鼠标移动到指定位置并按下按钮
        messagebox.showinfo("提示", f"请将鼠标移动到第 {position_index} 个位置，然后按下'Enter（回车）'按钮来记录鼠标当前位置。")
        x, y = pyautogui.position()
    
        # 获取点击次数
        click_count = self.get_input(f"请输入在第 {position_index} 个位置点击的次数")
        if click_count is None:
            return None
        
        # 获取点击时间间隔
        interval = self.get_input("请输入与下一次点击的时间间隔（秒），输入0表示同时点击")
        if interval is None:
            return None
    
        return (x, y, click_count, interval)

    def get_input(self, message):
        user_input = simpledialog.askstring("输入", message)
        if user_input is None:
            return None
        try:
            value = float(user_input) if "." in user_input else int(user_input)
            if value < 0:
                messagebox.showerror("错误", "请输入一个大于或等于0的数字！")
                return None
            return value
        except ValueError:
            messagebox.showerror("错误", "输入无效，请输入一个数字！")
            return None

    def execute_clicks(self):
        self.status_label.config(text="正在执行点击任务...")
        for position in self.positions:
            self.click_mouse((position[0], position[1]), position[2], position[3])
        self.status_label.config(text="所有点击任务完成！")

    def click_mouse(self, position, click_count, interval):
        try:
            for i in range(click_count):
                pyautogui.click(x=position[0], y=position[1])
                print(f"已点击位置 {position}，第 {i + 1} 次")
                if interval > 0:
                    time.sleep(interval)
            print(f"位置 {position} 点击结束")
        except Exception as e:
            print(f"点击失败: {e}")
            messagebox.showerror("错误", f"点击失败: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerGUI(root)
    root.mainloop()