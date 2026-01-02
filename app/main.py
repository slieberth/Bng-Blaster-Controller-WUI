import reflex as rx

class AppState(rx.State):
    pass

def index():
    return rx.container(
        rx.heading("BNG Blaster Controller WUI"),
        rx.text("Reflex is running 🚀"),
    )

app = rx.App()
app.add_page(index)
app.compile()
