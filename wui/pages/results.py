"""Result viewer page."""

import reflex as rx


def results_page() -> rx.Component:
    """Displays execution results (placeholder)."""
    return rx.container(
        rx.vstack(
            rx.heading("Results", size="6"),
            rx.text("TODO: session summary, logs, metrics"),
            rx.link("Back to Home", href="/"),
            spacing="3",
        ),
        padding="2em",
    )
