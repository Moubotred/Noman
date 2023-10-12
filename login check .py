import reflex as rx

class State(rx.State):
    usuario: str = ""
    password : str = ""
    estado: str = "/"
    def home(self):
        if self.usuario == "kivi" and self.password == "bin123":
            print(self.usuario,self.password)
            self.estado = "/about"
            print(self.estado)
        else:
            self.estado = "/"
        # self.estado = "/"
        
def about():
    return rx.box(rx.text("hola"))

def seccion()-> rx.Component:
    return rx.box(
                rx.link(
                    rx.button("continuar"),
                    href = State.estado
                )
    )


def index():
    return rx.vstack(
                rx.input(placeholder="username",value=State.usuario, on_change=State.set_usuario),
                rx.input(placeholder="password",value=State.password, on_change=State.set_password),
                rx.button("Iniciar sesion",on_click=State.home),
                seccion(),
    )

app = rx.App()
app.add_page(index)
app.add_page(about)
app.compile()