import create
import time

"""
1. how to smoothly transition between large left and large right or for/bak?

2. How to stay responsive to changing commands
"""


class Sim(object):
    def go(mv, tv):
        print mv, tv

class Robot(object):
    STATES = ("DRIVING", "STOPPING", "TURNING", "IDLE")
    DRIVING, STOPPING, TURNING, IDLE = STATES
    def __init__(self, port, sim=False):
        if sim:
            self.r = Sim()
        else:
            self.r = create.Create(port)

        #The list to store commands
        self.commands = []

        #The rate at which the velocity ramps up as a button is held
        self.vel_ramp = 1.2

        #The velocities for forward/backward movement
        self.current_move_velocity = 0
        self.base_move_velocity = 5
        self.max_move_velocity = 50

        #The velocities for turning
        self.current_turn_velocity = 0
        self.base_turn_velocity = 5
        self.max_turn_velocity = 25

        #Keep track of if moving direction, 1 is forward
        self.move_direction = 1

        #Keep track of turning direction 1 is to the right
        self.turn_direction = 1

        #Track the current state the robot is in
        self.state = self.IDLE

    def up_arrow(self):
        self.move_direction = 1
        self.move()

    def down_arrow(self):
        self.move_direction = -1
        self.move()

    def move(self):
        #The idea behind the movement is that it ramps up an down smoothly
        #over the course of a few cycles of the main loop
        if self.current_move_velocity == 0:
            self.current_move_velocity = self.base_move_velocity
        else:
            self.current_move_velocity *= self.vel_ramp

        if self.current_move_velocity > self.max_move_velocity:
            self.current_move_velocity = self.max_move_velocity

        self.r.go(self.current_move_velocity, self.current_turn_velocity)
        self.state = self.DRIVING

    def stop(self):
        #Stop like move tries to slow down smoothly instead of coming straight
        #to a dead stop. But some logic is needed to deal with a move command
        #in the middle of a stop cycle
        down_ramp = 3.0

        self.current_move_velocity = self.current_move_velocity/down_ramp
        self.current_turn_velocity = self.current_turn_velocity/down_ramp

        if self.current_move_velocity < self.base_move_velocity:
            self.current_move_velocity = 0
        if self.current_turn_velocity < self.current_turn_velocity:
            self.current_turn_velocity = 0

        self.go(self.current_move_velocity, self.current_turn_velocity)
        self.state = self.STOPPING

    def right_arrow(self):
        self.turn_direction = 1
        self.turn()

    def left_arrow(self):
        self.turn_direction = -1
        self.turn()

    def command_loop(self):
        """
        The main loop that runs the robot around.
        """
        command_delay = 0.5
        while 1:
            try:
                cmd = self.commands.pop()
            except IndexError:
                cmd = "Stop"

            if cmd == "Up":
                self.up_arrow()
            elif cmd == "Down":
                self.down_arrow()
            elif cmd == "Left":
                self.left_arrow()
            elif cmd == "Right":
                self.right_arrow()
            else:
                #Add more commands as needed
                continue

            time.sleep(command_delay)
