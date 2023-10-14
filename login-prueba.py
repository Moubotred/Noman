# https://consultadatosreniec.online/consulta-de-datos-reniec/
# https://eldni.com/
# http://158.69.119.209/data/index.php?view=mostrar&cod=73617355
# http://app.sis.gob.pe/SisConsultaEnLinea/Consulta/frmResultadoEnLinea.aspx
# http://app.sis.gob.pe/SisConsultaEnLinea/Consulta/frmConsultaEnLinea.aspx
# CaptchaImage.aspx?guid=0eeec414-d3d8-4065-a6b6-587365a76e5c

from .pages import login
import reflex as rx
from doxeo_web import prefex
import json

# como proteger las rutas si tengo creado un login y no quiero que saltena a otra ruta sin antes aver ingresado sus creedenciales 
# mensaje de aviso como haria si tengo un login pero si ingresa credenciales que me indique que el usuario no esta registrado 

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
                print("Acceso concedido")
                self.msg = "verificado"
                return rx.redirect("/login")
            else:
                print("denedado")
                self.show = True
                return rx.box(
                        rx.alert_dialog(
                            rx.alert_dialog_overlay(
                                    rx.alert_dialog_content(
                                    rx.alert_dialog_header("Confirm"),
                                    rx.alert_dialog_body("Do you want to confirm example?"),
                                    rx.alert_dialog_footer(rx.button("Close",self.show)),
                                )
                            ),
                            is_open=self.show,
                        ),

                    )
            
                

@rx.page(route="/",title="Nomada")
def index():
    return rx.hstack(
        rx.box(
            rx.box( 
                rx.image(src="ixon.png",style = prefex.icono),
                rx.input(placeholder="usuario",style = prefex.usuario,value = State.username,on_change = State.set_username),
                rx.input(placeholder="contrasena",style = prefex.contrasena,value = State.password,on_change = State.set_password),
                rx.button('iniciar secion',on_click = State.verified,style = prefex.boton_login),style = prefex.login),
            ),
    style = prefex.index,
    )

app = rx.App()
app.add_page(index)
app.compile()
