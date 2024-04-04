from config import *

# ---------------------------------------------------------------------------- #
#                                Metodos Utiles                                #
# ---------------------------------------------------------------------------- #


def cambiar_ventana(ventana_actual, nueva_ventana, *args):
    # Borrar la ventana actual
    ventana_actual.destroy()
    # Crear la nueva ventana
    return nueva_ventana(*args)


# ---------------------------------------------------------------------------- #
#                              Contenido Principal                             #
# ---------------------------------------------------------------------------- #


class ContenidoInicial:
    """
    Clase para la interfaz de usuario inicial.

    Componentes:
    - root: El widget raíz en el que se basa esta interfaz.
    - logica: Un objeto que parece manejar la lógica del programa.
    - frame: Marco principal que contiene todos los elementos.
    - titleFrame: Marco para el título.
    - introductionFrame: Marco para el texto de introducción.
    - buttonFrame: Marco para el botón de inicio.
    """

    def __init__(self, raiz, logica):
        self.root = raiz
        self.logica = logica

        # Frame Principal
        self.frame = ctk.CTkFrame(
            master=raiz, fg_color="#fff", width=680, corner_radius=0
        )
        self.frame.pack_propagate(0)
        self.frame.pack(fill="y", anchor="e", side="right")

        # Frame del Titulo
        self._crear_frame_titulo()

        # Frame de texto de introduccion
        self._crear_frame_introduccion()

        # Frame para el boton de empezar
        self._crear_frame_boton()

    def _crear_frame_titulo(self):
        titleFrame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        titleFrame.pack(anchor="n", fill="both", pady=(38, 50))

        ctk.CTkLabel(
            master=titleFrame,
            text="Calculando el plan de riego optimo de una finca",
            font=fuente_titulo,
            text_color=color_verde,
            justify="center",
        ).pack(anchor="center")

    def _crear_frame_introduccion(self):
        introductionFrame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        introductionFrame.pack(anchor="n", fill="both", pady=(0, 100), padx=20)

        textbox_introduction = ctk.CTkTextbox(
            master=introductionFrame,
            scrollbar_button_color=color_verde,
            font=fuente_texto,
            text_color=color_verde,
            fg_color="transparent",
            corner_radius=5,
        )
        textbox_introduction.pack(anchor="center", fill="x", padx=10)

        default_text = "Este proyecto se centra en encontrar la mejor manera de regar los cultivos en una \nfinca, minimizando el tiempo de sufrimiento de los tablones por falta de agua. \nExploraremos tres enfoques: fuerza bruta, algoritmo voraz y programación dinámica,para resolver este desafío. La interfaz proporcionará herramientas para comprender y comparar estos métodos, ayudando a encontrar la solución más eficiente para la \ngestión del agua en las fincas."
        textbox_introduction.insert("end", default_text)

        textbox_introduction.configure(state="disabled")

    def _crear_frame_boton(self):
        buttonFrame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        buttonFrame.pack(anchor="n", fill="both", pady=(0, 0), padx=20)

        button = ctk.CTkButton(
            master=buttonFrame,
            text="Empezar",
            corner_radius=30,
            fg_color=color_verde,
            hover_color=color_verde_hover,
            command=self.empezar,
            font=fuente_button,
        )

        button.pack(anchor="center", ipadx=5, ipady=5)

    def empezar(self):
        self.seleccionar_algoritmo = cambiar_ventana(
            self.frame, SeleccionarAlgoritmo, self.root, self.logica
        )


# ---------------------------------------------------------------------------- #
#                          Clase Seleccionar Algoritmo                         #
# ---------------------------------------------------------------------------- #


