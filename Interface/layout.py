from Interface.sidebar import Sidebar
from Interface.contenido_principal import ContenidoInicial

class Layout:
    def __init__(self, raiz, logica):
        self.sidebar = Sidebar(raiz)
        self.contenido_principal = ContenidoInicial(raiz, logica)
