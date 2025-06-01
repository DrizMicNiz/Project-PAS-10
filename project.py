import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb

conversion_factors = {
    "Jarak": {
        "km": 1_000,
        "hm": 100,
        "dam": 10,
        "m": 1,
        "dm": 0.1,
        "cm": 0.01,
        "mm": 0.001
    },
    "Volume": {
        "kl": 1_000,
        "hl": 100,
        "dal": 10,
        "l": 1,
        "dl": 0.1,
        "cl": 0.01,
        "ml": 0.001
    },
    "Massa": {
        "kg": 1_000,
        "hg": 100,
        "dag": 10,
        "g": 1,
        "dg": 0.1,
        "cg": 0.01,
        "mg": 0.001
    }
}

def update_units(event=None):
    category = combo_category.get()
    units = list(conversion_factors[category].keys())
    combo_unit_from['values'] = units
    combo_unit_to['values'] = units
    combo_unit_from.set(units[0])
    combo_unit_to.set(units[1])

def convert():
    try:
        category = combo_category.get()
        value = float(entry_value.get())
        unit_from = combo_unit_from.get()
        unit_to = combo_unit_to.get()
        if unit_from not in conversion_factors[category] or unit_to not in conversion_factors[category]:
            messagebox.showerror("Error", "Satuan tidak dikenali!")
            return
        value_in_base = value * conversion_factors[category][unit_from]
        result = value_in_base / conversion_factors[category][unit_to]
        messagebox.showinfo("Hasil Konversi", f"Hasil konversi: {result} {unit_to}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

root = tb.Window(themename="morph")
root.title("Konversi Satuan")
root.geometry("400x320")

label_category = ttk.Label(root, text="Pilih kategori:")
label_category.pack(pady=5)
combo_category = ttk.Combobox(root, values=["Jarak", "Volume", "Massa"], state="readonly")
combo_category.pack(pady=5)
combo_category.bind("<<ComboboxSelected>>", update_units)
combo_category.set("Jarak")

label_value = ttk.Label(root, text="Masukkan nilai:")
label_value.pack(pady=5)
entry_value = ttk.Entry(root)
entry_value.pack(pady=5)

label_unit_from = ttk.Label(root, text="Dari satuan:")
label_unit_from.pack(pady=5)
combo_unit_from = ttk.Combobox(root, state="readonly")
combo_unit_from.pack(pady=5)

label_unit_to = ttk.Label(root, text="Ke satuan:")
label_unit_to.pack(pady=5)
combo_unit_to = ttk.Combobox(root, state="readonly")
combo_unit_to.pack(pady=5)

btn_convert = ttk.Button(root, text="Konversi", command=convert)
btn_convert.pack(pady=10)

update_units()

root.mainloop()