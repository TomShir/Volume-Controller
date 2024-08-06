from tkinter import *
import pyautogui 
font_info=('Arial',18,'bold')
window=Tk()
window.config(background='#075264')
window.geometry('600x600')
decrease_volume_image=PhotoImage(file='decrease.png')
increase_volume_image=PhotoImage(file='increase_volume1.png')
mute_volume_image=PhotoImage(file='smally2.png')
window.title=('Volume controller gui')
def  increase_volume():
    pyautogui.press('volumeup')
    
def decrease_volume():
    pyautogui.press('volumedown')
    
def mute_sound():
    pyautogui.press('volumemute')
    
def create_button(message,function,background1,foreground1,activebackground1,activeforeground1,fonty,compoundy,Image,position):
    button=Button(text=message,command=function,background=background1,foreground=foreground1,font=fonty,compound=compoundy,image=Image,activebackground=activebackground1,activeforeground=activeforeground1)
    button.pack(side=position)
    
#Creating a label for the tkinter gui 
volume_label=Label(text='volume controller'.title(),font=('Arial',18,'bold'),background='black',foreground='blue')
volume_label.pack()
create_button(message='Increase Volume',function=increase_volume,background1='#047cb6',activebackground1='#047cb6',Image=increase_volume_image,fonty=('Arial',18,'bold'),activeforeground1='red',foreground1='red',position='right',compoundy='bottom')
create_button(message='Decrease Volume',function=decrease_volume,background1='#d41212',activebackground1='#d41212',Image=decrease_volume_image,fonty=('Arial',18,'bold'),activeforeground1='#047cb6',foreground1= '#047cb6',position='left',compoundy='bottom')
create_button(message='Mute',function=mute_sound,background1='#191970',activebackground1='#191970',Image=mute_volume_image,fonty=('Arial',18,'bold'),activeforeground1='#73ced0',foreground1='#73ced0',position='left',compoundy='bottom')
window.mainloop()