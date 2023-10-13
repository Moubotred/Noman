import reflex as rx

class CondState(rx.State):
    show: bool = True

    def change(self):
        if self.show:
            self.show = False

def about():
    return rx.box(rx.text("adios"))

def index():
    return rx.vstack(
                rx.button("Toggle", on_click=CondState.change),
                rx.cond(
                    CondState.show,
                    rx.link(rx.button("iniciar sesion"),href="/about"),
                    rx.link(rx.button("cargando"))
            ),
        )

app = rx.App()
app.add_page(index)
app.add_page(about)
app.compile()



# class State(rx.State):
#     p1:str = "1"
#     p2:str = "-1"
#     usuario:str = ""
#     password:str = ""
#     estado:bool = False
#     def main(self):
#         if self.usuario == "kivi" and self.password == "bin123":
#             print(self.usuario,self.password)
#             self.p1 = "-1"
#             self.p2 = "1"
#             self.estado = True
#         else:
#             self.p1 = "1"
#             self.p2 = "-1"
#             self.estado = False

#         self.estado = False
#         self.usuario = ""
#         self.password = ""


# def seccion():
#     return rx.box(rx.text("texto"))
    
# def index():
#     return rx.hstack(
#                 rx.input(placeholder="username",value=State.usuario, on_change=State.set_usuario),
#                 rx.input(placeholder="passwprd",value=State.password, on_change=State.set_password),
#                 rx.button("iniciar sesion",
#                           #boton pricipal 1
#                           on_click=State.main,
#                           z_index = State.p1,
#                           id = "front"),
#                 rx.cond(
#                     State.estado,
#                     rx.link(rx.button("continuar",z_index = State.p2,id = "back")),
#                     rx.link(rx.button("iniciar secion",z_index = State.p2,id = "back"),href = "/seccion")
#                 )
#     )


# app = rx.App(stylesheets=["styles.css"])
# app.add_page(index)
# app.add_page(seccion)
# app.compile()

#     usuario: str = ""
#     password : str = ""
#     estado: str = "/"
#     msg: str = ""
#     pos: str = "-1"
#     rop: str = "1"
    
#     def home(self):
#         if self.usuario == "kivi" and self.password == "bin123":
#             print(self.usuario,self.password)
#             self.estado = "/about"
#             self.msg = "continuar"
#             self.pos = "1"
#             self.rop = "-1"

#         else:
#             self.estado
        
# def about():
#     return rx.box(rx.text("hola"))


# def seccion() -> rx.Component:
#         return rx.vstack(
#             rx.link(
#                 rx.button(State.msg),
#                 href = State.estado
#             ),
#             position = "fixed",
#             width = "100px",
#             height = "100px",
#             # z_index = f"{State.pos}",
#             z_index = "1",
#             top = "14%",
#         )


# def index():
#     return rx.vstack(
#                 rx.input(placeholder="username",value=State.usuario, on_change=State.set_usuario),
#                 rx.input(placeholder="password",value=State.password, on_change=State.set_password),
#                 rx.button("Iniciar secion",on_click=State.home,style = {"z_index":"-1"}),
#                 seccion()
#     )

# app = rx.App()
# app.add_page(index)
# app.add_page(about)
# app.compile()