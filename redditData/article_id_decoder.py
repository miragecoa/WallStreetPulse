def base36encode(integer: int) -> str:
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    sign = '-' if integer < 0 else ''
    integer = abs(integer)
    result = ''
    while integer > 0:
        integer, remainder = divmod(integer, 36)
        result = chars[remainder] + result
    return sign + result


def base36decode(base36: str) -> int:
    return int(base36, 36)


def get_next_ids(start_id, count):
    start_num = base36decode(start_id)
    ids = []
    id_num = -1
    for id_num in range(start_num, start_num + count):
        ids.append(base36encode(id_num))
    return ids, base36encode(id_num)


def get_prev_ids(start_id, count):
    start_num = base36decode(start_id)
    ids = []
    id_num = -1
    for id_num in range(start_num - 1, start_num - count - 1, -1):
        ids.append(base36encode(id_num))
    return ids, base36encode(id_num)




