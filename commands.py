# Commands for the SRS FS725 Rubidium Frequency Standard

# flake8: noqa

from collections import namedtuple, OrderedDict

# Namedtuple to store a command for the FS725
Cmd = namedtuple("Cmd", ["mnem", "eeprom", "rtn_type", "description"])

# List of FS725 commands, stored as Command namedtuples with these fields:
# mnem:         Two-letter (plus possible number) ASCII mnemonic of the command
# eeprom:       Whether it's possible to query the value from EEPROM
# rtn_type:     What type the returned string should be converted to
# description:  Description of command
fs725_commands = OrderedDict({
    #           mnem,     eeprom, rtn_type,   description
    # Initialize
    "vb":   Cmd("vb",     False,  int,        "Verbose mode"),
    "sn":   Cmd("sn",     True,   int,        "Serial number"),
    "st":   Cmd("st",     False,  [int] * 6,  "Status values"),
    "lm":   Cmd("lm",     True,   int,        "Lock pin mode configuration"),
    # Freq. Lock
    "lo":   Cmd("lo",     False,  int,        "Frequency lock loop status"),
    "fc":   Cmd("fc",     True,   [int] * 2,  "Frequency control values"),
    "ds":   Cmd("ds",     False,  [int] * 2,  "Detected signals"),
    "sf":   Cmd("sf",     False,  int,        "Frequency offset"),
    "ss":   Cmd("ss",     True,   int,        "Frequency calibration slope"),
    "ga":   Cmd("ga",     True,   int,        "FLL gain"),
    "ph":   Cmd("ph",     True,   int,        "Phase angle"),
    "sp":   Cmd("sp",     True,   [int] * 3,  "Synthesizer parameters"),
    # Magnetic Tuning
    "ms":   Cmd("ms",     False,  int,        "Magnetic switching"),
    "mo":   Cmd("mo",     True,   int,        "Magnetic offset"),
    "mr":   Cmd("mr",     False,  int,        "Magnet read"),
    # 1PPS Lock
    "tt":   Cmd("tt",     False,  int,        "Time tag"),
    "ts":   Cmd("ts",     True,   int,        "Time slope"),
    "to":   Cmd("to",     True,   int,        "Time tag offset"),
    "ps":   Cmd("ps",     True,   int,        "Pulse slope"),
    "pl":   Cmd("pl",     True,   int,        "Phase lock"),
    "pt":   Cmd("pt",     True,   int,        "Phase lock time constant"),
    "pf":   Cmd("pf",     True,   int,        "Phase lock stability factor"),
    "pi":   Cmd("pi",     False,  int,        "Phase lock integral term"),
    # D/A Control
    "sd0":  Cmd("sd0",    True,   int,        "DAC RF amplitude"),
    "sd1":  Cmd("sd1",    True,   int,        "DAC 1PPS delay"),
    "sd2":  Cmd("sd2",    True,   int,        "DAC lamp intensity"),
    "sd3":  Cmd("sd3",    True,   int,        "DAC lamp temperature"),
    "sd4":  Cmd("sd4",    True,   int,        "DAC crystal temperature"),
    "sd5":  Cmd("sd5",    True,   int,        "DAC cell temperature"),
    "sd6":  Cmd("sd6",    True,   int,        "DAC 10 MHz amplitude"),
    "sd7":  Cmd("sd7",    True,   int,        "DAC RF deviation"),
    # Analog Test (12-bit values)
    "ad0":  Cmd("ad0",    False,  float,      "ADC Spare J204 voltage"),
    "ad1":  Cmd("ad1",    False,  float,      "ADC 24V heater supply voltage divided by 10"),
    "ad2":  Cmd("ad2",    False,  float,      "ADC 24V electronics supply divided by 10"),
    "ad3":  Cmd("ad3",    False,  float,      "ADC Drain voltage to lamp FET divided by 10"),
    "ad4":  Cmd("ad4",    False,  float,      "ADC Gate voltage to lamp FET divided by 10"),
    "ad5":  Cmd("ad5",    False,  float,      "ADC Crystal heater control voltage"),
    "ad6":  Cmd("ad6",    False,  float,      "ADC Resonance cell heater control voltage"),
    "ad7":  Cmd("ad7",    False,  float,      "ADC Discharge lamp heater control voltage"),
    "ad8":  Cmd("ad8",    False,  float,      "ADC Amplified AC photosignal"),
    "ad9":  Cmd("ad9",    False,  float,      "ADC Photocell IV converter voltage divided by 4"),
    "ad10": Cmd("ad10",   False,  float,      "ADC Case temperature Celsius divided by 100"),
    "ad11": Cmd("ad11",   False,  float,      "ADC Crystal thermistors"),
    "ad12": Cmd("ad12",   False,  float,      "ADC Cell thermistors"),
    "ad13": Cmd("ad13",   False,  float,      "ADC Lamp thermistors"),
    "ad14": Cmd("ad14",   False,  float,      "ADC Frequency calibration pot voltage"),
    "ad15": Cmd("ad15",   False,  float,      "ADC Analog ground"),
    # Analog Test (8-bit values)
    "ad16": Cmd("ad16",   False,  float,      "ADC VCXO varactor voltage divided by 4"),
    "ad17": Cmd("ad17",   False,  float,      "ADC VCO varactor voltage divided by 4"),
    "ad18": Cmd("ad18",   False,  float,      "ADC AGC for RF voltage divided by 4"),
    "ad19": Cmd("ad19",   False,  float,      "ADC RF PLL lock signal voltage"),
})
