def at_decoder(val):
    print(val)

def speed(val):
    try:
        data = float(int('0x'+ val, 0)) * .6214
    except ValueError:
        data = None
    return data

def rpm(val):
    print "RPM: {0}".format(val)
    upper = float(int('0x'+ val[0:2], 0)) * 256
    lower = float(int('0x'+ val[2:4], 0))
    data = (upper + lower) / 4
    return data

def engine_load(val):
    try:
        data = float(int('0x'+ val, 0)) / 2.55
    except ValueError:
        data = None
    return data

def engine_coolant_temp(val):
    try:
        data = float(int('0x'+ val, 0)) - 40
    except:
        data = None
    return data

def short_term_fuel_trim(val):
    return ((100/128)*float(int('0x'+ val, 0))) - 100

def fuel_pressure(val):
    return 3 * float(int('0x'+ val, 0))

def intake_manifold_pressure(val):
    return float(int('0x'+ val, 0))

def timing_advance(val):
    return (float(int('0x'+ val, 0))/2) - 64

def intake_air_temp(val):
    float(int('0x'+ val, 0)) - 40

def maf_rate(val):
    upper = float(int('0x'+ val[0:2], 0)) * 256
    lower = float(int('0x'+ val[2:4], 0))
    return (upper + lower) / 100

def throttle_position(val):
    return (100/255) * float(int('0x'+ val, 0))

def o2_sensor(val):
    voltage = float(int('0x'+ val[0:2], 0))/200
    short_term_fuel_trim = ((100/128)*float(int('0x'+ val[2:4], 0))) - 100

def runtime_since_engine_start(val):
    return (256 * (float(int('0x'+ val[0:2], 0)))) + float(int('0x'+ val[2:4], 0))

def distance_with_mil(val):
    return (256 * (float(int('0x'+ val[0:2], 0)))) + float(int('0x'+ val[2:4], 0))

def fuel_rail_pressure(val):
    return .079 * ((256 * (float(int('0x'+ val[0:2], 0)))) + float(int('0x'+ val[2:4], 0)))

def fuel_rail_gauge(val):
    return 10 * ((256 * (float(int('0x'+ val[0:2], 0)))) + float(int('0x'+ val[2:4], 0)))

def barometric_pressure(val):
    return float(int('0x'+ val, 0))

def engine_percent_tq(val):
    upper = float(int('0x'+ val[0:2], 0)) * 256
    lower = float(int('0x'+ val[2:4], 0))
    return (upper+lower) * 0.73756

def engine_reference_tq(val):
    upper = float(int('0x'+ val[0:2], 0)) * 256
    lower = float(int('0x'+ val[2:4], 0))
    return (upper+lower)

