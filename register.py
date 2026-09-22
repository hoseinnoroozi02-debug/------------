import flet as ft

from config import (
    BACKGROUND,
    CARD,
    INPUT,
    PRIMARY,
    TEXT,
    MUTED,
    WHITE,
    RED,
)


def show_register(page):

    name = ft.TextField(
        label="Name",
        hint_text="نام",
        width=340,
        bgcolor=INPUT,
    )

    family = ft.TextField(
        label="Family",
        hint_text="نام خانوادگی",
        width=340,
        bgcolor=INPUT,
    )

    username = ft.TextField(
        label="Username",
        hint_text="نام کاربری",
        width=340,
        bgcolor=INPUT,
    )

    email = ft.TextField(
        label="Email",
        hint_text="ایمیل",
        width=340,
        bgcolor=INPUT,
    )

    age = ft.TextField(
        label="Age",
        hint_text="سن",
        width=340,
        bgcolor=INPUT,
    )

    phone = ft.TextField(
        label="Phone",
        hint_text="شماره تماس",
        width=340,
        bgcolor=INPUT,
    )

    password = ft.TextField(
        label="Password",
        hint_text="رمز عبور",
        width=340,
        password=True,
        can_reveal_password=True,
        bgcolor=INPUT,
    )

    confirm_password = ft.TextField(
        label="Confirm Password",
        hint_text="تکرار رمز عبور",
        width=340,
        password=True,
        can_reveal_password=True,
        bgcolor=INPUT,
    )

    message = ft.Text(
        "",
        size=13,
    )

    def register(e):

        user = username.value.strip()

        pwd = password.value
        confirm = confirm_password.value

        if not user or not pwd or not confirm:

            message.value = "لطفاً اطلاعات ضروری را تکمیل کنید."
            message.color = RED

            page.update()
            return

        from login import users

        if user in users:

            message.value = "این نام کاربری قبلاً ثبت شده است."
            message.color = RED

            page.update()
            return

        if pwd != confirm:

            message.value = "رمز عبور و تکرار رمز عبور یکسان نیست."
            message.color = RED

            page.update()
            return

        users[user] = {
            "password": pwd,
            "name": name.value.strip() or user,
            "family": family.value.strip(),
            "email": email.value.strip(),
            "age": age.value.strip(),
            "phone": phone.value.strip(),
        }

        from welcome import show_welcome

        show_welcome(page, user)

    def back_to_login(e):

        from login import show_login

        show_login(page)

    page.clean()

    page.add(
        ft.Container(
            expand=True,
            bgcolor=BACKGROUND,
            alignment=ft.Alignment.CENTER,

            content=ft.Container(
                width=440,
                padding=35,
                bgcolor=CARD,
                border_radius=16,

                shadow=ft.BoxShadow(
                    blur_radius=20,
                    color="#22000000",
                ),

                content=ft.Column(
                    controls=[

                        ft.Text(
                            "Create Account",
                            size=28,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT,
                        ),

                        ft.Text(
                            "ایجاد حساب کاربری جدید",
                            size=14,
                            color=MUTED,
                        ),

                        ft.Container(height=5),

                        name,
                        family,
                        username,
                        email,
                        age,
                        phone,
                        password,
                        confirm_password,

                        message,

                        ft.Button(
                            content="ثبت‌نام",
                            width=340,
                            height=45,
                            bgcolor=PRIMARY,
                            color=WHITE,
                            on_click=register,
                        ),

                        ft.TextButton(
                            "بازگشت به صفحه ورود",
                            on_click=back_to_login,
                        ),
                    ],

                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    spacing=10,

                    scroll=ft.ScrollMode.AUTO,
                ),
            ),
        )
    )

    page.update()