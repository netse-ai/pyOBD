def speed(val):
    return "SPEED: ", float(int('0x'+ val, 0))

def rpm(val):
    upper = float(int('0x'+ val[0:2], 0)) * 256
    lower = float(int('0x'+ val[2:4], 0))
    return "RPM: ", (upper + lower) / 4

def engine_load(val):
    return "ENGINE_LOAD: ", float(int('0x'+ val, 0)) / 2.55

def engine_coolant_temp(val):
    return "ENGINE_COOLANT_TEMP: ", float(int('0x'+ val, 0)) - 40

def short_term_fuel_trim(val):
    return "SHORT_TERM_FUEL_TRIM: ", ((100/128)*float(int('0x'+ val, 0))) - 100

def fuel_pressure(val):
    return "FUEL_PRESSURE: ", 3 * float(int('0x'+ val, 0))

def intake_manifold_pressure(val):
    return "INTAKE_PRESSURE", float(int('0x'+ val, 0))
