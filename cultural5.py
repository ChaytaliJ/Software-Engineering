import random

class CulturalDestination:
    def _init_(self, name, city, description):
        self.name = name
        self.city = city
        self.description = description
        self.events = []
        self.artists = []
    
    def add_event(self, event):
        self.events.append(event)
    
    def add_artist(self, artist):
        self.artists.append(artist)
    
class Event:
    def _init_(self, name, date, location, description):
        self.name = name
        self.date = date
        self.location = location
        self.description = description
        self.performers = []
    
    def add_performer(self, performer):
        self.performers.append(performer)
    
class Artist:
    def _init_(self, name, age, art_type, description):
        self.name = name
        self.age = age
        self.art_type = art_type
        self.description = description
    
    def perform(self, event):
        event.add_performer(self.name)

class VisualArtist(Artist):
    def _init_(self, name, age, art_type, medium, description):
        super()._init_(name, age, art_type, description)
        self.medium = medium
    
    def create_artwork(self):
        return f"{self.name} is creating a {random.choice(self.medium)} artwork."

class PerformingArtist(Artist):
    def _init_(self, name, age, art_type, genre, description):
        super()._init_(name, age, art_type, description)
        self.genre = genre
    
    def rehearse(self):
        return f"{self.name} is rehearsing for their {self.genre} performance."

class DigitalPlatform:
    def _init_(self, name, description):
        self.name = name
        self.description = description
    
    def collaborate(self, artist):
        return f"{artist.name} is collaborating with {self.name}."

    def invest(self, artist):
        return f"{self.name} is investing in {artist.name}."

class Aggregator:
    def _init_(self, name, description):
        self.name = name
        self.description = description
    
    def aggregate(self, event):
        return f"{self.name} is aggregating {event.name}."

class Accelerator:
    def _init_(self, name, description):
        self.name = name
        self.description = description
    
    def accelerate(self, artist):
        return f"{self.name} is accelerating {artist.name}."

if __name__ == '__main__':
    # create a new cultural destination
    destination = CulturalDestination('Heritage House', 'New Delhi', 'A first-of-its-kind, multi-disciplinary space for the Arts in the heart of New Delhi.')
    
    # create some events
    event1 = Event('Music Night', '12/04/2023', 'Heritage House', 'Experience the magic of Indian music with our talented musicians.')
    event2 = Event('Dance Performance', '05/06/2023', 'Heritage House', 'Get ready to be captivated by the grace and beauty of Indian classical dance.')
    event3 = Event('Theatre Show', '08/08/2023', 'Heritage House', 'Laugh, cry and be moved by our powerful theatrical performances.')
    
    #add events to the destination
    destination.add_event(event1)
    destination.add_event(event2)
    destination.add_event(event3)
    
    #create some artists
    artist1 = VisualArtist('Amitabh', 50,'Canvas', ['oil painting', 'watercolor', 'acrylic painting'], 'A talented visual artist with a passion for creating stunning paintings.')
    artist2 = PerformingArtist('Sunita', 25, 'Dancer', 'Bharatanatyam', 'A passionate dancer with a love for Indian classical dance.')
    artist3 = PerformingArtist('Rahul', 30, 'Musician', 'Sitar', 'A skilled musician with a passion for playing the sitar.')    
    # add artists to the destination
destination.add_artist(artist2)
destination.add_artist(artist1)
destination.add_artist(artist3)

# have artists perform at events
artist1.perform(event1)
artist2.perform(event2)
artist3.perform(event1)
artist3.perform(event2)

# create digital platforms, aggregators and accelerators
platform1 = DigitalPlatform('ArtMart', 'A digital platform for artists to showcase and sell their work.')
aggregator1 = Aggregator('Culture Hub', 'An aggregator for cultural events and performances.')
accelerator1 = Accelerator('Art Boost', 'An accelerator for emerging artists.')

# collaborate, aggregate and accelerate
platform1.collaborate(artist1)
platform1.invest(artist1)
aggregator1.aggregate(event1)
aggregator1.aggregate(event2)
accelerator1.accelerate(artist2)

# print information about the destination, events and artists
print(f"Welcome to {destination.name} in {destination.city}!\n{destination.description}\n")
print("Events:")
for event in destination.events:
    print(f"- {event.name} on {event.date} at {event.location}: {event.description}")
    print("Performers:")
    for performer in event.performers:
        print(f"  - {performer}")
    print()
print("Artists:")
for artist in destination.artists:
    print(f"- {artist.name}, {artist.age}, {artist.art_type}: {artist.description}")
    if isinstance(artist, VisualArtist):
        print(artist.create_artwork())
    elif isinstance(artist, PerformingArtist):
        print(artist.rehearse())
    print()
print(f"Thank you for visiting {destination.name}! We hope to see you again soon.")