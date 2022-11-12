from doctest import master
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os


def conv_vp8(name, output):
    command = "ffmpeg -i {} -c:v libvpx -b:v 2M {}.webm".format(name, output)
    os.system(command)


def conv_vp9(name, output):
    command = "ffmpeg -i {} -c:v libvpx-vp9 -b:v 2M {}.webm ".format(name, output)
    os.system(command)


def conv_h265(name, output):
    command = "ffmpeg -i {} -c:v libx265 -b:v 2M {}.mp4".format(name, output)
    os.system(command)


def conv_av1(name, output):
    command = "ffmpeg -i {} -c:v libaom-av1 -b:v 2M {}.mkv".format(name, output)
    os.system(command)


def converter_win(inputtext):
    new = Toplevel(window)
    new.geometry("500x250")
    new.title("My Video Converter to other Codecs")
    # Create a Label in New window
    lbl1 = Label(new, text='What name do you want to give your video?', font=("Arial Bold", 15))
    lbl1.grid(column=0, row=0)
    output_name = Entry(new, width=20)
    output_name.grid(column=0, row=1)
    output_name.focus()

    lbl2 = Label(new, text='Convert the video into one of the following codecs: ', font=("Arial Bold", 15))
    lbl2.grid(column=0, row=2)

    #
    button1 = Button(new, text="VP8", command=lambda: conv_vp8(inputtext, output_name.get()))
    button1.grid(column=0, row=3)
    #
    button2 = Button(new, text="VP9", command=lambda: conv_vp9(inputtext, output_name.get()))
    button2.grid(column=1, row=3)
    #
    button3 = Button(new, text="H.265", command=lambda: conv_h265(inputtext, output_name.get()))
    button3.grid(column=0, row=4)
    #
    button4 = Button(new, text="AV1", command=lambda: conv_av1(inputtext, output_name.get()))
    button4.grid(column=1, row=4)


def conv_720p(win, name):
    name2 = '720p.mp4'
    command = 'ffmpeg -i {} -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 {}'.format(name, name2)
    os.system(command)
    converter_win(name2)
    win.destroy()


def conv_480p(win, name):
    name2 = '480p.mp4'
    command = 'ffmpeg -i {} -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 {}'.format(name, name2)
    os.system(command)
    converter_win(name2)
    win.destroy()


def conv_360x240(win, name):
    name2 = '360x240.mp4'
    command = 'ffmpeg -i {} -vf scale=360:240 {}'.format(name, name2)
    os.system(command)
    converter_win(name2)
    win.destroy()


def conv_160x120(win, name):
    name2 = '160x120.mp4'
    command = 'ffmpeg -i {} -vf scale=160:120 {}'.format(name, name2)
    os.system(command)
    converter_win(name2)
    win.destroy()


def resize_win(inputtext):
    new = Toplevel(window)
    new.geometry("400x250")
    new.title("My Video Converter to other Codecs")

    # Create a Label in New window
    lbl = Label(new, text='Resize the vide, choose an option: ', font=("Arial Bold", 15))
    lbl.grid(column=0, row=0)
    #
    button1 = Button(new, text="720p", command=lambda: conv_720p(new, inputtext))
    button1.grid(column=0, row=1)
    #
    button2 = Button(new, text="480p", command=lambda: conv_480p(new, inputtext))
    button2.grid(column=1, row=1)
    #
    button3 = Button(new, text="360x240", command=lambda: conv_360x240(new, inputtext))
    button3.grid(column=0, row=2)
    #
    button4 = Button(new, text="160x120", command=lambda: conv_160x120(new, inputtext))
    button4.grid(column=1, row=2)


window = Tk()
window.title("My Video Converter to other Codecs")
lbl = Label(window, text='Please, insert which video you want to convert (with the extension)', font=("Arial Bold", 15))
lbl.grid(column=0, row=0)
window.geometry('500x200')

text = Entry(window, width=20)
text.grid(column=0, row=4)
text.focus()

# botón de convertir
convert_button = Button(window, text="Convert", command=lambda: resize_win(text.get()))
convert_button.grid(column=0, row=5)

# botón para salir del programa
exit_button = Button(window, text="Exit", command=window.quit, fg='red')
exit_button.grid(column=0, row=6)

window.mainloop()
