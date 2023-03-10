from collections import ChainMap


def get_value(chain_m: ChainMap, key, from_left=True):
    if key in chain_m:
        if not from_left:
            chain_m.maps.reverse()
        return chain_m[key]
    else:
        return None


if __name__ == '__main__':
    chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

    print(get_value(chainmap, 'name', False))
