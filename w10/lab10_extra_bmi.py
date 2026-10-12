import tkinter as tk

def calculate():
    try:
        w = float(weight_entry.get())
        h = float(height_entry.get())
        bmi = w / (h * h)
        result.config(text="BMI = " + str(round(bmi, 2)))
    except ValueError:
        result.config(text="Please enter numbers")
    except ZeroDivisionError:
        # ส่วนสูงเป็น 0 หารไม่ได้
        result.config(text="Height cannot be 0")

window = tk.Tk()
window.title("BMI")

tk.Label(window, text="Weight (kg):").grid(row=0, column=0)
weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1)

tk.Label(window, text="Height (m):").grid(row=1, column=0)
height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1)

tk.Button(window, text="Calculate", command=calculate).grid(row=2, column=0, columnspan=2)

result = tk.Label(window, text="")
result.grid(row=3, column=0, columnspan=2)

window.mainloop()
