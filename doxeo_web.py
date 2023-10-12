
import reflex as rx
from doxeo_web import prefex,secion

class State(rx.State): 
    usuario: str = ""
    password : str = ""
    estado: bool = False
    def home(self):
        if self.usuario == "kivi" and self.password == "bin123":
            print(self.usuario,self.password)
            self.estado = True
        else:
            self.estado = False


def noma()->rx.Component:
    return rx.hstack(
                rx.text("hola"),
                style = secion.indexa
    )

def failed_login()->rx.Component:
    return rx.hstack(
                rx.text("fallo")
    )


def index()->rx.Component:
    return rx.hstack(
        rx.box(
            rx.box( 
                rx.image(src="ixon.png",style = prefex.icono),
                rx.input(placeholder="usuario",style = prefex.usuario,value = State.usuario,on_change = State.set_usuario),
                rx.input(placeholder="contrasena",style = prefex.contrasena,value = State.password,on_change = State.set_password),
                rx.button('iniciar secion',on_click = State.home,style = prefex.boton_login),
                    rx.cond(
                        State.estado,
                        rx.box(noma()),
                        rx.box(failed_login())
                        # rx.link(href = "/noma"),
                        # rx.link(href = "/index")
                    ),
                # rx.link(rx.button('iniciar secion',type_="submit",on_click = State.home,style = prefex.boton_login),href="/noman"),
                style = prefex.login),
        ),
    style = prefex.index,
    id = "main"
    )

app = rx.App()
app.add_page(index)
app.add_page(noma)
app.compile()
