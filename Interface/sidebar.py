from Interface.config import *

class Sidebar:
    def __init__(self, raiz):
        self.frame = ctk.CTkFrame(
            master=raiz, fg_color=color_verde, width=176, corner_radius=0
        )
        self.frame.pack_propagate(0)
        self.frame.pack(fill="y", anchor="w", side="left")

        # Logo
        logo_img_data = Image.open(os.path.join(carpeta_imagenes, "logo2.png"))
        ancho_nuevo = int(logo_img_data.width * 1.1)
        alto_nuevo = int(logo_img_data.height * 1.1)
        logo_img_data = logo_img_data.resize((ancho_nuevo, alto_nuevo))
        logo_img = ctk.CTkImage(
            dark_image=logo_img_data,
            light_image=logo_img_data,
            size=(ancho_nuevo, alto_nuevo),
        )
        ctk.CTkLabel(master=self.frame, text="", image=logo_img).pack(
            pady=(38, 0), anchor="center"
        )

        # -------------------------------- Integrantes ------------------------------- #
        ctk.CTkLabel(
            master=self.frame,
            text="Integrantes",
            fg_color="transparent",
            font=fuente_integrantes_titulo,
            anchor="center",
        ).pack(anchor="center", pady=(60, 10))

        ctk.CTkLabel(
            master=self.frame,
            text="Carlos Andres Hernandez",
            fg_color="transparent",
            font=fuente_integrantes_texto,
            anchor="w",
        ).pack(anchor="center", pady=(0, 5))
        ctk.CTkLabel(
            master=self.frame,
            text="Jose Luis Hincapie",
            fg_color="transparent",
            font=fuente_integrantes_texto,
            anchor="w",
        ).pack(anchor="center", pady=(0, 5))
        ctk.CTkLabel(
            master=self.frame,
            text="Sebastian Idrobo",
            fg_color="transparent",
            font=fuente_integrantes_texto,
            anchor="w",
        ).pack(anchor="center", pady=(0, 5))
        ctk.CTkLabel(
            master=self.frame,
            text="Brayan Andres Sanchez",
            fg_color="transparent",
            font=fuente_integrantes_texto,
            anchor="w",
        ).pack(anchor="center", pady=(0, 0))

        # Footer en sidebar
        ctk.CTkLabel(
            master=self.frame,
            text="Universidad del \nValle",
            fg_color="transparent",
            font=fuente_texto,
            anchor="s",
        ).pack(anchor="center", side="bottom", pady=(0, 20))
