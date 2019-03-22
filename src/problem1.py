"""
Exam 1, problem 1. 15 Points
Authors: Every CSSE faculty member, Dr. Brackin, and Kash.
"""
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """

    ###########################################################################
    # UN-comment tests as you work the problems.
    ###########################################################################

    run_test_init()
    run_test_go_to_floor()
    run_test_get_passengers()
    run_test_lose_passengers()


###############################################################################
# The   Elevator class (and its methods) begins here.
##############################################################################

class Elevator(object):
    """
    An Elevator has:
        -- OCCUPANTS, which is the number of humans currently on the elevator,
        -- CAPACITY, which is the maximum number of humans allowed on the elevator,
        -- NUMBER OF FLOORS, which is a non-negative integer and is the number of floors
                             that the elevator can access,
        -- CURRENT FLOOR is the floor at which the elevator resides.
                         The CURRENT FLOOR can never be greater than the NUMBER OF FLOORS.
    """

    def __init__(self, capacity, num_floors):
        """
        What comes in:
          -- self
          -- An integer that is the maximum number of humans allowed on the elevator
          -- An integer that is the number of floors that the elevator reaches
        What goes out: Nothing (i.e., None).
        Side effects:
          -- Maintains the number of humans on the elevator
          -- Maintains a record of the current floor
          -- Also initializes other instance variables as needed
              by other methods.
        Examples:
          e1 = Elevator(20, 18)
          #   e1.capacity is 20
          #   e1.num_floors is 18
          e2 = Elevator(10, 8)
          #   e2.capacity is 10
          #   e2.num_floors is 8
        Type hints:
          :type capacity: int
          :type num_floors: int
        """
        # ---------------------------------------------------------------------
        #     DONE: 2. Implement and test this function. (3 pts)
        #     See the testing code (below) for more examples.
        # ---------------------------------------------------------------------
        # ---------------------------------------------------------------------

        self.capacity = capacity
        self.num_floors = num_floors
        self.passengersi = 0
        self.floor = 0


    def go_to_floor(self,floor):
        """
        What comes in:
          -- self
          -- a positive integer, floor, that is the desired floor
        What goes out:
          --Returns False if the floor requested is not a valid floor
          --Returns True if the floor is updated to the requested floor
        Side effects:
          -- Sets the elevator's current floor to floor given, unless
             the value of floor is greater than the number of floors allowed.
             If the value of floor is greater than the number of floors allowed,
             the elevator remains where it is.
        Examples:
          e1 = Elevator(20, 18)
          e1.go_to_floor(4)
          #   e1.capacity is 20
          #   e1.num_floors is 18
          #   the current floor is set to 4
          #   True is returned by the method
          e1 = Elevator(20, 18)
          e1.go_to_floor(35)
          #   e1.capacity is 20
          #   e1.num_floors is 18
          #   the current floor does not change
          #   False is returned by the method
        """
        if floor < self.num_floors:
            self.floor = floor
            return True
        return False
        # ---------------------------------------------------------------------
        #     DONE: 4. Implement the go_to_floor method. (3 pts)
        #     Write the testing code (below) before writing this method.
        # ---------------------------------------------------------------------
        # ---------------------------------------------------------------------




    def get_passengers(self,num_passengers):
        """
        What comes in:
          -- self
          -- a positive integer, num_passengers, that is
             number of passengers who want to get on the elevator
        What goes out:
          -- Returns False if adding the passengers will exceed
             the capacity of the elevator
        Side effects:
          -- Updates the number of passengers on the elevator, unless
             the total of passengers will be greater than the maximum capacity.
             If the total will be greater than the maximum capacity,
             no one is allowed to enter the elevator.
        Examples:
          e1 = Elevator(20, 18)
          e1.get_passengers(4)
          #   e1.capacity is 20
          #   e1.num_floors is 18
          #   you will update the number of people on the elevator
          #   unless the capacity has already been exceeded.
          #   True is returned if all passengers are successfully added
          e1 = Elevator(20, 18)
          e1.get_passengers(35)
          #   e1.capacity is 20
          #   e1.num_floors is 18
          #   this exceeds the number of allowed passengers
          #   no passengers are added
          #   False is returned by the method
        """
        if num_passengers + self.passengersi < self.capacity:
            self.passengersi = self.passengersi + num_passengers
            return True
        return False

# ---------------------------------------------------------------------
#     DONE: 6. Implement the get_passengers method. (3 pts)
#     Write the testing code (below) before writing this function.
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------




# ---------------------------------------------------------------------
#     DONE: 7. Write methods, AS NEEDED, to allow passengers to exit
#      the elevator.  Show that your solution works with a test case. (2 pts)
#     Write the testing code (below) before writing this function.
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

    def lose_passengers(self, num_passengers):
        if self.passengersi - num_passengers > 0:
            self.passengersi = self.passengersi - num_passengers
            return True
        return False
###############################################################################
# The TEST functions for the  Elevator  class begin here.
###############################################################################
def run_test_init():
    """ Tests the   __init__   method of the Elevator class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the Elevator class.')
    print('-----------------------------------------------------------')

    # Test 1:  Creates elevator for small building.
    e1 = Elevator(20, 18)
    expected_capacity = 20
    expected_num_floors = 18
    print("Expected:", expected_capacity, expected_num_floors)
    print("Actual:  ", e1.capacity, e1.num_floors)
    if (expected_capacity == e1.capacity) and (expected_num_floors == e1.num_floors):
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()
    print()


