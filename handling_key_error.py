def get_city_population(populations, city):
    """returns population info based on the city

    Args:
        populations (dict): populations
        city (str): city

    Returns:
        int: return population if exists.
        
    Raises:
        KeyError: if city not found in population data.
    """
    try:
        return populations[city]  # This will naturally raise KeyError if key doesn't exist
    except KeyError:
        raise KeyError(f'City "{city}" not found in population data.')


city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

# Test existing city
city_name = "New York"
print(f"The population of {city_name} is {get_city_population(city_populations, city_name)}.")

# Test non-existing city (this will raise KeyError)
city_name = "Tampa"
try:
    result = get_city_population(city_populations, city_name)
except KeyError as e:
    print(e)  # This will print the custom error message