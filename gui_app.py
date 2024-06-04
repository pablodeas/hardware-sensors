import tkinter as tk
from core import get_stats

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hardware Sensors")
        self.geometry("200x100")

        self.label = tk.Label(self, text=get_stats(), font=("Helvetica", 12))
        self.label.pack(pady=15, padx=15)

        self.update_label()

    def update_label(self):
        self.label.config(text=get_stats())
        self.after(3000, self.update_label)  # Atualiza a cada 3 segundos

if __name__ == "__main__":
    app = App()
    app.mainloop()
