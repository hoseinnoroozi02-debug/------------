import flet as ft

from config import (
    BACKGROUND,
    CARD,
    PRIMARY,
    WHITE,
    TEXT,
    MUTED,
)


def show_welcome(page, username):

    from login import users

    user = users.get(username, {})

    name = user.get("name", username)

    def continue_to_main(e):

        from main_page import show_main_page

        show_main_page(page, username)

    def logout(e):

        from login import show_login

        show_login(page)

    page.clean()

    page.add(
        ft.Container(
            expand=True,
            bgcolor=BACKGROUND,
            alignment=ft.Alignment.CENTER,

            content=ft.Container(
                width=460,
                padding=45,
                bgcolor=CARD,
                border_radius=16,

                shadow=ft.BoxShadow(
                    blur_radius=20,
                    color="#22000000",
                ),

                content=ft.Column(
                    controls=[

                        ft.Container(
                            width=85,
                            height=85,
                            bgcolor=PRIMARY,
                            border_radius=50,
                            alignment=ft.Alignment.CENTER,

                            content=ft.Icon(
                                ft.Icons.PERSON,
                                size=55,
                                color=WHITE,
                            ),
                        ),

                        ft.Text(
                            "خوش آمدید",
                            size=30,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT,
                        ),

                        ft.Text(
                            f"سلام {name}",
                            size=20,
                            color=TEXT,
                        ),

                        ft.Text(
                            "شما با موفقیت وارد حساب کاربری شدید.",
                            size=14,
                            color=MUTED,
                        ),

                        ft.Container(height=15),

                        ft.Button(
                            content="ورود به داشبورد",
                            width=250,
                            height=45,
                            bgcolor=PRIMARY,
                            color=WHITE,
                            on_click=continue_to_main,
                        ),

                        ft.TextButton(
                            "خروج",
                            on_click=logout,
                        ),
                    ],

                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=14,
                ),
            ),
        )
    )

    page.update()