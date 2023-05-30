class Transaction:
    def __init__(self, identifier):
        self.id = identifier

        self.required_places = set()
        self.next_places = set()
        self.fired = False

    def fire(self, curr_state):
        """Fire the transaction and return the new State """
        self.fired = True
        new_state = set(curr_state)
        for place in self.required_places:
            new_state.remove(place)
        for place in self.next_places:
            new_state.add(place)
        return new_state

    def add_required_place(self, place):
        self.required_places.add(place)

    def add_next_place(self, place):
        self.next_places.add(place)
