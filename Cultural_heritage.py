# import random

# class Art:
#     def __init__(self, name, category, description, artist):
#         self.name = name
#         self.category = category
#         self.description = description
#         self.artist = artist

#     def __str__(self):
#         return f"{self.name} ({self.category}) by {self.artist}: {self.description}"


# class CulturalDestination:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city
#         self.art_list = []

#     def add_art(self, name, category, description, artist):
#         new_art = Art(name, category, description, artist)
#         self.art_list.append(new_art)
#         print(f"{new_art.name} added to {self.name} collection.")

#     def remove_art(self, art_name):
#         for art in self.art_list:
#             if art.name.lower() == art_name.lower():
#                 self.art_list.remove(art)
#                 print(f"{art.name} removed from {self.name} collection.")
#                 return
#         print(f"{art_name} not found in {self.name} collection.")

#     def display_art(self):
#         print(f"{self.name} collection:")
#         for art in self.art_list:
#             print(f"- {art}")

#     def get_random_art(self):
#         if len(self.art_list) == 0:
#             print(f"No art found in {self.name} collection.")
#             return
#         random_art = random.choice(self.art_list)
#         print(f"Random art from {self.name} collection: {random_art}")


# if __name__ == "__main__":
#     # Creating a new Cultural Destination
#     my_cultural_destination = CulturalDestination("Heritage Arts", "Delhi")

#     # Adding new art pieces
#     my_cultural_destination.add_art("Taj Mahal", "Architecture", "The iconic symbol of love in Agra", "Ustad Ahmad Lahauri")
#     my_cultural_destination.add_art("Bharatanatyam Dance", "Performing Arts", "Classical Indian dance form", "Rukmini Devi Arundale")
#     my_cultural_destination.add_art("Pattachitra Painting", "Visual Arts", "Traditional cloth-based scroll painting from Odisha", "Raghurajpur Artists")
    
#     # Displaying all the art pieces in the collection
#     my_cultural_destination.display_art()

#     # Removing an art piece
#     my_cultural_destination.remove_art("Bharatanatyam Dance")

#     # Displaying a random art piece
#     my_cultural_destination.get_random_art()

import random
import io
import unittest
from cultural_destination import CulturalDestination

class TestCulturalDestination(unittest.TestCase):
    def setUp(self):
        self.destination = CulturalDestination("Heritage Arts", "Delhi")
        self.destination.add_art("Taj Mahal", "Architecture", "The iconic symbol of love in Agra", "Ustad Ahmad Lahauri")
        self.destination.add_art("Bharatanatyam Dance", "Performing Arts", "Classical Indian dance form", "Rukmini Devi Arundale")
        self.destination.add_art("Pattachitra Painting", "Visual Arts", "Traditional cloth-based scroll painting from Odisha", "Raghurajpur Artists")

    def test_display_art(self):
        expected_output = "Heritage Arts collection:\n- Taj Mahal (Architecture) by Ustad Ahmad Lahauri: The iconic symbol of love in Agra\n- Bharatanatyam Dance (Performing Arts) by Rukmini Devi Arundale: Classical Indian dance form\n- Pattachitra Painting (Visual Arts) by Raghurajpur Artists: Traditional cloth-based scroll painting from Odisha\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.destination.display_art()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_remove_art(self):
        self.destination.remove_art("Bharatanatyam Dance")
        expected_output = "Bharatanatyam Dance removed from Heritage Arts collection.\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.destination.remove_art("Bharatanatyam Dance")
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_get_random_art(self):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.destination.get_random_art()
            self.assertIn("Random art from Heritage Arts collection:", fake_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
