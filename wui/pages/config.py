import reflex as rx

@rx.page(route="/config-builder", title="Config Builder")
def config_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Config Builder", size="7"),
            rx.text("Coming soon."),
            rx.link("Back to Home", href="/"),
            spacing="4",
            align="center",
        ),
        height="80vh",
    )
