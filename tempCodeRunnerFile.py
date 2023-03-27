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