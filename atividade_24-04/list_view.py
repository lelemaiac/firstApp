import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors

class usuario():
    def __init__(self, nome, salario, profissao):
        self.nome = nome
        self.salario = salario
        self.profissao = profissao

def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de listas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []

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

            objeto_usuario = usuario(
                nome=input_nome.value,
                profissao=input_profissao.value,
                salario=input_salario.value
            )

            lista.append(objeto_usuario)
            input_nome.value = ''
            input_salario.value = ""
            input_profissao.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()


    def exibir_lista(e):
        lv.controls.clear()
        for usuarios in lista:
            lv.controls.append(
                ft.Text(value=f'Nome: {usuarios.nome}, Salário: {usuarios.salario}, Profissao: {usuarios.profissao}')
            )
        page.update()

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
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv,
                    ],
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

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)