import serial
import time

"""
This class provides an interface between the application and a microcontroller.
"""
class MicrocontrollerInterface:

    # Define communication specifications
    PORT = 'COM3'
    BAUD = 9600
    TIMEOUT = .3

    """
    Constructor.
    """
    def __init__(self):
        # Define the controller serial interface
        self.controller = serial.Serial(port=self.PORT, baudrate=self.BAUD, timeout=self.TIMEOUT)

    """
    Write a value to the microcontroller and read a serial value back.

    controller_input(str): Provided input to be sent to the microcontroller

    return: Data read from the microntroller
    """
    def write_read(self, controller_input):
        self.controller.write(bytes(controller_input,'utf-8'))
        time.sleep(0.05)
        controller_output = self.controller.readline()
        return controller_output

    """
    Read data from the microcontroller.

    return: Data read from the microcontroller
    """
    def read_only(self):
        controller_output = []
        for i in range(30):

            # Read byte string and print output to see "live" reading
            line = self.controller.readline()
            if len(line) > 0:
                print(line)
            if line:
                # Convert the byte string to a unicode string
                string = line.decode()  
                controller_output.append(line)
        return controller_output

    """
    Provide an input to send to the microcontroller, then get input back from the microcontroller.

    return: The output from the microcontroller
    """
    def provide_input_receive_output(self):
        while True:
            num = input("Enter a number \n (Press 'q' and 'Enter' to quit): ")
            controller_output = write_read(num)
            print(controller_output)

            # Check if we need to quit the program
            if num == "q":
                print("Closing Program.")            
                break

        return controller_output

    """
    Wait and receive an output from the microcontroller.

    return: The output from the microcontroller
    """
    def receive_output_only(self):
        print("Receiving input now...")
        while True:

            # Receive the input
            controller_output = self.read_only()

            # Give user option to stop the program
            num = input("Press 'q' and 'Enter' to quit: ")
            if num == "q":
                print("Closing Program.")            
                break
        return controller_output
