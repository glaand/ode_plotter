import streamlit as st

st.title("Glaand's ODE Plotter")

# Python initialisieren:
import matplotlib.pyplot as pl;
import numpy as np;

cols = st.columns(4)
with cols[0]:
    x_0 = st.number_input('x_0', value=0.0, step=1.0)
with cols[1]:
    x_E = st.number_input('x_E', value=20.0, step=1.0)
with cols[2]:
    y_0 = st.number_input('y_0', value=-5.0, step=1.0)
with cols[3]:
    y_E = st.number_input('y_E', value=5.0, step=1.0)

cols = st.columns(4)
with cols[0]:
    N_x = st.number_input('N_x', value=30, step=1)
with cols[1]:
    N_y = st.number_input('N_y', value=30, step=1)
with cols[2]:
    sc = st.number_input('sc', value=50.0, step=1.0)
with cols[3]:
    aw = st.number_input('aw', value=0.002, step=0.001)

formula = st.text_input('Differential function', '''(12-4*y)/15''')

# Parameter:
fig = 1;

# Funktionen:
def f(x, y): return eval(formula)

def v(x, y):
	v_x = np.divide(1, np.sqrt(1+f(x,y)**2), out=np.zeros_like(f(x,y)))
	v_y = np.divide(f(x,y), np.sqrt(1+f(x,y)**2), out=np.zeros_like(f(x,y)))
	return v_x,v_y;
# Daten:
x_data=np.linspace(x_0,x_E,N_x);
y_data=np.linspace(y_0,y_E,N_y);
[x_grid,y_grid]=np.meshgrid(x_data,y_data);
[v_x_grid,v_y_grid]=v(x_grid,y_grid);
# Plot:
fig, ax = pl.subplots(2, 1, figsize=(10,10))
ax[0].streamplot(x_grid,y_grid,v_x_grid,v_y_grid, density=[0.2,8], color='k', linewidth=1.0);
ax[1].quiver(x_grid,y_grid,v_x_grid,v_y_grid,np.sin(np.arctan2(v_x_grid, v_y_grid)),scale=sc,width=aw,angles='xy', cmap='Blues');
pl.xlabel('x'); pl.ylabel('y');
pl.grid(False);
pl.title('Richtungsvektorfeld');

st.pyplot(fig)