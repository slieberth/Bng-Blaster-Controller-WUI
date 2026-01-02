import reflex as rx
from wui.components.layout import page

def tabs() -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Run", value="run"),
            rx.tabs.trigger("Config", value="config"),
            rx.tabs.trigger("Results", value="results"),
        ),
        rx.tabs.content(
            rx.vstack(
                rx.heading("Run", size="5"),
                rx.text("TODO: start/stop/kill + running config"),
                align="start",
                spacing="2",
            ),
            value="run",
        ),
        rx.tabs.content(
            rx.vstack(
                rx.heading("Config", size="5"),
                rx.text("TODO: config builder"),
                align="start",
                spacing="2",
            ),
            value="config",
        ),
        rx.tabs.content(
            rx.vstack(
                rx.heading("Results", size="5"),
                rx.text("TODO: results / logs / metrics"),
                align="start",
                spacing="2",
            ),
            value="results",
        ),
        default_value="run",
        width="100%",
    )

@rx.page(route="/instances/[instance_id]", title="Instance")
def instance_detail_page() -> rx.Component:
    # instance_id kommt später aus Router / State
    return page(
        rx.vstack(
            rx.heading("Instance Detail", size="7"),
            tabs(),
            spacing="4",
            align="start",
            width="100%",
        )
    )
