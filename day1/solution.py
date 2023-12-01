import math

def part_one():
    with open('./input.txt') as f:
        lines_list = f.read().split('\n')
        summation = 0

        for line in lines_list:
            numbers_list = []
            for character in line:
                if character.isdigit():
                    numbers_list.append(character)
            
            calibration_value = int(numbers_list[0] + numbers_list[-1])
            summation += calibration_value
        
        print('part 1:', summation)

def part_two():
    with open('./input.txt') as f:
        lines_list = f.read().split('\n')
        number_dict = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
        }
        summation = 0

        for line in lines_list:
            numbers_list = []

            # Add the first written out number we find
            min_first_replace_index = math.inf
            first_number_to_replace = ''

            for key in number_dict.keys():
                first_replace_index = line.find(key)
                if first_replace_index != -1 and first_replace_index < min_first_replace_index:
                    min_first_replace_index = first_replace_index
                    first_number_to_replace = key

            if first_number_to_replace != '':
                # Splicing instead of replacing in case the letters from the first written out number is also used
                # in the last written out number
                line = line[:min_first_replace_index] + number_dict[first_number_to_replace] + line[min_first_replace_index:]

            # Add the last written out number we find
            max_last_replace_index = -1
            last_number_to_replace = ''

            for key in number_dict.keys():
                last_replace_index = line.rfind(key)
                if last_replace_index != -1 and last_replace_index > max_last_replace_index:
                    max_last_replace_index = last_replace_index
                    last_number_to_replace = key
            
            if last_number_to_replace != '':
                line = line[:max_last_replace_index] + number_dict[last_number_to_replace] + line[max_last_replace_index:]

            # Same process as part 1
            for character in line:
                if character.isdigit():
                    numbers_list.append(character)
            
            calibration_value = int(numbers_list[0] + numbers_list[-1])
            summation += calibration_value
        
        print('part 2:', summation)

part_one()
part_two()
