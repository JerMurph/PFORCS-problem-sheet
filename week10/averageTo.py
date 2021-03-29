import logging

logging.basicConfig(level=logging.DEBUG)

#This function will calculate and return the average upto and including the index from a list
def averageTo(aList, toIndex):

    sum_num = 0
    avg = -1

    #Check if the index is greater than the list lenght and is greater than zero
    try:
        if (toIndex <= len(aList)) and (toIndex >= 0):
            try:
                for i in range(toIndex):
                    sum_num = sum_num + aList[i]
                avg = sum_num / toIndex
            except ZeroDivisionError: #If the index is zero
                logging.debug("Index is 0")
            except TypeError: #If the index is anything but a number
                logging.debug("List contains a non-numerical value")
        elif toIndex < 0: #If the index is not a positive number
            logging.debug("Index is negative")
        else: #If the index is a number not in the list
            logging.debug("Index out of range")
    except TypeError:
        logging.debug("Index is a non-numerical number.")
    return avg

#Print out a correct version to be sure the function works
print("Average: ", averageTo([1, 2, 3, 4, 5], 2))

#Main function to display the log messages of the possible errors that can occur
if __name__ == '__main__':
    assert averageTo([1, 2, 3, 4, 5], 2) #No issues with this one which means no log message will display for this one 
    assert averageTo([1, 2, 3, 4, 5], 0) #Log will state that the index is zero
    assert averageTo([1, 2, 3, 4, 5], -1) #Log will state that the index is a negative number
    assert averageTo([1, 2, 3, 4, 5], 6) #Log will state the index is out of range
    assert averageTo([1, 2, 3, 4, 5], 'a') #Log will state that the index is not a number
    assert averageTo([1, 2, 3, 'four', 5], 5) #Log will state that a list entry is not a number
