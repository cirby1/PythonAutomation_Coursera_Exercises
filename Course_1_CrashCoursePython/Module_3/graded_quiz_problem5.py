def counter(start, stop):
    if start > stop:
        return_string = "Counting Down: "
        while start >= stop:
            return_string = return_string + str(start) 
            if start > stop:
                return_string += ","
            start = start - 1
    else:
        return_string = "Counting up: "
        while stop >= start: 
            return_string = return_string + str(start) 
            if start < stop:
                return_string += ","
            start = start + 1
    return return_string

print(counter(1, 10))
