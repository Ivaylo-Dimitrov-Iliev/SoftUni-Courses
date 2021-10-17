import re

pattern = r"^(?P<surr_1>\@\#+)(?P<word>[A-Z][A-Za-z0-9]{4,}[A-Z])(?P<surr_2>\@\#+)$"

count_of_barcodes = int(input())

for _ in range(count_of_barcodes):
    barcode = input()
    match = re.match(pattern, barcode)
    if not match:
        print("Invalid barcode")
    else:
        matched_barcode = match.group("word")
        product_group = ""
        for el in matched_barcode:
            if el.isdigit():
                product_group += el
        if product_group == "":
            product_group = "00"
            print(f"Product group: {product_group}")
        else:
            print(f"Product group: {product_group}")
