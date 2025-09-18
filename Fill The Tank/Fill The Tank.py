def cost_to_fill(tank_size, fuel_level, price_per_gallon):


    fuel_needed = tank_size - fuel_level
    
    if fuel_needed < 0:
        fuel_needed = 0
    
    total_cost = fuel_needed * price_per_gallon

    rounded_cost = round(total_cost, 2)


    formatted_cost = f"${rounded_cost:.2f}"
    
    return formatted_cost




print(cost_to_fill(20, 0, 4.00))
