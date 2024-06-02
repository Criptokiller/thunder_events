import unittest
from unittest.mock import patch
from Gestores_de_eventos.boleteria import Boleteria
from Eventos.cliente import Cliente

class TestBoleteria(unittest.TestCase):
    def setUp(self):
        self.boleteria = Boleteria()

    def test_set_data(self):
        self.boleteria.set_data("client", "client_id", "type_of_event", "event_id", "type_of_ticket", "payment_method")
        self.assertEqual(self.boleteria.get_client(), "client")
        self.assertEqual(self.boleteria.get_client_id(), "client_id")
        self.assertEqual(self.boleteria.get_type_of_event(), "type_of_event")
        self.assertEqual(self.boleteria.get_event_id(), "event_id")
        self.assertEqual(self.boleteria.get_type_of_ticket(), "type_of_ticket")
        self.assertEqual(self.boleteria.get_payment_method(), "payment_method")
        self.assertEqual(self.boleteria.get_attendance(), False)

    def test_add_ticket(self):
        self.boleteria.add_ticket("client", "client_id", "type_of_event", "event_id", "type_of_ticket", "payment_method")
        self.assertEqual(len(self.boleteria.get_tickets()), 1)

    def test_add_client(self):
        client = Cliente()
        self.boleteria.add_client(client)
        self.assertEqual(len(self.boleteria.clients), 1)

    def test_get_client_data(self):
        client = Cliente()
        client.set_user_id("client_id")
        self.boleteria.add_client(client)
        self.assertEqual(self.boleteria.get_client_data("client_id"), client)

    def test_register_attendance(self):
        self.boleteria.add_ticket("client", "client_id", "type_of_event", "event_id", "type_of_ticket", "payment_method")
        self.assertEqual(self.boleteria.register_attendance("event_id"), True)

    @patch('Boleteria.Gestor_Eventos')
    @patch('Boleteria.generar_boleta.generate_ticket_pdf')
    def test_create_pdf(self, mock_generate_ticket_pdf, mock_Gestor_Eventos):
        self.boleteria.create_pdf("client_id")
        mock_generate_ticket_pdf.assert_called_once()

if __name__ == '__main__':
    unittest.main()