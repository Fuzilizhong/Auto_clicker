# 按照点击顺序，依次输入固定坐标、点击次数、间隔时间，静态位置点击
import pyautogui
import time
import threading



def click_mouse(position, click_count, interval):      #定义鼠标点击的位置、次数、间隔时间
    try:
        for i in range(click_count):
            pyautogui.click(x=position[0], y=position[1])
            print(f"已点击位置 {position}，第 {i + 1} 次")
            time.sleep(interval)
        print(f"位置 {position} 点击结束")
    except Exception as e:
        print(f"点击失败: {e}")

def main():           
    click_list = [                      #设置鼠标点击的位置、次数、间隔时间
        ((404, 432), 1, 0,),
        ((404, 432), 1, 0,),
        ((415, 469), 1, 0,),
        ((415, 469), 1, 0,),
    ]

    time.sleep(10)
    # 执行鼠标点击
    print("开始执行点击任务...")
    for (x, y), click_count, interval in click_list:
        click_mouse((x, y), click_count, interval)
    print("所有点击任务完成！")

if __name__ == "__main__":
    main()