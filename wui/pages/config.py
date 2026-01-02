"""Config builder page."""

import reflex as rx


def config_page() -> rx.Component:
    """Guided configuration builder (placeholder)."""
    return rx.container(
        rx.vstack(
            rx.heading("Config Builder", size="6"),
            rx.text("TODO: YAML/JSON driven UI options + validation"),
            rx.link("Back to Home", href="/"),
            spacing="3",
        ),
        padding="2em",
    )
