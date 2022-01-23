software_version = input().split(".")

software_version_as_int = []

parse = [software_version_as_int.append(int(current_num)) for current_num in software_version]

for i in range(len(software_version_as_int))[::-1]:
    if software_version_as_int[i] + 1 > 9:
        software_version_as_int[i] = 0
    else:
        software_version_as_int[i] += 1
        break

print(*software_version_as_int, sep=".")
