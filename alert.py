
class AlertDialogState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)


def index():
    return rx.box(
    rx.button("Show Alert Dialog",on_click=AlertDialogState.change,),
        rx.alert_dialog(
            rx.alert_dialog_overlay(
                    rx.alert_dialog_content(
                    rx.alert_dialog_header("Confirm"),
                    rx.alert_dialog_body("Do you want to confirm example?"),
                    rx.alert_dialog_footer(rx.button("Close",on_click=AlertDialogState.change)
                    ),
                )
            ),
            is_open=AlertDialogState.show,
        ),
    )
