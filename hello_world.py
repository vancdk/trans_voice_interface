import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.new_recording_button = tk.Button(self)
        self.new_recording_button["text"] = "Nouvel enregistrement"
        self.new_recording_button["command"] = self.start_new_recording
        self.new_recording_button.pack(side="top")

        self.quit = tk.Button(self, text="Quitter", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def start_new_recording(self):
        print("hi! Let's record something!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
