def parse_url(url1, url2):
    # parse two urls to find where integer variable is located.
    # returns a string with integer replaced by {}

    left_str = ''
    right_str = ''
    for a, b in zip(url1, url2):
        if a == b:
            left_str += a
        else:
            break
    for a, b in zip(reversed(url1), reversed(url2)):
        if a == b:
            right_str += a
        else:
            break

    return left_str + '{}' + right_str[::-1]
