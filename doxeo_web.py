# import reflex as rx
# from doxeo_web import prefex

# class State(rx.State): 
#     usuario: str = ""
#     password : str = ""
#     estado: bool = False
#     def home(self):
#         if self.usuario == "kivi" and self.password == "bin123":
#             self.estado = True


# @rx.page("/principal")
# def principal():
#     return rx.hstack(
#         rx.box("hola")
#     )
    
# @rx.page("/about")
# def about():
#     return rx.hstack(
#         rx.box("hola")
#     )


# @rx.page(route="/home", title="Home Page")
# def login() -> rx.Component:
#     return rx.box(
#         rx.image(src="ixon.png",style = prefex.icono),
#         rx.input(placeholder="usuario",style = prefex.usuario,value = State.usuario,on_change = State.set_usuario),
#         rx.input(placeholder="contrasena",style = prefex.contrasena,value = State.password,on_change = State.set_password),  
#         rx.button('iniciar secion',type_="submit",on_click = State.home,style = prefex.boton_login),
#         rx.cond(
#             State.estado,
#             rx.link(rx.button("continuar",href = "/principal")),
#             rx.text("hola",color = "red")
#         ),
#         style = prefex.login
#         )

# def index():
#     return rx.hstack(
#         login(),
#         style = prefex.index)    


# app = rx.App()
# app.add_page(index)
# # app.add_page(principal)
# # app.add_page(about)
# app.compile()



import reflex as rx
from doxeo_web import prefex

class State(rx.State): 
    usuario: str = ""
    password : str = ""
    estado: bool = False
    def home(self):
        if self.usuario == "kivi" and self.password == "bin123":
            self.estado = True

# Página de Inicio
@rx.page("/")
def index():
    return rx.box(
        rx.box( 
            rx.image(src="ixon.png",style = prefex.icono),
            rx.input(placeholder="usuario",style = prefex.usuario,value = State.usuario,on_change = State.set_usuario),
            rx.input(placeholder="contrasena",style = prefex.contrasena,value = State.password,on_change = State.set_password),
            rx.button('iniciar secion',type_="submit",on_click = State.home,style = prefex.boton_login),
            style = prefex.login,
                ),
            rx.cond(
                State.estado,
                rx.link(rx.button("iniciar secion"),href="/principal"),
                rx.text(""),
                # rx.link(rx.button("about"),href="/about"),
                ),
        style = prefex.index
        )

@rx.page("/principal")
def principal():
    return rx.box(
        rx.hstack("hola",
            style = prefex.index
        )
    )

# Página 'About'
@rx.page("/about")
def about():
    return rx.hstack("Estás en la página 'About'")

app = rx.App()
app.add_page(index)
app.add_page(about)
app.add_page(principal)
app.compile()

# crea 2 paginas una con un saludo y otra con adios que en la pgina de saludo tenga un boton que me rediriga a la pagina del adios 
# uso de redirect para para la redireccion de direfentes paginas ejemplos completos para poder usar nose nada de reflex explicame todo y no te olvides de poner el codigo completo 
# como usar rutas y usr redirect para principiantes nose nada de como se usa codigo completo
# 2 paginas y usar el decorador para llamar a una de las 2 paginas 
# termina el codigo ya que falta la forma de aceder a la otra pagina con un boton no te olvides de uar el decorador de @rx.page