class SeleccionarAlgoritmo:
    """
    Clase para seleccionar el algoritmo a utilizar.

    Componentes:
    - framePrincipal: Marco principal que contiene todos los elementos.
    - frameTitulo: Marco para el título.
    - frameIntroduccion: Marco para el texto de introducción.
    - frameBotones: Marco para los botones.
    - botonFuerzaBruta: Botón para seleccionar fuerza bruta.
    - botonVoraz: Botón para seleccionar algoritmo voraz.
    - botonDinamico: Botón para seleccionar programación dinámica.
    """

    def __init__(self, raiz, logica):
        self.raiz = raiz
        self.logica = logica

        self.framePrincipal = ctk.CTkFrame(
            master=self.raiz, fg_color="#fff", width=680, corner_radius=0
        )
        self.framePrincipal.pack_propagate(0)
        self.framePrincipal.pack(fill="y", anchor="e", side="right")

        self._crear_frame_titulo()
        self._crear_frame_introduccion()
        self._crear_frame_botones()

    def _crear_frame_titulo(self):
        self.frameTitulo = ctk.CTkFrame(
            master=self.framePrincipal, fg_color="transparent"
        )
        self.frameTitulo.pack(anchor="n", fill="both", pady=(38, 30))

        ctk.CTkLabel(
            master=self.frameTitulo,
            text="Seleccionar Algoritmo",
            font=fuente_titulo,
            text_color=color_verde,
            justify="center",
        ).pack(anchor="center")

    def _crear_frame_introduccion(self):
        self.frameIntroduccion = ctk.CTkFrame(
            master=self.framePrincipal, fg_color="transparent"
        )
        self.frameIntroduccion.pack(
            anchor="n", fill="x", expand=False, pady=(0, 0), padx=20
        )

        cuadroTextoIntroduccion = ctk.CTkTextbox(
            master=self.frameIntroduccion,
            scrollbar_button_color=color_verde,
            font=fuente_texto,
            text_color=color_verde,
            fg_color="transparent",
            corner_radius=5,
            height=70,
        )
        cuadroTextoIntroduccion.pack(anchor="center", fill="x", padx=10)

        texto_por_defecto = "Selecciona el algoritmo que deseas utilizar para calcular el plan de riego optimo \nde una finca."
        cuadroTextoIntroduccion.insert("end", texto_por_defecto)

        cuadroTextoIntroduccion.configure(state="disabled")

    def _crear_frame_botones(self):
        self.frameBotones = ctk.CTkFrame(
            master=self.framePrincipal, fg_color="transparent"
        )
        self.frameBotones.pack(anchor="n", fill="both", pady=(100, 0), padx=20)

        self.crear_boton_fuerza_bruta()
        self.crear_boton_voraz()
        self.crear_boton_dinamico()

    def crear_boton_fuerza_bruta(self):
        self.botonFuerzaBruta = ctk.CTkButton(
            master=self.frameBotones,
            text="Fuerza Bruta",
            corner_radius=30,
            fg_color=color_verde,
            hover_color=color_verde_hover,
            command=self.fuerza_bruta,
            font=fuente_button,
        )
        self.botonFuerzaBruta.pack(anchor="center", ipadx=5, ipady=5, pady=(0, 40))

    def crear_boton_voraz(self):
        self.botonVoraz = ctk.CTkButton(
            master=self.frameBotones,
            text="Algoritmo Voraz",
            corner_radius=30,
            fg_color=color_verde,
            hover_color=color_verde_hover,
            command=self.algoritmo_voraz,
            font=fuente_button,
        )
        self.botonVoraz.pack(anchor="center", ipadx=5, ipady=5, pady=(0, 40))

    def crear_boton_dinamico(self):
        self.botonDinamico = ctk.CTkButton(
            master=self.frameBotones,
            text="Programación Dinámica",
            corner_radius=30,
            fg_color=color_verde,
            hover_color=color_verde_hover,
            command=self.programacion_dinamica,
            font=fuente_button,
        )
        self.botonDinamico.pack(anchor="center", ipadx=5, ipady=5)

    def fuerza_bruta(self):
        self.logica.setAlgoritmoSeleccionado("AFB")
        self.seleccionar_entrada = cambiar_ventana(
            self.framePrincipal, SeleccionarEntrada, self.raiz, self.logica
        )

    def algoritmo_voraz(self):
        self.logica.setAlgoritmoSeleccionado("APV")
        self.seleccionar_entrada = cambiar_ventana(
            self.framePrincipal, SeleccionarEntrada, self.raiz, self.logica
        )

    def programacion_dinamica(self):
        self.logica.setAlgoritmoSeleccionado("APD")
        self.seleccionar_entrada = cambiar_ventana(
            self.framePrincipal, SeleccionarEntrada, self.raiz, self.logica
        )


