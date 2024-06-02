import unittest
from Eventos.filantropico import Filantropico
from Eventos.evento import Evento

class TestFilantropico(unittest.TestCase):
    def setUp(self):
        self.filantropico = Filantropico()
        self.filantropico.set_data("VIP", 100, 200, "Open", "Artist", "Event", "2022-12-31", "18:00", "20:00", "Location", "Address", "City", 0, 0, 1)
        self.filantropico.set_stats()

    def test_show_state(self):
        self.assertEqual(self.filantropico.show_state(), "Open")

    def test_artist_name(self):
        self.assertEqual(self.filantropico.artist_name(), "Carlos")

    def test_show_name(self):
        self.assertEqual(self.filantropico.show_name(), "Event")

    def test_show_date(self):
        self.assertEqual(self.filantropico.show_date(), "2022-12-31")

    def test_show_aperture(self):
        self.assertEqual(self.filantropico.show_aperture(), "18:00")

    def test_show_time(self):
        self.assertEqual(self.filantropico.show_time(), "20:00")

    def test_show_location(self):
        self.assertEqual(self.filantropico.show_location(), "Location")

    def test_show_address(self):
        self.assertEqual(self.filantropico.show_address(), "Address")

    def test_show_city(self):
        self.assertEqual(self.filantropico.show_city(), "City")

    def test_show_type_of_ticket(self):
        self.assertEqual(self.filantropico.show_type_of_ticket(), "Regular")

    def test_show_event_id(self):
        self.assertEqual(self.filantropico.show_event_id(), self.filantropico.event_id)

    def test_event_price(self):
        self.assertEqual(self.filantropico.event_price(), 100)

    def test_event_capacity(self):
        self.assertEqual(self.filantropico.event_capacity(), 200)

    def test_show_tickets_sold(self):
        self.assertEqual(self.filantropico.show_tickets_sold(True), 1)

    def test_number_to_id(self):
        number = self.filantropico.number_to_id()
        self.assertTrue(0 <= int(number) <= 10000)

    def test_total_commision(self):
        self.assertEqual(self.filantropico.total_commision(1), 0)

if __name__ == '__main__':
    unittest.main()