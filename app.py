from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.h1("Mi primera aplicación Shiny"),
    ui.input_slider(
        "n",
        "Elige un número:",
        min=1,
        max=100,
        value=50
    ),
    ui.output_text("resultado")
)


def server(input, output, session):

    @output
    @render.text
    def resultado():
        return f"Has elegido: {input.n()}"


app = App(app_ui, server)
