import dash

from dash import Dash, html, dcc, Input, Output, callback
import dash_daq as daq
import pandas as pd
from datetime import datetime
from dash.exceptions import PreventUpdate

# paso fundamental 1: nombramos app
app = dash.Dash(__name__)



# paso fundamental 2: figura / layout
app.layout = html.Div(
    [
        html.H1(
            "Hora Chile",
            style={
                'color': 'red',
                'text-align': 'center'
            }
        ),
        html.Div([
            daq.LEDDisplay(
                label={
                    'label': 'etiqueta label',
                    'style': {
                        'text-size': '0.5rem'
                    }
                },
                labelPosition="bottom",
                value='00:00',
                size=64,
            )
        ]),
        html.H2(
            id='reloj', 
            style={
                'color': 'blue',
                'textAlign': 'right'
            }
        ),
        dcc.Interval(
            id='componente',
            interval=1000,
            n_intervals=0
        ),
        html.Section([
            html.Span(
                id='spanId',
                style={
                    'color':'teal'
                },
                children = html.P(
                    "Texto Parrafo"
                )
            )
        ])
    ],
    style={
        'border': '1px solid #c2f1fa',
        'margin-top': '2.5rem',
        'backgroundColor': 'white'
    }

)


# callbacks
@app.callback(
    Output('reloj', 'children'),
    Input('componente', 'n_intervals')
)

# function reloj refresco
def actualizacion_hora(n):
    if n == 0:
        raise PreventUpdate
    else:
        hora_actual = datetime.now().strftime('%H:%M:%S')
        return hora_actual



# paso fundamental 3: levantar el servicio
if __name__ == '__main__':
    app.run_server(debug=True)