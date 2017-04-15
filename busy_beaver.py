"""
busy_beaver.py

This module contains the BusyBeaver class, which is a
Turing machine simulator used to discover "busy beaver" Turing
machines, which are defined as those which print a maximum number
of 1's before stopping, starting from an empty tape.

"""

import random, string


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

        # TODO


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

        # TODO -- MAKE SURE you verify the contents of the Turing
        # machine after you load it!


    def print_contents(self):
        """
        Pretty-print the contents of the Turing machine.
        This method prints the state transition information
        (number to print, direction to move, next state) for each state
        but not the contents of the tape.
        """

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


    def count_ones(self):
        """Count the number of ones on the tape."""

        # TODO


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

        # TODO


    def run(self, check=1000000, silent=False):
        """
        Start the tape and run it until it halts.
        Check for progress (in terms of the total number
        of 1s written on the tape) every 'check' steps.
        If 'silent' is True, don't print out anything during the run.
        """

        # TODO


#
# Test the class.
#

if __name__ == "__main__":
    bb = BusyBeaver(5, 20000)
    bb.load("bb.in")
    bb.print_contents()
    bb.run()
    # bb.print_tape()
    print "Number of 1s printed: %d" % bb.count_ones()
    bb.save("bb.out")



