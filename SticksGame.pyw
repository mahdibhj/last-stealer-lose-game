import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage
import time

root = tk.Tk()

HEIGHT=500
WIDTH=700
batons_nb=30
Mahdi_Score=0
My_Score=0


def display_images(x,y):

    image1 = Image.open("baton.png")
    image1 = image1.resize((60, 50), Image.ANTIALIAS)
    sticker_img= PhotoImage(image1)
    sticker_label=tk.Label(image=sticker_img)
    sticker_label.image = sticker_img
    sticker_label.place(relx=x, rely=y,relwidth=1, relheight=1)






def hide_frame1_show_frame2(frame2, button1, button2, button_restart):
    button1.place_forget()
    button2.place_forget()
    frame2.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')
    label['text']='30'
    button3.place(relx=0, rely=0,relwidth=0.45, relheight=1)
    button4.place(relx=0.55, rely=0,relwidth=0.45, relheight=1)
    label_score['text']='Mahdi: '+str(Mahdi_Score)+'   Me: '+str(My_Score)
    label_last_act.place(relx=0.2, rely=0.8,relwidth=0.5, relheight=0.1)



def mahdi_jeu (batons):
    if batons in(2,5,8,11,14,17,20,23,26,29) :
        retire_ordinateur = 1
    elif batons in(3,6,9,12,15,18,21,24,27,30) :
        retire_ordinateur = 2
    elif batons in(16,22,28) :
        retire_ordinateur = 2
    elif batons in(1,4,7,10,13,19,25) :
        retire_ordinateur = 1
    batons=batons-retire_ordinateur
    return retire_ordinateur

def opponent_jeu (batons, retire):
    global batons_nb
    global My_Score
    batons = batons - retire
    label['text']=str(batons)
    if (batons<=0):
        label_wl['text']='Sorry you lose'
        global Mahdi_Score
        Mahdi_Score+=1
        label_score['text']='Mahdi: '+str(Mahdi_Score)+'   Me: '+str(My_Score)
        button3.place_forget()
        button4.place_forget()
        button_restart.place(relx=0.3, rely=0,relwidth=0.4, relheight=1)
        batons=0
    else:
        retire_mahdi = mahdi_jeu(batons)
        batons=batons-retire_mahdi
        label_last_act['text']='Mahdi withdraw: '+ str(retire_mahdi)
        print("Mahdi retire ",retire_mahdi," allumettes")
        if (batons<=0):
            label_wl['text']='Congratulations! you Won'
            button3.place_forget()
            button4.place_forget()
            My_Score+=1
            label_score['text']='Mahdi: '+str(Mahdi_Score)+'   Me: '+str(My_Score)
            button_restart.place(relx=0.3, rely=0,relwidth=0.4, relheight=1)
            batons=0

    batons_nb =batons
    label['text']=str(batons)


def restart_game():
    global batons_nb
    batons_nb =30
    label_wl['text']=''
    label['text']=str(batons_nb)
    button1.place(relx=0, rely=0,relwidth=0.45, relheight=1)
    button2.place(relx=0.55, rely=0,relwidth=0.45, relheight=1)
    button_restart.place_forget()
    label_last_act.place_forget()
    button3.place_forget()
    button4.place_forget()




canvas=tk.Canvas(root,bg='#99ceff', height=HEIGHT , width=WIDTH )
canvas.pack()

frame2=tk.Frame(root, bg='#99ceff',bd=5)
#frame2.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')

button3 = tk.Button(frame2, text="withdraw 1", bg="gray", font=40 , command=lambda:opponent_jeu(batons_nb, retire=1))
button3.place(relx=0, rely=0,relwidth=0.45, relheight=1)

button4 = tk.Button(frame2, text="withdraw 2", bg="gray", font=40, command=lambda:opponent_jeu(batons_nb, retire=2))
button4.place(relx=0.55, rely=0,relwidth=0.45, relheight=1)

frame=tk.Frame(root, bg='#99ceff',bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

button1 = tk.Button(frame, text="Play First", bg="gray", font=40, command=lambda: hide_frame1_show_frame2(frame2, button1, button2, button_restart))
button1.place(relx=0, rely=0,relwidth=0.45, relheight=1)

button2 = tk.Button(frame, text="Play Second", bg="gray", font=40, command=lambda: hide_frame1_show_frame2(frame2, button1, button2, button_restart))
button2.place(relx=0.55, rely=0,relwidth=0.45, relheight=1)

button_restart = tk.Button(frame, text="Restart", bg="gray", font=40 ,command=lambda:restart_game())
#button_restart.place(relx=0.6, rely=0,relwidth=0.4, relheight=1)

label = tk.Label(root ,font=('modern',50), bg='#99ceff', justify='left')
label.place(relx=0.2, rely=0.4,relwidth=0.4, relheight=0.3)

label_wl = tk.Label(root, font=('modern',20), bg='#99ceff', justify='left')
label_wl.place(relx=0.2, rely=0.3,relwidth=0.5, relheight=0.1)

label_last_act = tk.Label(root ,font=('modern',20), bg='#99ceff', justify='left')
label_last_act.place(relx=0.2, rely=0.8,relwidth=0.5, relheight=0.1)

label_score = tk.Label(root ,font=('modern',20), bg='yellow', justify='left')
label_score.place(relx=0, rely=0,relwidth=0.3, relheight=0.07)







#sticker_label= tk.Label(root, image=sticker_img)
#sticker_label.place(x=0, y=0)



"""
def show_stickers(batons):
    stickers_window=tk.Label(root)

    image1 = Image.open("baton.png")
    image1 = image1.resize((60, 50), Image.ANTIALIAS)
    sticker_img= PhotoImage(image1)

    sticker_label= tk.Label(stickers_window, image=sticker_img)
    for x in range (1,batons):
        x_baton=5+50*x
        y_baton=5
        if (x%6==0):
            y_baton=y_baton+50
        sticker_label.place(x=x_baton, y=y_baton)
    return stickers_window.pack()


show_stickers(15)

"""
"""

who_starts=eval(input("If you want to start the game chose 1 else chose 2 (1 ou 2) :"))
batons = 30
if (who_starts ==2):
    print("Mahdi retire 2 allumettes")
    batons=batons-2

def mahdi_jeu (batons):
    if batons in(2,5,8,11,14,17,20,23,26,29) :
        retire_ordinateur = 1
    elif batons in(3,6,9,12,15,18,21,24,27,30) :
        retire_ordinateur = 2
    elif batons in(16,22,28) :
        retire_ordinateur = 2
    elif batons in(1,4,7,10,13,19,25) :
        retire_ordinateur = 1
    batons=batons-retire_ordinateur
    return retire_ordinateur
while (batons > 0):
    print("Il reste: ",batons," allumettes")
    retire = eval(input("combien d'allumettes voulez vous retirer parmi ? (1 ou 2) :"))
    if (retire in (1,2))  :
        batons = batons - retire
        if (batons<=0):
            print("Sorry, You Lose")
        else:
            retire_mahdi = mahdi_jeu(batons)
            batons=batons-retire_mahdi
            print("Mahdi retire ",retire_mahdi," allumettes")

"""


root.mainloop()
