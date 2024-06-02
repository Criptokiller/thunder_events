import streamlit as st
from streamlit_option_menu import option_menu
from Gestores_de_eventos.controlador import Controlador



class Interfaz:
    def __init__(self):
        # Crea un estado de sesión
        if 'user_type' not in st.session_state:
            st.session_state['user_type'] = None
        self.controlador = Controlador() #Guardar en un sesion state un controlador
        

    def interfaz_function(self):
        

        with st.sidebar:
            selected = option_menu(
                menu_title = "Welcome to Thunder events",
                options = ["User", "Administrator"]
            )
            if selected == "User":
                st.image("./imagenes_decorativas/fondo_usuario.jpg", use_column_width=True)
                if st.button('Usuario', key="button_usuario"):
            
                    st.session_state['user_type'] = 'Usuario'  # Guarda el tipo de usuario en el estado de la sesión
            # En la segunda columna, muestra la imagen y el botón de 'Administrador'
            elif selected == "Administrator":
                st.image("./imagenes_decorativas/fondo_administrador.jpg", use_column_width=True)
                if st.button('Administrador', key="button_administrador"):
                    st.session_state['user_type'] = 'Administrador'  # Guarda el tipo de usuario en el estado de la sesión
                    self.admin_interfaz()  # Llama a la función admin_interfaz
                    
                
                    
    def user_interfaz(self):
        # Si el tipo de usuario es 'Usuario', muestra la interfaz de usuario
        if st.session_state['user_type'] == 'Usuario':
            st.write('Bienvenido Usuario')
            activity = st.selectbox("¿What do you want to do??", ["Register to an event"], key = "jkabawdbjawjnawd")
            if activity == "Register to an event":
                self.controlador.register_user_to_event()
        
            
    
    def admin_interfaz(self):
        if st.session_state['user_type'] == 'Administrador':
            password = st.text_input("Please input the password", type="password", key="padjwannfjdjuejeefewefwef")
            if password == "admin":  # Reemplaza "contraseña_correcta" con la contraseña real
                st.session_state['user_type'] = 'Administrador'  # Guarda el tipo de usuario en el estado de la sesión
                self.admin_actions()  # Llama a la función admin_actions
            else:
                st.write('Wrong password. Please try again.')
                

    def admin_actions(self): # Cambiar por un nombre diferente como "draw"
        action = st.selectbox("¿What do you want to do?", ["Create event", "Delete event", "Edit a event", "Show stadistics", "Generate ticket"],key="admin_action")
        
       
        if action == "Create event":
            event_type = st.selectbox("¿What type of event you want to create?", ["--- Selection ---", "Theater", "Bar", "Filantropic"], key="event_type")
            
            options = {
                "Theater": self.controlador.create_event_theater,
                "Bar": self.controlador.create_event_bar,
                "Filantropic": self.controlador.create_event_filantropic
            }
            try:
                options[event_type]()
            except KeyError:
                st.error("You didn't select any option. Please select an option.")
           
        elif action == "Delete event":
            self.controlador.delete_event()
            
        elif action == "Show stadistics":
            self.controlador.events_stadistics()
            
        elif action == "Generate ticket":
            self.controlador.generate_ticket()
            
        elif action == "Edit a event":
            self.controlador.edit_event()