"""Instances & lifecycle management page."""

import reflex as rx


def instances_page() -> rx.Component:
    """Shows discovered instances and lifecycle controls (placeholder)."""
    return rx.container(
        rx.vstack(
            rx.heading("Instances", size="6"),
            rx.text("TODO: list instances, create/delete, start/stop/kill"),
            rx.link("Back to Home", href="/"),
            spacing="3",
        ),
        padding="2em",
    )
