def remove_char(str, n):
    firs_part = str[:n]
    last_part = str[n+1:]
    return firs_part + last_part


print(remove_char("bangladesh", 2))