source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

def save_applicant_data(source, output):
    with open(output, "w") as file:
        for abiturient in source:
            new_format_line = []
            for value in abiturient.values():
                new_format_line.append(str(value))
            print(new_format_line)
            line = ",".join(new_format_line).replace('"', '') + "\n"
            print(line)     
            file.write(line)

output = "output.txt"
save_applicant_data(source, output)
print(output)
