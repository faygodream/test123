
from tkinter import *



from datetime import datetime

temp = 0
after_id= ''

def tick():
    global temp, after_id, f_temp
    after_id = root.after(1000,tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S") #форматирование вида минут и секунд
    label1.configure(text=str(f_temp))
    temp += 1
    
def Resultticking():
        label2 = Label(root, width= 10,font =  ('Comic Sanc MS',30), text = f_temp)
        label2.pack()

def start_tick():
    btnStart.pack_forget() #кнопка скрывается
    btnStop.pack() #кнопка Стоп появляется
    btnResult.pack()
    tick()

def stop_tick():
    btnStop.pack_forget() #кнопка скрывается
    btnResult.pack_forget()
    btnContinue.pack()
    btnReset.pack()
    root.after_cancel(after_id)  #Остановка секундомера

def continue_tick():
    btnContinue.pack_forget() #кнопка скрывается
    btnReset.pack_forget() #кнопка скрывается
    btnResult.pack()
    btnStop.pack()
    tick()


def reset_tick():
    global temp
    temp = 0
    label1.configure(text='00:00')
    btnContinue.pack_forget() #кнопка скрывается
    btnResult.pack_forget()
    btnReset.pack_forget() #кнопка скрывается
    btnStart.pack()


#def Result():
    #Canvas.addtag(ftemp)
    #label2.pack()

root = Tk()
root.title('Секундомер')
root.resizable(width=False,height=False)
root.geometry('300x300')

label1 = Label(root, width= 10,font =  ('Comic Sanc MS',30), text = '00:00' )
label1.pack()

btnStart = Button(root, text = 'Старт',font =  ('Comic Sanc MS',20), width = 15, command = start_tick )
btnStop = Button(root, text = 'Стоп',font =  ('Comic Sanc MS',20), width = 15, command = stop_tick )
btnContinue = Button(root, text = 'Продолжить',font =  ('Comic Sanc MS',20), width = 15, command = continue_tick )
btnReset = Button(root, text = 'Сброс',font =  ('Comic Sanc MS',20), width = 15, command = reset_tick )
btnResult = Button(root, text = 'Результат',font =  ('Comic Sanc MS',20), width = 15, command = Resultticking)


btnStart.pack()


root.mainloop()