# -*- coding: utf-8 -*-
#
# Modified from https://github.com/uberdaff/kd3005p
#
# Requirements: pyserial
#

import sys
import time

import serial


class FS725Instrument:
    """Object to communicate with FS725 Rb Frequency Standard

    Parameters
    ----------
    com_port : str
        Path to serial device connected to FS725.

    Attributes
    ----------
    isConnected : bool
        Whether the serial connection is established.
    com : :obj:`serial.Serial`
        Serial port object that communicates with FS725.

    Methods
    -------
    close():
        Close serial port.
    serialWriteAndReceive(self, data, delay=0.05):
        Send data to FS725 via serial connection and receive response.
    getCurrentValue(self, mnem):
        Get value currently used by FS725.
    getEEPROMValue(self, mnem):
        Get value stored in EEPROM.
    setCurrentValue(self, mnem, val):
        Set parameter to new value.
    writeCurrentValueToEEPROM(self, mnem):
        Write currently used value to EEPROM for use after reset.
    """

    isConnected = False
    com = None

    def __init__(self, com_port):
        try:
            com = serial.Serial(
                port=com_port,
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
            )
            com.isOpen()
            self.com = com
            self.isConnected = True
        except Exception:
            print("COM port failure:")
            print(sys.exc_info())
            self.com = None
            self.isConnected = False

    def close(self):
        self.com.close()

    def serialWriteAndReceive(self, data, delay=0.05):
        self.com.write(data.encode())
        out = ""
        time.sleep(delay)
        while self.com.inWaiting() > 0:
            out += self.com.read(1).decode()
        if out == "":
            out = None
        return out

    def getCurrentValue(self, mnem):
        return self.serialWriteAndReceive(f"{mnem}?\r")

    def getEEPROMValue(self, mnem):
        return self.serialWriteAndReceive(f"{mnem}!?\r")

    def setCurrentValue(self, mnem, val):
        return self.serialWriteAndReceive(f"{mnem}{val}\r")

    def writeCurrentValueToEEPROM(self, mnem):
        return self.serialWriteAndReceive(f"{mnem}!\r")