# ---------------------------------------------------------------------------- #
#                           Clase SeleccionarEntrada                           #
# ---------------------------------------------------------------------------- #


class SeleccionarEntrada:
    """
    Algoritmo para seleccionar la entrada de datos.

    Componentes:
    - frame: Marco principal que contiene todos los elementos.
    - frameTitulo: Marco para el título.
    - loadButtonFrame: Marco para las entradas.
    - buttonUpload: Botón para subir archivo.
    - textboxFrame: Marco para el cuadro de texto.
    - textbox: Cuadro de texto para visualizar la entrada.
    """

    def __init__(self, root, logica):
        self.root = root
        self.logica = logica

        self.frame = ctk.CTkFrame(
            master=root, fg_color="#fff", width=680, corner_radius=0
        )
        self.frame.pack_propagate(0)
        self.frame.pack(fill="y", anchor="e", side="right")

        self._crear_frame_titulo()
        self._crear_load_button_frame()
        self._crear_textbox_frame()

        # Crear el controlador de ventanas
        self.controlador = ControladorVentanas(
            self.root,
            self.logica,
            self.frame,
            SeleccionarAlgoritmo,
            EntradaSeleccionada,
        )

    def _crear_frame_titulo(self):
        frameTitulo = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        frameTitulo.pack(anchor="n", fill="both", pady=(38, 0))

        ctk.CTkLabel(
            master=frameTitulo,
            text="Subir la Entrada de Datos",
            font=fuente_titulo,
            text_color=color_verde,
            justify="center",
        ).pack(anchor="center")

    def _crear_load_button_frame(self):
        loadButtonFrame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        loadButtonFrame.pack(anchor="n", fill="both", pady=(30, 0), padx=20)

        self.buttonUpload = ctk.CTkButton(
            master=loadButtonFrame,
            text="Subir Archivo",
            corner_radius=30,
            fg_color=color_verde,
            hover_color=color_verde_hover,
            command=self.subir_archivo,
            font=fuente_button,
        )

        self.buttonUpload.pack(anchor="center", ipadx=5, ipady=5, pady=(0, 40))

    def _crear_textbox_frame(self):
        textboxFrame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        textboxFrame.pack(anchor="n", fill="both", pady=(0, 0), padx=20)

        self.textbox = ctk.CTkTextbox(
            master=textboxFrame,
            scrollbar_button_color=color_verde,
            font=fuente_texto_grande,
            text_color=color_blanco,
            fg_color=color_verde_hover,
            corner_radius=5,
            height=350,
        )
        self.textbox.pack(anchor="center", fill="x", padx=10)
        self.textbox.insert(
            "end", "Sube un archivo para visualizar los datos de entrada."
        )
        self.textbox.configure(state="disabled")

    def subir_archivo(self):
        # Abrir el explorador de archivos
        archivo = tk.filedialog.askopenfilename(
            title="Seleccionar Archivo",
            filetypes=[("Archivos de Texto", "*.txt")],
        )

        # Si el usuario seleccionó un archivo, pasarlo a la lógica
        if archivo:
            resultado = self.logica.subir_archivo(archivo)
            if len(resultado) == 1:
                print(resultado[0])
                CTkMessagebox(
                    title="Error",
                    message=resultado[0],
                    icon="cancel",
                    button_color=color_verde,
                    button_hover_color=color_verde_hover,
                )
            else:
                self.controlador.habilitar_seguir()
                self.textbox.configure(state="normal")
                n = len(resultado)
                self.textbox.delete("1.0", "end")
                self.textbox.insert("end", f"{n}\n")
                for tablon in resultado:
                    self.textbox.insert("end", f"{tablon[0]},{tablon[1]},{tablon[2]}\n")
                self.textbox.configure(state="disabled")


