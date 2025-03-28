import flet as ft
from datetime import datetime

def main(page: ft.Page):
    #Configuração das páginas
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.LIGHT #ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667


    #Criar funções
    def calcular_idade(e):
        global conta
        data_nascimento = datetime.strptime(input_nascimento.value, "%d/%m/%Y")
        data_atual = datetime.today()
        data_atual_str = data_atual.strftime("%d/%m/%Y")
        idade = int(str((data_atual.year - data_nascimento.year)))
        mes_atual = datetime.today().month
        dia_atual = datetime.today().day

        try:
            if mes_atual < data_nascimento.month:
                idade = idade - 1

            elif mes_atual == data_nascimento.month:
                if dia_atual < data_nascimento.day:
                    idade = idade - 1

            if idade > 0 and idade < 120:
                if idade >= 18:
                    txt_resultado.value = f"Ele tem {idade} anos, então é maior de idade"

                elif idade < 18:
                    txt_resultado.value = f"Ele tem {idade} anos, então é menor de idade"

                else:
                    txt_resultado.value = "Idade inválida!"

            else:
                txt_resultado.value = "Informação inválida"

        except ValueError:
            txt_resultado.value = "Data inválida"

        page.update()


    # Criação de componentes
    input_nascimento = ft.TextField(label="Data de nascimento", hint_text="Digite sua data de nascimento")
    btn_verificar = ft.FilledButton(
        text="Verificar idade",
        width=page.window.width,
        on_click=calcular_idade,
    )

    txt_resultado = ft.Text(value="")

    #Criar layouts
    page.add(
        ft.Column(
            [
                input_nascimento,
                txt_resultado,
                btn_verificar,
            ]

        )
    )



ft.app(main)
