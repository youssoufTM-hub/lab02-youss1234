# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Just replace each `pass` with your code, using `return` to send the answer
# back (not `print`).


def seconds_to_hms(total_seconds):
    # TODO (Part 1): return the time as a string "H:MM:SS"
    #   e.g. seconds_to_hms(3661) should return "1:01:01"
    hour = total_seconds // 3600
    min = (total_seconds %3600)//60
    sec = (total_seconds%3600) % 60
    
    return f'{hour}:{min:02}:{sec:02}'


def admission_price(age):
    # TODO (Part 2): return the ticket price (a number) for someone of this age
    
    ticket_price = 0.00
    if (age <5):
        return 0.00

    elif (age >= 5 and age < 13):
        return 8.00
    
    elif (age >= 13 and age < 65):
        return 15.00
    
    else:
        return 10.00
    
    

def sum_multiples(limit):
    # TODO (Part 3): return the sum of every whole number below `limit`
    #   that is a multiple of 3 or of 5
    #Loops through every value thats less than the limit and if they are devisible by 5 or 3 they they get added to a total
    sum: int = 0
    for i in range(limit-1, 0, -1):
        if (i % 5 == 0):
            sum += i

        elif (i % 3 == 0):
            sum += i
    return sum


def total_of_positives(numbers):
    # TODO (Part 4 - STRETCH, optional): return the sum of just the
    #   positive numbers in the list `numbers`
    #Loops through all the values and if they are higher than zero they get added to the total
    total:int = 0
    for n in numbers:
        if n > 0:
            total += n
    return total



def main():
    # Optional scratch space - use this to try your functions with sample values.
    # Uncomment a line and run `python lab02.py` to see the result.
    print(seconds_to_hms(7325))            # 1:01:01
    print(admission_price(10))             # 8
    print(sum_multiples(10))               # 23
    print(total_of_positives([1, -2, 3]))  # 4
    pass


if __name__ == "__main__":
    main()
