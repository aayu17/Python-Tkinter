from tkinter import colorchooser
from tkinter import *
from tkinter import font
from tkinter.filedialog import *
import tkinter.messagebox as tmsg
from tkinter import ttk
import tkinter.font
import os.path
import ctypes
import datetime
from tkinter import colorchooser

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title(("TEXT EDITOR"))
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.config(background="Black")
root.geometry(f"{screen_width}x{screen_height}")
# root.geometry("600x600")
p1 = PhotoImage(file="notepad_logo.png")
root.iconphoto(0, p1)

file = None


def n_f(event=""):
    global file
    root.title("Untitled")
    file = None
    text.delete(1.0, END)


def o_f(*args):
    text.delete(1.0, END)
    file = askopenfile(mode='r', title="Open File", filetypes=[
                       ("Text Files", "*.txt"), ("All Files", "*.*"), ('Python Files', '*.py')])
    if file is not None:
        content = file.read()
        text.insert(END, content)
        root.title(os.path.basename(file.name))
        file.close()


def save_as(*args):
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[
                                 ("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            # Save as a new file
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
        # Save the file
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[
                                 ("All Files", "*.*"), ("Text Documents", "*.txt")])
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + " - Notepad")


def cut():
    text.event_generate(("<<Cut>>"))


def copy():
    text.event_generate(("<<Copy>>"))


def paste():
    text.event_generate(("<<Paste>>"))


def undo():
    text.event_generate(("<<Undo>>"))


def delete():
    text.delete(0.0, END)


def selectall():
    text.tag_add('sel', '1.0', 'end')


def t_d():
    current_time = datetime.datetime.now()
    tmsg.showinfo(
        "DATE-TIME", f"THE CUREENT DATE TIME IS \n{current_time}")


def about():
    tmsg.showinfo(
        "ABOUT", "THIS TEXT EDITOR IS CREATED BY AYUSH GUPTA \nFOLLOW ME ON INSTAGRAM @next_coders")


def send_feed():
    tmsg.showinfo(
        "FEEDBACK", "YOU CAN SEND ME FEEDBACK ON \nnext.coders89@gmail.com")


def quit():
    if tmsg.askokcancel("Save Changes", "Do you want to save changes?"):
        save_as()
        root.destroy
    elif tmsg.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


def c_m_s():
    Desired_font = tkinter.font.Font(family="Comic sans Ms",
                                     size=10, weight="normal")
    text.configure(font=Desired_font)


def h_va():
    Desired_font = tkinter.font.Font(family="Helvetica",
                                     size=10, weight="normal")

    text.configure(font=Desired_font)


def courier():
    Desired_font = tkinter.font.Font(family="Courier",
                                     size=10, weight="normal")
    text.configure(font=Desired_font)


def t_n_r():
    Desired_font = tkinter.font.Font(family="Times New Roman",
                                     size=10, weight="normal"
                                     )
    text.configure(font=Desired_font)


def arial():
    Desired_font = tkinter.font.Font(family="Arial",
                                     size=10, weight="normal"
                                     )
    text.configure(font=Desired_font)


def system():
    Desired_font = tkinter.font.Font(family="System",
                                     size=10, weight="normal"
                                     )
    text.configure(font=Desired_font)


def dark():
    text.configure(bg='Black', fg="White")


def light():
    text.configure(bg='White', fg="Black")


def red():
    text.configure(bg='Red', fg="Black")


def yellow():
    text.configure(bg='Yellow', fg="Black")


def blue():
    text.configure(bg='Blue', fg="Black")


def choose_color():

    color_code = colorchooser.askcolor(title="Choose color")
    try:
        text.tag_config("start", foreground=color_code[1])
        text.tag_add("start", "sel.first", "sel.last")
    except:
        return


def normal():

    Desired_font = tkinter.font.Font(weight="normal")
    text.configure(font=Desired_font)


def bold():

    Desired_font = tkinter.font.Font(weight="bold")
    text.configure(font=Desired_font)


def italic():

    Desired_font = tkinter.font.Font(slant="italic")
    text.configure(font=Desired_font)


def underline():

    Desired_font = tkinter.font.Font(underline=1)
    text.configure(font=Desired_font)


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)


text = Text(root, width=600, height=800,
            yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)


scrollbar.config(command=text.yview)


mainmenu = Menu(root, background="Black")
mainmenu.configure(bg='Black', fg="Black")


# -------------------FILE MENU--------------------------------------------------
file = Menu(mainmenu, tearoff=0, bg="Snow", )
file.add_command(label='New', command=n_f, accelerator="Ctrl+N")
file.add_command(label='Open...', command=o_f, accelerator="Ctrl+O")
file.add_command(label='Save As', command=save_as, accelerator="Ctrl+Shift+S")
file.add_separator()
file.add_command(label='Exit', command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=file)


# ------------------EDIT MENU--------------------------------
edit = Menu(mainmenu, tearoff=0, bg="White")
edit.add_command(label='Undo', command=undo, accelerator="Ctrl+Z")
edit.add_command(label='Cut', command=cut, accelerator="Ctrl+X")
edit.add_command(label='Copy', command=copy, accelerator="Ctrl+C")
edit.add_command(label='Paste', command=paste, accelerator="Ctrl+V")
edit.add_command(label='Delete', command=delete, accelerator="Del")
edit.add_separator()  # -------------

edit.add_command(label='Select All', command=selectall, accelerator="Ctrl+A")
edit.add_command(label='Time/Date', command=t_d, accelerator="F5")
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=edit)


# ------------------FONT MENU--------------------------------

font = Menu(mainmenu, tearoff=0, bg="White")
font.add_command(label='System', command=system)
font.add_command(label='Comic Sans Ms', command=c_m_s)
font.add_command(label='Helvetica', command=h_va)
font.add_command(label='Courier', command=courier)
font.add_command(label='Times New Roman', command=t_n_r)
font.add_command(label='Arial', command=arial)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Fonts", menu=font)

# ------------------FONT Style--------------------------------

font_style = Menu(mainmenu, tearoff=0, bg="White")
font_style.add_command(label='Normal', command=normal)
font_style.add_command(label='Bold', command=bold)
font_style.add_command(label='Italic', command=italic)
font_style.add_command(label='Underline', command=underline)


root.config(menu=mainmenu)
mainmenu.add_cascade(label="Text Style", menu=font_style)


# ------------------Theme MENU--------------------------------


theme = Menu(mainmenu, tearoff=0, bg="White")
theme.add_command(label='Dark Theme', command=dark)
theme.add_command(label='Light Theme', command=light)
theme.add_command(label='Red Theme', command=red)
theme.add_command(label='Yellow Theme', command=yellow)
theme.add_command(label='Blue Theme', command=blue)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Theme", menu=theme)

# ------------------Text color--------------------------------
color = Menu(mainmenu, tearoff=0, bg="White")
color.add_command(label='Select Color', command=choose_color)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Text Color", menu=color)

# ------------------HELP MENU--------------------------------

help = Menu(mainmenu, tearoff=0, bg="White")
help.add_command(label='About', command=about)
help.add_command(label='Send Feedback', command=send_feed)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help", menu=help)


n_f()
root.mainloop()
