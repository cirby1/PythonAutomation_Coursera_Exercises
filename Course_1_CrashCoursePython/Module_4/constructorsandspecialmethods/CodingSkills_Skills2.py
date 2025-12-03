def record_profit_years(recent_first, recent_last):
    recent_first.reverse()
    recent_last.extend(recent_first)
    return recent_last

recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989, 1992, 1997, 2001]

print(record_profit_years(recent_first, recent_last))
