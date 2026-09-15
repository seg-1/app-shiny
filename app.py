from shiny import App, ui, render
from shinywidgets import output_widget, render_widget
import plotly.graph_objects as go


app_ui = ui.page_fluid(
    ui.h1("Mi primera aplicación Shiny"),

    ui.input_slider(
        "n",
        "Elige un número:",
        min=1,
        max=100,
        value=50
    ),

    output_widget("grafico")
)


def server(input, output, session):

    @output
    @render_widget
    def grafico():

        valor = input.n()

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=valor,

                number={
                    "suffix": "%"
                },

                gauge={
                    "axis": {
                        "range": [0, 100]
                    },

                    "bar": {
                        "color": "#2E86DE"
                    },

                    "steps": [
                        {
                            "range": [0, 50],
                            "color": "#EAECEE"
                        },
                        {
                            "range": [50, 100],
                            "color": "#D6EAF8"
                        }
                    ]
                }
            )
        )

        fig.update_layout(
            height=300,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            )
        )

        return fig


app = App(app_ui, server)
