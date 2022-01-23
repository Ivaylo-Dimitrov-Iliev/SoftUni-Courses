import  re

pattern = r"(?P<surr>[\=|\/])(?P<name>[A-Z][A-Za-z]{3,})(?P=surr)"

places = input()

matches = re.finditer(pattern, places)

destinations = []

travel_points = 0

for match in matches:
    destinations.append(match.group("name"))
    travel_points += int(len(match.group("name")))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
