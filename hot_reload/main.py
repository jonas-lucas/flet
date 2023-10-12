import flet as ft  # type: ignore
from flet import Text


def main(page: ft.Page) -> None:
    page.title = 'Some Text'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.theme_mode = 'light'

    text: Text = Text(
        value='This is some text',
        text_align=ft.TextAlign.CENTER,
        width=200,
        size=30,
        color='red'
    )

    page.add(text)


# flet run hot_reload/main.py
if __name__ == '__main__':
    ft.app(target=main)
