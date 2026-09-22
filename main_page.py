from menu.menu import show_menu


def show_main_page(page, username):

    show_menu(
        page,
        username,
        selected="dashboard",
    )