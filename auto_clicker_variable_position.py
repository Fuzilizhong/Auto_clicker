import pyautogui
import time

def click_position_count():
    global click_position_counts
    while True:
        try:
            click_position_counts = int(input("一共要点击的位置数量: "))
            if click_position_counts <= 0:
                print("请输入一个大于0的整数！")
            else:
                break
        except ValueError:
            print("输入无效，请输入一个整数！")

def get_mouse_position():
    try:
        x, y = pyautogui.position()
        print(f"当前鼠标位置：({x}, {y})")
        return x, y
    except Exception as e:
        print(f"获取鼠标位置失败: {e}")
        return None, None

def click_mouse(position, click_count, interval):
    try:
        for i in range(click_count):
            pyautogui.click(x=position[0], y=position[1])
            print(f"已点击位置 {position}，第 {i + 1} 次")
            time.sleep(interval)
        print(f"位置 {position} 点击结束")
    except Exception as e:
        print(f"点击失败: {e}")

def main():
    print("欢迎使用鼠标自动点击程序！")
    click_position_count()  # 获取点击位置数量

    positions = []  # 用于存储每个位置的信息

    for j in range(1, click_position_counts + 1):
        print(f"请将鼠标移动到第 {j} 个位置，然后按下回车键。")
        input("按下回车键继续...")
        x, y = get_mouse_position()
        if x is None or y is None:
            print("无法获取鼠标位置，程序退出。")
            return

        while True:
            try:
                click_count = int(input(f"请输入位置 {j} 的点击次数："))
                if click_count <= 0:
                    print("请输入一个大于0的整数！")
                else:
                    break
            except ValueError:
                print("输入无效，请输入一个整数！")

        while True:
            try:
                interval = float(input(f"请输入位置 {j} 的点击时间间隔（秒）："))
                if interval < 0:
                    print("请输入一个非负数！")
                else:
                    break
            except ValueError:
                print("输入无效，请输入一个数字！")

        positions.append((x, y, click_count, interval))  # 将位置信息保存到列表

    print("所有位置信息已设置完成，开始执行点击任务...")
    for position in positions:
        click_mouse((position[0], position[1]), position[2], position[3])

    print("所有点击任务完成！")

if __name__ == "__main__":
    main()