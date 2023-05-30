from collections import defaultdict

from Transaction import Transaction


class Solver:
    def __init__(self, transitions: list[Transaction], initial_state, goal_place):
        self.transitions = transitions
        self.goal_place = goal_place
        self.initial_state = initial_state
        self.visited_states = set()
        self.reachability_graph = defaultdict(list)
        self.reachability_graph[tuple(sorted(initial_state))] = []

    def is_sound(self):
        return self.is_valid_path(self.initial_state)

    def is_valid_path(self, state, prev_state=None, prev_tran=None):
        state_tuple = tuple(sorted(state))
        if prev_state is not None and prev_tran is not None:
            prev_state_tuple = tuple(sorted(prev_state))
            self.reachability_graph[prev_state_tuple].append((prev_tran, state_tuple))

        # base case
        if self.goal_place in state:
            return len(state) == 1

        self.visited_states.add(state_tuple)
        should_fire = self.should_fire(state)

        if len(should_fire) == 0:
            return False

        for tran in should_fire:
            new_state = tran.fire(state)
            if new_state not in self.visited_states:
                if not self.is_valid_path(new_state, state, tran):
                    return False
        return True

    def is_all_fired(self):
        return all(transition.fired for transition in self.transitions)

    def should_fire(self, curr_state):
        """Return the transactions that can be fired from the current state"""
        return [transition for transition in self.transitions if not transition.required_places.difference(curr_state)]
