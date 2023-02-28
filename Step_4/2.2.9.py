def size_all(size: int):
    if size < 1024:
        return f'{size} {"B"}'
    elif 1024 <= size < 1048576:
        return f'{round(size / 1024)} {"KB"}'
    elif 1048576 <= size < 1073741824:
        return f'{round(size / (1024 * 1024))} {"MB"}'
    elif 1073741824 <= size < 1099511627776:
        return f'{round(size / (1024 * 1024 * 1024))} {"GB"}'


def size_b(size: int, u_i: str) -> int:
    unit_inform = {"B": 1, "KB": 1024, "MB": 1048576, "GB": 1073741824}
    return size * unit_inform[u_i]


if __name__ == '__main__':
    solid_dict = dict()
    with open('files.txt', 'r', encoding='UTF-8') as file:
        for row in file.readlines():
            name = row.split()[0]
            key = row.split()[0].split('.')[1]
            dig = int(row.split()[1])
            iz = row.split()[2].split('/')[0]
            if key in solid_dict:
                solid_dict[key][0].append(name)
                solid_dict[key][1] += size_b(dig, iz)
            else:
                solid_dict[key] = [[name], size_b(dig, iz)]
    solid_dict = dict(sorted(solid_dict.items()))
    for k, v in solid_dict.items():
        # for n in v:
        print(*sorted(v[0]), sep='\n')
        print(f'{"-" * 10}\nSummary: {size_all(v[1])}\n')

