import unittest
from unittest.mock import Mock, patch
from Gestores_de_eventos.reportes import Reportes

class TestReportes(unittest.TestCase):
    @patch('reportes.Gestor_Eventos')
    @patch('reportes.Boleteria')
    def setUp(self, mock_Boleteria, mock_Gestor_Eventos):
        # Crear instancias ficticias de Gestor_Eventos y Boleteria
        self.mock_gestor = mock_Gestor_Eventos.return_value
        self.mock_boleteria = mock_Boleteria.return_value

        # Crear una instancia de Reportes para probar
        self.reportes = Reportes()

    def test_set_regular_tickets_proffit(self):
        # Crear un evento ficticio con un tipo de ticket "Regular"
        mock_event = Mock()
        mock_event.show_type_of_ticket.return_value = "Regular"
        mock_event.get_proffit.return_value = 100.0

        # Configurar self.events para devolver una lista con nuestro evento ficticio
        self.mock_gestor.get_events.return_value = [mock_event]

        # Llamar al método que queremos probar
        self.reportes.set_regular_tickets_proffit()

        # Comprobar que las ganancias y las ventas de tickets regulares se actualizaron correctamente
        self.assertEqual(self.reportes.regular_tickets_proffit, 100.0)
        self.assertEqual(self.reportes.regular_tickets_sold, 1)

    def test_financial_report(self):
        # Configurar self.events_stats para devolver un valor específico
        self.reportes.events_stats = {'Cash': {'Regular': 1000, 'Presale': 500}}

        # Llamar al método que queremos probar
        self.reportes.financial_report()

        # Como este método no devuelve un valor, podríamos verificar que se llamaron los métodos correctos en su lugar
        self.reportes.st.write.assert_called()

    def test_data_client_report(self):
        # Configurar self.clients para devolver una lista de clientes ficticios
        self.reportes.clients = [self.mock_client]

        # Configurar los métodos de mock_client para devolver valores específicos
        self.mock_client.get_user_id.return_value = '123'
        self.mock_client.get_user_name.return_value = 'Test User'
        self.mock_client.get_email.return_value = 'test@example.com'
        self.mock_client.get_phone_number.return_value = '1234567890'
        self.mock_client.get_city.return_value = 'Test City'

        # Llamar al método que queremos probar
        self.reportes.data_client_report()

        # Como este método no devuelve un valor, podríamos verificar que se llamaron los métodos correctos en su lugar
        self.reportes.st.write.assert_called()
        self.reportes.st.plotly_chart.assert_called()
        self.reportes.st.download_button.assert_called()

    def test_data_per_artist(self):
        # Configurar self.events para devolver una lista de eventos ficticios
        self.reportes.events = [self.mock_event]

        # Configurar los métodos de mock_event para devolver valores específicos
        self.mock_event.artist_name.return_value = 'Test Artist'
        self.mock_event.show_name.return_value = 'Test Show'
        self.mock_event.show_date.return_value = '2022-01-01'
        self.mock_event.show_address.return_value = 'Test Address'
        self.mock_event.show_slots.return_value = 100
        self.mock_event.event_capacity.return_value = 200

        # Llamar al método que queremos probar
        self.reportes.data_per_artist('Test Artist')

        # Como este método no devuelve un valor, podríamos verificar que se llamaron los métodos correctos en su lugar
        self.reportes.st.text.assert_called()


if __name__ == '__main__':
    unittest.main()