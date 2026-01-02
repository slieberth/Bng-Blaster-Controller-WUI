# wui/components/layout.py
import reflex as rx


def page_layout(*children: rx.Component) -> rx.Component:
    """Shared page wrapper used by all pages.

    - Keeps page styling consistent.
    - Central place for header/nav/footer later.
    """
    return rx.center(
        rx.box(
            *children,
            width="100%",
            max_width="900px",
            padding="2rem",
        ),
        width="100%",
        min_height="100vh",
    )
