import reflex as rx

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("BNG Blaster Controller WUI"),
            rx.text("Reflex läuft ✅"),
            spacing="4",
        ),
        min_height="100vh",
    )

app = rx.App()
app.add_page(index, route="/")
