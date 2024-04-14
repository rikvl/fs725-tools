
import sys

from fs725 import FS725Instrument


def set_fs725_sf(com_port, sf_val):
    """Set frequency offset of FS725 Rb Frequency Standard

    Parameters
    ----------
    com_port : str
        Path to device to talk to FS725.
    sf_val : int
        SF number. I.e., frequency offset in units of parts per 10^12.
    """

    # Connect to FS725
    fs725 = FS725Instrument(com_port)

    if fs725.isConnected is True:

        sf_current = int(fs725.getCurrentValue("sf"))

        # Send SF command to set frequency offset, if not already
        if sf_current != sf_val:
            fs725.setCurrentValue("sf", sf_val)

        # Close connection to FS725
        fs725.close()


if __name__ == "__main__":
    com_port = "/dev/ttyUSB0"
    sf_val = int(sys.argv[1]) if len(sys.argv) == 2 else -177
    sys.exit(set_fs725_sf(com_port=com_port, sf_val=sf_val))