def run_test_go_to_floor():
    """ Tests the   go_to_floor method of the Elevator class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   go_to_floor   method of the Elevator class.')
    print('-----------------------------------------------------------')
    #     DONE: 3. Write tests for the go_to_floor method. (2 pts)
    #     A recommended format is shown below.  Be sure to
    #     add your actual code where indicated.  Include two
    #     test cases - one that works and one that returns False
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    # Test 1:  Sends elevator to 4th floor.
    e1 = Elevator(20, 18)
    expected_capacity = 20
    expected_num_floors = 18
    expected_go_to_floor = 4
    print('Expected: go_to_floor returns :', True)
    print("Expected:", expected_capacity, expected_num_floors, expected_go_to_floor)
    ################################################################
    #
    #     Add your values for actual below here
    #
    ################################################################
    actual = e1.go_to_floor(4)
    print('Actual:   go_to_floor returns :', actual)
    print()

    # Test 2:
    e1 = Elevator(1, 100)
    expected_capacity = 1
    expected_num_floors = 100
    expected_go_to_floor = 10
    actual = e1.go_to_floor(10)
    print('Expected: go_to_floor returns :', True)
    print("Expected:", expected_capacity, expected_num_floors, expected_go_to_floor)
    print('Actual:   go_to_floor returns :', actual)

    print()

    # Test 3:
    e1 = Elevator(1, 1)
    expected_capacity = 1
    expected_num_floors = 1
    expected_go_to_floor = 1
    actual = e1.go_to_floor(10)
    print('Expected: go_to_floor returns :', False)
    print("Expected:", expected_capacity, expected_num_floors, expected_go_to_floor)
    print('Actual:   go_to_floor returns :', actual)


def run_test_get_passengers():
    """ Tests the   get_passengers method of the Elevator class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   get_passengers   method of the Elevator class.')
    print('-----------------------------------------------------------')
    #     DONE: 5. Write tests for the get_passengers method. (2 pts)
    #     A recommended format is shown below.  Be sure to
    #     add your actual code where indicated.  Include several
    #     test cases - at least one that works
    #     and one that returns False
    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    # Test 1:  Adds 2 passengers to an empty elevator.
    e1 = Elevator(20, 18)
    expected_capacity = 20
    expected_num_floors = 18
    expected_num_passengers = 2
    print('Expected passengers returns ', True)
    print("Expected:", expected_capacity, expected_num_floors, expected_num_passengers)

    ################################################################
    #
    #     Add your values for actual below here
    #
    ################################################################
    actual = e1.get_passengers(2)
    print("Actual passengers returns   ", actual)
    print()

    # Test 2:
    e1 = Elevator(30,56)
    expected_capacity = 30
    expected_num_floors = 56
    expected_num_passengers = 12
    print('Expected passengers returns ', True)
    print("Expected:", expected_capacity, expected_num_floors, expected_num_passengers)
    actual = e1.get_passengers(12)
    print("Actual passengers returns   ", actual)
    print()

    # Test 3:
    e1 = Elevator(10, 10)
    expected_capacity = 10
    expected_num_floors = 10
    expected_num_passengers = 500
    print('Expected passengers returns ', False)
    print("Expected:", expected_capacity, expected_num_floors, expected_num_passengers)
    actual = e1.get_passengers(500)
    print("Actual passengers returns   ", actual)

def run_test_lose_passengers():

    print()
    print('-----------------------------------------------------------')
    print('Testing the   lose_passengers   method of the Elevator class.')
    print('-----------------------------------------------------------')

    # Test 1:
    e1 = Elevator(20, 18)
    expected_capacity = 20
    expected_num_floors = 18
    expected_num_passengers = 2
    print('Expected passengers returns ', True)
    print("Expected:", expected_capacity, expected_num_floors, expected_num_passengers)
    e1.get_passengers(10)
    actual = e1.lose_passengers(8)
    print("Actual passengers returns   ", actual)
    print()

    # Test 1:
    expected_capacity = 20
    expected_num_floors = 18
    expected_num_passengers = -3
    print('Expected passengers returns ', False)
    print("Expected:", expected_capacity, expected_num_floors, expected_num_passengers)
    actual = e1.lose_passengers(5)
    print("Actual passengers returns   ", actual)


def print_failure_message():
    print('  *** FAILED the above test. ***')

    """ Prints a message . """


main()