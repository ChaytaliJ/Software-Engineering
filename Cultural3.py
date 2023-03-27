class Event:
    def __init__(self, name, date, time, venue, price, tickets_available):
        self.name = name
        self.date = date
        self.time = time
        self.venue = venue
        self.price = price
        self.tickets_available = tickets_available

    def display_info(self):
        print(f"Event Name: {self.name}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Venue: {self.venue}")
        print(f"Price: {self.price}")
        print(f"Tickets Available: {self.tickets_available}")

class Ticket:
    def __init__(self, event, quantity):
        self.event = event
        self.quantity = quantity

    def total_cost(self):
        return self.event.price * self.quantity

class TicketBookingSystem:
    def __init__(self, events):
        self.events = events
        self.bookings = []

    def display_events(self):
        for event in self.events:
            event.display_info()
            print()

    def make_booking(self, event_name, quantity):
        for event in self.events:
            if event.name == event_name:
                if event.tickets_available >= quantity:
                    ticket = Ticket(event, quantity)
                    self.bookings.append(ticket)
                    event.tickets_available -= quantity
                    return ticket.total_cost()
                else:
                    print("Sorry, not enough tickets available")
                    return None
        print("Sorry, event not found")
        return None

# sample data
events = [
    Event("Indian Classical Music Concert", "2023-04-10", "7:00 PM", "Shanmukhananda Hall", 500, 100),
    Event("Bharatanatyam Dance Performance", "2023-04-15", "6:30 PM", "NCPA", 750, 50),
    Event("Hindi Stand-up Comedy Show", "2023-04-20", "8:00 PM", "Canvas Laugh Club", 1000, 30)
]

# create ticket booking system instance
ticket_booking_system = TicketBookingSystem(events)

# display available events
ticket_booking_system.display_events()

# make a booking
total_cost = ticket_booking_system.make_booking("Indian Classical Music Concert", 2)
if total_cost:
    print(f"Booking successful. Total Cost: {total_cost}")

# integrated testing
assert ticket_booking_system.make_booking("Non-existent Event", 1) == None
assert ticket_booking_system.make_booking("Hindi Stand-up Comedy Show", 50) == None
assert ticket_booking_system.make_booking("Bharatanatyam Dance Performance", 10) == 7500
assert ticket_booking_system.make_booking("Indian Classical Music Concert", 99) == None
assert len(ticket_booking_system.bookings) == 1
assert ticket_booking_system.bookings[0].total_cost() == 1000

