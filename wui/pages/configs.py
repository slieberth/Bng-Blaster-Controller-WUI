import reflex as rx
from wui.components.layout import page

@rx.page(route="/configs", title="Configs")
def configs_page() -> rx.Component:
    return page(
        rx.vstack(
            rx.heading("Configs", size="7"),
            rx.text("TODO: CRUD config templates"),
            spacing="3",
            align="start",
        )
    )
