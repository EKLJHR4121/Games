import random
import time

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def cultivate():
    return random.randint(5, 15)

def meditate():
    return random.randint(10, 20)

def fight():
    return random.randint(0, 10)

def play_game():
    delay_print("欢迎来到修仙游戏！")
    delay_print("在这个游戏中，你将进行二十回合的修炼。")
    delay_print("每回合你可以选择不同的修炼方式，增加你的修为。")

    cultivation = 0
    for i in range(1, 21):
        delay_print(f"\n第 {i} 回合开始：")
        delay_print("请选择修炼方式：")
        delay_print("1. 修炼功法（增加 5-15 修为）")
        delay_print("2. 冥想修行（增加 10-20 修为）")
        delay_print("3. 闯荡江湖（增加 0-10 修为）")

        choice = int(input("请输入你的选择（1/2/3）："))

        if choice == 1:
            cultivation += cultivate()
            delay_print(f"你选择了修炼功法，增加了 {cultivate()} 修为。")
        elif choice == 2:
            cultivation += meditate()
            delay_print(f"你选择了冥想修行，增加了 {meditate()} 修为。")
        elif choice == 3:
            cultivation += fight()
            delay_print(f"你选择了闯荡江湖，增加了 {fight()} 修为。")
        else:
            delay_print("无效的选择，本回合未进行修炼。")
        
        delay_print(f"当前修为：{cultivation}")
    
    delay_print("\n游戏结束！你的二十回合修仙之旅结束了。")
    delay_print(f"最终修为：{cultivation}")

if __name__ == "__main__":
    play_game()
