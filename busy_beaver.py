"""
busy_beaver.py

This module contains the BusyBeaver class, which is a
Turing machine simulator used to discover "busy beaver" Turing
machines, which are defined as those which print a maximum number
of 1's before stopping, starting from an empty tape.

"""

import random
import string
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end-start))
        return r
    return wrapper


DELTA_ONES = {(0, 0): 0, (0, 1): 1, (1, 0): -1, (1, 1): 0}

# Exception classes.


class InvalidTuringMachineState(Exception):
    """
    This exception class is raised if a Turing Machine state
    is improperly initialized.
    """
    pass


class InvalidTuringMachine(Exception):
    """
    This exception class is raised if a Turing Machine
    is improperly initialized.
    """
    pass


class TuringMachineRuntimeError(Exception):
    """
    This exception class is raised if an error occurs while
    simulating a Turing Machine.

    Examples:
    -- running off the tape
    -- insufficient progress after a certain number of steps
    """
    pass


class TuringMachineIOError(Exception):
    """
    This exception class is raised if an error occurs while
    loading the representation of a Turing Machine from a file
    or while saving the representation of a Turing Machine to a file.
    """
    pass


class BusyBeaver:
    """
    This class simulates Turing machines and is used to search for
    Busy Beaver Turing machines, which print a maximal number of 1's
    before stopping.

    The tape on this Turing machine consists only of zeros and ones
    (all zeros to start with) and is finite in length.

    """

    def __init__(self, nstates=5, tape_length=10000, contents=None):
        """
        Create the Turing machine.  Initialize all the states
        and create the tape.

        Arguments:
        -- nstates: number of states of the Turing machine.
        -- tape_length: the length of the tape.
        -- contents: a list of tuples representing the data
               associated with a single state of the Turing
               machine.  Each tuple is of the form:
                   ((p, dir, next), (p, dir, next))
               where:
               -- p: the number to print on the tape (0 or 1)
               -- dir: the direction to move (-1 = left, 1 = right)
               -- next: the next state (-1 = halt)
           If contents == None then generate random contents
           with the same structure.
        """

        self.nstates = nstates
        self.tape_length = tape_length
        self.tape = [0 for i in range(self.tape_length)]
        self.current_position = self.tape_length // 2
        self.current_state = 0
        if contents:
            self.contents = contents
        else:
            self.contents = self.generate_random_contents()

    def verify_state_info(self, state_info):
        """
        Verify the information about a particular Turing Machine
        state, and raise an exception if the state information
        is invalid.
        """

        # TODO

    def generate_random_contents(self):
        """
        This function generates random valid values for the
        contents of the Turing machine.  It is guaranteed to
        have a single halt state which is reached from only
        one path.
        """

        # TODO

    def save(self, filename):
        """
        Save the contents of the Turing machine to a file.
        """

        # TODO

    def load(self, filename):
        """
        Load the contents of the Turing machine from a file.
        """

        with open(filename, 'rt') as f:
            t_contents = []
            for line in f:
                line = line.replace('L', '-1')
                line = line.replace('R', '1')
                vals = line.split()
                vals = [int(val) for val in vals]
                t_contents.append((tuple(vals[0:3]), tuple(vals[3:6])))
        self.contents = t_contents

        # TODO -- MAKE SURE you verify the contents of the Turing
        # machine after you load it!

    def get_transition_string(self, transition):
        return '({:>2} {:>2} {:>2})'.format(*transition)

    def print_contents(self):
        """
        Pretty-print the contents of the Turing machine.
        This method prints the state transition information
        (number to print, direction to move, next state) for each state
        but not the contents of the tape.
        """

        for i, state in enumerate(self.contents):
            zero, one = state
            zero_text = self.get_transition_string(zero)
            one_text = self.get_transition_string(one)
            print('{:<3}: {} | {}'.format(i, zero_text, one_text))
        # TODO -- Make sure the printout is in a human-readable form
        # i.e. annotate the contents with a description of what they
        # represent.

    def print_tape(self, ncolumns=70):
        """
        Prints out the tape of the Turing machine with 'ncolumns'
        values per line.

        Limitation: Does not print the position of the tape head.
        """

        # TODO

    def print_current_state(self, steps):
        print('STEP:{} POS:{} ST:{} VAL:{} 1S:{}'.format(steps, self.current_position, self.current_state, self.tape[self.current_position], self.count_ones()))

    def count_ones(self):
        """Count the number of ones on the tape."""

        return sum(self.tape)

    def step(self):
        """
        Execute one step of the Turing machine.
        Returns:
           (0, 1)  if the count of the tape has increased by 1
           (0, -1) if the count has decreased by 1
           (0, 0)  if no change
           (1, x)  if we're now in the halt state
                   (x = count increment as above)
        """

        # Read current positon
        current_read = self.tape[self.current_position]

        # Write to cell based on transition table
        current_transition = self.contents[self.current_state][current_read]
        self.tape[self.current_position] = current_transition[0]

        # Move to new position
        self.current_position = self.current_position + current_transition[1]
        if self.current_position < 0 or self.current_position >= len(self.tape):
            raise TuringMachineRuntimeError('ran off edge of tape')

        # Transition to a new state
        self.current_state = current_transition[2]

        if self.current_state == -1:
            halt_flag = 1
        else:
            halt_flag = 0

        return (halt_flag, DELTA_ONES[(current_read, current_transition[0])])

    @timethis
    def run(self, check=1000000, silent=False):
        """
        Start the tape and run it until it halts.
        Check for progress (in terms of the total number
        of 1s written on the tape) every 'check' steps.
        If 'silent' is True, don't print out anything during the run.
        """

        result = (0, 0)
        t_num_ones = self.count_ones()
        steps = 0
        while not result[0]:
            if (not silent) and ((steps % 1000000) == 0):
                self.print_current_state(steps)
            result = self.step()
            if (steps % check) == 0:
                if t_num_ones == self.count_ones():
                    raise(TuringMachineRuntimeError('insufficient progress'))
                else:
                    t_num_ones = self.count_ones
            steps = steps + 1


#
# Test the class.
#

if __name__ == "__main__":
    bb = BusyBeaver(5, 20000)
    bb.load("bb.in")
    bb.print_contents()
    bb.run(silent=True)
    # bb.print_tape()
    print("Number of 1s printed: %d" % bb.count_ones())
    bb.save("bb.out")
