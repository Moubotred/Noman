from doxeo_web import prefex
from .pages import login
import reflex as rx
import json

class State(rx.State): 
    username: str = ""
    password : str = ""
    show:bool = False
    def verified(self):
        with open('/home/user/Documents/doxeo-web/doxeo_web/usuarios.json', 'r') as archivo:
            datos = json.load(archivo)
        usuarios = datos["usuarios"]
        for usuario in usuarios:
            if usuario["username"] == self.username and usuario["password"] == self.password:
                return rx.redirect("/login")
            else:
                self.show = True
    def estado(self):
            self.show = False
            self.username: str = ""
            self.password : str = ""

                
@rx.page(route="/",title="Nomada")
def index():
    return rx.hstack(
        rx.box(
            rx.box( 
                rx.image(src="ixon.png",style = prefex.icono),
                rx.input(placeholder="usuario",style = prefex.usuario,value = State.username,on_change = State.set_username),
                rx.input(placeholder="contrasena",style = prefex.contrasena,value = State.password,on_change = State.set_password),
                rx.button('iniciar secion',on_click = State.verified,style = prefex.boton_login),style = prefex.login),
                rx.alert_dialog(
                    rx.alert_dialog_overlay(
                            rx.alert_dialog_content(
                            rx.alert_dialog_header("Credenciales"),
                            rx.alert_dialog_body(f"Uso De Las Credenciales USER:{State.username} PASSWORD:{State.password}\nno validas"),
                            rx.alert_dialog_footer(rx.button("Close",on_click=State.estado)
                            ),
                        )
                    ),
                    is_open=State.show,
                ),
            ),
    style = prefex.index,
    )

app = rx.App(stylesheets=["tarjeta.css"])
app.add_page(index)
app.compile()
