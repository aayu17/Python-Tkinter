#----BMI CALCULATOR GUI-----
# CREATED BY AYUSH GUPTA
# FOLLOW ME ON INSTAGRAM @next_coders



from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title(("BMI CALCULATOR"))
root.geometry("400x400")

p1 = PhotoImage(file='bmi_logo.png')
root.iconphoto(0, p1)

root.maxsize(800, 600)

root.config(background="Black")

root.resizable(0, 0)  # window size can't me maximize


def click_w(*args):
    weight_entry.delete(0, 'end')


def click_h(*args):
    height_entry.delete(0, 'end')


def toggle_state(*_):
    a = float(weight.get())
    b = float(height.get())
    if a and b:
        b1['state'] = 'normal'
    else:
        b1['state'] = 'disabled'


def get_bmi():
    try:
        choice_height = clicked.get()
        choice_weight = clicked_weight.get()
        a = float(weight.get())
        b = float(height.get())

        bmi = float(a/(b*b))

    except ZeroDivisionError:
        tmsg.showerror("Wrong Input", "Please Input Correct Values")
        return

    if choice_weight == options_weight[0]:  # weight in kilogram

        if choice_height == options[0]:  # height in centimeter
            b = b/100
            bmi = float(a/(b*b))
            bmi = round(bmi, 1)
            if bmi <= 18.5:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE UNDERWEIGHT")
            elif bmi > 18.5 and bmi <= 25.0:
                tmsg.showinfo("BMI", f"Your BMI is {bmi} \nYOU ARE NORMAL")
            else:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE OVERWEIGHT")

        if choice_height == options[1]:  # height in meters
            bmi = float(a/(b*b))
            bmi = round(bmi, 1)
            if bmi <= 18.5:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE UNDERWEIGHT")
            elif bmi > 18.5 and bmi <= 25.0:
                tmsg.showinfo("BMI", f"Your BMI is {bmi} \nYOU ARE NORMAL")
            else:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE OVERWEIGHT")

        if choice_height == options[2]:  # height in feet
            b = b*0.3048
            bmi = float(a/(b*b))
            bmi = round(bmi, 1)
            if bmi <= 18.5:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE UNDERWEIGHT")
            elif bmi > 18.5 and bmi <= 25.0:
                tmsg.showinfo("BMI", f"Your BMI is {bmi} \nYOU ARE NORMAL")
            else:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE OVERWEIGHT")

        if choice_height == options[3]:  # height in inches
            b = b/39.37
            bmi = float(a/(b*b))
            bmi = round(bmi, 1)
            if bmi <= 18.5:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE UNDERWEIGHT")
            elif bmi > 18.5 and bmi <= 25.0:
                tmsg.showinfo("BMI", f"Your BMI is {bmi} \nYOU ARE NORMAL")
            else:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE OVERWEIGHT")

    if choice_weight == options_weight[1]:  # weight in pounds
        a = a*0.453
        if choice_height == options[0]:  # height in centimeters

            b = b/100
            bmi = float(a/(b*b))
            bmi = round(bmi, 1)
            if bmi <= 18.5:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE UNDERWEIGHT")
            elif bmi > 18.5 and bmi <= 25.0:
                tmsg.showinfo("BMI", f"Your BMI is {bmi} \nYOU ARE NORMAL")
            else:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE OVERWEIGHT")

        if choice_height == options[1]:  # height in meters

            bmi = float(a/(b*b))
            bmi = round(bmi, 1)
            if bmi <= 18.5:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE UNDERWEIGHT")
            elif bmi > 18.5 and bmi <= 25.0:
                tmsg.showinfo("BMI", f"Your BMI is {bmi} \nYOU ARE NORMAL")
            else:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE OVERWEIGHT")

        if choice_height == options[2]:  # height im feet

            b = b*0.3048
            bmi = float(a/(b*b))
            bmi = round(bmi, 1)
            if bmi <= 18.5:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE UNDERWEIGHT")
            elif bmi > 18.5 and bmi <= 25.0:
                tmsg.showinfo("BMI", f"Your BMI is {bmi} \nYOU ARE NORMAL")
            else:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE OVERWEIGHT")

        if choice_height == options[3]:  # height in inches

            b = b/39.37
            bmi = float(a/(b*b))
            bmi = round(bmi, 1)
            if bmi <= 18.5:
                tmsg.showinfo(
                    "BMI", f"Your BMI is {bmi} \nYOU ARE UNDERWEIGHT")
            elif bmi > 18.5 and bmi <= 25.0:
                tmsg.showinfo("BMI", f"Your BMI is {bmi} \nYOU ARE NORMAL")
            else:
                tmsg.showinfo("BMI", f"Your BMI is {bmi} \nYOU ARE OVERWEIGHT")


# LABEL FOR HEADING "BMI CALCULATOR"------------------------------------
l1 = Label(root, text="BMI CALCULATOR", bg="Black",
           fg="darkgoldenrod", bd=1, font=("Comic Sans MS", 18, "bold"))
l1.place(x=95, y=4)

# LABEL FOR WEIGHT------------------------------------------------------
l1 = Label(root, text="WEIGHT", bg="Black",
           fg="gold", pady=10, font=("Comic Sans MS", 15))
l1.place(x=13, y=50)


# Dropdown menu options for weight--------------------------------------
options_weight = ["Kilogram", "Pounds"]
# datatype of menu text
clicked_weight = StringVar()
# initial menu text
clicked_weight.set("Kilogram")
# Create Dropdown menu
drop_w = OptionMenu(root, clicked_weight, *options_weight)
drop_w.place(x=110, y=63)
drop_w.config(bg="Black", fg="gold", bd=0, relief=SUNKEN,
              highlightthickness=0, font=("Comic Sans MS", 10))
drop_w["menu"].config(bg="Black", fg="gold")


# ENTRY FOR WEIGHT--------------------------------------------------------
weight = DoubleVar()
weight_entry = Entry(root, textvariable=weight)
weight_entry.bind("<Button-1>", click_w)
weight_entry.place(x=220, y=65)


# LABEL FOR HEIGHT------------------------------------------------------
l2 = Label(root, text="HEIGHT", bd=0, bg="Black",
           fg="gold", pady=10, font=("Comic Sans MS", 15))
l2.place(x=13, y=110)

#  Dropdown menu options for height---------------------------------------
options = ["Centimeters", "Meters", "Feet", "Inches"]
# datatype of menu text
clicked = StringVar()
# initial menu text
clicked.set("Feet")
# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.place(x=110, y=120)
drop.config(bg="Black", fg="gold", bd=0, relief=SUNKEN,
            highlightthickness=0, font=("Comic Sans MS", 10))
drop["menu"].config(bg="Black", fg="gold")


# ENTRY FOR hEIGHT-----------------------------------------------------------
height = DoubleVar()
height_entry = Entry(root, textvariable=height)
height_entry.bind("<Button-1>", click_h)
height_entry.place(x=220, y=130)


# SUBMIT BUTTON--------------------------------------------------------
b1 = Button(text="SUBMIT", command=get_bmi, bg="darkgoldenrod",
            bd=1, font=("comic sans", 10, "bold"))
b1.place(x=160, y=180)


root.mainloop()
