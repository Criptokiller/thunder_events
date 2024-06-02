from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

"""
    Exporto una libreria que me permite generar un pdf, en base a la información de un ticket
    
    La función recibe como parámetros la instancia de la boletería, los tickets, el id del cliente y el gestor de eventos.
    esto para poder acceder a los metodos que estos poseen, y obtener la información necesaria para generar el pdf.
    
    Luego los ciclos for sirven para recorrer los tickets y los eventos, y obtener la información del ticket que se desea generar.
    el motivo dde por el cual se usa isinstance es para verificar si el ticket es de la instancia de la boletería, y si el id del cliente
    ya que de lo contrario no tendría forma de obtener la información del ticket. esto a que python no podría saber de que clase es
    el ticket, y por ende no podría acceder a los métodos de la clase.
    
    se usa type, porque isinstance no puede ser usado con variables, y se usa para verificar si el ticket es de la instancia de la boletería.
    
    
    Luego se crea el pdf, se establece el tamaño de la hoja, se establece el color y la fuente del texto, y se dibuja el texto en la hoja.
"""


def generate_ticket_pdf(boleteria_instance, tickets, client_id, gestor_eventos):
    ticket_to_generate = None
    event_information = None
    
    for ticket in tickets:
        if isinstance(ticket, type(boleteria_instance)) and ticket.get_client_id() == client_id:
            ticket_to_generate = ticket
    
    for event in gestor_eventos.get_events():
        if event.show_event_id() == ticket_to_generate.get_event_id():
            event_information = event
                  
    if ticket_to_generate is None:
        raise ValueError(f"There's no ticket for client with the id: {client_id}")
            
    c = canvas.Canvas(f"ticket_{client_id}.pdf", pagesize=letter)
    width, height = letter
    c.setFillColor(colors.red)
    c.setFont("Times-Roman", 24)
    c.drawString(30, height - 50, f"Ticket para un evento de tipo {ticket_to_generate.get_type_of_event()}")
    
    c.setFont("Helvetica", 16)
    c.drawString(30, height - 190, f"Cliente: {ticket_to_generate.get_client()}")
    c.drawString(30, height - 100, f"ID del evento: {ticket_to_generate.get_event_id()}")
    c.drawString(30, height - 130, f"Tipo de boleto: {ticket_to_generate.get_type_of_ticket()}")
    c.drawString(30, height - 160, f"Método de pago: {ticket_to_generate.get_payment_method()}")
    
    # Dibuja una línea debajo de "Método de pago"
    c.line(30, height - 190, width - 30, height - 190)

    
    c.drawString(30, height - 220, f"Nombre del evento: {event_information.show_name()}")
    c.drawString(30, height - 250, f"Nombre del artista: {event_information.artist_name()}")
    c.drawString(30, height - 280, f"Fecha: {event_information.show_date()}")
    c.drawString(30, height - 310, f"Hora de apertura: {event_information.show_aperture()}")
    c.drawString(30, height - 340, f"Hora de inicio: {event_information.show_time()}")
    c.drawString(30, height - 370, f"Lugar: {event_information.show_location()}")
    c.drawString(30, height - 400, f"Dirección: {event_information.show_address()}")
    c.drawString(30, height - 430, f"Ciudad: {event_information.show_city()}")
    
    
    

    c.save()
