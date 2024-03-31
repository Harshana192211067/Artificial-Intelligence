%Database of planets with their properties
planet(mercury, rocky, 0.39).
planet(venus, rocky, 0.72).
planet(earth, rocky, 1.00).
planet(mars, rocky, 1.52).
planet(jupiter, gas_giant, 5.20).
planet(saturn, gas_giant, 9.58).
planet(uranus, ice_giant, 19.22).
planet(neptune, ice_giant, 30.05).

% Query to retrieve properties of a planet
planet_properties(Name, Type, Distance_from_sun) :-
    planet(Name, Type, Distance_from_sun).

% Query to retrieve planets of a specific type
planets_of_type(Type, Planets) :-
    findall(Name, planet(Name, Type, _), Planets).

% Query to retrieve planets within a specific distance range from the sun
planets_within_distance(MinDistance, MaxDistance, Planets) :-
    findall(Name, (planet(Name, _, Distance), Distance >= MinDistance, Distance =< MaxDistance), Planets).

