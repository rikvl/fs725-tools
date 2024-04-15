# Commands for the SRS FS725 Rubidium Frequency Standard

# flake8: noqa

from collections import namedtuple, OrderedDict

# Namedtuple to store a command for the FS725
Cmd = namedtuple("Cmd", ["mnem", "rtn_type", "description"])

# List of FS725 commands, stored as Command namedtuples with these fields:
# mnem:         Two-letter (plus possible number) ASCII mnemonic of the command
# rtn_type:     What type the returned string should be converted to
# description:  Description of command
fs725_commands = OrderedDict({
    #           mnem,     rtn_type,   description
    # Initialize
    "vb":   Cmd("vb",     int,        "Verbose mode"),
    "sn":   Cmd("sn",     int,        "Serial number"),
    "st":   Cmd("st",     [int] * 6,  "Status values"),
    "lm":   Cmd("lm",     int,        "Lock pin mode configuration"),
    # Freq. Lock
    "lo":   Cmd("lo",     int,        "Frequency lock loop status"),
    "fc":   Cmd("fc",     [int] * 2,  "Frequency control values"),
    "ds":   Cmd("ds",     [int] * 2,  "Detected signals"),
    "sf":   Cmd("sf",     int,        "Frequency offset"),
    "ss":   Cmd("ss",     int,        "Frequency calibration slope"),
    "ga":   Cmd("ga",     int,        "FLL gain"),
    "ph":   Cmd("ph",     int,        "Phase angle"),
    "sp":   Cmd("sp",     [int] * 3,  "Synthesizer parameters"),
    # Magnetic Tuning
    "ms":   Cmd("ms",     int,        "Magnetic switching"),
    "mo":   Cmd("mo",     int,        "Magnetic offset"),
    "mr":   Cmd("mr",     int,        "Magnet read"),
    # 1PPS Lock
    "tt":   Cmd("tt",     int,        "Time tag"),
    "ts":   Cmd("ts",     int,        "Time slope"),
    "to":   Cmd("to",     int,        "Time tag offset"),
    "ps":   Cmd("ps",     int,        "Pulse slope"),
    "pl":   Cmd("pl",     int,        "Phase lock"),
    "pt":   Cmd("pt",     int,        "Phase lock time constant"),
    "pf":   Cmd("pf",     int,        "Phase lock stability factor"),
    "pi":   Cmd("pi",     int,        "Phase lock integral term"),
    # D/A Control
    "sd0":  Cmd("sd0",    int,        "DAC RF amplitude"),
    "sd1":  Cmd("sd1",    int,        "DAC 1PPS delay"),
    "sd2":  Cmd("sd2",    int,        "DAC Lamp intensity"),
    "sd3":  Cmd("sd3",    int,        "DAC Lamp temperature"),
    "sd4":  Cmd("sd4",    int,        "DAC Crystal temperature"),
    "sd5":  Cmd("sd5",    int,        "DAC Cell temperature"),
    "sd6":  Cmd("sd6",    int,        "DAC 10 MHz amplitude"),
    "sd7":  Cmd("sd7",    int,        "DAC RF deviation"),
    # Analog Test (12-bit values)
    "ad0":  Cmd("ad0",    float,      "ADC Spare (J204)"),
    "ad1":  Cmd("ad1",    float,      "ADC +24V (heater supply) / 10"),
    "ad2":  Cmd("ad2",    float,      "ADC +24V (electronics supply) / 10"),
    "ad3":  Cmd("ad3",    float,      "ADC Drain voltage to lamp FET / 10"),
    "ad4":  Cmd("ad4",    float,      "ADC Gate voltage to lamp FET / 10"),
    "ad5":  Cmd("ad5",    float,      "ADC Crystal heater control voltage"),
    "ad6":  Cmd("ad6",    float,      "ADC Resonance cell heater control voltage"),
    "ad7":  Cmd("ad7",    float,      "ADC Discharge lamp heater control voltage"),
    "ad8":  Cmd("ad8",    float,      "ADC Amplified AC photosignal"),
    "ad9":  Cmd("ad9",    float,      "ADC Photocell's I/V converter voltage / 4"),
    "ad10": Cmd("ad10",   float,      "ADC Case temperature (10 mV/degC)"),
    "ad11": Cmd("ad11",   float,      "ADC Crystal thermistors"),
    "ad12": Cmd("ad12",   float,      "ADC Cell thermistors"),
    "ad13": Cmd("ad13",   float,      "ADC Lamp thermistors"),
    "ad14": Cmd("ad14",   float,      "ADC Frequency calibration pot / external calibration voltage"),
    "ad15": Cmd("ad15",   float,      "ADC Analog ground"),
    # Analog Test (8-bit values)
    "ad16": Cmd("ad16",   float,      "ADC Varactor voltage for 22.48 MHz VCXO / 4"),
    "ad17": Cmd("ad17",   float,      "ADC Varactor voltage for 360 MHz VCO / 4"),
    "ad18": Cmd("ad18",   float,      "ADC AGC for RF voltage / 4"),
    "ad19": Cmd("ad19",   float,      "ADC RF PLL lock signal voltage"),
})
