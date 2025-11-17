import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import dot, random

dati = pd.read_csv("data.csv")

X = dati.iloc[:, :-1].to_numpy()
y = dati.iloc[:, -1].to_numpy()

#####

# Inizializza i pesi
pesi = random.rand(X.shape[1])

# Allena il modello
for _ in range(1000):  # Numero di iterazioni
    previsioni = dot(X, pesi)
    errori = y - previsioni
    gradiente = dot(X.T, errori) / len(X)
    pesi += 0.01 * gradiente  # Tasso di apprendimento

# Prevedi
y_pred = dot(X, pesi)
#####

fig, assi = plt.subplots(
    1, 2, figsize=(8, 4), subplot_kw=dict(projection="3d")
)
for azim, asse in zip([0, 20], assi):
    asse.scatter(X[:, 0], X[:, 1], y, color="black", label="Dati")

    x_surf, y_surf = np.meshgrid(
        np.linspace(X[:, 0].min(), X[:, 0].max(), 100),
        np.linspace(X[:, 1].min(), X[:, 1].max(), 100),
    )
    z_surf = (np.array([x_surf.ravel(), y_surf.ravel()]).T @ pesi).reshape(
        x_surf.shape
    )

    asse.plot_surface(
        x_surf, y_surf, z_surf, color="#000", alpha=0.2, label="Superficie Modello"
    )
    asse.set_xlabel("Peso (ton)")
    asse.set_ylabel("Cilindrata (L)")
    asse.set_zlabel("Consumo (L/100km)")
    asse.view_init(elev=30, azim=azim)  # Aggiungi rotazione
    plt.title("Dati e modello")
plt.show()
#####
