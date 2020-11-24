class Bus:
    def __init__(self, route_number, destinations):
        self.route_number = route_number
        self.destinations = destinations
        self.passengers = []


    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers = []
        # or self.passengers.clear()

    # def pick_up_from_stop(self, bus_stop):
    #     self.passengers.extend(bus_stop.queue)
    #     bus_stop.clear()
    
    #def bus_at_bus_stop(self, bus_stop_string):
        # loop through passengers at the stop and
        # add to bus if the destination exists

        # loop through passengers on the bus and
        # remove if the destination is the bus stop
        #pass

        

