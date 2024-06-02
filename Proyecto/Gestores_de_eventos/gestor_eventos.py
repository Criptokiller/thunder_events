import streamlit as st
from Eventos.teatro import Teatro
from Eventos.bar import Bar
from Eventos.filantropico import Filantropico  


class Gestor_Eventos:
    def __init__(self):
        if 'events' not in st.session_state:
            st.session_state['events'] = []
        if 'events_stats' not in st.session_state:
            st.session_state['events_stats'] = {}

        self.events = st.session_state['events']
        self.events_stats = st.session_state['events_stats']
        self.teatro = Teatro()
        self.bar = Bar()
        self.filantropico = Filantropico()
        
        
    def add_event(self, event): #Añade un evento a la lista de eventos
        self.events.append(event)
        st.session_state['events'] = self.events
    
    def add_event_stats(self, payment_method, ticket_type, proffit): #Añade las estadísticas de los eventos
        """
        Como toda esta información se guarda en un diccionario de diccionarios, se verifica si el método de pago ya está en el diccionario
        si no está entonces lo agrega como primera clave y como valor otro diccionario, que contendra de clave el tipo de ticket
        y como valor las ganancias de ese tipo de ticket.
        
        Si el metodo de pago ya está en el diccionario, entonces se verifica si el tipo de ticket ya está en el diccionario
        si no está entonces lo agrega como clave y como valor las ganancias de ese tipo de ticket.
        y si ya está, entonces simplemente actualiza las ganancias de ese tipo de ticket.
        
        """
        if payment_method not in self.events_stats: 
            self.events_stats[payment_method] = {ticket_type: proffit}
        else:
            if ticket_type not in self.events_stats[payment_method]:
                self.events_stats[payment_method][ticket_type] = proffit
            else:
                self.events_stats[payment_method][ticket_type] += proffit   
        
        st.session_state['events_stats'] = self.events_stats


    def delete_a_event(self, event_ID): #Hecho
        found = False #banderas para evitar el uso de break
        stop_list = False
        #La función enumerate obtiene el índice y el valor de la lista
        #Esto se hace debido a que los eventos se guardan en una lista, se tiene que acceder tanto al indice como al objeto que guarda la información dl evento
        for i, event in enumerate(self.events): 
            #Si no se ha encontrado el evento y el evento es de tipo Teatro, Bar o Filantropico y el id del evento es igual al id del evento que se quiere eliminar
            #Primero verifica que no tenga espacios ocupados o que el estado no sea realizado, para eliminarlo
            if not found and isinstance(event, (Teatro, Bar, Filantropico)) and event.show_event_id() == event_ID:
                if event.get_occupied_slots() > 0:
                    st.write("You can't delete an event with occupied slots")
                    found = True
                    stop_list = True
                elif event.show_state() == "Realizado":
                    st.write("You can't delete an event that has already been done")
                    found = True
                    stop_list = True
                else: 
                    
                    del self.events[i]
                    if not stop_list:
                        for j, session_event in enumerate(st.session_state['events']): #Se hace el mismo procedimiento con la lista que se guarda en la session de streamlit
                            if session_event.show_event_id() == event_ID:
                                del st.session_state['events'][j]
                                stop_list = True
                                st.success("Event deleted")
                    found = True
                    
    #Cambiar a otra parte, porque no va aquí
    def show_event(self, selected_event): #Hecho
        
        event_found = False
        for event in self.events:
 
            if selected_event == "Teatro" and isinstance(event, Teatro): #Comprueba si el evento es de tipo teatro
                event_found = True
                st.write("Type of event: Teatro")
                st.write(f"Artist: {event.artist_name()}") #Funciones para obtener los atributos de la instancia
                st.write(f"Event id: {event.show_event_id()}")  # Aquí estás accediendo a los atributos de la instancia
                st.write(f"Event name: {event.show_name()}")
                st.write(f"Event price: {event.event_price()}")
                st.write(f"Event date: {event.show_date()}")
                st.write(f"Event location: {event.show_location()}")
                st.write(f"Event address: {event.show_address()}")
                st.write(f"Event city: {event.show_city()}")
                st.write(f"Event status: {event.show_state()}")
                st.write(f"Avaible slots: {event.show_slots()}")
                
                
                    
            elif selected_event == "Bar" and isinstance(event, Bar):
                event_found = True
                st.write("Type of event: Bar")
                st.write(f"Artist: {event.artist_name()}")
                st.write(f"Event id: {event.show_event_id()}")
                st.write(f"Event name: {event.show_name()}")
                st.write(f"Event price: {event.event_price()}")
                st.write(f"Event date: {event.show_date()}")
                st.write(f"Event location: {event.show_location()}")
                st.write(f"Event address: {event.show_address()}")
                st.write(f"Event city: {event.show_city()}")
                st.write(f"Event status: {event.show_state()}")
                st.write(f"Avaible slots: {event.show_slots()}")
                
            
                    
            elif selected_event == "Filantropico" and isinstance(event, Filantropico):
                    event_found = True
                    st.write("Type of event: Filantropico")
                    st.write(f"Event id: {event.show_event_id()}")
                    st.write(f"Event name: {event.show_name()}")
                    st.write(f"Event price: {event.event_price()}")
                    st.write(f"Event date: {event.show_date()}")
                    st.write(f"Event location: {event.show_location()}")
                    st.write(f"Event address: {event.show_address()}")
                    st.write(f"Event city: {event.show_city()}")
                    st.write(f"Event status: {event.show_state()}")
                    st.write(f"Artist: {event.artist_name()}")
                    st.write(f"Avaible slots: {event.show_slots()}")
        if not event_found: #Si no encuentra el evento le manda un mensaje de error
            st.error("Event not found")  
            
                    
    def find_event(self, event_id): #Hecho
        found_event = None
        founded = False
        
        for event in self.events:
            #Como busca en toda la lista de los eventos, entonces comprueba si el evento "event" pertenece a alguna de esas clases de objetos
            #Si es así, entoncs guarda ese evento en una variable y la retorna, para su uso posterior
            if isinstance(event, (Teatro, Bar, Filantropico)) and event.show_event_id() == event_id:
                found_event = event
                founded = True
        if not founded:
            st.error("Sorry, the event was not found")  
            
        return found_event   
    
    def edit_event(self, event_id, type_of_ticket, price, capacity, status, artist, event_name, event_date, opening_time, start_time, event_location, address, city):
        for event in self.events:
            if event.show_state() == "Realizado":
                st.error("You can't edit a done event")
                
            elif isinstance(event, (Teatro, Bar, Filantropico)) and event.show_event_id() == event_id:
                event.update_data(type_of_ticket, price, capacity, status, artist, event_name, event_date, opening_time, start_time, event_location, address, city)
                st.success("Event updated")
            
            else:
                st.error("Event not found")
        
            
    def get_events(self): #Obtiene toda la lista de los eventos
        return self.events
    
    def get_events_stats(self): #Obtiene las estadísticas de los eventos
        return self.events_stats
    