import reflex as rx
from wui.components.layout import page_layout


def nav_tile(
    *,
    href: str,
    title: str,
    subtitle: str,
    icon: str,
) -> rx.Component:
    """Reusable navigation tile for the landing page."""
    return rx.link(
        rx.card(
            rx.hstack(
                rx.box(
                    rx.icon(icon, size=28),
                    padding="0.75rem",
                    border_radius="999px",
                    background_color=rx.color("gray", 2),
                ),
                rx.vstack(
                    rx.heading(title, size="4"),
                    rx.text(subtitle, color=rx.color("gray", 10)),
                    spacing="1",
                    align_items="start",
                ),
                align_items="center",
                spacing="4",
            ),
            width="100%",
            max_width="420px",
            _hover={"transform": "translateY(-2px)"},
            style={"transition": "transform 120ms ease"},
        ),
        href=href,
        underline="none",
    )


@rx.page(route="/", title="BNG Blaster Controller WUI")
def index() -> rx.Component:
    return page_layout(
        rx.center(
            rx.vstack(
                rx.heading("BNG Blaster Controller WUI", size="7"),
                rx.hstack(
                    rx.text("Reflex is running"),
                    rx.icon("check", color="green", size=18),
                    spacing="2",
                    align="center",
                ),
                rx.spacer(),
                rx.vstack(
                    nav_tile(
                        href="/instances",
                        title="Instances",
                        subtitle="Create, start, stop, and monitor instances.",
                        icon="play",
                    ),
                    nav_tile(
                        href="/config-builder",
                        title="Config Builder",
                        subtitle="Build valid BNG Blaster configs from guided inputs.",
                        icon="wrench",
                    ),
                    nav_tile(
                        href="/results",
                        title="Results",
                        subtitle="View execution status, logs, and summaries.",
                        icon="gauge",
                    ),
                    spacing="3",
                    width="100%",
                    max_width="520px",
                ),
                spacing="5",
                padding_y="8",
                width="100%",
                align="center",
            ),
            width="100%",
            min_height="70vh",
        )
    )
