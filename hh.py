import tkinter as tk

def klik(tombol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(tombol))

def hapus():
    entry.delete(0, tk.END)

def hitung():
    try:
        hasil = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(hasil))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

#window utama
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("300x400")

#input 
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
entry.pack(fill="x", padx=10, pady=10)

#tombol
tombol =  [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
    '='
]
frame = tk.Frame(root)
frame.pack()

row = 0
col = 0
for t in tombol:
    if t == '=':
        btn = tk.Button(frame, text=t, width=32, height=3, command=hitung)
        btn.grid(row=row, column=col, columnspan=4)
    elif t == 'C':
        btn = tk.Button(frame, text=t, width=8, height=3, command=hapus)
        btn.grid(row=row, column=col)
    else:
        btn = tk.Button(frame, text=t, width=8, height=3, command=lambda x=t: klik(x))
        btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='clear', command=hapus).pack(fill="x", padx=10, pady=5)
root.mainloop()

