import struct
import tkinter as tk
from tkinter import messagebox
import pefile

PATH = "Redfall.exe"
START_RVA = 0xD3F9BB - 9  # start of the 18-byte pattern

PREFIX = bytes.fromhex("8B8128010000894348")
SUFFIX = bytes.fromhex("894348")

def apply():
    mult = round(slider.get(), 2)
    try:
        pe = pefile.PE(PATH, fast_load=True)
        start = pe.get_offset_from_rva(START_RVA)
        pe.close()

        with open(PATH, "r+b") as f:
            f.seek(start)
            data = f.read(18)

            # Pattern check: only the prefix and suffix are verified, so the
            # middle 6 bytes may be the original code or an earlier patch
            if len(data) != 18 or data[:9] != PREFIX or data[15:] != SUFFIX:
                messagebox.showerror("Error", f"Bytes do not match:\n{data.hex(' ').upper()}")
                return

            f.seek(start + 9)
            f.write(b"\xB8" + struct.pack("<f", mult) + b"\x90")  # mov eax, imm32 ; nop

        messagebox.showinfo("Success", "Fix applied successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Redfall ADS Sensitivity Fix")
root.resizable(False, False)

tk.Label(root, text="aim-down-sights sensitivity multiplier (default game value: 0.5)").pack()

slider = tk.Scale(root, from_=0.1, to=1.1, resolution=0.01, width=20, length=400, orient="horizontal")
slider.set(0.7)
slider.pack()

tk.Button(root, text="Apply", command=apply).pack(pady=(0, 4))

root.mainloop()