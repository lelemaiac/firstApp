import flet as ft
from flet import AppBar, Text, ElevatedButton, View
from flet.core.colors import  Colors


def main(page: ft.Page):
    #Configuração das páginas
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT #ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda")),
                ],
            )
        )
        page.update()

        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(f'Olá {input_nome.value}, seja bem vindo!'),
                    ]
                )
            )

            page.update()
    page.on_route_change = gerenciar_rotas
    page.go(page.route)

    # Criação de componentes
    input_nome = ft.TextField(label="Nome", hint_text="Digite seu nome")

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar

ft.app(main)