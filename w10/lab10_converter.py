import tkinter as tk

def convert():
    try:
        c = float(entry.get())
        f = c * 9 / 5 + 32
        result.config(text=str(f) + " F")
    except ValueError:
        # พิมพ์ไม่ใช่ตัวเลขจะมาตรงนี้
        result.config(text="Please enter a number")

window = tk.Tk()
window.title("C to F")

tk.Label(window, text="Celsius:").grid(row=0, column=0)
entry = tk.Entry(window)
entry.grid(row=0, column=1)

tk.Button(window, text="Convert", command=convert).grid(row=1, column=0, columnspan=2)

result = tk.Label(window, text="")
result.grid(row=2, column=0, columnspan=2)

window.mainloop()
