def liters100km_to_MPG(liters):
    # 1 galón = 3.7854411784 litros.
    Gallons = liters / 3.785411784
    # 100 kilometros = 100 * 1000 metros / 1609.344 metros por milla 
    miles = 100 * 1000 / 1609.344
    return miles / Gallons 

def MPG_to_liters100km(miles):
    
    km = miles * 1609.344 / 1000 / 100
    liters = 3.785411784
    return liters / km

print(liters100km_to_MPG(3.9))
print(liters100km_to_MPG(7.5))
print(liters100km_to_MPG(10.))
print(MPG_to_liters100km(23.5))
print(MPG_to_liters100km(31.4))
print(MPG_to_liters100km(60.3))