class EntradaSeleccionada:
    """
    Clase para visualizar los datos y algoritmo seleccionado

    Componentes:
    - frame: Marco principal que contiene todos los elementos.
    - frameTitulo: Marco para el título.
    - frameEntrada: Marco para las entradas.
    - entryNumeroTablones: Entrada para el número de tablones.
    - entryAlgoritmo: Entrada para el algoritmo seleccionado.
    - textboxFrame: Marco para el cuadro de texto.
    - textbox: Cuadro de texto para visualizar la entrada.
    - controlador: Controlador de ventanas.
    """

    def __init__(self, root, logica):
        self.root = root
        self.logica = logica

        self.frame = ctk.CTkFrame(
            master=root, fg_color="#fff", width=680, corner_radius=0
        )
        self.frame.pack_propagate(0)
        self.frame.pack(fill="y", anchor="e", side="right")

        self._crear_frame_titulo()
        self._crear_frame_entrada()
        self._crear_frame_textbox()

        self.controlador = ControladorVentanas(
            self.root,
            self.logica,
            self.frame,
            SeleccionarEntrada,
            Cargando,
        )

        self.controlador.habilitar_seguir()

    def _crear_frame_titulo(self):
        # Frame del Titulo
        frameTitulo = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        frameTitulo.pack(anchor="n", fill="both", pady=(38, 0))

        ctk.CTkLabel(
            master=frameTitulo,
            text="Salida",
            font=fuente_titulo,
            text_color=color_verde,
            justify="center",
        ).pack(anchor="center")

    def _crear_frame_entrada(self):
        frameEntrada = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        frameEntrada.pack(anchor="center", fill="x", pady=(40, 0), padx=20)

        entryNumeroTablones = ctk.CTkLabel(
            master=frameEntrada,
            font=fuente_texto_grande,
            text_color=color_verde,
            fg_color=color_blanco,
            corner_radius=5,
            text="Número de Tablones: " + str(self.logica.getNumeroTablones()),
        )
        entryNumeroTablones.pack(side="top", anchor="w")

        entryAlgoritmo = ctk.CTkLabel(
            master=frameEntrada,
            font=fuente_texto_grande,
            text_color=color_verde,
            fg_color=color_blanco,
            corner_radius=5,
            text="Algoritmo Seleccionado: " + self.logica.getValorAlgoritmo(),
        )
        entryAlgoritmo.pack(side="top", anchor="w", pady=(10, 0))

    def _crear_frame_textbox(self):
        textboxFrame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        textboxFrame.pack(anchor="n", fill="both", pady=(40, 0), padx=20)

        self.textbox = ctk.CTkTextbox(
            master=textboxFrame,
            scrollbar_button_color=color_verde,
            font=fuente_texto_grande,
            text_color=color_blanco,
            fg_color=color_verde_hover,
            corner_radius=5,
            height=350,
        )
        self.textbox.pack(anchor="center", fill="x", padx=10)
        for i, tablon in enumerate(self.logica.getFinca()):
            self.textbox.insert("end", f"Tablon {i + 1}:\n")
            self.textbox.insert("end", f"- Tiempo de supervivencia: {tablon[0]}\n")
            self.textbox.insert("end", f"- Tiempo de regado: {tablon[1]}\n")
            self.textbox.insert("end", f"- Prioridad: {tablon[2]}\n\n")

        self.textbox.configure(state="disabled")

class Cargando:
    """
    Clase que simula la carga o progreso de la ejecuion del algoritmo
    """
    def __init__(self, root, logica):
        self.root = root
        self.logica = logica

        self.frame = ctk.CTkFrame(
            master=root, fg_color="#fff", width=680, corner_radius=0
        )
        self.frame.pack_propagate(0)
        self.frame.pack(fill="y", anchor="e", side="right")

        self._crear_frame_carga()

        self.iniciar_algoritmo()

    def iniciar_algoritmo(self):
        thread = threading.Thread(target=self._ejecutar_algoritmo)
        thread.start()

    def _ejecutar_algoritmo(self):
        time.sleep(0.5)
        executionTime = self.logica.usar_algoritmo()
        cambiar_ventana(self.frame, Salida, self.root, self.logica, executionTime)

    def _crear_frame_carga(self):
        frameCarga = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        frameCarga.pack(anchor="center", fill="both", expand=True, pady=(0, 0))

        ctk.CTkLabel(
            master=frameCarga,
            text="Cargando...",
            font=fuente_titulo,
            text_color=color_verde,
            justify="center",
        ).place(relx=0.5, rely=0.5, anchor="center")


