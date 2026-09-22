import flet as ft

from config import (
    CARD,
    PRIMARY,
    GREEN,
    ORANGE,
    TEXT,
    MUTED,
    BORDER,
)


def dashboard_page(username):

    from login import users

    user = users.get(username, {})

    name = user.get("name", username)
    family = user.get("family", "")
    phone = user.get("phone", "-")
    age = user.get("age", "-")
    email = user.get("email", "-")

    def summary_card(icon, icon_color, title, value):

        return ft.Container(
            expand=True,
            height=130,
            padding=20,
            bgcolor=CARD,
            border_radius=14,

            shadow=ft.BoxShadow(
                blur_radius=10,
                color="#16000000",
            ),

            content=ft.Column(
                controls=[

                    ft.Icon(
                        icon,
                        color=icon_color,
                        size=28,
                    ),

                    ft.Text(
                        title,
                        size=13,
                        color=MUTED,
                    ),

                    ft.Text(
                        str(value),
                        size=17,
                        weight=ft.FontWeight.BOLD,
                        color=TEXT,
                    ),
                ],

                spacing=7,
            ),
        )

    def info_row(title, value):

        return ft.Container(
            width=300,

            padding=ft.Padding.only(
                top=11,
                bottom=11,
            ),

            border=ft.Border(
                bottom=ft.BorderSide(
                    1,
                    BORDER,
                )
            ),

            content=ft.Row(
                controls=[

                    ft.Text(
                        title,
                        size=13,
                        color=MUTED,
                        width=115,
                    ),

                    ft.Text(
                        str(value),
                        size=13,
                        color=TEXT,
                    ),
                ],
            ),
        )

    return ft.Column(
        controls=[

            ft.Text(
                "داشبورد",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=TEXT,
            ),

            ft.Text(
                f"{name} خوش آمدید 👋",
                size=14,
                color=MUTED,
            ),

            ft.Container(height=15),

            ft.Row(
                controls=[

                    summary_card(
                        ft.Icons.PERSON,
                        PRIMARY,
                        "نام",
                        name,
                    ),

                    summary_card(
                        ft.Icons.ACCOUNT_CIRCLE,
                        GREEN,
                        "نام کاربری",
                        username,
                    ),

                    summary_card(
                        ft.Icons.PHONE,
                        ORANGE,
                        "شماره تماس",
                        phone,
                    ),
                ],

                spacing=14,
            ),

            ft.Container(height=20),

            ft.Container(
                width=float("inf"),
                padding=25,
                bgcolor=CARD,
                border_radius=14,

                shadow=ft.BoxShadow(
                    blur_radius=10,
                    color="#16000000",
                ),

                content=ft.Column(
                    controls=[

                        ft.Text(
                            "اطلاعات کاربر",
                            size=21,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT,
                        ),

                        ft.Container(height=10),

                        info_row(
                            "نام",
                            name,
                        ),

                        info_row(
                            "نام خانوادگی",
                            family,
                        ),

                        info_row(
                            "نام کاربری",
                            username,
                        ),

                        info_row(
                            "سن",
                            age,
                        ),

                        info_row(
                            "شماره تماس",
                            phone,
                        ),

                        info_row(
                            "ایمیل",
                            email,
                        ),
                    ],

                    spacing=0,
                ),
            ),
        ],

        spacing=4,
    )