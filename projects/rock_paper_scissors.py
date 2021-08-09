class enemy:
    def __init__(self):
        self.win_count = 0;
        self.lose_count = 0;
        self.type = ["가위","바위","보"]
        self.myhand = 0
    def game_start(self):
        print("가위바위보! (0=가위,1=바위,2=보)")
        enemyhand = random.randint(0,2)
        
        print("나 : {}\n적 : {}".format(self.type[self.myhand],self.type[enemyhand]))
        self.result(self.myhand,enemyhand)
    def result(self,my,enemy):
        if (my==enemy):
            print("무승부!")
        elif(my == enemy+1 or enemy-2 == my):
            print("나의 승리!")
        else:
            print("나의 패배")
    def SetScissors(self):
        self.myhand = 0
    def SetRock(self):
        self.myhand = 1
    def SetPaper(self):
        self.myhand = 2

import tkinter
window = tkinter.Tk()



window.title("가위바위보 게임")
window.geometry("640x400")
window.resizable(False,False)

king = enemy()

button1 = tkinter.Button(window, text= "가위", command=king.SetScissors)
button2 = tkinter.Button(window, text= "바위", command=king.SetRock)
button3 = tkinter.Button(window, text= "보", command=king.SetPaper)
button4 = tkinter.Button(window, text= "내기", command=king.game_start)

button1.pack()
button2.pack()
button3.pack()
button4.pack()
window.mainloop()







