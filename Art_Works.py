import requests
import random
import unittest
from unittest.mock import patch, MagicMock

class Art:
    def __init__(self, name, category, description, artist):
        self.name = name
        self.category = category
        self.description = description
        self.artist = artist

    def __str__(self):
        return f"{self.name} ({self.category}) by {self.artist}: {self.description}"


class CulturalDestination:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.art_list = []

    def add_art(self, name, category, description, artist):
        new_art = Art(name, category, description, artist)
        self.art_list.append(new_art)
        print(f"{new_art.name} added to {self.name} collection.")

    def remove_art(self, art_name):
        for art in self.art_list:
            if art.name.lower() == art_name.lower():
                self.art_list.remove(art)
                print(f"{art.name} removed from {self.name} collection.")
                return
        print(f"{art_name} not found in {self.name} collection.")

    def display_art(self):
        print(f"{self.name} collection:")
        for art in self.art_list:
            print(f"- {art}")

    def get_random_art(self):
        if len(self.art_list) == 0:
            print(f"No art found in {self.name} collection.")
            return
        random_art = random.choice(self.art_list)
        print(f"Random art from {self.name} collection: {random_art}")

    def get_artist_info(self, artist_name):
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "q": artist_name,
            "cx": "YOUR_SEARCH_ENGINE_ID",
            "key": "YOUR_API_KEY",
            "searchType": "image",
            "imgSize": "large",
            "num": 1,
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json()["items"]
            if len(results) > 0:
                image_url = results[0]["link"]
                print(f"{artist_name} image URL: {image_url}")
            else:
                print(f"No images found for {artist_name}.")
        else:
            print(f"Error fetching images for {artist_name}. Status code: {response.status_code}")



class TestCulturalDestination(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.my_cultural_destination = CulturalDestination("Heritage Arts", "Delhi")

    def test_add_art(self):
        self.my_cultural_destination.add_art("Taj Mahal", "Architecture", "The iconic symbol of love in Agra", "Ustad Ahmad Lahauri")
        self.my_cultural_destination.add_art("Bharatanatyam Dance", "Performing Arts", "Classical Indian dance form", "Rukmini Devi Arundale")
        self.my_cultural_destination.add_art("Pattachitra Painting", "Visual Arts", "Traditional cloth-based scroll painting from Odisha", "Raghurajpur Artists")
        self.assertEqual(len(self.my_cultural_destination.art_list), 3)
        self.assertEqual(self.my_cultural_destination.art_list[0].name, "Taj Mahal")

    def test_remove_art(self):
        self.my_cultural_destination.remove_art("Taj Mahal")
        self.assertEqual(len(self.my_cultural_destination.art_list), 2)
        self.assertEqual(self.my_cultural_destination.art_list[0].name, "Bharatanatyam Dance")

    def test_get_random_art(self):
        with patch('random.choice') as mock_random:
            mock_random.return_value = Art("Pattachitra Painting", "Visual Arts", "Traditional cloth-based scroll painting from Odisha", "Raghurajpur Artists")
            self.my_cultural_destination.get_random_art()
            mock_random.assert_called_once_with(self.my_cultural_destination.art_list)

    def test_get_artist_info(self):
        with patch('requests.get') as mock_get:
            mock_json = MagicMock()
            mock_json.return_value = {
                "items": [
                    {
                        "link": "https://example.com/image.jpg"
                    }
                ]
            }
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json = mock_json
            mock_get.return_value = mock_response
            self.my_cultural_destination.get_artist_info("Ustad Ahmad Lahauri")
            mock_get.assert_called_once_with(
                "https://www.googleapis.com/customsearch/v1",
                params={
                    "q": "Ustad Ahmad Lahauri",
                    "cx": "YOUR_SEARCH_ENGINE_ID",
                    "key": "YOUR_API_KEY",
                    "searchType": "image",
                    "imgSize": "large",
                    "num": 1,
                }
            )
            self.assertEqual(mock_json.call_count, 1)
            self.assertEqual(mock_response.json.call_count, 1)
            self.assertEqual(mock_response.status_code, 200)
            self.assertEqual(mock_response.json()["items"][0]["link"], "https://example.com/image.jpg")

if __name__ == "__main__":
    # Creating a new Cultural Destination
    my_cultural_destination = CulturalDestination("Heritage Arts", "Delhi")

    # Adding new art pieces
    my_cultural_destination.add_art("Taj Mahal", "Architecture", "The iconic symbol of love in Agra", "Ustad Ahmad Lahauri")
    my_cultural_destination.add_art("Bharatanatyam Dance", "Performing Arts", "Classical Indian dance form", "Rukmini Devi Arundale")
    my_cultural_destination.add_art("Pattachitra Painting", "Visual Arts", "Traditional cloth-based scroll painting from Odisha", "Raghurajpur Artists")

    unittest.main()


