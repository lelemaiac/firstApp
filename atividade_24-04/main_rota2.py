import flet as ft
from flet import AppBar, Text, ElevatedButton, View
from flet.core.colors import  Colors


class livros():
    def __init__(self, titulo, descricao, categoria, autor):
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.autor = autor

def main(page: ft.Page):
    #Configuração das páginas
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT #ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    lista = []

    def salvar(e):
        if (input_titulo.value == "" or input_descricao.value == ""
                or input_categoria.value == "" or input_autor.value == ""):
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            objeto_livro = livros(
                titulo=input_titulo.value,
                categoria=input_categoria.value,
                descricao=input_descricao.value,
                autor=input_autor.value,
            )

            lista.append(objeto_livro)
            input_titulo.value = ''
            input_descricao.value = ""
            input_categoria.value = ""
            input_autor.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()


    def exibir_lista(e):
        lv.controls.clear()
        for livros in lista:
            lv.controls.append(
                ft.Text(value=f'Titulo: {livros.titulo}, Descrição: {livros.descricao},'
                              f' Categoria: {livros.categoria}, Autor: {livros.autor}')
            )
        page.update()


    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Cadastarr"), bgcolor=Colors.PRIMARY_CONTAINER),
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
                        on_click=lambda _: page.go("/segunda")
                    )
                ],
            )
        )

        if page.route == "/segunda":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Dados"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv
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

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar

ft.app(main)