import unittest
from Eventos.teatro import Teatro
from Eventos.evento import Evento

class TestTeatro(unittest.TestCase):
    def setUp(self):
        self.teatro = Teatro()
        self.evento = Evento()
        self.evento.set_data("Regular", 100, 200, "Open", "Artist", "Event Name", "2022-01-01", "18:00", "20:00", "Location", "Address", "City", 0, 0, 1)

    def test_get_id(self):
        self.teatro.set_data("Regular", 100, 200, "Open", "Artist", "Event Name", "2022-01-01", "18:00", "20:00", "Location", "Address", "City", 0, 0, 1)
        self.assertEqual(self.teatro.get_id(), 1)

    def test_get_occupied_slots(self):
        self.assertEqual(self.teatro.get_occupied_slots(1), 0)


    def test_assign_slot_to_client(self):
        self.teatro.assign_slot_to_client(1)
        self.assertEqual(self.teatro.get_occupied_slots(1), 1)

    def test_show_state(self):
        self.assertEqual(self.teatro.show_state(), "Open")

    def test_artist_name(self):
        self.assertEqual(self.teatro.artist_name(), "Artist")

    def test_show_name(self):
        self.assertEqual(self.teatro.show_name(), "Event Name")

    def test_show_date(self):
        self.assertEqual(self.teatro.show_date(), "2022-01-01")

    def test_show_aperture(self):
        self.assertEqual(self.teatro.show_aperture(), "18:00")

    def test_show_time(self):
        self.assertEqual(self.teatro.show_time(), "20:00")

    def test_show_location(self):
        self.assertEqual(self.teatro.show_location(), "Location")

    def test_show_address(self):
        self.assertEqual(self.teatro.show_address(), "Address")

    def test_show_city(self):
        self.assertEqual(self.teatro.show_city(), "City")

    def test_show_type_of_ticket(self):
        self.assertEqual(self.teatro.show_type_of_ticket(), "Regular")

    def test_show_event_id(self):
        self.assertEqual(self.teatro.show_event_id(), 1)

    def test_event_price(self):
        self.assertEqual(self.teatro.event_price(), 100)

    def test_event_capacity(self):
        self.assertEqual(self.teatro.event_capacity(), 200)

    def test_show_slots(self):
        self.assertEqual(self.teatro.show_slots(1), 200)

    def test_show_tickets_sold(self):
        self.assertEqual(self.teatro.show_tickets_sold(True), 1)

    def test_total_commision(self):
        self.assertEqual(self.teatro.total_commision(1), 93)


if __name__ == '__main__':
    unittest.main()