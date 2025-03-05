from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key
import threading

# 定义鼠标点击事件的回调函数
def on_click(x, y, button, pressed):
    if pressed:
        print(f"鼠标点击位置的坐标为：({x}, {y})")

# 定义键盘事件的回调函数
def on_press(key):
    try:
        # 如果按下的是 ESC 键，则退出程序
        if key == Key.esc:  # ESC 键的 ASCII 码是 '\x1b'
            print("按下 ESC 键，程序退出。")
            return False  # 停止监听
    except AttributeError:
        pass

# 创建鼠标监听器
mouse_listener = MouseListener(on_click=on_click)

# 创建键盘监听器
keyboard_listener = KeyboardListener(on_press=on_press)

# 启动鼠标监听器
mouse_listener.start()

# 启动键盘监听器
keyboard_listener.start()

# 等待键盘监听器停止（即按下 ESC 键）
keyboard_listener.join()

# 停止鼠标监听器
mouse_listener.stop()