

def filter_func(s: str) -> bool:
    return "BEAR" in s or "X-RAY" in s


with open("system.log") as f_in:
    with open("filtered.log", 'w') as f_out:
        f_out.writelines(filter(filter_func, f_in))
