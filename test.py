import math
import pprint

myspreadsheet = """Subject,Height,Occupation
1,74.37000326528938,Psychologist
2,67.49686206937491,Psychologist
3,74.92356434760966,Psychologist
4,64.62372198999978,Psychologist
5,67.76787900026083,Linguist
6,61.50397707923559,Psychologist
7,62.73680961908566,Psychologist
8,68.60803984763902,Linguist
9,70.16090500135535,Psychologist
10,76.81144438287173,Linguist"""

def csv_parser(s):
    """Parses the string s into lines, and then parses those lines by
    splitting on the comma and converting the numerical data to int.
    The output is a list of lists of subject data."""
    data = []
    lines = s.splitlines()
    lines = lines[1: ]
    for line in lines:
        l = line.strip().split(",")
        l[0] = int(l[0])
        l[1] = float(l[1])
        data.append(l)
    return data

    #data.pop[i]
    #file2 = s.split()
    #lines = []
    #lines.append(file2)
    #lines.pop[0]
    #print(lines)
    #for line in lines:
        

    # Data is our output. It will be a list of lists.

    # Split csv into lines and store them in a list called 'lines'.
    
    # Remove the first element from lines, so that you have only the data lines left.
    
    # At this stage, we loop through the list called lines.
    # As you loop
    #     i. split each line on the commas;
    #    ii. convert the Subject variable to int.
    #   iii. convert the Height variable to float.
    #    iv. add to data a list consisting of this line's Subject, Height, and Occupation values 

def csv_parser_test():
    """Display the output of csv_parser(myspreadsheet) and
    test it a little bit."""
    data = csv_parser(myspreadsheet)
    print('Your data object:')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)      
    # Did your parser work?
    for row_num, row in enumerate(data):
        try:
            assert len(row) == 3
        except AssertionError:
            print (("Row %s seems to be misparsed; its length is %s") % (row_num, len(row)))
    # Check on one of the values:
    try:
        assert data[4][2] == 'Linguist'
    except AssertionError:
        print (("Error: data[4][2] should equal 'Linguist'; actual value is %s") % data[4][2])
    # Did you remember your int conversions?
    try:
        assert isinstance(data[0][0], int)
    except AssertionError:
        print ("Error: data[0][0] should be an int")
    # Did you remember your float conversions?
    try:
        assert isinstance(data[6][1], float)
    except AssertionError:
        print ("Error: data[6][1] should be a float")
        
def mean_height(data):
    """Return the mean numerical value of column 1 in an list of lists.
    data is the output of csv_parser(myspreadsheet)"""
    

    
if __name__ == '__main__':
    print(csv_parser_test())
