import ipywidgets as widgets
from IPython.display import display

# Widgets para la entrada de datos
capital_inicial_input = widgets.FloatText(
    value=1000.0,
    description='Capital Inicial:',
)

rentabilidad_input = widgets.FloatText(
    value=5.0,
    description='Rentabilidad (%):',
)

años_input = widgets.IntText(
    value=1,
    description='Años:',
)

# Botón de cálculo
calcular_btn = widgets.Button(
    description="Calcular",
    button_style='success'
)

# Función de cálculo
def calcular_capital_final(b):
    capital_inicial = capital_inicial_input.value
    rentabilidad = rentabilidad_input.value / 100
    años = años_input.value
    capital_final = capital_inicial * (1 + rentabilidad) ** años
    print(f"El capital final después de {años} años será: ${capital_final:,.2f}")

# Asociar la función al botón
calcular_btn.on_click(calcular_capital_final)

# Mostrar los widgets
display(capital_inicial_input, rentabilidad_input, años_input, calcular_btn)
