import time

class Character:
    def __init__(self, name, beauty, charm, intelligence):
        self.name = name
        self.beauty = beauty
        self.charm = charm
        self.intelligence = intelligence

    def talk(self):
        print(f"{self.name}: 你好，我叫{self.name}，很高兴认识你。")

class Player(Character):
    def __init__(self, name):
        super().__init__(name, beauty=10, charm=10, intelligence=10)
        self.level = 1

    def level_up(self):
        self.level += 1
        self.beauty += 5
        self.charm += 5
        self.intelligence += 5

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    player_name = input("请输入你的名字：")
    player = Player(player_name)

    delay_print(f"欢迎来到美女养成游戏，{player_name}！")
    delay_print("在这个游戏中，你将与不同的角色互动，发展自己的魅力。")

    npc = Character("小美女", beauty=8, charm=7, intelligence=9)

    delay_print("你遇到了一个小美女，你想要与她聊点什么？")
    player.talk()
    npc.talk()

    delay_print("你与小美女聊得很开心，她似乎对你有好感。")
    player.level_up()
    delay_print("你的魅力提升了！")

    delay_print("游戏结束，谢谢参与！")

if __name__ == "__main__":
    main()
