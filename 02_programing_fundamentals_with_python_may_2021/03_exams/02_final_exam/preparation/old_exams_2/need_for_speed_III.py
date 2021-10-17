count_of_cars = int(input())

cars = {}

for _ in range(count_of_cars):
    text = input()
    data = text.split("|")
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])
    cars[car] = {"mileage": mileage, "fuel": fuel}

command = input()

while not command == "Stop":
    data = command.split(" : ")
    action = data[0]

    if action == "Drive":
        car = data[1]
        distance = int(data[2])
        fuel = int(data[3])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            cars.pop(car)

    elif action == "Refuel":
        car = data[1]
        fuel = int(data[2])
        if 75 - cars[car]["fuel"] < fuel:
            print(f"{car} refueled with {75 - cars[car]['fuel']} liters")
            cars[car]["fuel"] = 75
        else:
            cars[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        car = data[1]
        kilometers = int(data[2])
        if cars[car]["mileage"] - kilometers < 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

sorted_cars = sorted(cars.items(), key=lambda tkvp: (-tkvp[1]["mileage"], tkvp[0]))

for car, data in sorted_cars:
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")
