import tkinter as tk

window = tk.Tk()

window.columnconfigure(3, weight=1, minsize=75)
window.rowconfigure(1, weight=1, minsize=50)


frame = tk.Frame(
    bg="grey",
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame.grid(row=1, column=3, padx=5, pady=5)

btn_v1 = tk.Button(master=frame, text=f"Ventil 1", fg="white", bg="black", width=10, height=5).pack(padx=5, pady=5, side=tk.LEFT)
btn_v2 = tk.Button(master=frame, text=f"Ventil 2", fg="white", bg="black", width=10, height=5).pack(padx=5, pady=5, side=tk.LEFT)
btn_v3 = tk.Button(master=frame, text=f"Ventil 3", fg="white", bg="black", width=10, height=5).pack(padx=5, pady=5, side=tk.LEFT)
    
def btn_v1_handle_left_click(event):
    print("V1 clicked")

def btn_v2_handle_left_click(event):
    print("V2 clicked")

def btn_v3_handle_left_click(event):
    print("V3 clicked")

btn_v1.bind("<Button-1>", btn_v1_handle_left_click)    
btn_v2.bind("<Button-1>", btn_v2_handle_left_click)    
btn_v3.bind("<Button-1>", btn_v3_handle_left_click)    
    


window.mainloop()

