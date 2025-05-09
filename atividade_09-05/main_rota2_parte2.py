import flet as ft
from flet import AppBar, Text, ElevatedButton, View
from flet.core.colors import Colors
from models import *


def main(page: ft.Page):
    # Configuração das páginas
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def salvar(e):
        if (input_titulo.value == "" or input_descricao.value == ""
                or input_categoria.value == "" or input_autor.value == ""):
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            objeto_livro = Livro(
                titulo=input_titulo.value,
                categoria=input_categoria.value,
                descricao=input_descricao.value,
                autor=input_autor.value,
            )
            objeto_livro.save()
            input_titulo.value = ''
            input_descricao.value = ""
            input_categoria.value = ""
            input_autor.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    def detalhes(titulo, categoria, descricao, autor):
        txt_titulo.value = titulo
        txt_categoria.value = categoria
        txt_descricao.value = descricao
        txt_autor.value = autor

        page.update()
        page.go("/detalhes_livros")


    def livros(e):
        lv.controls.clear()
        sql_livros = select(Livro)
        resultado_livros = db_session.execute(sql_livros).scalars()

        for livro in resultado_livros:
            lv.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.BOOK),
                    title=ft.Text(f'Título: {livro.titulo}'),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="DETALHES", on_click=lambda _, l=livro: detalhes(l.titulo,l.categoria, l.descricao, l.autor)),
                        ]
                    )
                )
            )


    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Cadastrar"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_descricao,
                    input_categoria,
                    input_autor,
                    ft.Button(
                        "Salvar",
                        on_click=lambda _: salvar(e)
                    ),
                    ft.Button(
                        "Exibir lista",
                        on_click=lambda _: page.go("/lista_livros")
                    )
                ],
            )
        )

        if page.route == "/lista_livros" or page.route == "/detalhes_livros":
            livros(e)
            page.views.append(
                View(
                    "/lista_livros",
                    [
                        AppBar(title=Text("Livros"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv
                    ]
                )
            )

        if page.route == "/detalhes_livros":
            page.views.append(
                View(
                    "/detalhes_livros",
                    [
                        AppBar(title=Text("Detalhes"), bgcolor=Colors.SECONDARY_CONTAINER),
                        txt_titulo,
                        txt_descricao,
                        txt_categoria,
                        txt_autor,
                    ]
                )
            )
        page.update()


    # Criação de componentes
    input_titulo = ft.TextField(label="Titulo", hint_text="Digite o título do livro")
    input_descricao = ft.TextField(label="Descricao", hint_text="Digite uma breve descrição")
    input_categoria = ft.TextField(label="Categoria", hint_text="Digite uma categoria")
    input_autor = ft.TextField(label="Autor", hint_text="Digite o autor")
    lv = ft.ListView(
        height=500
    )

    msg_sucesso = ft.SnackBar(
        bgcolor=Colors.GREEN,
        content=ft.Text("Informações salvas com sucesso")
    )

    msg_error = ft.SnackBar(
        bgcolor=Colors.RED,
        content=ft.Text("Dados não inseridos não podem ser salvos")
    )

    txt_titulo = ft.Text()
    txt_descricao = ft.Text()
    txt_autor = ft.Text()
    txt_categoria = ft.Text()


    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar

    page.go(page.route)

ft.app(main)
