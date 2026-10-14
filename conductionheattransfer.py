import math
import streamlit as st

st.set_page_config(
    page_title="Conduction Heat Transfer Calculator",
    page_icon="🔥",
    layout="centered"
)

st.title("🔥 Conduction Heat Transfer Calculator")
st.write("Calculate steady-state heat conduction across plane, cylindrical, and spherical geometries.")

# Sidebar Navigation
st.sidebar.header("Geometry Selection")
option = st.sidebar.radio(
    "Select Wall Geometry:",
    ["Plane Wall", "Cylindrical Wall", "Spherical Wall"]
)

# ---------------------------------------------------------
# 1. Plane Wall Conduction
# ---------------------------------------------------------
if option == "Plane Wall":
    st.subheader("1D Heat Conduction: Plane Wall")
    st.latex(r"Q = \frac{k \cdot A \cdot (T_1 - T_2)}{L}")

    col1, col2 = st.columns(2)
    with col1:
        k = st.number_input("Thermal Conductivity (k in W/m·K)", value=15.0, min_value=0.001, step=0.1)
        A = st.number_input("Surface Area (A in m²)", value=2.0, min_value=0.001, step=0.1)
        L = st.number_input("Wall Thickness (L in m)", value=0.05, min_value=0.0001, step=0.01)
    with col2:
        T1 = st.number_input("Inner Temperature (T₁ in °C or K)", value=100.0, step=1.0)
        T2 = st.number_input("Outer Temperature (T₂ in °C or K)", value=25.0, step=1.0)

    if st.button("Calculate Heat Transfer Rate"):
        if L <= 0:
            st.error("Error: Thickness must be greater than zero.")
        else:
            Q = (k * A * (T1 - T2)) / L
            st.success("Calculation Complete!")
            st.metric(label="Heat Transfer Rate (Q)", value=f"{Q:.2f} W")

# ---------------------------------------------------------
# 2. Cylindrical Wall Conduction
# ---------------------------------------------------------
elif option == "Cylindrical Wall":
    st.subheader("1D Heat Conduction: Cylindrical Wall")
    st.latex(r"Q = \frac{2 \pi k L (T_1 - T_2)}{\ln(r_2 / r_1)}")

    col1, col2 = st.columns(2)
    with col1:
        k = st.number_input("Thermal Conductivity (k in W/m·K)", value=45.0, min_value=0.001, step=0.1)
        L = st.number_input("Cylinder Length (L in m)", value=1.0, min_value=0.001, step=0.1)
        T1 = st.number_input("Inner Surface Temp (T₁ in °C or K)", value=150.0, step=1.0)
        T2 = st.number_input("Outer Surface Temp (T₂ in °C or K)", value=30.0, step=1.0)
    with col2:
        r1 = st.number_input("Inner Radius (r₁ in m)", value=0.05, min_value=0.0001, step=0.01)
        r2 = st.number_input("Outer Radius (r₂ in m)", value=0.10, min_value=0.0001, step=0.01)

    if st.button("Calculate Heat Transfer Rate"):
        if r1 <= 0 or r2 <= 0:
            st.error("Error: Radii must be greater than zero.")
        elif r2 <= r1:
            st.error("Error: Outer radius (r₂) must be greater than inner radius (r₁).")
        else:
            Q = (2 * math.pi * k * L * (T1 - T2)) / math.log(r2 / r1)
            st.success("Calculation Complete!")
            st.metric(label="Heat Transfer Rate (Q)", value=f"{Q:.2f} W")

# ---------------------------------------------------------
# 3. Spherical Wall Conduction
# ---------------------------------------------------------
elif option == "Spherical Wall":
    st.subheader("1D Heat Conduction: Spherical Wall")
    st.latex(r"Q = \frac{4 \pi k r_1 r_2 (T_1 - T_2)}{r_2 - r_1}")

    col1, col2 = st.columns(2)
    with col1:
        k = st.number_input("Thermal Conductivity (k in W/m·K)", value=2.0, min_value=0.001, step=0.1)
        T1 = st.number_input("Inner Surface Temp (T₁ in °C or K)", value=200.0, step=1.0)
        T2 = st.number_input("Outer Surface Temp (T₂ in °C or K)", value=40.0, step=1.0)
    with col2:
        r1 = st.number_input("Inner Radius (r₁ in m)", value=0.1, min_value=0.0001, step=0.01)
        r2 = st.number_input("Outer Radius (r₂ in m)", value=0.2, min_value=0.0001, step=0.01)

    if st.button("Calculate Heat Transfer Rate"):
        if r1 <= 0 or r2 <= 0:
            st.error("Error: Radii must be greater than zero.")
        elif r2 <= r1:
            st.error("Error: Outer radius (r₂) must be greater than inner radius (r₁).")
        else:
            Q = (4 * math.pi * k * r1 * r2 * (T1 - T2)) / (r2 - r1)
            st.success("Calculation Complete!")
            st.metric(label="Heat Transfer Rate (Q)", value=f"{Q:.2f} W")
