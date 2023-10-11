import reflex as rx
from doxeo_web import prefex,secion


# class State(rx.State): 
#     email:bool = False
#     op : str = ""
#     def resp(self):
#         if self.op == "kivi":
#             self.email = not (self.email)
            

# def noman() -> rx.Component:
#     return rx.box(
#         style = prefex.index
#     )
    

# def index():
#     return rx.box(
#         rx.input(placeholder="estado de colores",
#                 value= State.op,
#                 on_change = State.set_op,
#                 ),
#         rx.button('send',type_="submit",on_click=State.resp),
#             rx.cond(
#                 State.email,
#                 rx.box(noman()),
#                 rx.text("red",color = "red")        
#         ),
#     )

# app = rx.App()
# app.add_page(index)
# app.compile()




class State(rx.State): 
    usuario: str = ""
    password : str = ""
    estado : bool = False
    def home(self):
        if self.usuario == "kivi" and self.password == "bin123":
            self.estado = not (self.estado)


def about()-> rx.Component:
    return rx.box("adios")


def principal()-> rx.Component:
     return rx.hstack("hola",style = secion.index_p)


def login() -> rx.Component:
    return rx.box(
        rx.image(src="ixon.png",style = prefex.icono),
        rx.input(placeholder="usuario",style = prefex.usuario,value = State.usuario,on_change = State.set_usuario),
        rx.input(placeholder="contrasena",style = prefex.contrasena,value = State.password,on_change = State.set_password),  
        rx.button('iniciar secion',type_="submit",on_click = State.home,style = prefex.boton_login),
            rx.cond(
                State.estado,
                rx.box(principal()),
                rx.box(about())        
        ),
        # rx.button("iniciar sesion",on_click = State.home,style = prefex.boton_login),
        # rx.cond(State.estado,
        #         rx.box(principal()),
        #         rx.text("verde",color = "green")
        #         ),
        style = prefex.login
        )
    
def index():
    return rx.hstack(
        login(),
        style = prefex.index)

app = rx.App()
app.add_page(index,title="Noman")
app.add_page(principal,title="Noman")
app.compile()





# import reflex as rx
# from doxeo_web import prefex

# class State(rx.State): 
#     pass

# @rx.page(route='/about')
# def principal():
#     return rx.box("hola")
#     pass


# def index():
#     return rx.box(
#                 rx.input(placeholder = "usuario",style = prefex.usuario),
#                 rx.input(placeholder = "contrasena",style = prefex.contrasena),
#                 rx.link(
#                     rx.button("Example"),
#                     href="http://localhost:3000/about",
#                     color="rgb(107,99,246)",
#                     button=True,
#                 )
#     )

# app = rx.App()
# app.add_page(index)
# app.compile()
