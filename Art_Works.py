import requests
import random

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


if __name__ == "__main__":
    # Creating a new Cultural Destination
    my_cultural_destination = CulturalDestination("Heritage Arts", "Delhi")

    # Adding new art pieces
    my_cultural_destination.add_art("Taj Mahal", "Architecture", "The iconic symbol of love in Agra", "Ustad Ahmad Lahauri")
    my_cultural_destination.add_art("Bharatanatyam Dance", "Performing Arts", "Classical Indian dance form", "Rukmini Devi Arundale")
    my_cultural_destination.add_art("Pattachitra Painting", "Visual Arts", "Traditional cloth-based scroll painting from Odisha", "Raghurajpur Artists")

