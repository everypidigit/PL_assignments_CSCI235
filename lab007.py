class WrongDate( Exception ) :
    def __init__( self, reason ) :
        self.__reason = reason

def __repr__( self ) :
    return self.__reason


monthnames = ("january",
              "february",
              "march",
              "april",
              "may",
              "june",
              "july",
              "august",
              "september",
              "october",
              "november",
              "december")

monthindex = {
    monthnames[0]: 0,
    monthnames[1]: 1,
    monthnames[2]: 2,
    monthnames[3]: 3,
    monthnames[4]: 4,
    monthnames[5]: 5,
    monthnames[6]: 6,
    monthnames[7]: 7,
    monthnames[8]: 8,
    monthnames[9]: 9,
    monthnames[10]: 10,
    monthnames[11]: 11
}

#a function to briefly test if monthnames and monthindex are behaving correctly
def test_namesandindex() :
    print(monthindex['january'])
    print(monthnames[monthindex['january']])
    print(monthindex['november'])
    print(monthnames[monthindex['february']])
#testing monthnames and monthindex a bit
test_namesandindex() #seems to be working


normalyear = (31,
              28,
              31,
              30,
              31,
              30,
              31,
              31,
              30,
              31,
              30,
              31,)

leapyear = (31,
            29,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31,)

#a function to briefly test if normalyear and leapyear are behaving correctly
def test_normalandleapyear():
    print(leapyear[1])
    print(normalyear[11])
    print(leapyear[7])
    print(normalyear[3])
#testing normalyear and leapyear a bit
test_normalandleapyear() #seems to be working


#defining a function to test a year's leapness (if that's a word(this word is being highlighted so it's not a real word
#but I hope it is understandable))
def isleapyear(y) :
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            elif y % 400 != 0:
                return False
        elif y % 100 != 0 :
            return True
    elif y % 4 != 0 :
        return False
#a function to find out if isleapyear is behaving correctly
def test_leapness():
    print(isleapyear(1904))
    print(isleapyear(1917))
    print(isleapyear(1873))
    print(isleapyear(2005))
    print(isleapyear(1905))
    print(isleapyear(2237))
    print(isleapyear(2984))
    print(isleapyear(1900))
    print(isleapyear(2100))
    print(isleapyear(1600))
    print(isleapyear(2000))
    print(isleapyear(2400))
    print(isleapyear(2200))
    print(isleapyear(2300))
    print(isleapyear(2500))
    print(isleapyear(2600))
    print(isleapyear(1936))
    print(isleapyear(2237))
    print(isleapyear(2108))
    print(isleapyear(2109))
    print(isleapyear(3098))
    print(isleapyear(1672))
    print(isleapyear(1890))
    print(isleapyear(930))
    print(isleapyear(1333))
#testing out isleapyear a bit
test_leapness() #seems to be working


def checkdate( year, month, day) :
    if type(year) is int and year >= 1900 :

        if type(month) is str and month in monthnames:

            if type(day) is int and day > 0:

                if isleapyear(year) == 1:

                    if day <= leapyear[monthindex[month]]:
                        return [year, month, day]
                    elif day > leapyear[monthindex[month]]:
                        raise WrongDate("month %s does not have %d in year %d" %(month, day, year))
                elif isleapyear(year) == 0:
                    if day <= normalyear[monthindex[month]]:
                        return [year, month, day]
                    elif day > normalyear[monthindex[month]]:
                        raise WrongDate("month %s does not have %d in year %d" %(month, day, year))

            elif type(day) is not int:
                raise WrongDate("Day %s is not an integer" %(day))
            elif day < 0:
                raise WrongDate("Day %d cannot be less than 0" %(day))

        elif type(month) is int and month (0,12):

            raise WrongDate("Month %d is not a valid month because it's not in range 0-12"%(month))

        elif type(month) is str and month not in monthnames:
            raise WrongDate("Month %s is not a month in monthnames" %(month))
    elif type(year) is not int :
        raise WrongDate("Year %s is not an integer" %(year))
    elif year < 1900 :
        raise WrongDate('Year %d is before 1900' %(year))
#a function to check if checkdate is working
def test_checkdate():
    print(checkdate(1935, "december", "B"))
    print(checkdate( 'dani' ,"january", 13))
    print(checkdate(1900, "februa", 29))
    print(checkdate( 1878 ,"january", 29))
    print(checkdate( 1938 ,"february", 29))
    print(checkdate( 1900 ,"february", 29))
    print(checkdate( 1936 ,"february", 29))

#testing a bit
test_checkdate() #seems to be working except the raise WrongDate component


#I did not have enough time to complete below functions

#def weekday(year, month, day) :
 #   try:
  #      year, month, day = checkdate(year, month, day)
   # except WrongDate as w:
    #    print(" date error: {}".format(w))
    #return "???"


#unlucky(year)











