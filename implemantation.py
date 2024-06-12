import os

def find_duplicates(input_dir, input_filename, output_dir, output_filename):
    counts = {}
    input_path = os.path.join(input_dir, input_filename)
    output_path = os.path.join(output_dir, output_filename)
    
    with open(input_path, 'r') as infile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 1:
                continue
            try:
                number = int(parts[0])
            except ValueError:
                continue
            if number in counts:
                counts[number] += 1
            else:
                counts[number] = 1
    
    duplicates = [num for num, count in counts.items() if count > 1]
    duplicates.sort()
    
    with open(output_path, 'w') as outfile:
        for num in duplicates:
            outfile.write(f"{num}\n")

# paths of my files 
input_directory = 'Input_file'
input_file = 'test_01.txt'
output_directory = 'Output_file'
output_file = 'sample_results.txt'

find_duplicates(input_directory, input_file, output_directory, output_file)
