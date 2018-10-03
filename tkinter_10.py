import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    # tk.messagebox.showinfo(title='hi', message='hahahhaha')   #return ok
    # tk.messagebox.showwarning(title='Hi', message='noooooooo')   #return ok
    # tk.messagebox.showerror(title='hi', message='No, never')     #return ok
    # print(tk.messagebox.askquestion(title='Hi', message='hahhahh')) #return yes, no
    # print(tk.messagebox.askyesno(title='Hi', message='hahhahh'))  # return True, False
    # print(tk.messagebox.asktrycancel(title='Hi', message='hahhahh'))  # return True, False
    # print(tk.messagebox.askokcancel(title='Hi', message='hahahaha'))   # return True, False
    print(tk.messagebox.askyesnocancel(title="Hi", message="haha"))  # return, True, False, None


tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()