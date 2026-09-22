import flet as ft

from config import (
    CARD,
    PRIMARY,
    TEXT,
    MUTED,
    BORDER,
)


def reports_page(username):

    from login import users

    user = users.get(username, {})

    name = user.get("name", username)
    family = user.get("family", "")
    phone = user.get("phone", "-")
    age = user.get("age", "-")
    email = user.get("email", "-")

    return ft.Column(
        controls=[

            ft.Text(
                "گزارشات",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=TEXT,
            ),

            ft.Text(
                "گزارش اطلاعات کاربر",
                size=14,
                color=MUTED,
            ),

            ft.Container(height=15),

            ft.Container(
                width=float("inf"),
                padding=28,
                bgcolor=CARD,
                border_radius=14,

                shadow=ft.BoxShadow(
                    blur_radius=10,
                    color="#16000000",
                ),

                content=ft.Column(
                    controls=[

                        ft.Row(
                            controls=[

                                ft.Icon(
                                    ft.Icons.BAR_CHART,
                                    color=PRIMARY,
                                    size=30,
                                ),

                                ft.Text(
                                    "گزارش کاربر",
                                    size=21,
                                    weight=ft.FontWeight.BOLD,
                                    color=TEXT,
                                ),
                            ],

                            spacing=12,
                        ),

                        ft.Divider(
                            color=BORDER,
                        ),

                        ft.Text(
                            f"نام: {name}",
                            size=14,
                            color=TEXT,
                        ),

                        ft.Text(
                            f"نام خانوادگی: {family}",
                            size=14,
                            color=TEXT,
                        ),

                        ft.Text(
                            f"نام کاربری: {username}",
                            size=14,
                            color=TEXT,
                        ),

                        ft.Text(
                            f"سن: {age}",
                            size=14,
                            color=TEXT,
                        ),

                        ft.Text(
                            f"شماره تماس: {phone}",
                            size=14,
                            color=TEXT,
                        ),

                        ft.Text(
                            f"ایمیل: {email}",
                            size=14,
                            color=TEXT,
                        ),
                    ],

                    spacing=12,
                ),
            ),
        ],
    )