import reflex as rx
from wui.components.layout import page

@rx.page(route="/settings", title="Settings")
def settings_page() -> rx.Component:
    return page(
        rx.vstack(
            rx.heading("Settings", size="7"),
            rx.text("TODO: UI-definition YAML, defaults, etc."),
            spacing="3",
            align="start",
        )
    )
