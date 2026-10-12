import tkinter as tk

def count_char():
    text = text_entry.get()
    ch = char_entry.get()
    result.config(text="'" + ch + "' found " + str(text.count(ch)) + " time(s)")

def count_vowels():
    text = text_entry.get().lower()
    n = 0
    i = 0
    # ไล่ดูทีละตัว
    while i < len(text):
        if text[i] in "aeiou":
            n = n + 1
        i = i + 1
    result.config(text="Vowels: " + str(n))

def check_palindrome():
    text = text_entry.get().lower()
    # กลับคำแล้วเทียบกับคำเดิม
    if text == text[::-1]:
        result.config(text="Palindrome")
    else:
        result.config(text="Not palindrome")

window = tk.Tk()
window.title("Text Analyzer")

tk.Label(window, text="Text:").grid(row=0, column=0)
text_entry = tk.Entry(window, width=25)
text_entry.grid(row=0, column=1, columnspan=2)

tk.Label(window, text="Char:").grid(row=1, column=0)
char_entry = tk.Entry(window, width=5)
char_entry.grid(row=1, column=1)

tk.Button(window, text="Count Character", command=count_char).grid(row=2, column=0)
tk.Button(window, text="Count Vowels", command=count_vowels).grid(row=2, column=1)
tk.Button(window, text="Check Palindrome", command=check_palindrome).grid(row=2, column=2)

result = tk.Label(window, text="")
result.grid(row=3, column=0, columnspan=3)

window.mainloop()
