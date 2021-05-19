import tkinter as tk
import threading
import pyaudio
import wave

# --- functions ---

class Application(tk.Frame):
    chunk = 1024 
    sample_format = pyaudio.paInt16 
    channels = 2
    fs = 44100  
    
    frames = []  
    def __init__(self, master=None):
        super().__init__(master)
        self.isrecording = False
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.record_button = tk.Button(main, text='Enregistrer avec l\'audio de l\'ordinateur', fg="blue", command=self.startrecording)
        self.stop_button = tk.Button(main, text='Arrêter l\'enregistrement,command=self.stoprecording)
        self.quit = tk.Button(self, text="Quitter", fg="red", command=self.master.destroy)
        
        self.record_button.pack(side="top")
        self.quit.pack()


    def startrecording(self):
        self.p = pyaudio.PyAudio()  
        self.stream = self.p.open(format=self.sample_format,channels=self.channels,rate=self.fs,frames_per_buffer=self.chunk,input=True)
        self.isrecording = True
        self.stop_button.pack()

        print('Recording')

        t = threading.Thread(target=self.record)
        t.start()

    def stoprecording(self):
        self.isrecording = False
        self.stop_button.pack_forget()
        print('recording complete')

        self.filename=input('the filename?')
        self.filename = self.filename+".wav"
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def record(self):
        while self.isrecording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)


main = tk.Tk()
main.title('Trans voice recorder')
main.geometry('1000x500')

app = Application(main)
main.mainloop()

