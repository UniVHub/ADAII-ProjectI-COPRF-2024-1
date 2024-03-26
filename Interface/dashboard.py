import sys
import os

# Añadir al path el directorio actual
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from config import *
from layout import Layout


class Dashboard:
    def __init__(self, logica):
        self.root = ctk.CTk()
        self.root.title("Proyecto I - ADA II - 2024")
        self.root.geometry("856x645")
        self.root.resizable(0, 0)

        self.logica = logica

        self.layout = Layout(self.root, self.logica)

        self.root.mainloop()
