import panel as pn
import pandas as pd

# Cargar el dataset
train_df = pd.read_csv('train.csv')

# Función para filtrar los datos según la entrada del usuario
def filter_data(keyword=None, location=None):
    filtered = train_df.copy()
    if keyword:
        filtered = filtered[filtered['keyword'].str.contains(keyword, case=False, na=False)]
    if location:
        filtered = filtered[filtered['location'].str.contains(location, case=False, na=False)]
    return filtered

# Widgets para la entrada del usuario
keyword_input = pn.widgets.TextInput(name='Keyword', value='')
location_input = pn.widgets.TextInput(name='Location', value='')
button = pn.widgets.Button(name='Search', button_type='primary')

# Tabla para mostrar los resultados
table = pn.widgets.DataFrame(filter_data(), width=600, height=400)

# Función para actualizar la tabla cuando el usuario haga clic en el botón de búsqueda
def update(event):
    table.value = filter_data(keyword_input.value, location_input.value)

button.on_click(update)

# Organizar los widgets y la tabla en un layout
layout = pn.Column(
    pn.Row(keyword_input, location_input, button),
    table
)

# Mostrar la aplicación
layout.servable()
