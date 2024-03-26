# ------------------------------- Importaciones ------------------------------ #
import Interface.dashboard as gui
from logica import Logica

logica = Logica()

# Instancia de la ventana de login
interfaz = gui.Dashboard(logica)
