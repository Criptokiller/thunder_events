import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from interfaz import Interfaz


def main():
    # Crea una instancia de Interfaz
    
    interview = Interfaz()

    if 'show_login' not in st.session_state:
        st.session_state['show_login'] = False
    st.image("./imagenes_decorativas/fondo_usuario.jpg")  

    st.markdown("# Bienvenido a Thunder events")

    if st.button("Entrar", key="button_entrar"):
        # Cuando el usuario haga clic en el botón "Entrar", cambia 'show_login' a True
        st.session_state['show_login'] = True
        

    # Solo muestra el cuadro de usuario y administrador si 'show_login' es True
    if st.session_state['show_login']:
        interview.interfaz_function()  # Llama a la función de tu archivo interfaz.py

    # Si 'user_type' existe en st.session_state, entonces verifica el tipo de usuario
    if 'user_type' in st.session_state:
        # Si el tipo de usuario es 'Usuario', muestra la interfaz del usuario
        if st.session_state['user_type'] == 'Usuario':
            interview.user_interfaz()

        # Si el tipo de usuario es 'Administrador', muestra la interfaz del administrador
        if st.session_state['user_type'] == 'Administrador':
           interview.admin_interfaz()


if __name__ == "__main__":
    main()