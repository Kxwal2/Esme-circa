CHARS = "123456789ABCDEFGHJKLMNPQRTUVWXYZ"

def decode_cid(cid: str) -> int:
    """
    Decode integer character id from alphabetical

    Args:
        cid: Alphabetical character id (6 characters)
    """
    if len(cid) != 6:
        return 0

    result = 0
    for i, char in enumerate(cid):
        index = CHARS.find(char)
        if index == -1:
            index = 0

        result += index * (32 ** i)

    return result


def encode_cid(value: int) -> str:
    """
    Encode integer character id into alphabetical.

    Args:
        value: Integer character id
    """
    if not 0 <= value < 32**6:
        raise ValueError("CID value out of range")

    result = ""
    for _ in range(6):
        result += CHARS[value % 32]
        value //= 32

    return result
