# ---------------------------------------------------------------------------- #
#                                 IMPORTACIONES                                #
# ---------------------------------------------------------------------------- #
from PIL import Image
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import tkinter as tk
import os
import time
import threading

# ---------------------------------------------------------------------------- #
#                                     RUTAS                                    #
# ---------------------------------------------------------------------------- #
carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "images")

# ---------------------------------------------------------------------------- #
#                           CONFIGURACIONES DE COLOR                           #
# ---------------------------------------------------------------------------- #
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
modo_color = ctk.get_appearance_mode()
color_verde = "#2A8C55"
color_verde_hover = "#216e43"
color_blanco = "#FFFFFF"
color_negro = "#000000"

# ---------------------------------------------------------------------------- #
#                                    FUENTES                                   #
# ---------------------------------------------------------------------------- #
fuente_titulo = ("Ralway", 25, tk.font.BOLD)
fuente_integrantes_titulo = ("Ralway", 18, tk.font.BOLD)
fuente_integrantes_texto = ("Ralway", 13)
fuente_texto = ("Ralway", 15)
fuente_texto_grande = ("Ralway",20)
fuente_button = ("Ralwey", 20, tk.font.BOLD)
