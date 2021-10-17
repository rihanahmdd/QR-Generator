import pyqrcode
from pyqrcode import QRCode
import png
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image


############################### Starting Funcationlaity ####################################

# QR Generator Funcation 
def qr_func(qr_name, qr_text):
    filename = f"{qr_name}.png"
    url = pyqrcode.create(qr_text)
    url.png(filename, scale=8)
    image = Image.open(filename)
    image_size = (290,290)
    image.thumbnail(image_size)
    image.save(filename)

 
# Checking Existness 
if os.path.exists("QR Code's"):
    os.chdir("QR Code's")
    qr_func("DefaultQR", "Thanks for using QR Generator ")
else:
    os.mkdir("QR Code's")
    os.chdir("QR Code's")
    qr_func("DefaultQR", "Thanks for using QR Generator ")


filename = "DefaultQR.png"


##################################### GUI ############################################
win = tk.Tk()
win.geometry("380x480")
win.title("QR Generator")

# Labels
space_lbl1 = ttk.Label(win, width=6)
space_lbl1.pack()

inp_lbl = ttk.Label(win, text="Enter Text\\Link", font=('Cambria', 12)) 
inp_lbl.pack(pady=10)

# Entry boxes 
QR_data = ttk.Entry(win, width=45)
QR_data.focus_set()
QR_data.pack(pady=2)

# Button frame
btn_frame = tk.Frame(win)
btn_frame.pack(pady=5)

paste_btn = ttk.Button(btn_frame, text="Paste")
paste_btn.grid(row=0, column=0, padx=5)

open_btn = ttk.Button(btn_frame, text="Open Text")
open_btn.grid(row=0, column=1) 

# Qr 
default_qr_icon = tk.PhotoImage(file=filename)
qr_lbl = ttk.Label(win, image=default_qr_icon)
qr_lbl.pack(pady=5)

# Buttons 
btn_frame2 = tk.Frame(win)
btn_frame2.pack(side=tk.BOTTOM, pady=12)

exit_btn = ttk.Button(btn_frame2, text="Exit")
exit_btn.grid(row=0, column=0)

generate_btn = ttk.Button(btn_frame2, text="Generate")
generate_btn.grid(row=0, column=1, padx=5)

save_btn = ttk.Button(btn_frame2, text="Save")
save_btn.grid(row=0, column=2)



####################################### Buttons Funcationlaity ###########################

# Paste Button
def paste():
    try:
        data = win.clipboard_get().strip()
        QR_data.delete(0, tk.END)
        QR_data.insert(0, data)
    except tk.TclError:
        messagebox.showerror("Can Not Paste", "Empty Clipboard, Nothing in Clipboard")


# Open Button 
def open_text():
    text_file = filedialog.askopenfilename(
        initialdir=os.getcwd(), title="Select file", filetypes=(('Text file', '*.txt'), ('', '*.txt')))
    try:
        with open(text_file, 'r') as rf:
            QR_data.delete(0, tk.END)
            QR_data.insert(0, rf.read())
    except FileNotFoundError:
        pass


# Exit Button 
def exit_qr():
    result= messagebox.askyesno('Exit', "Do You Want To Exit ??")
    if result== True:
        win.destroy()
    else:
        pass


# Generate Button 
def qr_generator():
    qr_text = QR_data.get().strip()
    if qr_text=="":
        messagebox.showerror("QR Generation Failed", "Empty box, No Link\\Text Found")
    else:
        try:
            qr_func("DefaultQR", qr_text)
            default_qr_icon.config(file="DefaultQR.png")
            messagebox.showinfo("Generated", "QR Code Generated Successfully")
            QR_data.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Failed", "Generation Failed, Too Much Data")


# Save Button 
def save_qr():
    image = Image.open(filename)
    save_path = filedialog.asksaveasfile(
        initialdir="QR Code's", defaultextension=".png",
        filetypes=(('PNG File', '*.png'), ('All files', '*.*')), title='Save'
        )
    try:
        image.save(f"{save_path.name}")
    except AttributeError:
        pass


# Binding Keys
paste_btn.config(command=paste)
open_btn.config(command=open_text)
exit_btn.config(command=exit_qr) 
generate_btn.config(command=qr_generator)
save_btn.config(command=save_qr)




win.mainloop()



# Created and Programmed by Rihan Ahmed