class Salida:
    """
    Clase para visualizar los datos de salida del algoritmo seleccionado.

    Componentes:
    frame: Marco principal que contiene todos los elementos.
    frameTitulo: Marco para el título.
    frameEntradas: Marco para las entradas.
    entryNumeroTablones: Entrada para el número de tablones.
    entryAlgoritmo: Entrada para el algoritmo seleccionado.
    frameTextbox: Marco para el cuadro de texto.
    textbox: Cuadro de texto para visualizar la salida.
    frameBotones: Marco para los botones.
    botonDescargar: Botón para descargar la salida.
    botonSalir: Botón para salir.
    """

    def __init__(self, root, logica, executionTime):
        self.root = root
        self.logica = logica
        self.executionTime = executionTime

        self.frame = ctk.CTkFrame(
            master=root, fg_color="#fff", width=680, corner_radius=0
        )
        self.frame.pack_propagate(0)
        self.frame.pack(fill="y", anchor="e", side="right")

        self._crear_frame_titulo()
        self._crear_frame_entrada()
        self._crear_frame_textbox()
        self._crear_frame_botones()

    def _crear_frame_titulo(self):
        # Frame del Titulo
        frameTitulo = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        frameTitulo.pack(anchor="n", fill="both", pady=(38, 0))

        ctk.CTkLabel(
            master=frameTitulo,
            text="Entrada Seleccionada",
            font=fuente_titulo,
            text_color=color_verde,
            justify="center",
        ).pack(anchor="center")

    def _crear_frame_entrada(self):
        frameEntrada = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        frameEntrada.pack(anchor="center", fill="x", pady=(40, 0), padx=20)

        entryNumeroTablones = ctk.CTkLabel(
            master=frameEntrada,
            font=fuente_texto_grande,
            text_color=color_verde,
            fg_color=color_blanco,
            corner_radius=5,
            text="Número de Tablones: " + str(self.logica.getNumeroTablones()),
        )
        entryNumeroTablones.pack(side="top", anchor="w")

        entryAlgoritmo = ctk.CTkLabel(
            master=frameEntrada,
            font=fuente_texto_grande,
            text_color=color_verde,
            fg_color=color_blanco,
            corner_radius=5,
            text="Algoritmo Seleccionado: " + self.logica.getValorAlgoritmo(),
        )
        entryAlgoritmo.pack(side="top", anchor="w", pady=(10, 0))

        if self.executionTime < 0.001:
            executionTimeParsed = "{:.3f} microsegundos".format(self.executionTime * 1000000)
        else:
            executionTimeParsed = "{:.3f} segundos".format(self.executionTime)
            
        entryExecutionTime = ctk.CTkLabel(
            master=frameEntrada,
            font=fuente_texto_grande,
            text_color=color_verde,
            fg_color=color_blanco,
            corner_radius=5,
            text="Tiempo de ejecución: " + str(executionTimeParsed),
        )
        entryExecutionTime.pack(side="top", anchor="w", pady=(10, 0))

    def _crear_frame_textbox(self):
        textboxFrame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        textboxFrame.pack(anchor="n", fill="both", pady=(40, 0), padx=20)

        self.textbox = ctk.CTkTextbox(
            master=textboxFrame,
            scrollbar_button_color=color_verde,
            font=fuente_texto_grande,
            text_color=color_blanco,
            fg_color=color_verde_hover,
            corner_radius=5,
            height=300,
        )
        self.textbox.pack(anchor="center", fill="x", padx=10)
        self.textbox.insert("end", "El algoritmo se esta ejecutando...")
        self.textbox.configure(state="disabled")

        solucion = self.logica.resultadoOptimo
        
        # Clear the textbox
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")

        # # Insert the cost
        self.textbox.insert("end", f"Costo: {solucion[0]}\n")

        # # Insert the order of the planks
        self.textbox.insert("end", "Orden de los tablones:\n")
        for tablon in solucion[1:]:
            self.textbox.insert("end", f"{tablon}\n")

        # Disable the textbox to prevent user input
        self.textbox.configure(state="disabled")

    def _crear_frame_botones(self):
        # Frame para los botones
        buttonsFrame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        buttonsFrame.pack(side="bottom", fill="x")

        self.botonDecargar = ctk.CTkButton(
            master=buttonsFrame,
            text="Descargar Solución",
            command=self.descargarSolucion,
            corner_radius=30,
            fg_color=color_verde,
            hover_color=color_verde_hover,
            font=fuente_button,
        )

        self.botonSalir = ctk.CTkButton(
            master=buttonsFrame,
            text="Salir",
            command=self.salir,
            corner_radius=30,
            fg_color=color_verde,
            hover_color=color_verde_hover,
            font=fuente_button,
        )

        self.botonDecargar.pack(
            side="left", anchor="center", ipadx=5, ipady=5, padx=(40, 0), pady=(0, 20)
        )
        self.botonSalir.pack(
            side="right", anchor="center", ipadx=5, ipady=5, padx=(0, 40), pady=(0, 20)
        )

    def descargarSolucion(self):
        # Abre el diálogo de guardar archivo y obtén la ubicación del archivo
        archivo = tk.filedialog.asksaveasfilename(defaultextension='.txt')

        solucion = self.logica.usar_algoritmo()

        # Si el usuario seleccionó una ubicación, guarda el archivo
        if archivo:
            with open(archivo, 'w') as f:
                for numero in solucion:
                    f.write(str(numero) + '\n')

    def salir(self):
        cambiar_ventana(self.frame, ContenidoInicial, self.root, self.logica)


