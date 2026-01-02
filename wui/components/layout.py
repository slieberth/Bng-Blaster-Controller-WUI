import reflex as rx

def nav() -> rx.Component:
    return rx.hstack(
        rx.link("Instances", href="/instances"),
        rx.link("Configs", href="/configs"),
        rx.link("Settings", href="/settings"),
        spacing="4",
        padding="1rem",
        border_bottom="1px solid #ddd",
    )

def page(content: rx.Component) -> rx.Component:
    return rx.vstack(
        nav(),
        rx.box(content, padding="1rem", width="100%"),
        width="100%",
        min_height="100vh",
    )
