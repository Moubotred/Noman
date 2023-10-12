import reflex as rx

def index():
    return rx.box(
                rx.vstack(
                    rx.card(
                        rx.box(
                            rx.hstack(
                                rx.image(
                                    src = "/login.jpg",
                                    width = "80px",
                                    height = "120px"
                                    ),
                                position = "absolute",
                                left = "10px",
                                top = "40px"
                            ),
                            rx.hstack(
                                rx.heading("REPUBLICA DEL PERU",font_size="0.5em"),
                                position = "absolute",
                                left = "10px",
                                top = "8px"
                            ),
                            rx.hstack(
                                rx.heading("REGISTRO NACIONAL DE IDENTIFICACION Y ESTADO CIVIL",font_size="0.4em"),
                                position = "absolute",
                                left = "103px",
                                top = "8px"
                            ),
                            rx.hstack(
                                rx.heading("DOCUMENTO NACIONAL DE IDENTIDAD",font_size="0.4em"),
                                position = "absolute",
                                left = "103px",
                                top = "15px"
                            ),
                            rx.hstack(
                                rx.heading("DNI",font_size="0.5em"),
                                position = "absolute",
                                left = "290px",
                                top= "15px"
                            ),
                            rx.box(
                                rx.vstack(rx.text("Apellidos",font_size="0.7em",text_align = "center",
                                                  border_radius = "10px",
                                                  width = "70px",
                                                  bg = "rgb(156, 156, 156)",
                                                  position="absolute",
                                                  left="90px",
                                                  top = "30px"),
                                          rx.text("GUIZADO VASQUEZ",font_size="0.7em",text_align = "center",
                                                  border_radius = "10px",
                                                  width = "200px",
                                                  bg = "rgb( 202, 184, 184 )",
                                                  position="absolute",
                                                  left="90px",
                                                  top = "55px",
                                                  ),
                                          spacing = "-1",
                                          ),
                                rx.vstack(rx.text("Pre Nombres",font_size="0.7em",text_align = "center",
                                                  border_radius = "10px",
                                                  width = "100px",
                                                  bg = "rgb(156, 156, 156)",
                                                  position="absolute",
                                                  left="90px",
                                                  top = "70px",
                                                  ),
                                          rx.text("TONY RUBEN",font_size="0.7em",text_align = "center",
                                                  border_radius = "10px",
                                                  width = "100px",
                                                  bg = "rgb( 202, 184, 184 )",
                                                  position="absolute",
                                                  left="90px",
                                                  top = "95px",
                                                  ),
                                          spacing = "-1"
                                          ),
                                rx.vstack(rx.text("Edad",font_size="0.7em",text_align = "center",
                                                  border_radius = "10px",
                                                  width = "100px",
                                                  bg = "rgb(156, 156, 156)",
                                                  position="absolute",
                                                  left="90px",
                                                  top = "112px",
                                                  ),
                                          rx.text("21",font_size="0.7em",text_align = "center",
                                                  border_radius = "10px",
                                                  width = "50px",
                                                  bg = "rgb( 202, 184, 184 )",
                                                  position="absolute",
                                                  left="110px",
                                                  top = "140px",
                                                  ),
                                          rx.text("Nacimiento",font_size="0.7em",text_align = "center",
                                                  border_radius = "10px",
                                                  width = "100px",
                                                  bg = "rgb(156, 156, 156)",
                                                  position="absolute",
                                                  left="195px",
                                                  top = "115px",
                                                  ),
                                          rx.text("2002-06-19",font_size="0.7em",text_align = "center",
                                                  border_radius = "10px",
                                                  width = "100px",
                                                  bg = "rgb( 202, 184, 184 )",
                                                  position = "absolute",
                                                  left = "200px",
                                                  top = "140px",
                                                  ),
                                          spacing = "-1"
                                          ),
                                position = "relative",
                            right = "10px",
                            bottom = "10px"
                            ),
                            rx.hstack(
                                rx.vstack(
                                    rx.box(
                                        rx.text("Sexo",font_size = "0.6em",             
                                                position = "relative",
                                                left = "30%"),
                                        rx.text("M",font_size = "0.6em",color ="rgb( 255, 96, 96)",
                                                
                                                position = "relative",
                                                left = "39%",
                                                bottom = "5px"),
                                        width = "70px",
                                        height = "28px",
                                        bg = "rgb(111, 189, 236)",
                                        style = {"border":"1px solid black"}
                                    ),
                                    rx.box(
                                        rx.text("Estado Civil",font_size = "0.6em",
                                                position = "relative",
                                                left = "12%"),
                                        rx.text("S",font_size = "0.6em",color ="rgb( 255, 96, 96)",
                                                position = "relative",
                                                left = "39%",
                                                bottom = "5px"),
                                        width = "70px",
                                        height = "28px",
                                        bg = "rgb(111, 189, 236)",
                                        style = {"border":"1px solid black"}
                                    ),
                                    rx.box(
                                        rx.text("Coicidencias",font_size = "0.6em",
                                                position = "relative",
                                                left = "12%"),
                                        rx.text("4",font_size = "0.6em",color ="rgb( 255, 96, 96)",
                                                position = "relative",
                                                left = "38%",
                                                bottom = "5px"),
                                        width = "70px",
                                        height = "28px",
                                        bg = "rgb(111, 189, 236)",
                                        style = {"border":"1px solid black"}
                                    ),
                                    position = "absolute",
                                    top = "18px",
                                    spacing = "-1",
                                ),
                                position = "absolute",
                                left = "360px",
                            ),
                            rx.vstack(    
                                rx.heading('''>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n
                                              >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n
                                              >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>''',font_size = "0.8em"),
                                position = "absolute",
                                left = "20px",
                                top = "180px"
                            )
                        ),
                        position = "absolute",
                        left = "-2px",
                        top = "-2px",      
                        width = "450px",
                        height = "30px",            
                        style = {"font-size":"16px","font-family":"Arial","border":"2px solid rgb(116, 179, 255)"},
                        border_radius="15px",
                        bg = "rgb(156, 156, 156)"
                    ),
                    
                position = "absolute",
                left = "120px",
                top = "90px",
                bg="rgb(111, 189, 236)",
                border_radius="15px",
                width = "450px",
                height = "250px",
                style = {"font-size":"16px","font-family":"Arial","border":"2px solid rgb(116, 179, 255)"},
                )
            )

app = rx.App()
app.add_page(index)
app.compile()


# rx.box(
#                 rx.text("REPUBLICA DEL PERU"),
#                 rx.text("REGISTRO NACIONAL DE IDENTIFICACION Y ESTADO CIVIL"),
#                 rx.text("DOCUMENTO NACIONAL DE IDENTIDAD"),
#                 rx.text("DNI")
#             )



# return rx.box(
#         rx.hstack(
#             rx.heading("My App"),
#         ),
#         position="fixed",
#         width="100%",
#         left = "10%",
#         top="10%",
#         # z_index="5",
#     )

# https://play.hbomax.com/player/urn:hbo:episode:GYL-YXgsAKKjDwgEAAABH

#"fovimed123@hotmail.com:Beatriz14
# elizabeth_dra@hotmail.com:Xiadani16 
# adymejiar@hotmail.com:Adymr1809
# svalevar@gmail.com:qwerty04
# victor_med91@hotmail.com:Lucas235# 
# yuri_iol@hotmail.com:Yuri2127
# mddanielgnz@hotmail.com:Dragon2121922:32"