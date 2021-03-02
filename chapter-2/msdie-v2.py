import random

class MSDie:
    """
    Multi-sided Die
    '''''''''''''''
    Instance variables: current_value, num_sides
    """
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value
    
    def __str__(self):
        return f"{self.current_value}"

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)
    
    def __eq__(self, other):
        return self.current_value == other.current_value

    def __lt__(self, other):
        return self.current_value < other.current_value

    def __le__(self, other):
        return self.current_value <= other.current_value

my_die = MSDie(6)
for i in range(5):
    print(my_die)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)