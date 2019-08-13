from obdcommand import OBDCommand

cmds = [

    OBDCommand("PIDS_A"                     , "Supported PIDS[01-20]"                   , "0100", 6, fast=True),
    OBDCommand("STATUS"                     , "Status since DTCs cleared"               , "0101", 6, fast=True),
    OBDCommand("SPEED"                      , "Vehicle speed"                           , "010D", 1, fast=True),
    OBDCommand("RPM"                        , "Enginer RPM"                             , "010C", 2, fast=True),
    OBDCommand("PIDS_A"                     , "Supported PIDs [01-20]"                  , "0100", 6, fast=True),
    OBDCommand("STATUS"                     , "Status since DTCs cleared"               , "0101", 6, fast=True),
    OBDCommand("FREEZE_DTC"                 , "DTC that triggered the freeze frame"     , "0102", 4, fast=True),
    OBDCommand("FUEL_STATUS"                , "Fuel System Status"                      , "0103", 4, fast=True),
    OBDCommand("ENGINE_LOAD"                , "Calculated Engine Load"                  , "0104", 3, fast=True),
    OBDCommand("COOLANT_TEMP"               , "Engine Coolant Temperature"              , "0105", 3, fast=True),
    OBDCommand("SHORT_FUEL_TRIM_1"          , "Short Term Fuel Trim - Bank 1"           , "0106", 3, fast=True),
    OBDCommand("LONG_FUEL_TRIM_1"           , "Long Term Fuel Trim - Bank 1"            , "0107", 3, fast=True),
    OBDCommand("SHORT_FUEL_TRIM_2"          , "Short Term Fuel Trim - Bank 2"           , "0108", 3, fast=True),
    OBDCommand("LONG_FUEL_TRIM_2"           , "Long Term Fuel Trim - Bank 2"            , "0109", 3, fast=True),
    OBDCommand("FUEL_PRESSURE"              , "Fuel Pressure"                           , "010A", 3, fast=True),
    OBDCommand("INTAKE_PRESSURE"            , "Intake Manifold Pressure"                , "010B", 3, fast=True),
    OBDCommand("TIMING_ADVANCE"             , "Timing Advance"                          , "010E", 3, fast=True),
    OBDCommand("INTAKE_TEMP"                , "Intake Air Temp"                         , "010F", 3, fast=True),
    OBDCommand("MAF"                        , "Air Flow Rate (MAF)"                     , "0110", 4, fast=True),
    OBDCommand("THROTTLE_POS"               , "Throttle Position"                       , "0111", 3, fast=True),
    OBDCommand("AIR_STATUS"                 , "Secondary Air Status"                    , "0112", 3, fast=True),
    OBDCommand("O2_SENSORS"                 , "O2 Sensors Present"                      , "0113", 3, fast=True),
    OBDCommand("O2_B1S1"                    , "O2: Bank 1 - Sensor 1 Voltage"           , "0114", 4, fast=True),
    OBDCommand("O2_B1S2"                    , "O2: Bank 1 - Sensor 2 Voltage"           , "0115", 4, fast=True),
    OBDCommand("O2_B1S3"                    , "O2: Bank 1 - Sensor 3 Voltage"           , "0116", 4, fast=True),
    OBDCommand("O2_B1S4"                    , "O2: Bank 1 - Sensor 4 Voltage"           , "0117", 4, fast=True),
    OBDCommand("O2_B2S1"                    , "O2: Bank 2 - Sensor 1 Voltage"           , "0118", 4, fast=True),
    OBDCommand("O2_B2S2"                    , "O2: Bank 2 - Sensor 2 Voltage"           , "0119", 4, fast=True),
    OBDCommand("O2_B2S3"                    , "O2: Bank 2 - Sensor 3 Voltage"           , "011A", 4, fast=True),
    OBDCommand("O2_B2S4"                    , "O2: Bank 2 - Sensor 4 Voltage"           , "011B", 4, fast=True),
    OBDCommand("OBD_COMPLIANCE"             , "OBD Standards Compliance"                , "011C", 3, fast=True),
    OBDCommand("O2_SENSORS_ALT"             , "O2 Sensors Present (alternate)"          , "011D", 3, fast=True),
    OBDCommand("AUX_INPUT_STATUS"           , "Auxiliary input status (power take off)" , "011E", 3, fast=True),
    OBDCommand("RUN_TIME"                   , "Engine Run Time"                         , "011F", 4, fast=True),

    #          name                           description                                  cmd  bytes fast
    OBDCommand("PIDS_B"                     , "Supported PIDs [21-40]"                  , "0120", 6, fast=True),
    OBDCommand("DISTANCE_W_MIL"             , "Distance Traveled with MIL on"           , "0121", 4, fast=True),
    OBDCommand("FUEL_RAIL_PRESSURE_VAC"     , "Fuel Rail Pressure (relative to vacuum)" , "0122", 4, fast=True),
    OBDCommand("FUEL_RAIL_PRESSURE_DIRECT"  , "Fuel Rail Pressure (direct inject)"      , "0123", 4, fast=True),
    OBDCommand("O2_S1_WR_VOLTAGE"           , "02 Sensor 1 WR Lambda Voltage"           , "0124", 6, fast=True),
    OBDCommand("O2_S2_WR_VOLTAGE"           , "02 Sensor 2 WR Lambda Voltage"           , "0125", 6, fast=True),
    OBDCommand("O2_S3_WR_VOLTAGE"           , "02 Sensor 3 WR Lambda Voltage"           , "0126", 6, fast=True),
    OBDCommand("O2_S4_WR_VOLTAGE"           , "02 Sensor 4 WR Lambda Voltage"           , "0127", 6, fast=True),
    OBDCommand("O2_S5_WR_VOLTAGE"           , "02 Sensor 5 WR Lambda Voltage"           , "0128", 6, fast=True),
    OBDCommand("O2_S6_WR_VOLTAGE"           , "02 Sensor 6 WR Lambda Voltage"           , "0129", 6, fast=True),
    OBDCommand("O2_S7_WR_VOLTAGE"           , "02 Sensor 7 WR Lambda Voltage"           , "012A", 6, fast=True),
    OBDCommand("O2_S8_WR_VOLTAGE"           , "02 Sensor 8 WR Lambda Voltage"           , "012B", 6, fast=True),
    OBDCommand("COMMANDED_EGR"              , "Commanded EGR"                           , "012C", 3, fast=True),
    OBDCommand("EGR_ERROR"                  , "EGR Error"                               , "012D", 3, fast=True),
    OBDCommand("EVAPORATIVE_PURGE"          , "Commanded Evaporative Purge"             , "012E", 3, fast=True),
    OBDCommand("FUEL_LEVEL"                 , "Fuel Level Input"                        , "012F", 3, fast=True),
    OBDCommand("WARMUPS_SINCE_DTC_CLEAR"    , "Number of warm-ups since codes cleared"  , "0130", 3, fast=True),
    OBDCommand("DISTANCE_SINCE_DTC_CLEAR"   , "Distance traveled since codes cleared"   , "0131", 4, fast=True),
    OBDCommand("EVAP_VAPOR_PRESSURE"        , "Evaporative system vapor pressure"       , "0132", 4, fast=True),
    OBDCommand("BAROMETRIC_PRESSURE"        , "Barometric Pressure"                     , "0133", 3, fast=True),
    OBDCommand("O2_S1_WR_CURRENT"           , "02 Sensor 1 WR Lambda Current"           , "0134", 6, fast=True),
    OBDCommand("O2_S2_WR_CURRENT"           , "02 Sensor 2 WR Lambda Current"           , "0135", 6, fast=True),
    OBDCommand("O2_S3_WR_CURRENT"           , "02 Sensor 3 WR Lambda Current"           , "0136", 6, fast=True),
    OBDCommand("O2_S4_WR_CURRENT"           , "02 Sensor 4 WR Lambda Current"           , "0137", 6, fast=True),
    OBDCommand("O2_S5_WR_CURRENT"           , "02 Sensor 5 WR Lambda Current"           , "0138", 6, fast=True),
    OBDCommand("O2_S6_WR_CURRENT"           , "02 Sensor 6 WR Lambda Current"           , "0139", 6, fast=True),
    OBDCommand("O2_S7_WR_CURRENT"           , "02 Sensor 7 WR Lambda Current"           , "013A", 6, fast=True),
    OBDCommand("O2_S8_WR_CURRENT"           , "02 Sensor 8 WR Lambda Current"           , "013B", 6, fast=True),
    OBDCommand("CATALYST_TEMP_B1S1"         , "Catalyst Temperature: Bank 1 - Sensor 1" , "013C", 4, fast=True),
    OBDCommand("CATALYST_TEMP_B2S1"         , "Catalyst Temperature: Bank 2 - Sensor 1" , "013D", 4, fast=True),
    OBDCommand("CATALYST_TEMP_B1S2"         , "Catalyst Temperature: Bank 1 - Sensor 2" , "013E", 4, fast=True),
    OBDCommand("CATALYST_TEMP_B2S2"         , "Catalyst Temperature: Bank 2 - Sensor 2" , "013F", 4, fast=True),

    #                      name                             description                    cmd  bytes       decoder           ECU       fast
    OBDCommand("PIDS_C"                     , "Supported PIDs [41-60]"                  , "0140", 6, fast=True),
    OBDCommand("STATUS_DRIVE_CYCLE"         , "Monitor status this drive cycle"         , "0141", 6, fast=True),
    OBDCommand("CONTROL_MODULE_VOLTAGE"     , "Control module voltage"                  , "0142", 4, fast=True),
    OBDCommand("ABSOLUTE_LOAD"              , "Absolute load value"                     , "0143", 4, fast=True),
    OBDCommand("COMMANDED_EQUIV_RATIO"      , "Commanded equivalence ratio"             , "0144", 4, fast=True),
    OBDCommand("RELATIVE_THROTTLE_POS"      , "Relative throttle position"              , "0145", 3, fast=True),
    OBDCommand("AMBIANT_AIR_TEMP"           , "Ambient air temperature"                 , "0146", 3, fast=True),
    OBDCommand("THROTTLE_POS_B"             , "Absolute throttle position "             , "0147", 3, fast=True),
    OBDCommand("THROTTLE_POS_C"             , "Absolute throttle position C"            , "0148", 3, fast=True),
    OBDCommand("ACCELERATOR_POS_D"          , "Accelerator pedal position D"            , "0149", 3, fast=True),
    OBDCommand("ACCELERATOR_POS_E"          , "Accelerator pedal position E"            , "014A", 3, fast=True),
    OBDCommand("ACCELERATOR_POS_F"          , "Accelerator pedal position F"            , "014B", 3, fast=True),
    OBDCommand("THROTTLE_ACTUATOR"          , "Commanded throttle actuator"             , "014C", 3, fast=True),
    OBDCommand("RUN_TIME_MIL"               , "Time run with MIL on"                    , "014D", 4, fast=True),
    OBDCommand("TIME_SINCE_DTC_CLEARED"     , "Time since trouble codes cleared"        , "014E", 4, fast=True),
    OBDCommand("MAX_VALUES"                 , "Various Max values"                      , "014F", 6, fast=True), # todo: decode this
    OBDCommand("MAX_MAF"                    , "Maximum value for mass air flow sensor"  , "0150", 6, fast=True),
    OBDCommand("FUEL_TYPE"                  , "Fuel Type"                               , "0151", 3, fast=True),
    OBDCommand("ETHANOL_PERCENT"            , "Ethanol Fuel Percent"                    , "0152", 3, fast=True),
    OBDCommand("EVAP_VAPOR_PRESSURE_ABS"    , "Absolute Evap system Vapor Pressure"     , "0153", 4, fast=True),
    OBDCommand("EVAP_VAPOR_PRESSURE_ALT"    , "Evap system vapor pressure"              , "0154", 4, fast=True),
    OBDCommand("SHORT_O2_TRIM_B1"           , "Short term secondary O2 trim - Bank 1"   , "0155", 4, fast=True), # todo: decode seconds value for banks 3 and 4
    OBDCommand("LONG_O2_TRIM_B1"            , "Long term secondary O2 trim - Bank 1"    , "0156", 4, fast=True),
    OBDCommand("SHORT_O2_TRIM_B2"           , "Short term secondary O2 trim - Bank 2"   , "0157", 4, fast=True),
    OBDCommand("LONG_O2_TRIM_B2"            , "Long term secondary O2 trim - Bank 2"    , "0158", 4, fast=True),
    OBDCommand("FUEL_RAIL_PRESSURE_ABS"     , "Fuel rail pressure (absolute)"           , "0159", 4, fast=True),
    OBDCommand("RELATIVE_ACCEL_POS"         , "Relative accelerator pedal position"     , "015A", 3, fast=True),
    OBDCommand("HYBRID_BATTERY_REMAINING"   , "Hybrid battery pack remaining life"      , "015B", 3, fast=True),
    OBDCommand("OIL_TEMP"                   , "Engine oil temperature"                  , "015C", 3, fast=True),
    OBDCommand("FUEL_INJECT_TIMING"         , "Fuel injection timing"                   , "015D", 4, fast=True),
    OBDCommand("FUEL_RATE"                  , "Engine fuel rate"                        , "015E", 4, fast=True),
    OBDCommand("EMISSION_REQ"               , "Designed emission requirements"          , "015F", 3, fast=True),
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
