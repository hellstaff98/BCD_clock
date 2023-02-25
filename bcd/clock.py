from tkinter import *
from tkinter.ttk import *
from datetime import *

def bin_arr(now):
    arr = now.split(':')
    arr_b = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr_b.append((bin(int(arr[i][j]))[2:][::-1]+'000'))
    print(arr_b)
    return arr_b


def canvas_updating():
    global timeNow_arr, circles
    for item in circles:
        box.delete(item)
    circles = []
    letter = ['H', 'M', 'S']
    for e in range(4):
        circles.append(box.create_text(-10, spacing_y*(-e)+165, text=2**e, font=('Times New Roman', 15), fill='#C0C0C0'))
        circles.append(box.create_text(420, spacing_y*(-e)+165, text=2**e, font=('Times New Roman', 15), fill='#C0C0C0'))
    for s in enumerate(letter):
        circles.append(box.create_text(50 + s[0] * 150, 220, text = letter[s[0]], font=('Times New Roman', 15), fill='#C0C0C0'))
    for i in range(6):
        #if i == 2 or i == 5:
        #    for j in range(4):
        #        circles.append(box.create_oval(i * spacing_x, j * spacing_y, i * spacing_x + size, j * spacing_y + size, outline='white'))

            for j in range(4):
                if i in [0, 2, 4]:
                    if timeNow_arr[i][abs(j-3)] == "1":
                        circles.append(box.create_image(i * spacing_x + 30, j * spacing_y, anchor='nw', image=circ))

                    else:
                        circles.append(
                            box.create_oval(i * spacing_x+ 30, j * spacing_y, i * spacing_x + size+ 30, j * spacing_y + size, outline='#696969', width=2))
                else:
                    if timeNow_arr[i][abs(j-3)] == "1":
                        #circles.append(box.create_oval(i * spacing_x, j * spacing_y, i * spacing_x + size, j * spacing_y + size, fill='red'))
                        circles.append(box.create_image(i * spacing_x, j * spacing_y, anchor='nw', image=circ))

                    else:
                        circles.append(box.create_oval(i * spacing_x, j * spacing_y, i * spacing_x + size, j * spacing_y + size, outline='#696969', width=2))


    #circles = [box.create_oval(i * spacing_x, j * spacing_y, i * spacing_x + size, j * spacing_y + size) for j in range(4) for i in range(6)]
    for item in circles:
        box.move(item, 100, 110)
    print(size * 8 + spacing_x * 7)
    print(box.winfo_reqwidth())

def time_updating():
    global timeNow_arr
    timeNow = datetime.strftime(datetime.now(), '%H:%M:%S')
    print(timeNow)
    timeNow_arr = bin_arr(timeNow)
    timeL['text'] = 'Time : '
    timeL['text'] += str(timeNow)
    win.after(1000, time_updating)
    win.after(1000, canvas_updating)


size = 30
spacing_x = 70
spacing_y = 50

circles= []

win = Tk()
win.geometry('600x500')
win.resizable(False, False)
win.title('BCD-clock')
win['bg'] ='#696969'


backG = PhotoImage(file='cont/back.png')
circ = PhotoImage(file='cont/circ.png')

win.iconphoto(True, circ)

box = Canvas(win, width=600, height=450, bg = 'white')
box.create_image(0, 0, anchor='nw', image=backG)
box.pack()

timeL = Label(win, text='Time:', font=('Times New Roman', 20), background='#696969')
timeL.pack()

time_updating()
canvas_updating()

mainloop()