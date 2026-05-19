LIMIT = 1000

capacityofjuga = 0
capacityofjugb = 0


# Function to display current status
def displaystatus(step, a, b):

    print(f"{step:<10}{a:<10}{b:<10}")


# Function to find minimum value
def findminimum(value1, value2):

    return min(value1, value2)


# Main AI Logic
def findsolution(required):

    a = 0
    b = 0
    step = 0

    print("\n")
    print(f"{'Operation':<20}{'Step#':<10}{'Jug A':<10}{'Jug B':<10}")
    print("-" * 50)

    while a != required and step < LIMIT:

        step += 1

        # If Jug A empty -> Fill it
        if a == 0:

            a = capacityofjuga

            print(f"{'Fill Jug A':<20}", end="")
            displaystatus(step, a, b)

        # If Jug B full -> Empty it
        elif b == capacityofjugb:

            b = 0

            print(f"{'Empty Jug B':<20}", end="")
            displaystatus(step, a, b)

        # Pour water from A to B
        else:

            temp = findminimum(capacityofjugb - b, a)

            b = b + temp
            a = a - temp

            print(f"{'Pour A into B':<20}", end="")
            displaystatus(step, a, b)

    # Return result
    if step == LIMIT:

        return False, step

    else:

        return True, step


# Main Program
if __name__ == "__main__":

    capacityofjuga = int(input("Capacity of Jug A: "))
    capacityofjugb = int(input("Capacity of Jug B: "))
    required = int(input("Required water in Jug A: "))

    # Error checking
    if capacityofjuga < required:

        print("\nError! Required water cannot fit in Jug A.")

    elif (capacityofjuga == capacityofjugb) and (capacityofjuga != required):

        print("\nError! Invalid input values.")

    else:

        success, steps = findsolution(required)

        if success:

            print(f"\nSolution found in {steps} steps.")

        else:

            print(f"\nSolution not found even after {steps} steps.")