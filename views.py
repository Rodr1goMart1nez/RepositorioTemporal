import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.io as pio
from django.shortcuts import render

def fraude_mensual_view(request):
    # ... Tus datos y código para crear 'fig' (mismo que antes) ...
    data = {
        "Mes": ["ENE 25", "FEB 25", "MAR 25", "ABR 25", "MAY 25"],
        "AMEX": [43222, 37937, 32188, 43320, 54622],
        "VISA": [273799, 424020, 244443, 257993, 362781],
        "MC": [266308, 136400, 67439, 45347, 34229],
        "CANTIDAD_25": [1338, 1313, 1444, 1104, 1702],
    }
    df = pd.DataFrame(data)

    fig = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        row_heights=[0.7, 0.3],
        vertical_spacing=0.04,
        specs=[[{"secondary_y": True}], [{"type": "table"}]]
    )

    # Añade tus trazos aquí (igual que antes)
    fig.add_trace(go.Bar(x=df["Mes"], y=df["MC"], name="MASTERCARD", marker_color="#F28B2C"), row=1, col=1, secondary_y=False)
    fig.add_trace(go.Bar(x=df["Mes"], y=df["VISA"], name="VISA", marker_color="#B2B2B2"), row=1, col=1, secondary_y=False)
    fig.add_trace(go.Bar(x=df["Mes"], y=df["AMEX"], name="AMEX", marker_color="#4A7DB8"), row=1, col=1, secondary_y=False)
    fig.add_trace(go.Scatter(
        x=df["Mes"], y=df["CANTIDAD_25"], name="CANTIDAD_25", mode='lines+markers+text',
        line=dict(color='black', width=2),
        text=[str(i) for i in df["CANTIDAD_25"]],
        textposition="top center"
    ), row=1, col=1, secondary_y=True)
    fig.add_trace(go.Table(
        header=dict(
            values=["<b></b>", "<b>ENE 25</b>", "<b>FEB 25</b>", "<b>MAR 25</b>", "<b>ABR 25</b>", "<b>MAY 25</b>"],
            align='center',
            fill_color="white",
            line_color="#308CFF"
        ),
        cells=dict(
            values=[
                ["AMEX", "VISA", "MC"],
                ["43.222", "273.799", "266.308"],
                ["37.937", "424.020", "136.400"],
                ["32.188", "244.443", "67.439"],
                ["43.320", "257.993", "45.347"],
                ["54.622", "362.781", "34.229"],
            ],
            align='center',
            fill_color=[["white", "#F4F4F4"]*3],
            line_color="#308CFF"
        ),
    ), row=2, col=1)

    fig.update_layout(
        title="Evolución Mensual del Fraude por Marca",
        barmode='group',
        legend=dict(orientation="h", yanchor="bottom", y=1.08, xanchor="center", x=0.5),
        height=700,
        margin=dict(t=70, b=30)
    )

    fig.update_yaxes(
        row=1, col=1, secondary_y=False,
        title_text="0 mil",
        showgrid=True,
        gridcolor="#cccccc",
        tickformat=",.0f",
        tickvals=[0, 100_000, 200_000, 300_000, 400_000],
        ticktext=["0 mil", "100 mil", "200 mil", "300 mil", "400 mil"]
    )
    fig.update_yaxes(
        row=1, col=1, secondary_y=True,
        title_text="",
        showgrid=False,
        tickvals=[400, 600, 800, 1000, 1200, 1400, 1600, 1800],
    )

    # Genera el HTML del gráfico
    plot_html = pio.to_html(fig, full_html=False)

    return render(request, 'fraude_mensual.html', {'plot_html': plot_html})