import tkinter as tk
window = tk.Tk()
window.geometry('200x200')

canvas = tk.Canvas(window, height=150, width=500)
#canvas.grid(row=1, column=1)
#image_file = tk.PhotoImage(file='welcome.gif')
#image = canvas.create_image(0, 0, anchor='nw', image=image_file)

window.mainloop()