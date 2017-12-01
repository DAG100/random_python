class IntWithBase:
    """A class for representing whole numbers of a specifc base.
    Uses alphabets to represent numbers greater than 9, e.g. 10 = A, 11 = B, etc.
    The input class is a string because letters can't be in integers/floats."""

    def __init__(self, strvalue, base):
        self.pureval = strvalue
        self.base = int()
        self.faceValue = str()
        self.decimalvalue = int()
        validchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        letter_values = dict()

        class IntWithBaseException(Exception):
            """An exception about the base."""

        class CharException(Exception):
            """An exception concerning the value of the number."""

        for letter in range(0, len(validchars)-10):
            letter_values[letter + 10] = validchars[letter]

        try:
            int(base)

            for Letter in str(strvalue):
                print(Letter)
                if validchars.find(Letter) == -1:
                    raise CharException
                elif int(Letter) >= base:
                    raise CharException
                elif

            if int(base) > 37 or int(base) < 2:
                raise BaseException

        except ValueError:
            print("The value of base is invalid. Please enter a value between 2 and 36 for the base.")
        except CharException:
            print("The value of the number is invalid. Please enter the number in the format 'numberLETTER', where the\
 letter is capitalised. Also, any value within the base cannot be larger than the base.")
        except IntWithBaseException:
            print("The value of base is beyond the valid parameters. Please enter a value between 2 and 36.")
        else:
            self.base = base
            self.faceValue = str(strvalue)

        del validchars

        for i in range(0, len(str(self.faceValue))):
            val = 0
            found = "no"
            j = len(self.faceValue) - (i + 1)
            digit = self.faceValue[i]
            for value, letter in letter_values.items():
                if value == digit:
                    val = value*(base**j)
                    found = "yes"
                    break
            if found != "yes":
                val = int(self.faceValue[i])*(base**j)

            self.decimalvalue += val

    def printfields(self):
        print("base is {}. face value is {}. decimal value is {}. original value is {}.".format(self.base, self.faceValue, self.decimalvalue, self.pureval))


my_num = IntWithBase("2", 2)

my_num.printfields()
