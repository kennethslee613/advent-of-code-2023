def part_one():
    with open('./input.txt') as f:
        lines_list = f.read().split('\n')
        criteria = {
            'red': 12,
            'green': 13,
            'blue': 14
        }
        game_id_sum = 0

        for line in lines_list:
            colon_index = line.index(':')
            game_id = int(line[:colon_index].split(' ')[1])

            sets_in_text = line[colon_index + 2:].split('; ')

            is_draw_set_valid = True
            for draw_set in sets_in_text:
                for marbles in draw_set.split(', '):
                    [quantity, color] = marbles.split(' ')
                    if criteria[color] < int(quantity):
                        is_draw_set_valid = False
                        break
            
            if is_draw_set_valid:
                game_id_sum += game_id

        print('part 1:', game_id_sum)

def part_two():
    with open('./input.txt') as f:
        lines_list = f.read().split('\n')
        power_sum = 0

        for line in lines_list:
            criteria = {
                'red': 0,
                'green': 0,
                'blue': 0
            }

            colon_index = line.index(':')
            sets_in_text = line[colon_index + 2:].split('; ')

            for draw_set in sets_in_text:
                for marbles in draw_set.split(', '):
                    [quantity, color] = marbles.split(' ')
                    if criteria[color] < int(quantity):
                        criteria[color] = int(quantity)
            
            power_sum += criteria['red'] * criteria['green'] * criteria['blue']

        print('part 2:', power_sum)

part_one()
part_two()
