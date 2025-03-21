import flet as ft

def main(page: ft.Page):
    #Configuração das páginas
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT #ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    #Criar função
    def soma(e):
        try:
            soma = int(input_numero1.value) + int(input_numero2.value)
            txt_resultado.value=  f'Resultadoi = {soma}'
            page.update()

        except ValueError:
            txt_resultado.value = "Deve ser um número inteiro"

        page.update()


    def sub(e):
        try:
            subtracao = int(input_numero1.value) - int(input_numero2.value)
            txt_resultado.value = f'Resultadoi = {subtracao}'
            page.update()

        except ValueError:
           txt_resultado.value = "Deve ser um número inteiro"

        page.update()


    def mul(e):
        try:
            multiplicacao = int(input_numero1.value) * int(input_numero2.value)
            txt_resultado.value = f'Resultado = {multiplicacao}'

        except ValueError:
            txt_resultado.value = "Deve ser um número inteiro"

        page.update()

    def div(e):
        try:
            divisao = int(input_numero1.value) / int(input_numero2.value)
            if int(input_numero1.value) > 0 and int(input_numero2.value) > 0:
                txt_resultado.value = f'Resultado = {divisao}'

            else:
                txt_resultado.value = 'Os números devem ser maior que 0'

        except ValueError:
            txt_resultado.value = "Número inválido"

        page.update()


    #Criação de componentes
    input_numero1 = ft.TextField(label="Número", hint_text="Digite um número")
    input_numero2 = ft.TextField(label="Número", hint_text="Digite um número")
    btn_adicao = ft.FilledButton(
        text="Adição",
        width=page.window.width,
        on_click=soma
    )

    btn_subtracao = ft.FilledButton(
        text="Subtração",
        width=page.window.width,
        on_click=sub
    )

    btn_divisao = ft.FilledButton(
        text="Divisão",
        width=page.window.width,
        on_click=div
    )

    btn_multiplicacao = ft.FilledButton(
        text="Multiplicação",
        width=page.window.width,
        on_click=mul
    )

    txt_resultado = ft.Text(value="")

    #Criar layouts
    page.add(
        ft.Column(
            [
                input_numero1,
                input_numero2,
                btn_adicao,
                btn_subtracao,
                btn_divisao,
                btn_multiplicacao,
                txt_resultado,
            ]

        )
    )



ft.app(main)