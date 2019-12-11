from obdcommand import OBDCommand
from decoders import *
cmds = [
    #          name                           description                                 cmd   bytes   decoder      fast
    OBDCommand("PIDS_A"                     , "Supported PIDS[01-20]"                   , "0100", 4, decoder=None,  fast=True),
    OBDCommand("STATUS"                     , "Status since DTCs cleared"               , "0101", 4, decoder=None,  fast=True),
    OBDCommand("FREEZE_DTC"                 , "DTC that triggered the freeze frame"     , "0102", 2, decoder=None, fast=True),
    OBDCommand("FUEL_STATUS"                , "Fuel System Status"                      , "0103", 2, decoder=None, fast=True),
    OBDCommand("ENGINE_LOAD"                , "Calculated Engine Load"                  , "0104", 1, decoder=engine_load, fast=True),
    OBDCommand("COOLANT_TEMP"               , "Engine Coolant Temperature"              , "0105", 1, decoder=engine_coolant_temp, fast=True),
    OBDCommand("SHORT_FUEL_TRIM_1"          , "Short Term Fuel Trim - Bank 1"           , "0106", 1, decoder=short_term_fuel_trim, fast=True),
    OBDCommand("LONG_FUEL_TRIM_1"           , "Long Term Fuel Trim - Bank 1"            , "0107", 1, decoder=short_term_fuel_trim, fast=True),
    OBDCommand("SHORT_FUEL_TRIM_2"          , "Short Term Fuel Trim - Bank 2"           , "0108", 1, decoder=short_term_fuel_trim, fast=True),
    OBDCommand("LONG_FUEL_TRIM_2"           , "Long Term Fuel Trim - Bank 2"            , "0109", 1, decoder=short_term_fuel_trim, fast=True),
    OBDCommand("FUEL_PRESSURE"              , "Fuel Pressure"                           , "010A", 1, decoder=fuel_pressure, fast=True),
    OBDCommand("INTAKE_PRESSURE"            , "Intake Manifold Pressure"                , "010B", 1, decoder=intake_manifold_pressure, fast=True),
    OBDCommand("RPM"                        , "Engine RPM"                              , "010C", 2, decoder=rpm,   fast=True),
    OBDCommand("SPEED"                      , "Vehicle speed"                           , "010D", 1, decoder=speed, fast=True),
    OBDCommand("TIMING_ADVANCE"             , "Timing Advance"                          , "010E", 1, decoder=timing_advance, fast=True),
    OBDCommand("INTAKE_TEMP"                , "Intake Air Temp"                         , "010F", 1, decoder=intake_air_temp, fast=True),
    OBDCommand("MAF"                        , "Air Flow Rate (MAF)"                     , "0110", 2, decoder=maf_rate, fast=True),
    OBDCommand("THROTTLE_POS"               , "Throttle Position"                       , "0111", 1, decoder=throttle_position, fast=True),
    OBDCommand("AIR_STATUS"                 , "Secondary Air Status"                    , "0112", 1, decoder=None, fast=True),
    OBDCommand("O2_SENSORS"                 , "O2 Sensors Present"                      , "0113", 1, decoder=None, fast=True),
    OBDCommand("O2_B1S1"                    , "O2: Bank 1 - Sensor 1 Voltage"           , "0114", 2, decoder=o2_sensor, fast=True),
    OBDCommand("O2_B1S2"                    , "O2: Bank 1 - Sensor 2 Voltage"           , "0115", 2, decoder=o2_sensor, fast=True),
    OBDCommand("O2_B1S3"                    , "O2: Bank 1 - Sensor 3 Voltage"           , "0116", 2, decoder=o2_sensor, fast=True),
    OBDCommand("O2_B1S4"                    , "O2: Bank 1 - Sensor 4 Voltage"           , "0117", 2, decoder=o2_sensor, fast=True),
    OBDCommand("O2_B2S1"                    , "O2: Bank 2 - Sensor 1 Voltage"           , "0118", 2, decoder=o2_sensor, fast=True),
    OBDCommand("O2_B2S2"                    , "O2: Bank 2 - Sensor 2 Voltage"           , "0119", 2, decoder=o2_sensor, fast=True),
    OBDCommand("O2_B2S3"                    , "O2: Bank 2 - Sensor 3 Voltage"           , "011A", 2, decoder=o2_sensor, fast=True),
    OBDCommand("O2_B2S4"                    , "O2: Bank 2 - Sensor 4 Voltage"           , "011B", 2, decoder=o2_sensor, fast=True),
    OBDCommand("OBD_COMPLIANCE"             , "OBD Standards Compliance"                , "011C", 1, decoder=None, fast=True),
    OBDCommand("O2_SENSORS_ALT"             , "O2 Sensors Present (alternate)"          , "011D", 1, decoder=None, fast=True),
    OBDCommand("AUX_INPUT_STATUS"           , "Auxiliary input status (power take off)" , "011E", 1, decoder=None, fast=True),
    OBDCommand("RUN_TIME"                   , "Engine Run Time"                         , "011F", 2, decoder=runtime_since_engine_start, fast=True),
    OBDCommand("PIDS_B"                     , "Supported PIDs [21-40]"                  , "0120", 4, decoder=None, fast=True),
    OBDCommand("DISTANCE_W_MIL"             , "Distance Traveled with MIL on"           , "0121", 2, decoder=distance_with_mil, fast=True),
    OBDCommand("FUEL_RAIL_PRESSURE_VAC"     , "Fuel Rail Pressure (relative to vacuum)" , "0122", 2, decoder=fuel_rail_pressure, fast=True),
    OBDCommand("FUEL_RAIL_PRESSURE_DIRECT"  , "Fuel Rail Pressure (direct inject)"      , "0123", 2, decoder=fuel_rail_gauge, fast=True),
    OBDCommand("O2_S1_WR_VOLTAGE"           , "02 Sensor 1 WR Lambda Voltage"           , "0124", 4, decoder=None, fast=True),
    OBDCommand("O2_S2_WR_VOLTAGE"           , "02 Sensor 2 WR Lambda Voltage"           , "0125", 4, decoder=None, fast=True),
    OBDCommand("O2_S3_WR_VOLTAGE"           , "02 Sensor 3 WR Lambda Voltage"           , "0126", 4, decoder=None, fast=True),
    OBDCommand("O2_S4_WR_VOLTAGE"           , "02 Sensor 4 WR Lambda Voltage"           , "0127", 4, decoder=None, fast=True),
    OBDCommand("O2_S5_WR_VOLTAGE"           , "02 Sensor 5 WR Lambda Voltage"           , "0128", 4, decoder=None, fast=True),
    OBDCommand("O2_S6_WR_VOLTAGE"           , "02 Sensor 6 WR Lambda Voltage"           , "0129", 4, decoder=None, fast=True),
    OBDCommand("O2_S7_WR_VOLTAGE"           , "02 Sensor 7 WR Lambda Voltage"           , "012A", 4, decoder=None, fast=True),
    OBDCommand("O2_S8_WR_VOLTAGE"           , "02 Sensor 8 WR Lambda Voltage"           , "012B", 4, decoder=None, fast=True),
    OBDCommand("COMMANDED_EGR"              , "Commanded EGR"                           , "012C", 1, decoder=None, fast=True),
    OBDCommand("EGR_ERROR"                  , "EGR Error"                               , "012D", 1, decoder=None, fast=True),
    OBDCommand("EVAPORATIVE_PURGE"          , "Commanded Evaporative Purge"             , "012E", 1, decoder=None, fast=True),
    OBDCommand("FUEL_LEVEL"                 , "Fuel Level Input"                        , "012F", 1, decoder=None, fast=True),
    OBDCommand("WARMUPS_SINCE_DTC_CLEAR"    , "Number of warm-ups since codes cleared"  , "0130", 1, decoder=None, fast=True),
    OBDCommand("DISTANCE_SINCE_DTC_CLEAR"   , "Distance traveled since codes cleared"   , "0131", 2, decoder=None, fast=True),
    OBDCommand("EVAP_VAPOR_PRESSURE"        , "Evaporative system vapor pressure"       , "0132", 2, decoder=None, fast=True),
    OBDCommand("BAROMETRIC_PRESSURE"        , "Barometric Pressure"                     , "0133", 1, decoder=barometric_pressure, fast=True),
    OBDCommand("O2_S1_WR_CURRENT"           , "02 Sensor 1 WR Lambda Current"           , "0134", 4, decoder=None, fast=True),
    OBDCommand("O2_S2_WR_CURRENT"           , "02 Sensor 2 WR Lambda Current"           , "0135", 4, decoder=None, fast=True),
    OBDCommand("O2_S3_WR_CURRENT"           , "02 Sensor 3 WR Lambda Current"           , "0136", 4, decoder=None, fast=True),
    OBDCommand("O2_S4_WR_CURRENT"           , "02 Sensor 4 WR Lambda Current"           , "0137", 4, decoder=None, fast=True),
    OBDCommand("O2_S5_WR_CURRENT"           , "02 Sensor 5 WR Lambda Current"           , "0138", 4, decoder=None, fast=True),
    OBDCommand("O2_S6_WR_CURRENT"           , "02 Sensor 6 WR Lambda Current"           , "0139", 4, decoder=None, fast=True),
    OBDCommand("O2_S7_WR_CURRENT"           , "02 Sensor 7 WR Lambda Current"           , "013A", 4, decoder=None, fast=True),
    OBDCommand("O2_S8_WR_CURRENT"           , "02 Sensor 8 WR Lambda Current"           , "013B", 4, decoder=None, fast=True),
    OBDCommand("CATALYST_TEMP_B1S1"         , "Catalyst Temperature: Bank 1 - Sensor 1" , "013C", 2, decoder=None, fast=True),
    OBDCommand("CATALYST_TEMP_B2S1"         , "Catalyst Temperature: Bank 2 - Sensor 1" , "013D", 2, decoder=None, fast=True),
    OBDCommand("CATALYST_TEMP_B1S2"         , "Catalyst Temperature: Bank 1 - Sensor 2" , "013E", 2, decoder=None, fast=True),
    OBDCommand("CATALYST_TEMP_B2S2"         , "Catalyst Temperature: Bank 2 - Sensor 2" , "013F", 2, decoder=None, fast=True),
    OBDCommand("PIDS_C"                     , "Supported PIDs [41-60]"                  , "0140", 4, decoder=None, fast=True),
    OBDCommand("STATUS_DRIVE_CYCLE"         , "Monitor status this drive cycle"         , "0141", 4, decoder=None, fast=True),
    OBDCommand("CONTROL_MODULE_VOLTAGE"     , "Control module voltage"                  , "0142", 2, decoder=None, fast=True),
    OBDCommand("ABSOLUTE_LOAD"              , "Absolute load value"                     , "0143", 2, decoder=None, fast=True),
    OBDCommand("COMMANDED_EQUIV_RATIO"      , "Commanded equivalence ratio"             , "0144", 2, decoder=None, fast=True),
    OBDCommand("RELATIVE_THROTTLE_POS"      , "Relative throttle position"              , "0145", 1, decoder=None, fast=True),
    OBDCommand("AMBIANT_AIR_TEMP"           , "Ambient air temperature"                 , "0146", 1, decoder=None, fast=True),
    OBDCommand("THROTTLE_POS_B"             , "Absolute throttle position "             , "0147", 1, decoder=None, fast=True),
    OBDCommand("THROTTLE_POS_C"             , "Absolute throttle position C"            , "0148", 1, decoder=None, fast=True),
    OBDCommand("ACCELERATOR_POS_D"          , "Accelerator pedal position D"            , "0149", 1, decoder=None, fast=True),
    OBDCommand("ACCELERATOR_POS_E"          , "Accelerator pedal position E"            , "014A", 1, decoder=None, fast=True),
    OBDCommand("ACCELERATOR_POS_F"          , "Accelerator pedal position F"            , "014B", 1, decoder=None, fast=True),
    OBDCommand("THROTTLE_ACTUATOR"          , "Commanded throttle actuator"             , "014C", 1, decoder=None, fast=True),
    OBDCommand("RUN_TIME_MIL"               , "Time run with MIL on"                    , "014D", 2, decoder=None, fast=True),
    OBDCommand("TIME_SINCE_DTC_CLEARED"     , "Time since trouble codes cleared"        , "014E", 2, decoder=None, fast=True),
    OBDCommand("MAX_VALUES"                 , "Various Max values"                      , "014F", 4, decoder=None, fast=True), # todo: decode this
    OBDCommand("MAX_MAF"                    , "Maximum value for mass air flow sensor"  , "0150", 4, decoder=None, fast=True),
    OBDCommand("FUEL_TYPE"                  , "Fuel Type"                               , "0151", 1, decoder=None, fast=True),
    OBDCommand("ETHANOL_PERCENT"            , "Ethanol Fuel Percent"                    , "0152", 1, decoder=None, fast=True),
    OBDCommand("EVAP_VAPOR_PRESSURE_ABS"    , "Absolute Evap system Vapor Pressure"     , "0153", 2, decoder=None, fast=True),
    OBDCommand("EVAP_VAPOR_PRESSURE_ALT"    , "Evap system vapor pressure"              , "0154", 2, decoder=None, fast=True),
    OBDCommand("SHORT_O2_TRIM_B1"           , "Short term secondary O2 trim - Bank 1"   , "0155", 2, decoder=None, fast=True), # todo: decode seconds value for banks 3 and 4
    OBDCommand("LONG_O2_TRIM_B1"            , "Long term secondary O2 trim - Bank 1"    , "0156", 2, decoder=None, fast=True),
    OBDCommand("SHORT_O2_TRIM_B2"           , "Short term secondary O2 trim - Bank 2"   , "0157", 2, decoder=None, fast=True),
    OBDCommand("LONG_O2_TRIM_B2"            , "Long term secondary O2 trim - Bank 2"    , "0158", 2, decoder=None, fast=True),
    OBDCommand("FUEL_RAIL_PRESSURE_ABS"     , "Fuel rail pressure (absolute)"           , "0159", 2, decoder=None, fast=True),
    OBDCommand("RELATIVE_ACCEL_POS"         , "Relative accelerator pedal position"     , "015A", 1, decoder=None, fast=True),
    OBDCommand("HYBRID_BATTERY_REMAINING"   , "Hybrid battery pack remaining life"      , "015B", 1, decoder=None, fast=True),
    OBDCommand("OIL_TEMP"                   , "Engine oil temperature"                  , "015C", 1, decoder=None, fast=True),
    OBDCommand("FUEL_INJECT_TIMING"         , "Fuel injection timing"                   , "015D", 2, decoder=None, fast=True),
    OBDCommand("FUEL_RATE"                  , "Engine fuel rate"                        , "015E", 2, decoder=None, fast=True),
    OBDCommand("EMISSION_REQ"               , "Designed emission requirements"          , "015F", 1, decoder=None, fast=True),
    OBDCommand("ENGINE_REFERENCE_TQ"        , "Engine reference torque"                 , "0163", 2, decoder=engine_reference_tq, fast=True),
    OBDCommand("ENGINE_PERCENT_TQ"          , "Engine percent torque"                   , "0164", 1, decoder=engine_percent_tq, fast=True),

            #################################### OBD AT COMMANDS ############################################
    OBDCommand("RESET_ALL"                  , "Reset all"                               , "ATZ",  1, decoder=at_decoder, fast=True),    
    OBDCommand("LINE_FEED_OFF"              , "Turn off the line feed"                  , "ATL0", 1, decoder=at_decoder, fast=True),
    OBDCommand("LINE_FEED_ON"               , "Turn on the line feed"                   , "ATL1", 1, decoder=at_decoder, fast=True),
    OBDCommand("HEADERS_OFF"                , "Turn off the headers"                    , "ATH0", 1, decoder=at_decoder, fast=True),
    OBDCommand("HEADERS_ON"                 , "Turn on the headers"                     , "ATH1", 1, decoder=at_decoder, fast=True),
    OBDCommand("MONITOR_ALL"                , "Monitor all"                             , "ATMA", 1, decoder=at_decoder, fast=True)
]

class Commands():
    def __init__(self):
        for cmd in cmds:
            if cmd is not None:
                self.__dict__[cmd.name] = cmd

    def __getitem__(self, key):
        if isinstance(key, basestring):
            return self.__dict__[key]
        else:
            print ("Command Error")


commands = Commands()
