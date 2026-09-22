import flet as ft

from config import (
    SIDEBAR,
    SIDEBAR_ACTIVE,
    BACKGROUND,
    CARD,
    PRIMARY,
    WHITE,
    TEXT,
    MUTED,
    BORDER,
)

from menu.dashboard import dashboard_page
from menu.profile import profile_page
from menu.reports import reports_page
from menu.settings import settings_page


def show_menu(page, username, selected="dashboard"):

    from login import users

    user = users.get(username, {})

    name = user.get("name", username)
    family = user.get("family", "")

    page.clean()

    # -------------------------------
    # Navigation
    # -------------------------------

    def navigate(section):

        show_menu(
            page,
            username,
            selected=section,
        )

    def logout(e):

        from login import show_login

        show_login(page)

    # -------------------------------
    # Sidebar Item
    # -------------------------------

    def sidebar_item(icon, title, section):

        active = selected == section

        return ft.Container(
            height=48,
            padding=12,
            border_radius=8,

            bgcolor=(
                SIDEBAR_ACTIVE
                if active
                else None
            ),

            on_click=lambda e: navigate(section),

            content=ft.Row(
                controls=[

                    ft.Icon(
                        icon,
                        color=WHITE,
                        size=20,
                    ),

                    ft.Text(
                        title,
                        color=WHITE,
                        size=14,
                    ),
                ],

                spacing=13,
            ),
        )

    # -------------------------------
    # Sidebar
    # -------------------------------

    sidebar = ft.Container(
        width=210,
        bgcolor=SIDEBAR,
        padding=14,

        content=ft.Column(
            controls=[

                ft.Container(
                    padding=15,

                    content=ft.Column(
                        controls=[

                            ft.Icon(
                                ft.Icons.GRID_VIEW,
                                color=WHITE,
                                size=38,
                            ),

                            ft.Text(
                                "My Dashboard",
                                size=19,
                                weight=ft.FontWeight.BOLD,
                                color=WHITE,
                            ),
                        ],

                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=15,
                    ),
                ),

                ft.Divider(
                    color="#334155",
                ),

                sidebar_item(
                    ft.Icons.HOME,
                    "داشبورد",
                    "dashboard",
                ),

                sidebar_item(
                    ft.Icons.PERSON,
                    "پروفایل",
                    "profile",
                ),

                sidebar_item(
                    ft.Icons.BAR_CHART,
                    "گزارشات",
                    "reports",
                ),

                sidebar_item(
                    ft.Icons.SETTINGS,
                    "تنظیمات",
                    "settings",
                ),

                ft.Container(
                    expand=True,
                ),

                ft.Divider(
                    color="#334155",
                ),

                ft.Container(
                    height=48,
                    padding=12,
                    border_radius=8,
                    on_click=logout,

                    content=ft.Row(
                        controls=[

                            ft.Icon(
                                ft.Icons.LOGOUT,
                                color=WHITE,
                                size=20,
                            ),

                            ft.Text(
                                "خروج",
                                color=WHITE,
                                size=14,
                            ),
                        ],

                        spacing=13,
                    ),
                ),
            ],
        ),
    )

    # -------------------------------
    # Page Content
    # -------------------------------

    if selected == "profile":

        current_page = profile_page(username)

    elif selected == "reports":

        current_page = reports_page(username)

    elif selected == "settings":

        current_page = settings_page()

    else:

        current_page = dashboard_page(username)

    # -------------------------------
    # User Avatar
    # -------------------------------

    if name:

        avatar_letter = name[0].lower()

    elif username:

        avatar_letter = username[0].lower()

    else:

        avatar_letter = "u"

    # -------------------------------
    # Header
    # -------------------------------

    header = ft.Container(
        height=62,
        bgcolor=CARD,

        padding=ft.Padding.only(
            left=22,
            right=22,
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
                    "پنل مدیریت",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=TEXT,
                ),

                ft.Container(
                    expand=True,
                ),

                ft.Column(
                    controls=[

                        ft.Text(
                            f"{name} {family}",
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT,
                        ),

                        ft.Text(
                            f"@{username}",
                            size=11,
                            color=MUTED,
                        ),
                    ],

                    spacing=0,

                    horizontal_alignment=ft.CrossAxisAlignment.END,
                ),

                ft.Container(
                    width=40,
                    height=40,
                    bgcolor=PRIMARY,
                    border_radius=25,
                    alignment=ft.Alignment.CENTER,

                    content=ft.Text(
                        avatar_letter,
                        color=WHITE,
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),
            ],

            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    # -------------------------------
    # Main Body
    # -------------------------------

    body = ft.Container(
        expand=True,
        bgcolor=BACKGROUND,
        padding=22,

        content=ft.Column(
            controls=[
                current_page,
            ],

            expand=True,
            scroll=ft.ScrollMode.AUTO,
        ),
    )

    # -------------------------------
    # Footer
    # -------------------------------

    footer = ft.Container(
        height=42,
        bgcolor=CARD,
        alignment=ft.Alignment.CENTER,

        border=ft.Border(
            top=ft.BorderSide(
                1,
                BORDER,
            )
        ),

        content=ft.Text(
            "© 2026 My Dashboard   |   ساخته شده با Python و Flet",
            size=11,
            color=MUTED,
        ),
    )

    # -------------------------------
    # Final Layout
    # -------------------------------

    page.add(
        ft.Row(
            controls=[

                sidebar,

                ft.Column(
                    controls=[

                        header,

                        body,

                        footer,
                    ],

                    expand=True,
                    spacing=0,
                ),
            ],

            expand=True,
            spacing=0,
        )
    )

    page.update()