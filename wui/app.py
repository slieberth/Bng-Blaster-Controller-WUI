import reflex as rx

# Pages importieren reicht, damit rx sie registriert
from wui.pages.instances import instances_page
from wui.pages.instance_detail import instance_detail_page
from wui.pages.configs import configs_page
from wui.pages.settings import settings_page

app = rx.App()
