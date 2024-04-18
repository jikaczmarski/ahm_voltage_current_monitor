import time
# Import third-party modules
import automationhat

# Define custom functions
def data_stream():
    """Produce voltage and current from automation hat mini analog channels"""

    # Calculate shunt resistance
    r = (0.031 - .016) / 11

    # Read analog channel 0: battery voltage
    voltage = automationhat.analog[0].read()

    # Read analog channel 1: calculate current
    #current = automationhat.analog[1].read() / r 
    current = (automationhat.analog[1].read() - 0.016) / r
    # Output the result
    print(voltage, ",", current)

    # Wait
    time.sleep(1)
