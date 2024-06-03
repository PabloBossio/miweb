def liters100km_to_MPG(liters):
    # 1 galón es = 3.785411784 litros.
    gallons = liters / 3.785411784
    # 100 kilometros = 100 * 1000 / 1609.344 metros por milla.
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def MPG_to_liters100km(mpg):
    # 1 milla = 1609.344 metros.
    km_per_mile = 1609.344 / 1000
    # 1 galón = 3.78541784 litros.
    lietrs_per_gallon = 3.785411784
    # kilometros recorridos por galón (mpg)
    km_per_gallon = mpg * km_per_mile
    # convertir a litros por 100kilometros. 
    liters_per_100km = lietrs_per_gallon / km_per_gallon * 100
    return liters_per_100km

print(liters100km_to_MPG(3.9))    
print(liters100km_to_MPG(7.5)) 
print(liters100km_to_MPG(10.0))
print(MPG_to_liters100km(23.5))   
print(MPG_to_liters100km(31.4))  
print(MPG_to_liters100km(60.3)) 
