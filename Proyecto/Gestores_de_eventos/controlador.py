import streamlit as st
import random
from Eventos.teatro import Teatro
from Eventos.bar import Bar
from Eventos.filantropico import Filantropico
from Gestores_de_eventos.gestor_eventos import Gestor_Eventos
from Eventos.cliente import Cliente
from Gestores_de_eventos.boleteria import Boleteria
from Gestores_de_eventos.reportes import Reportes

#En este archivo se piden todos los datos necesarios, se llaman a las funciones, entre otros.


class Controlador:
    def __init__(self):
        
        self.gestor_eventos = Gestor_Eventos() #Objeto de la clase Gestor_Eventos
        self.teatro = Teatro() # objeto de la clase Teatro
        self.bar = Bar() # objeto de la clase Bar
        self.filantropico = Filantropico() # objeto de la clase Filantropico
        self.boleteria = Boleteria() # objeto de la clase Boleteria
        self.reports = Reportes() # objeto de la clase Reportes
        
        
    """
    La función está encargada de crear un evento de tipo teatro, le va a pedir al administrador
    el tipo de ticket del que va a ser el evento, junto con todos los datos necesarios del evento
    luego verifica que el usuario haya rellenado por completo todos los campos, si es así, crea el evento
    y lo guarda en la sesión.
    """
    
    
    def create_event_theater(self):
        
        
        st.title("Welcome administrator, please input the next values")
        ticket_option = st.selectbox("The ticket is", options=[1, 2], format_func=lambda x: "Regular" if x == 1 else "Presale", key="ticket_option")
        type_of_ticket = "Regular" if ticket_option == 1 else "Presale"
        event_price = st.number_input("Please input the price of the ticket", key="wddw")

        aforo = st.number_input("Capacity of the theatre",key="aforo")
        event_status = st.text_input("State of the event",key="event_status")
        artist = st.text_input("Artist name", key = "artist")
        event_name = st.text_input("Event name", key ="event_name")
        event_date = st.text_input("Event date", key = "event_date")
        opening_time = st.text_input("Opening time",key = "opening_time")
        start_time = st.text_input("Start time", key = "start_time")
        event_location = st.text_input("Event location", key = "event_location")
        address = st.text_input("Address", key = "address")
        city = st.text_input("City", key = "city")
        event_id = self.teatro.number_to_id()
        
        if st.button("Create event", key = "dauwyduawd"):
            if all([type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city]):
                #
                object_theater = Teatro(type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city, 0, 0, event_id)
                # Guardar los datos en la sesión
                self.gestor_eventos.add_event(object_theater)
                
                st.success("The event was succesfully created")
            else:
                st.error("Fill all the blank camps")
        



    #El mismo procedimiento que la función anterior
    def create_event_bar(self):
       
        
        st.title("Welcome administrator, please input the next values")
        
        ticket_option = st.selectbox("The ticket is", options=[1, 2], format_func=lambda x: "Regular" if x == 1 else "Presale", key = "jkawhdvidhopke")
        type_of_ticket = "Regular" if ticket_option == 1 else "Presale"
        event_price = st.number_input("Please input the price of the ticket", key = "dwadwadw")

        aforo = st.number_input("Capacity of the bar", key = "daawdwad")
        event_status = st.text_input("State of the event", key ="w")
        artist = st.text_input("Artist name", key = "wdwadwadwa")
        event_name = st.text_input("Event name", key = "jadawhbda")
        event_date = st.text_input("Event date", key = "kjawdbahdwad")
        opening_time = st.text_input("Opening time", key = "kladabdadwd")
        start_time = st.text_input("Start time", key = "89371bnkm")
        event_location = st.text_input("Event location", key = "kldjhwvqd")
        address = st.text_input("Address", key = "ioiruf3ygq2eow")
        city = st.text_input("City", key = "jlkadhcawvdi")
        event_id = self.bar.number_to_id()
        
        if st.button("Create event", key = "jkdhbwf"):
            
            if all([type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city]):
                object_bar = Bar(type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city, 0, 0, event_id)
                # Guardar los datos en la sesión
                self.gestor_eventos.add_event(object_bar)
                
                st.success("The event was succesfully created")
                
            else:
                st.error("Please complete the blank camps")
        
        
        
    #Mismo procedimiento que la función anterior
    def create_event_filantropic(self):
        
        st.title("Welcome administrator, please input the next values")
        ticket_option = st.selectbox("The ticket is", options=[1, 2], format_func=lambda x: "Regular" if x == 1 else "Presale", key = "jwhduvadhw")
        type_of_ticket = "Regular" if ticket_option == 1 else "Presale"
        sponsor = st.text_input("Please input the sponsor name", key = "j213123")
        event_price = st.number_input(f"Hi {sponsor}, please input the amount of money you want to spend in this event", key = "jdawhdwk")
        aforo = st.number_input("Capacity of the filantropic event", key = "891238t124")
        event_status = st.text_input("State of the event", key = "idahbmawfe")
        artist = st.text_input("Artist name", key = "jkdabwada")
        event_name = st.text_input("Event name", key = "akjdbhawjdbaw")
        event_date = st.text_input("Event date", key = "jhfvaydnaw")
        opening_time = st.text_input("Opening time", key = "uidaywbna")
        start_time = st.text_input("Start time", key = "jdvagwdh")
        event_location = st.text_input("Event location", key = "kfjgvahbjdk")
        address = st.text_input("Address", key = "KLhjadvjbnk")
        city = st.text_input("City", key = "jkadyuybwa")
        event_id = self.filantropico.number_to_id()
        
        if st.button("Create event", key = "dawjdhgawdva"):
            
            if all([type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city]):
                filantropic = Filantropico(type_of_ticket, event_price, aforo, event_status, artist, event_name, event_date, opening_time, start_time, event_location, address, city, 0, 0, event_id)
                # Guardar los datos en la sesión
                self.gestor_eventos.add_event(filantropic)
                
                st.success("The event was succesfully created")
            else:
                st.error("Please complete the blank camps")
        
        """
        Esta función se encarga de registrar a los usuarios al evento, le pide al usuario que seleccione el tipo de evento al que quiere asistir
        o marcar asistencia al evento al que quiere asistir, luego le pide los datos necesarios para registrarlo, verifica que el usuario haya rellenado
        todos los campos y si es así, antes de completar el registro, comprueba que hayan espacios disponibles y que tenga el dinero suficiente para asistir
        al evento, si es así, lo registra y llama a las funciones necesarias para completar el registro.
        """
    
    def register_user_to_event(self):
        no_more_slots = False #Flag de parada
        user_id = str(random.randint(0, 10000)) #El id aleatorio que tendrá cada usuario
      
        
        st.title("Welcome user, please select the type of event you want to attend or mark attend to the event you want to attend")
        
        selected_event_type = st.selectbox("Select event type", options=["Teatro", "Bar", "Filantropico", "Register attendance"], key="event_type")
        if(selected_event_type == "Register attendance"): #Comprueba si lo que el usuario quiere hacer es registrar su asistencia al evento
            self.register_attend()
            
        else:
            
            ticket_type = st.selectbox("Select ticket type", options=["Presale", "Regular"], key="ticket_type")
            
            self.gestor_eventos.show_event(selected_event_type) #Muestra todos los eventos disponibles del tipo seleccionado
            
            #Pide los datos necesarios para registrar al usuario
                
            st.title("Welcome user, please input the next values")
            name = st.text_input("Name", key = "name")
            email = st.text_input("Email", key = "email")
            phone = st.text_input("Phone", key = "phone")
            address = st.text_input("Address", key = "address")
            city = st.text_input("City", key = "city")
            payment = st.text_input("Payment method", key = "payment")
            money = st.number_input("Money", key = "money")
            event_id = st.text_input("Write the ID of the event you want to enter", key = "awdwdawd")
            
                
            if st.button("Register", key = "register"):
                
                event = self.gestor_eventos.find_event(event_id)
                if(event.get_occupied_slots() == event.event_capacity()): #Comprueba que haya slots disponibles 
                    st.error("Sorry, there's no more slots available for this event")
                    no_more_slots = True
                    
                elif (money < event.event_price()): #Comprueba que tenga el dinero suficiente
                    st.error("You don't have enough money to attend this event")
                        
                elif all([name, email, phone, address, city, payment, money, event_id]) and not no_more_slots: #Comprueba que haya rellenado todos los espacios
                    st.success("The user was succesfully registered")
                    st.write(f"This is your ID, don't forget it!! {user_id}")
                    proffit = event.total_commision() #Las ganancias que se obtienen por la venta de tickets
                    client = Cliente(name, user_id, city, address, payment, email, phone, money, selected_event_type) #Crea un objeto de tipo cliente
                    self.boleteria.add_client(client) #Añade el cliente a la lista de clientes
                    self.boleteria.add_ticket(name, user_id, selected_event_type, event_id, ticket_type, payment) #Añade el ticket a la lista de tickets
                    event.add_ticket_sold() #Aumenta la cantida de tickets vendidos del evento
                    event.assign_slot_to_client() #Asigna un slot al cliente
                    event.add_proffit() #Añade las ganancias al evento
                    self.gestor_eventos.add_event_stats(payment, ticket_type, proffit) #Añade las estadísticas del evento
                    
                else:
                    st.error("Fill all the blank camps")
                    
                    
                    
    def register_attend(self):
        
        st.write("Welcome user, please input the next values to register your attendance") 
        
        event_id = st.text_input("Write the ID of the event you want to attend", key = "event_id")
        
        if (st.button("Register attendance", key = "register")):
            register = self.boleteria.register_attendance(event_id) #llama a la función que se encarga de verificar que el evento exista y que el usuario esté en la lista
            if not register:
                st.error("The event was not found or you're not in the list")
            else:
                st.success("You were succesfully registered")
                
    def edit_event(self):
        st.write("Welcome administrador, please select the type of event you want to edit")
        
        st.selectbox("Select event type", options=["-- Select a event --", "Theater", "Bar", "Filantropic"], key="event_type")
        event_id = st.text_input("Write the ID of the event you want to edit", key="event_id")
        type_of_ticket = st.text_input("Type of ticket", key="type_of_ticket")
        price = st.number_input("Price", key="price")
        capacity = st.number_input("Capacity", key="capacity")
        status = st.text_input("Status", key="status")
        artist = st.text_input("Artist", key="artist")
        event_name = st.text_input("Event name", key="event_name")
        event_date = st.text_input("Event date", key="event_date")
        opening_time = st.text_input("Opening time", key="opening_time")
        start_time = st.text_input("Start time", key="start_time")
        event_location = st.text_input("Event location", key="event_location")
        address = st.text_input("Address", key="address")
        city = st.text_input("City", key="city")
        if st.button("Edit event", key="edit"):
            self.gestor_eventos.edit_event(event_id, type_of_ticket, price, capacity, status, artist, event_name, event_date, opening_time, start_time, event_location, address, city)
            
        
        
    def delete_event(self):
        
        st.title("Welcome administrator, please select the type of event you want to delete")
        selected_event_type = st.selectbox("Select event type", options=["-- Select a event --", "Teatro", "Bar", "Filantropico"], key="event_type")
        event_id = st.text_input("Write the ID of the event you want to delete", key = "event_id")
        
        if st.button("Delete event", key = "delete"):
            self.gestor_eventos.delete_a_event(event_id) #Llama a la función que se encarga de eliminar el evento
            
            
    def generate_ticket(self):
    
        st.title("Welcome admin, please input the next values to generate your ticket")
        
        client_id = st.text_input("Write the ID of the client", key = "client_id")
        
        if st.button("Generate ticket", key = "generate"):
            self.boleteria.create_pdf(client_id) #Llama a la función que genera al pdf
            st.success("The ticket was succesfully generated")
            
            
    def events_stadistics(self):
        
        st.title("Welcome admin, please select the type of report you want to see.")
        
        type_of_report = st.selectbox("Select report type", options=["-- Select a report --", "Tickets sales", "Financial report", "Data client report", "Artist report"], key = "report")	
        
        if type_of_report == "Artist report":
            artist_name = st.text_input("Write the name of the artist", key = "artist_name")
            if st.button("Generate report", key = "generate"):
                self.reports.data_per_artist(artist_name)
        else:
        
            if st.button("Generate report", key = "generate"):
                """
                Esto es una alternativa para evitar el uso de distintos if anidados y para que se vea un poco más estetico
                genera un diccionario que como clave, es el tipo de reporte y como valor, la función que se encarga de generar el reporte
                """
                report_functions = {
                    "Tickets sales": self.reports.tickets_sales,
                    "Financial report": self.reports.financial_report,
                    "Data client report": self.reports.data_client_report,
                }
                try:
                    report_functions[type_of_report]() #Llama a la función que se encarga de generar el reporte
                except KeyError:
                    st.error("Please select a report")
        
        