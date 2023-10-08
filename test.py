import tkinter as tk

window = tk.Tk()

window.columnconfigure(3, weight=1, minsize=75)
window.rowconfigure(1, weight=1, minsize=50)

btn_v1_pressed = False
btn_v2_pressed = False
btn_v3_pressed = False

def btn_v1_handle_left_click(event):
    global btn_v1_pressed
    print("V1 clicked")
    if(btn_v1_pressed):
        btn_v1_pressed = False
        btn_v1.configure(bg="black")
    else:
        btn_v1_pressed = True
        btn_v1.configure(bg="green")
        
def btn_v2_handle_left_click(event):
    global btn_v2_pressed
    print("V2 clicked")
    if(btn_v2_pressed):
        btn_v2_pressed = False
        btn_v2.configure(bg="black")
    else:
        btn_v2_pressed = True
        btn_v2.configure(bg="green")
        
def btn_v3_handle_left_click(event):
    global btn_v3_pressed
    print("V3 clicked")
    if(btn_v3_pressed):
        btn_v3_pressed = False
        btn_v3.configure(bg="black")
    else:
        btn_v3_pressed = True
        btn_v3.configure(bg="green")
    


frame = tk.Frame(
    bg="grey",
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame.grid(row=1, column=3, padx=5, pady=5)

btn_v1 = tk.Button(master=frame, text="Ventil 1", fg="white", bg="black", width=10, height=5)
btn_v1.pack(padx=5, pady=5, side=tk.LEFT)
btn_v1.bind('<Button-1>', btn_v1_handle_left_click)    
btn_v2 = tk.Button(master=frame, text="Ventil 2", fg="white", bg="black", width=10, height=5)
btn_v2.pack(padx=5, pady=5, side=tk.LEFT)
btn_v2.bind('<Button-1>', btn_v2_handle_left_click)    
btn_v3 = tk.Button(master=frame, text="Ventil 3", fg="white", bg="black", width=10, height=5)
btn_v3.pack(padx=5, pady=5, side=tk.LEFT)
btn_v3.bind('<Button-1>', btn_v3_handle_left_click)    
    

    


window.mainloop()

