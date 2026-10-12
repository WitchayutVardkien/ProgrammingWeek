import tkinter as tk

count = 0

def increase():
    global count
    count = count + 1
    label.config(text=count)

def decrease():
    global count
    count = count - 1
    label.config(text=count)

def reset():
    global count
    count = 0
    label.config(text=count)

window = tk.Tk()
window.title("Counter App")

# ตัวเลขตรงกลาง
label = tk.Label(window, text=count, font=("Arial", 40))
label.pack()

# ปุ่มทั้ง 3 อัน
tk.Button(window, text="Increase", width=10, command=increase).pack()
tk.Button(window, text="Decrease", width=10, command=decrease).pack()
tk.Button(window, text="Reset", width=10, command=reset).pack()

window.mainloop()
