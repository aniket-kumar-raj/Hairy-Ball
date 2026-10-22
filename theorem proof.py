import matplotlib.pyplot as plt
import numpy as np

t, p = np.linspace(0.1, np.pi - 0.1, 14), np.linspace(0, 2 * np.pi, 28)
T, P = np.meshgrid(t, p)
X, Y, Z = np.sin(T) * np.cos(P), np.sin(T) * np.sin(P), np.cos(T)

U, V, W = (
    -np.sin(P) * np.sin(T) - np.cos(T) * np.cos(P),
    np.cos(P) * np.sin(T) - np.cos(T) * np.sin(P),
    np.sin(T),
)
fig, ax = plt.subplots(subplot_kw={'projection': '3d'}, figsize=(7, 7))
ax.plot_surface(X,Y,Z, color='skyblue', edgecolor='none',zorder=1)
azim_deg=50
ax.view_init(elev=25, azim= azim_deg)
angle = np.radians(azim_deg)
mask = Y * np.cos(angle) + X * np.sin(angle) > -0.05

ax.quiver(
    X[mask],
    Y[mask],
    Z[mask],
    U[mask],
    V[mask],
    W[mask],
    length=0.22,
    normalize=True,
    color='crimson',
    zorder=2,
    )
ax.set_axis_off()
plt.title(
    'Hairy Ball Theorem1!!!!\n(you cannot com a hairy ball flat without creating at least one colick,tuft either blad spot)'
    ,fontsize =11)
plt.show()
