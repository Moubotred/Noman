from .pages import login
import reflex as rx
from doxeo_web import prefex
import json

class State(rx.State): 
    show: bool = False
    user:str
    passw:str
    def change(self):
        if self.user == "kivi" and self.passw == "bin123":
            print("user valido")
            pass
        else:
            self.show = True

    def estate(self):
            self.show = False
        # self.show = not (self.show)


def index():
    return rx.box(
        rx.input(placeholder="user",value=State.user,on_change=State.set_user),
        rx.input(placeholder="pass",value=State.passw,on_change=State.set_passw),
        rx.button("iniciar sesion",on_click=State.change),
        rx.alert_dialog(
            rx.alert_dialog_overlay(
                    rx.alert_dialog_content(
                    rx.alert_dialog_header("Confirm"),
                    rx.alert_dialog_body("Do you want to confirm example?"),
                    rx.alert_dialog_footer(rx.button("Close",on_click=State.estate)
                    ),
                )
            ),
            is_open=State.show,
        ),
    )

app = rx.App()
app.add_page(index)
app.compile()
