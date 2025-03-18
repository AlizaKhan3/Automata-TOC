class DFA:
    def __init__(self, num_states, input_chars, initial_state, final_states, transition_table):
        self.num_states = num_states  
        self.input_chars = input_chars  
        self.initial_state = initial_state  
        self.final_states = final_states
        self.transition_table = transition_table  

    def validate(self, word):
        """
        Validate if the input word is accepted by the DFA.
        """
        current_state = self.initial_state
        for char in word:
            if char not in self.input_chars:  
                raise ValueError(f"Invalid character '{char}' in input. Valid characters are: {self.input_chars}")
            # Get the index of the input character
            char_index = self.input_chars.index(char)
            # Transition to the next state
            current_state = self.transition_table[current_state][char_index]

        # Check if the final state is an accepting state
        return current_state in self.final_states


# Define the DFA
input_chars = ['a', 'b']  # Alphabet
final_states = [0, 2, 3]  # Accepting states
transition_table = [
    [1, 3],  # State 0 transitions
    [2, 5],  # State 1 transitions
    [1, 3],  # State 2 transitions
    [1, 4],  # State 3 transitions
    [5, 3],  # State 4 transitions
    [5, 5],  # State 5 transitions
]

# Create the DFA
dfa = DFA(6, input_chars, 0, final_states, transition_table)

# Test the DFA
print('DFA: Words in which whenever "a" occurs, it occurs in a clump of even length, and "b" occurs in a clump of odd length.')
word = input('Input: ')  # Example: "aabbb"
try:
    print("Accepted" if dfa.validate(word) else "Rejected")
except ValueError as e:
    print(e)