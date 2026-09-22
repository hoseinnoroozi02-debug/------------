import flet as ft

from config import (
    CARD,
    PRIMARY,
    WHITE,
    TEXT,
    MUTED,
    BORDER,
)


def profile_page(username):

    from login import users

    user = users.get(username, {})

    name = user.get("name", username)
    family = user.get("family", "")
    email = user.get("email", "-")
    phone = user.get("phone", "-")
    age = user.get("age", "-")

    return ft.Column(
        controls=[

            ft.Text(
                "پروفایل کاربری",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=TEXT,
            ),

            ft.Text(
                "اطلاعات حساب کاربری",
                size=14,
                color=MUTED,
            ),

            ft.Container(height=15),

            ft.Container(
                width=float("inf"),
                padding=35,
                bgcolor=CARD,
                border_radius=14,

                shadow=ft.BoxShadow(
                    blur_radius=10,
                    color="#16000000",
                ),

                content=ft.Column(
                    controls=[

                        ft.Container(
                            width=76,
                            height=76,
                            bgcolor=PRIMARY,
                            border_radius=50,
                            alignment=ft.Alignment.CENTER,

                            content=ft.Icon(
                                ft.Icons.PERSON,
                                size=52,
                                color=WHITE,
                            ),
                        ),

                        ft.Text(
                            f"{name} {family}",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT,
                        ),

                        ft.Text(
                            f"@{username}",
                            size=14,
                            color=MUTED,
                        ),

                        ft.Container(height=5),

                        ft.Container(
                            height=1,
                            bgcolor=BORDER,
                        ),

                        ft.Container(height=5),

                        ft.Text(
                            f"ایمیل: {email}",
                            size=14,
                            color=TEXT,
                        ),

                        ft.Text(
                            f"شماره تماس: {phone}",
                            size=14,
                            color=TEXT,
                        ),

                        ft.Text(
                            f"سن: {age}",
                            size=14,
                            color=TEXT,
                        ),
                    ],

                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12,
                ),
            ),
        ],
    )