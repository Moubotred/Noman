import reflex as rx

style_body = {
    "display":"flex",
    "justify-content":"center",
    "align-items":"center",
    "height":"100vh",
    "margin":"0"
}

style_card ={
    "width": "200px",
    "height":"300px",
    "perspective": "1000px"
}

style_inner = {
    "width": "100%",
    "height": "100%",
    "transition": "transform 0.5s",
    "transform-style": "preserve-3d"
}

style_frontend = {
    "width":"100%",
    "height": "100%",
    "position": "absolute",
    "backface-visibility": "hidden",
    "display": "flex",
    "justify-content": "center",
    "align-items": "center",
    "font-size": "24px",
    "font-weight":"bold",
    "border": "1px solid #ccc",
    "background-color":"#3498db",
    "color":"#fff",
    "transform":"rotateY(0deg)"
}

style_backend = {
    "width":"100%",
    "height": "100%",
    "position": "absolute",
    "backface-visibility": "hidden",
    "display": "flex",
    "justify-content": "center",
    "align-items": "center",
    "font-size": "24px",
    "font-weight":"bold",
    "border": "1px solid #ccc",
    "background-color":"#e74c3c",
    "color":"#fff",
    "transform":"rotateY(180deg)"
}

def index():
    return  rx.box( 
                rx.box(
                    rx.box(
                        rx.box("Hola",class_name = "front",style = style_frontend),
                        rx.box("Adios",class_name = "back",style = style_backend),
                        class_name = "card-inner",
                        style = style_inner,
                        _hover = {"transform":"rotateY(180deg)"}
                        )
                    ,
            class_name = "card",
            style = style_card
            ),
        style = style_body
        )
    

app = rx.App()
app.add_page(index)
app.compile()



