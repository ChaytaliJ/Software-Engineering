class CulturalDestination:
    def __init__(self, city, name):
        self.city = city
        self.name = name
        self.events = []
        self.artists = []
    
    def add_event(self, event):
        self.events.append(event)
    
    def add_artist(self, artist):
        self.artists.append(artist)
class Theatre:
    def __init__(self, name, region):
        self.name = name
        self.region = region
        
class Music:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        
class Dance:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        
class SpokenWord:
    def __init__(self, name, language):
        self.name = name
        self.language = language

class Artist:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

# Create a cultural destination in Delhi
delhi_cultural_destination = CulturalDestination("Delhi", "Indian Cultural Centre")

# Create some events
theatre_event = Theatre("Theatre Event", "North India")
music_event = Music("Music Event", "Classical")
dance_event = Dance("Dance Event", "Bharatanatyam")
spoken_word_event = SpokenWord("Spoken Word Event", "Hindi")

# Add events to the cultural destination
delhi_cultural_destination.add_event(theatre_event)
delhi_cultural_destination.add_event(music_event)
delhi_cultural_destination.add_event(dance_event)
delhi_cultural_destination.add_event(spoken_word_event)

# Create some artists
artist1 = Artist("Artist1", "Theatre")
artist2 = Artist("Artist2", "Music")
artist3 = Artist("Artist3", "Dance")
artist4 = Artist("Artist4", "Spoken Word")

# Add artists to the cultural destination
delhi_cultural_destination.add_artist(artist1)
delhi_cultural_destination.add_artist(artist2)
delhi_cultural_destination.add_artist(artist3)
delhi_cultural_destination.add_artist(artist4)

print(f"{delhi_cultural_destination.name} in {delhi_cultural_destination.city}")
print("Events:")
for event in delhi_cultural_destination.events:
    print(f"- {event.name}")
print("Artists:")
for artist in delhi_cultural_destination.artists:
    print(f"- {artist.name} ({artist.specialty})")
