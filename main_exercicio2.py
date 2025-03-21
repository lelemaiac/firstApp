import flet as ft

def main(page: ft.Page):
    #Configuração das páginas
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT #ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    #Definição de funções
    def verificar_numero(e):
        try:
            num1 = int(input_numero.value)
            par_impar = num1 % 2
            if par_impar == 0:
                txt_resultado.value = "Par"
            else:
                txt_resultado.value = "Impar"
        except ValueError:
            print("Digite apenas números inteiros")
            
        page.update()


    # Criação de componentes
    input_numero = ft.TextField(label="Número", hint_text="Digite um número")
    btn_verificar = ft.FilledButton(
        text="Verificar",
        width=page.window.width,
        on_click=verificar_numero
    )
    txt_resultado = ft.Text(value="")


    #Criar layouts
    page.add(
        ft.Column(
            [
                input_numero,
                btn_verificar,
                txt_resultado,
            ]

        )
    )

ft.app(main)