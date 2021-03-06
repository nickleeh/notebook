def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "{:3.2f} {}{}".format(num, unit, suffix)
        num /= 1024.0
    return "{:.2f} {}{}".format(num, 'Yi', suffix)
