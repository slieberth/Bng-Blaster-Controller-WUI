"""
Main Reflex app definition.

This file registers all pages (routes) explicitly to avoid 404s when navigating
directly to URLs such as /instances.
"""

import reflex as rx

from wui.pages.index import index
from wui.pages.instances import instances_page
from wui.pages.config import config_page
from wui.pages.results import results_page


def make_app() -> rx.App:
    """Create and configure the Reflex application."""
    app = rx.App()

    # Explicit route registration
    app.add_page(index, route="/", title="BNG Blaster Controller WUI")
    app.add_page(instances_page, route="/instances", title="Instances")
    app.add_page(config_page, route="/config", title="Config Builder")
    app.add_page(results_page, route="/results", title="Results")

    return app


app = make_app()
