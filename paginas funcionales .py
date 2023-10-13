import reflex as rx
from doxeo_web import prefex
from .pages import login


class State(rx.State): 
    usuario: str = ""
    password : str = ""
    def home(self):
        if self.usuario == "kivi" and self.password == "bin123":
            return rx.redirect("/hola")
        else:
            return rx.redirect("/fallo")


@rx.page(route="/fallo",title="pantalla de error")
def fallo():
    return rx.hstack(rx.text("fallo"),)

@rx.page(route="/noma",title="pantalla de logeo")
def noma():
    return rx.hstack(rx.text("hola"),)

@rx.page(route="/",title="pantalla principal")
def index():
    return rx.hstack(
        rx.box(
            rx.box( 
                rx.image(src="ixon.png",style = prefex.icono),
                rx.input(placeholder="usuario",style = prefex.usuario,value = State.usuario,on_change = State.set_usuario),
                rx.input(placeholder="contrasena",style = prefex.contrasena,value = State.password,on_change = State.set_password),
                rx.button('iniciar secion',on_click = State.home,style = prefex.boton_login),style = prefex.login),
            ),
    style = prefex.index,
    )

app = rx.App()
app.add_page(index)
# app.add_page(login)
# app.add_page(fallo)
app.compile()