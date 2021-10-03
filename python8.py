from tkinter.filedialog import askopenfilename
import pandas as pd
import tkinter as tk

root = tk.Tk().withdraw()

file_path = askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])

df = pd.read_excel(file_path)
print(df)
