import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl

from Gestores_de_eventos.gestor_eventos import Gestor_Eventos
from Gestores_de_eventos.boleteria import Boleteria

class Reportes:
    def __init__(self):
        """
        Inicializa las variables que se van a utilizar en los reportes
        como por ejemplo las ganancias totales de todos los tipos de tickets, instancias de las clases boleteria y gestor de eventos
        y las listas de eventos, eventos_stats y clientes.
        """
        self.regular_tickets_proffit = 0.0
        self.presale_tickets_proffit = 0.0
        self.regular_tickets_sold = 0
        self.presale_tickets_sold = 0
        self.gestor = Gestor_Eventos()
        self.boleteria = Boleteria()
        self.events = self.gestor.get_events()
        self.events_stats = self.gestor.get_events_stats()
        self.clients = self.boleteria.get_clients_list()
    
    def set_regular_tickets_proffit(self): 
        
        for event in self.events: #Recorre toda la lista de eventos
            #Si el tipo de ticket es Regular, entonces se suma el proffit de ese evento a las ganancias totales de los tickets regulares
            if event.show_type_of_ticket() == "Regular":
                self.regular_tickets_proffit += event.get_proffit()
                self.regular_tickets_sold += 1
           
    
    def set_presale_tickets_proffit(self):
        
        for event in self.events:# Recorre toda la lista de eventos
            #Si el tipo de ticket es Presale, entonces se suma el proffit de ese evento a las ganancias totales de los tickets de preventa
            if event.show_type_of_ticket() == "Presale":
                self.presale_tickets_proffit += event.get_proffit()
                self.presale_tickets_sold += 1
    
    def tickets_sales(self):
        """
        Como no es necesario guardar las ganancias en un session state, simplemente se vuelven a llamar a estas funciones
        para obtener las ganancias de los tickets regulares y de preventa.
        """
        self.set_regular_tickets_proffit()
        self.set_presale_tickets_proffit()
        
        st.write("Tickets sales")
        st.write(f"Total regular tickets sold: {self.regular_tickets_sold}") #Muestra el total de tickets regulares vendidos
        st.write(f"Regular tickets proffit:  {self.regular_tickets_proffit}")
        st.write(f"Total presale tickets sold: {self.presale_tickets_sold}")
        st.write(f"Presale tickets proffit: {self.presale_tickets_proffit}")
        
    def financial_report(self):
        
        for payment, value in self.events_stats.items(): #Recorre el diccionario de eventos_stats
            #Como son diccionarios y estoy usando items, entonces value es otro diccionario y payment es la clave (del primer diccionario)
            
            st.write(f"Payment method: {payment}")
            for ticket_type, profit in value.items(): #La segunda clave del diccionario anidado y el valor (que son las ganancias)
                st.write(f"    Ticket type: {ticket_type}")
                st.write(f"    Profit: {profit}")
    
    
    """
    Genera un informe de datos del cliente.

    Este método crea un DataFrame de pandas con los datos de los clientes, incluido su ID, nombre, correo electrónico, número de teléfono y ciudad.
    Luego elimina cualquier dato duplicado según la columna 'ID de cliente'.
    Los datos se muestran en Streamlit usando la función st.write().
    Además, se crea un gráfico de histograma usando Plotly para mostrar la distribución de clientes por ciudad, que también se muestra en Streamlit.
    Los datos se exportan a un archivo de Excel llamado 'clients_data.xlsx' usando la función to_excel().
    Finalmente, se agrega un botón de descarga en Streamlit para permitir al usuario descargar el archivo de Excel.

    
    """
    def data_client_report(self):
    # Crear un DataFrame de pandas con los datos de los clientes
    
    
        data = {
            'Client ID': [],
            'Client Name': [],
            'Client Email': [],
            'Client Phone Number': [],
            'Client City': []
        }
        
        
        for client in self.clients:
            data['Client ID'].append(client.get_user_id())
            data['Client Name'].append(client.get_user_name())
            data['Client Email'].append(client.get_email())
            data['Client Phone Number'].append(client.get_phone_number())
            data['Client City'].append(client.get_city())
            
        df = pd.DataFrame(data)
        
        df.drop_duplicates(subset=['Client ID'], inplace=True) #Elimina datos duplicados del excel

        # Mostrar los datos en Streamlit
        st.write(df)

        # Crear gráficos con Plotly
        fig1 = px.histogram(df, x='Client City', title='Distribución de clientes por ciudad')
        

        # Mostrar los gráficos en Streamlit
        st.plotly_chart(fig1)

        # Exportar los datos a Excel
        df.to_excel('clients_data.xlsx', engine='openpyxl') 
        
        with open('clients_data.xlsx', 'rb') as file:
            st.download_button(
                label="Descargar datos de clientes",
                data=file,
                file_name='clients_data.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )   
    
    def data_per_artist(self, artist_name): #Función que se encarga de mostrar los datos de un artista en específico
        
        for event in self.events:
            if event.artist_name() == artist_name:
                st.text(f"Artist name: {artist_name}\nEvent name: {event.show_name()}\nDate: {event.show_date()}\nAddress: {event.show_address()}\nRemaining slots: {event.show_slots()} of {event.event_capacity()}\n")
                
    