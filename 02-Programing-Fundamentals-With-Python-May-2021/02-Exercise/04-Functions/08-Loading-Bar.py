def loading_bar(number):
    bar = ["."] * 10
    for current_number in range(1, number + 1, 10):
        current_symbol = "%"
        bar[current_number // 10] = current_symbol
    bar_as_string = "".join(bar)
    if number == 100:
        result = f"{number}% Complete!\n[{bar_as_string}]"
    else:
        result = f"{number}% [{bar_as_string}]\nStill loading..."
    return result


input_number = int(input())

print(loading_bar(input_number))
