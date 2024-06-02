import unittest
from Eventos.bar import Bar


class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar()
        self.bar.set_data("VIP", 100, 200, "Open", "Artist", "Event", "2022-12-31", "18:00", "20:00", "Location", "Address", "City", 0, 0, 1)
        self.bar.set_bar_id()

    def test_get_bar_id(self):
        self.assertEqual(self.bar.get_bar_id(), self.bar._bar_id)

    def test_show_state(self):
        self.assertEqual(self.bar.show_state(), "Open")

    def test_artist_name(self):
        self.assertEqual(self.bar.artist_name(), "Artist")

    def test_show_name(self):
        self.assertEqual(self.bar.show_name(), "Event")

    def test_show_date(self):
        self.assertEqual(self.bar.show_date(), "2022-12-31")

    def test_show_aperture(self):
        self.assertEqual(self.bar.show_aperture(), "18:00")

    def test_show_time(self):
        self.assertEqual(self.bar.show_time(), "20:00")

    def test_show_location(self):
        self.assertEqual(self.bar.show_location(), "Location")

    def test_show_address(self):
        self.assertEqual(self.bar.show_address(), "Address")

    def test_show_city(self):
        self.assertEqual(self.bar.show_city(), "City")

    def test_show_type_of_ticket(self):
        self.assertEqual(self.bar.show_type_of_ticket(), "VIP")

    def test_show_event_id(self):
        self.assertEqual(self.bar.show_event_id(), 1)

    def test_event_price(self):
        self.assertEqual(self.bar.event_price(), 100)

    def test_event_capacity(self):
        self.assertEqual(self.bar.event_capacity(), 200)

    def test_random_number(self):
        number = self.bar.random_number()
        self.assertTrue(0 <= number <= 10000)

    def test_show_tickets_sold(self):
        self.assertEqual(self.bar.show_tickets_sold(True), 1)

    def test_show_slots(self):
        self.assertEqual(self.bar.show_slots(1), 200)

    def test_assign_slot_to_client(self):
        self.bar.assign_slot_to_client(1)
        self.assertEqual(self.bar.get_occupied_slots(1), 1)

    def test_total_commision(self):
        self.assertEqual(self.bar.total_commision(1), 20)

    def test_get_occupied_slots(self):
        self.assertEqual(self.bar.get_occupied_slots(1), 1)

    def test_number_to_id(self):
        number = self.bar.number_to_id()
        self.assertTrue(0 <= int(number) <= 10000)

if __name__ == '__main__':
    unittest.main()