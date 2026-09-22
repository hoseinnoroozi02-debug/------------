import flet as ft

from config import (
    CARD,
    TEXT,
    MUTED,
)


def settings_page():

    notifications = ft.Switch(
        label="اعلان‌ها",
        value=True,
    )

    dark_mode = ft.Switch(
        label="حالت تاریک",
        value=False,
    )

    return ft.Column(
        controls=[

            ft.Text(
                "تنظیمات",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=TEXT,
            ),

            ft.Text(
                "تنظیمات حساب کاربری",
                size=14,
                color=MUTED,
            ),

            ft.Container(height=15),

            ft.Container(
                width=200,
                padding=24,
                bgcolor=CARD,
                border_radius=14,

                shadow=ft.BoxShadow(
                    blur_radius=10,
                    color="#16000000",
                ),

                content=ft.Column(
                    controls=[

                        ft.Text(
                            "تنظیمات برنامه",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT,
                        ),

                        notifications,

                        dark_mode,
                    ],

                    spacing=15,
                ),
            ),
        ],
    )