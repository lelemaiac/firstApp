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
                    AppBar(title=Text("Cadastarr"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo, input_descricao, input_categoria, input_autor,
                    ElevatedButton(text="Enviar", on_click=lambda _: page.go("/segunda")),
                ],
            )
        )

        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Dados"), bgcolor=Colors.SECONDARY_CONTAINER),
                        Text(f'Título: {input_titulo.value}'),
                        Text(f'Descrição: {input_descricao.value}'),
                        Text(f'Categoria: {input_categoria.value}'),
                        Text(f'Autor: {input_autor.value}'),
                    ]
                )
            )
        page.update()
    page.on_route_change = gerenciar_rotas
    page.go(page.route)

    # Criação de componentes
    input_titulo = ft.TextField(label="Titulo", hint_text="Digite o título do livro")
    input_descricao = ft.TextField(label="Descricao", hint_text="Digite uma breve descrição")
    input_categoria = ft.TextField(label="Categoria", hint_text="Digite uma categoria")
    input_autor = ft.TextField(label="Autor", hint_text="Digite o autor")

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar

ft.app(main)