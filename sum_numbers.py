# This program sums a list of numbers
def sum_list(inp_list):
    """
    This function sums up a list of numbers
    """
    total = 0
    for item in inp_list:
        total = total + item
    return total

if __name__=='__main__':
   print(f"The sum of the list={sum_list([2,5,8,25,40,36])}")


