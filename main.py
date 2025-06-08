import tkinter as tk

window = tk.Tk()
window.geometry("800x800")
window.title("Currency Converter")

def eurose():
    value = entry1.get()
    value = float(value)
    label_show.configure(text = f"${value} in Euros is €{value * 0.88}")

def Ruble():
    value = entry1.get()
    value = float(value)
    label_show.configure(text=f"${value} in Ruble is ₽{value * 78,85}")

def yen():
    value = entry1.get()
    value = float(value)
    label_show.configure(text=f"${value} in Yen is ¥{value * 144,85}")

def pound():
    value = entry1.get()
    value = float(value)
    label_show.configure(text=f"${value} in Pound is £{value * 0,74}")

def australian():
    value = entry1.get()
    value = float(value)
    label_show.configure(text=f"${value} in Australian is A${value * 1,54}")

def canadian():
    value = entry1.get()
    value = float(value)
    label_show.configure(text=f"${value} in Canadian is CAN${value * 1,37}")

def swiss():
    value = entry1.get()
    value = float(value)
    label_show.configure(text=f"${value} in Swiss is ₣{value * 0,82}")

def Korean():
    value = entry1.get()
    value = float(value)
    label_show.configure(text=f"${value} in Korean is ₩{value * 1.359,18}")



label_title = tk.Label(text = "Currency Converter", font = ("Comic Sans MS", 20))
label_title.place(relx = 0.5, rely = 0.1, anchor  = "center")

label_enter = tk.Label(text = "Enter an amount of money in dollars", font = ("Comic Sans MS", 20))
label_enter.place(relx = 0.5, rely = 0.5, anchor = "center")

entry1 = tk.Entry(font = ("Comic Sans MS", 20))
entry1.place(relx = 0.5, rely = 0.55, anchor = "center")

button_eurose = tk.Button(text = "€", font = ("Comic Sans MS", 20), command = eurose)
button_eurose.place(relx = 0.7, rely = 0.2, anchor = "center")

button_Ruble = tk.Button(text = "₽", font = ("Comic Sans MS", 20), command = Ruble)
button_Ruble.place(relx = 0.7, rely = 0.3, anchor = "center")

button_yen = tk.Button(text = "¥", font = ("Comic Sans MS", 20), command = yen)
button_yen.place(relx = 0.7, rely = 0.4, anchor = "center")

button_pound = tk.Button(text = "£", font = ("Comic Sans MS", 20), command = pound)
button_pound.place(relx = 0.7, rely = 0.5, anchor = "center")

button_australianDollars = tk.Button(text = "A$", font = ("Comic Sans MS", 20), command = australian)
button_australianDollars.place(relx = 0.7, rely = 0.6, anchor = "center")

button_CanadianDollars = tk.Button(text = "CAN$", font = ("Comic Sans MS", 20), command = canadian)
button_CanadianDollars.place(relx = 0.7, rely = 0.7, anchor = "center")

button_Swiss = tk.Button(text = "₣", font = ("Comic Sans MS", 20), command = swiss)
button_Swiss.place(relx = 0.7, rely = 0.8, anchor = "center")

button_Korean = tk.Button(text = "₩", font = ("Comic Sans MS", 20), command = Korean)
button_Korean.place(relx = 0.7, rely = 0.9, anchor = "center")

label_show = tk.Label(text = "", font = ("Comic Sans MS", 20))
label_show.place(relx = 0.5, rely = 0.7, anchor = "center")




window.mainloop()
