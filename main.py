import flet as ft

from config import BACKGROUND
from login import show_login


def main(page: ft.Page):

    page.title = "My Dashboard"

    page.padding = 0
    page.spacing = 0

    page.bgcolor = BACKGROUND

    page.theme_mode = ft.ThemeMode.LIGHT

    show_login(page)


ft.run(main)