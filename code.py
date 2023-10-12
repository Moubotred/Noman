import reflex as rx
from lxml import html
import requests

class buscar(rx.State):
    text:str = ''
    message: str = 'info!'
    def seeker(self):
        url = f'http://158.69.119.209/data/index.php?view=mostrar&cod={self.text}'
        response = requests.get(url)
        html_source = response.content
        busqueda_elementos = html.fromstring(html_source)
        nombre = busqueda_elementos.xpath('//h2[@class="name"]/text()')
        # estado = response.status_code
        if nombre:
            self.message = f"Nombre = {nombre[0]}"
        else:
            self.message = "estado fallido"
        self.text = ""
        message: str = 'info!'
        yield
    

def index():
    return rx.vstack(
        rx.text(
            
		),
        rx.input(
            placeholder="Dni",
			value= buscar.text,
            on_change = buscar.set_text,
        	width="70%",
            height = "3em",
        	style = {"font-size":"16px","font-family":"Arial","border":"2px solid rgb(116, 179, 255)"},
        	position = "absolute",
        	left = "10%",
        	top = "30px",
		),
        rx.button("Buscar",type_="submit",
            position = "absolute",
        	left = "82%",
        	top = "27px",
            style = {"font-size":"16px","font-family":"Arial","border":"2px solid rgb(116, 179, 255)"},
            on_click=buscar.seeker
        ),
        rx.card(
            rx.text(
                buscar.message,
				position = "relative",
                left = "5%",
                top = "50%",
                text_align = 'center'                    
			),
            style = {"font-size":"16px","font-family":"Arial","border":"2px solid rgb(116, 179, 255)"},   
            position = "absolute",
            width="26%",
            height = "13em",
        	left = "36%",
            bottom = "-20em"
    	)
)     



# class buscar(rx.State):
#     numero: str = ''
#     def seeker(self):
#         # equation with self.numero
#         print(self.numero)

# def index():
#     return rx.vstack(
        
#         rx.input(
#             value=buscar.numero,
#             on_change=buscar.set_numero
#             ),
            
#         rx.button("Buscar",type_="submit",
#             position = "absolute",
#         	left = "82%",
#         	top = "27px",
#             style = {"font-size":"16px","font-family":"Arial","border":"2px solid rgb(116, 179, 255)"},
#             on_click=buscar.seeker
#             ),
        
# )


app = rx.App()
app.add_page(index)
app.compile()
