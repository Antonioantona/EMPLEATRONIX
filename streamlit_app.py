import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("EMPLEATRONIX")
st.write("Todos los datos sobre los empleados en una aplicación.")

employees = pd.read_csv("employees.csv")
st.write(employees)


col0, col1, col2 = st.columns(3)

with col0:
  color = st.color_picker("Elige un color para las barras", "#3475B3")


with col1:
  nombre = st.toggle("Mostrar el nombre", True)

with col2:
  sueldo = st.toggle("Mostrar sueldo en la barra", False)


# Crear la gráfica de barras
fig, ax = plt.subplots()
if nombre and sueldo:
  ax.barh(employees['full name'], employees['salary'], color=color)
  for i, v in enumerate(employees['salary']):
    ax.text(v, i, f"{v}€", color='black', va='center')
elif nombre:
  ax.barh(employees['full name'], employees['salary'], color=color)
elif sueldo:
  ax.barh(range(len(employees)), employees['salary'], color=color)
  for i, v in enumerate(employees['salary']):
    ax.text(v, i, f"{v}€", color='black', va='center')
  ax.set_yticks(range(20))
  ax.set_yticklabels(['' for _ in range(20)])
else:
  ax.barh(range(len(employees)), employees['salary'], color=color)
  ax.set_yticks(range(20))
  ax.set_yticklabels(['' for _ in range(20)])


# Establecer el límite del eje X
ax.set_xlim(0, 4500)

# Mostrar la gráfica en Streamlit
st.pyplot(fig)



st.write("© José Antonio García Antona - CPIFP Alan Turing")