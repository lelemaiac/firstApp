import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from models import *


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de listas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667


    def salvar(e):
        if input_nome.value == "" or input_profissao.value == "" or input_salario.value == "":
            page.overlay.append(msg_error)
            msg_error.open= True
            page.update()

        else:
            salario = input_salario.value

            if not salario.isnumeric():
                input_salario.error = True
                input_salario.error_text = "Preencha este campo com números inteiros"
                page.update()
                return

            objeto_usuario = Usuario(
                nome=input_nome.value,
                profissao=input_profissao.value,
                salario=input_salario.value
            )

            objeto_usuario.save()
            input_nome.value = ''
            input_salario.value = ""
            input_profissao.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()


    def detalhes(nome, profissao, salario):
        txt_nome.value = nome
        txt_profissao.value = profissao
        txt_salario.value = salario

        page.update()
        page.go("/detalhes_usuarios")

    def usuarios(e):
        lv.controls.clear()
        sql_usuarios = select(Usuario)
        resultado_usuario = db_session.execute(sql_usuarios).scalars()

        for usuario in resultado_usuario:
            lv.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f'Nome: {usuario.nome}'),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text="DETALHES", on_click=lambda _, u=usuario: detalhes(u.nome, u.profissao, u.salario)),
                        ]
                    )
                )
            )


    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    input_salario,
                    input_profissao,
                    ft.Button(
                        "Salvar",
                        on_click=lambda _: salvar(e)
                    ),
                    ft.Button(
                        "Exibir lista",
                        on_click=lambda _: page.go("/lista_usuarios")
                    )
                ],
            )
        )
        if page.route == "/lista_usuarios" or page.route == "/detalhes_usuarios":
            usuarios(e)
            page.views.append(
                View(
                    "/lista_usuarios",
                    [
                        AppBar(title=Text("Lista"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv,
                    ],
                )
            )

        if page.route == "/detalhes_usuarios":
            page.views.append(
                View(
                    "/detalhes_usuarios",
                    [
                        AppBar(title=Text("Detalhes"), bgcolor=Colors.SECONDARY_CONTAINER),
                        txt_nome,
                        txt_profissao,
                        txt_salario,
                    ]
                )
            )
        page.update()



    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    input_nome = ft.TextField(label="Nome")
    input_profissao = ft.TextField(label="Profissão")
    input_salario = ft.TextField(label="Salário")

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

    txt_nome = ft.Text()
    txt_profissao = ft.Text()
    txt_salario = ft.Text()


    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)