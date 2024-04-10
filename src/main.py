import dash
import fonctions as cm
from dash import html
import os

# =============================================================#
# ===================== INITIALISATIONS ====================== #
# =============================================================#

# Créer une instance de Dash
app = dash.Dash(__name__)

# Charger les données et la carte
bookshops = cm.bookshop_locations()
m = cm.creer_carte(bookshops)

# =============================================================#
# ======================= MISE EN PAGE ======================= #
# =============================================================#

app.layout = html.Div(children=[
    # Carte
    html.Iframe(
        id="carte",
        srcDoc=m,
        style={"position": "absolute", "width": "100%", "height": "100%", "left": "0", "top": "0", "border": "none"}
    ),
    # Titre
    html.Div(
        children=[
            html.B("Les librairies de France", style={"fontSize": "24px", "font-family": "Roboto, sans-serif"}),
            html.Br(),
            html.B("Année des données : ", style={"fontSize": "15px", "font-family": "Roboto, sans-serif"}),
            html.B("2018", style={"fontSize": "15px", "font-family": "Roboto, sans-serif"})
        ],
        style={
            "position": "absolute",
            "top": "20px",
            "left": "20px",
            "color": "white",
            "backgroundColor": "rgba(0,0,0,0.5)",
            "border-radius": "10px",
            "padding": "10px",
            "font-family": "Roboto, sans-serif"
        }
    ),
    # Lien vers la source des données
    html.B(
        "Source des données : https://www.data.gouv.fr/fr/datasets/librairies-francaises/",
        style={"position": "absolute", "bottom": "20px", "right": "20px", "color": "white", "fontSize": "13px",
               "backgroundColor": "rgba(0,0,0,0.5)", "border-radius": "10px", "padding": "10px",
               "font-family": "Roboto, sans-serif"}
    )
])

# =============================================================#
# ======================= APP STARTUP ======================== #
# =============================================================#

# if __name__ == "__main__":
#    app.run_server(debug=False)

port = int(os.environ.get("PORT", 10000))
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=port)
    print("run")
