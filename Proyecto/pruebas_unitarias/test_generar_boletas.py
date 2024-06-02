import unittest
from unittest.mock import Mock, patch
from Gestores_de_eventos.generar_boleta import generate_ticket_pdf

class TestGenerarBoleta(unittest.TestCase):
    @patch('generar_boleta.Boleteria')
    @patch('generar_boleta.Ticket')
    @patch('generar_boleta.Client')
    @patch('generar_boleta.Event')
    @patch('generar_boleta.GestorEventos')
    def setUp(self, mock_GestorEventos, mock_Event, mock_Client, mock_Ticket, mock_Boleteria):
        # Crear instancias ficticias de Boleteria, Ticket, Client y Event
        self.mock_boleteria = mock_Boleteria.return_value
        self.mock_ticket = mock_Ticket.return_value
        self.mock_client = mock_Client.return_value
        self.mock_event = mock_Event.return_value
        self.mock_gestor_eventos = mock_GestorEventos.return_value

        # Configurar los métodos de mock_ticket para devolver valores específicos
        self.mock_ticket.get_client_id.return_value = '123'
        self.mock_ticket.get_event_id.return_value = '456'
        self.mock_ticket.get_type_of_event.return_value = 'Test Event'
        self.mock_ticket.get_client.return_value = 'Test Client'
        self.mock_ticket.get_type_of_ticket.return_value = 'Regular'
        self.mock_ticket.get_payment_method.return_value = 'Cash'

        # Configurar los métodos de mock_event para devolver valores específicos
        self.mock_event.show_event_id.return_value = '456'
        self.mock_event.show_name.return_value = 'Test Show'
        self.mock_event.artist_name.return_value = 'Test Artist'
        self.mock_event.show_date.return_value = '2022-01-01'
        self.mock_event.show_aperture.return_value = '18:00'
        self.mock_event.show_time.return_value = '20:00'
        self.mock_event.show_location.return_value = 'Test Location'
        self.mock_event.show_address.return_value = 'Test Address'
        self.mock_event.show_city.return_value = 'Test City'

        # Configurar mock_gestor_eventos para devolver una lista de eventos ficticios
        self.mock_gestor_eventos.get_events.return_value = [self.mock_event]

    def test_generate_ticket_pdf(self):
        # Llamar a la función que queremos probar
        generate_ticket_pdf(self.mock_boleteria, [self.mock_ticket], '123', self.mock_gestor_eventos)

        # Como esta función no devuelve un valor, podríamos verificar que se llamaron los métodos correctos en su lugar
        self.mock_ticket.get_client_id.assert_called()
        self.mock_ticket.get_event_id.assert_called()
        self.mock_gestor_eventos.get_events.assert_called()

if __name__ == '__main__':
    unittest.main()