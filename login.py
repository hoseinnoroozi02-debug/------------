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

from register import show_register


# کاربران تست
users = {

    "hosein1387": {

        "password": "hosein",

        "name": "Hosein",

        "family": "Ahmadi",

        "email": "hosein@gmail.com",

        "age": "25",

        "phone": "09120000000",
    }

}


def show_login(page):


    username = ft.TextField(

        label="Username",

        hint_text="نام کاربری",

        width=340,

        bgcolor=INPUT,

        border_radius=8,
    )


    password = ft.TextField(

        label="Password",

        hint_text="رمز عبور",

        width=340,

        password=True,

        can_reveal_password=True,

        bgcolor=INPUT,

        border_radius=8,
    )


    message = ft.Text(

        "",

        size=13,

    )


    def login(e):


        user = username.value.strip()

        pwd = password.value



        if not user or not pwd:


            message.value = "Please fill all fields."

            message.color = RED

            page.update()

            return



        if user not in users:


            message.value = "User not found."

            message.color = RED

            page.update()

            return



        if users[user]["password"] != pwd:


            message.value = "Wrong password."

            message.color = RED

            page.update()

            return



        from welcome import show_welcome


        show_welcome(

            page,

            user

        )



    def go_register(e):


        show_register(page)



    page.clean()



    page.add(

        ft.Container(

            expand=True,

            bgcolor=BACKGROUND,

            alignment=ft.Alignment.CENTER,


            content=ft.Container(

                width=420,

                padding=40,

                bgcolor=CARD,

                border_radius=16,


                shadow=ft.BoxShadow(

                    blur_radius=20,

                    color="#22000000",

                ),


                content=ft.Column(

                    controls=[



                        ft.Container(

                            width=70,

                            height=70,

                            bgcolor=PRIMARY,

                            border_radius=20,

                            alignment=ft.Alignment.CENTER,


                            content=ft.Icon(

                                ft.Icons.GRID_VIEW,

                                size=40,

                                color=WHITE,

                            ),

                        ),



                        ft.Text(

                            "My Dashboard",

                            size=30,

                            weight=ft.FontWeight.BOLD,

                            color=TEXT,

                        ),



                        ft.Text(

                            "Login to your account",

                            size=14,

                            color=MUTED,

                        ),



                        ft.Container(height=10),



                        username,



                        password,



                        message,



                        ft.Button(

                            content="Login",

                            width=340,

                            height=45,

                            bgcolor=PRIMARY,

                            color=WHITE,

                            on_click=login,

                        ),



                        ft.TextButton(

                            "Create Account",

                            on_click=go_register,

                        ),

                    ],



                    spacing=15,



                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                ),

            ),

        )

    )



    page.update()