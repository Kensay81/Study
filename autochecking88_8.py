def to_indexed(source_file, output_file):
    clear_lines = []
    with open(source_file, "r") as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            #line = line.rstrip()
            clear_lines.append( f"{index}: {line}")
    
    with open(output_file, "w") as file:
        for line in clear_lines:
            file.write(line)

python
Copy code
def to_indexed(source_file, output_file):
    with open(source_file, "r") as file:
        lines = file.readlines()
        
    with open(output_file, "w") as file:
        for index, line in enumerate(lines):
            line = line.strip()  # Удаляем символы перевода строки справа от строки
            file.write(f"{index}: {line}\n")