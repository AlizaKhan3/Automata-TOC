class DFA:
    def __init__(self, num_states, input_chars, initial_state, final_states, transition_table):
        self.num_states = num_states  
        self.input_chars = input_chars  
        self.initial_state = initial_state  
        self.final_states = final_states
        self.transition_table = transition_table  

    def validate(self, word):
        current_state = self.initial_state
        for char in word:
            if char not in self.input_chars:  
                raise ValueError(f"Invalid character '{char}' in input. Valid characters are: {self.input_chars}")
            char_index = self.input_chars.index(char)
            current_state = self.transition_table[current_state][char_index]
        return current_state in self.final_states

input_chars = ['a', 'b']  
final_states = [2]  
transition_table = [[1, 3], [2, 3],[2, 2],[3, 3]]
dfa = DFA(4, input_chars, 0, final_states, transition_table)

print("DFA of aa(a+b)*: A string that starts with 'aa'")
word = input('Input: ')
try:
    print("Accepted" if dfa.validate(word) else "Rejected")
except ValueError as e:
    print(e)