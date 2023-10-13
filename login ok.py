# ingresar usuario y contrasena
# evaluar si es verdadero o falso
# si es verdadero borrar las cajas de texto 

import reflex as rx

class State(rx.State):
    usuario:str 
    password:str 

    def main(self):
        if self.usuario == "kivi" and self.password == "bin123":
            print(self.usuario,self.password)
            return rx.redirect("/seccion")

def seccion():
    return rx.box(rx.text("texto"))
    
def index():
    return rx.hstack(
                rx.input(placeholder="username",value=State.usuario, on_change=State.set_usuario),
                rx.input(placeholder="password",value=State.password, on_change=State.set_password),
                rx.button("iniciar sesion",
                          on_click = State.main,
                        #   z_index = State.sesion,
                          id = "front"),
    )


app = rx.App(stylesheets=["styles.css"])
app.add_page(index)
app.add_page(seccion)
app.compile()