# ---------------------------------------------------------------------------- #
#                         Clase Controlador de Ventanas                        #
# ---------------------------------------------------------------------------- #


class ControladorVentanas:
    def __init__(
        self,
        root,
        logica,
        ventana_actual,
        ventana_anterior,
        proxima_ventana,
    ):
        self.root = root
        self.logica = logica
        self.ventana_actual = ventana_actual
        self.ventana_anterior = ventana_anterior
        self.proxima_ventana = proxima_ventana

        # Frame para los botones
        buttons_frame = ctk.CTkFrame(master=self.ventana_actual, fg_color="transparent")
        buttons_frame.pack(side="bottom", fill="x")

        # Crear los botonescargando
        self.boton_volver = ctk.CTkButton(
            master=buttons_frame,
            text="Volver",
            command=self.volver,
            corner_radius=30,
            fg_color=color_verde,
            hover_color=color_verde_hover,
            font=fuente_button,
        )
        self.boton_seguir = ctk.CTkButton(
            master=buttons_frame,
            text="Seguir",
            command=self.seguir,
            corner_radius=30,
            fg_color=color_verde,
            hover_color=color_verde_hover,
            font=fuente_button,
            state="disabled",
        )

        # Añadir los botones al root
        self.boton_volver.pack(
            side="left", anchor="center", ipadx=5, ipady=5, padx=(40, 0), pady=(0, 20)
        )
        self.boton_seguir.pack(
            side="right", anchor="center", ipadx=5, ipady=5, padx=(0, 40), pady=(0, 20)
        )

    def habilitar_seguir(self):
        self.boton_seguir.configure(state="normal")

    def deshabilitar_seguir(self):
        self.boton_seguir.configure(state="disabled")

    def volver(self):
        cambiar_ventana(
            self.ventana_actual, self.ventana_anterior, self.root, self.logica
        )

    def seguir(self):
        cambiar_ventana(
            self.ventana_actual, self.proxima_ventana, self.root, self.logica
        )
