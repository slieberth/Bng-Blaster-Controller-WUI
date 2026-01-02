"""Home page (dashboard)."""

import reflex as rx


def index() -> rx.Component:
    """Landing page with basic status / links."""
    return rx.center(
        rx.vstack(
            rx.heading("BNG Blaster Controller WUI", size="7"),
            rx.text("Reflex is running ✅"),
            rx.hstack(
                rx.link("Instances", href="/instances"),
                rx.link("Config Builder", href="/config"),
                rx.link("Results", href="/results"),
                spacing="4",
            ),
            spacing="4",
            align="center",
        ),
        height="100vh",
    )
