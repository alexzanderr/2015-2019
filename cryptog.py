
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ?!@#$%^&*()-=_+,./\|[]{}`~;:\'\"<>"
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '?', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', ',', '.', '/', '\\', '|', '[', ']', '{', '}', '`', '~', ';', ':', "'", '"', '<', '>']

""" 
    ====================================================================================================================
    we dont need this anymore:
    
    def CreatingTheList(string):
        list = []
        for char in string:
            list.append(char)
        return list
    
    all = CreatingTheList(chars)
    
    but we keep it here
    ====================================================================================================================
    Essential information:
    
    print("=" * limit)
    print("Essential information:")
    print("Interval for cryptation is from 0 -> {0}.".format(len(all) - 1))
    print("Interval for a-z is from {0} -> {1}.".format(all.index('a'), all.index('z')))
    print("Interval for A-Z is from {0} -> {1}.".format(all.index('A'), all.index('Z')))
    print("Interval for digits is from {0} -> {1}.".format(all.index('0'), all.index('9')))
    print("Interval for the rest of all chars is from {0} -> {1}.".format(all.index('?'), all.index('>')))
    print("=" * limit)
    ====================================================================================================================

"""


def crypt(param):

    """
        This :param can be either a string, either a list with a crypted string.
        Also has :return.
    """

    if str(type(param)) == "<class 'list'>":
        # if the list transfered as paramter contains characters will crash the program
        # the list must contains digits to be decoded
        for iter in param:
            if type(iter) == chr:
                print("Wrong data type in list, cant decrypt characters...")
                raise TypeError

        decrypted = str()
        for number in param:
            decrypted += list[number]
        return decrypted

    elif str(type(param)) == "<class 'str'>":
        crypted = []
        for char in param:
            crypted.append(list.index(char))
        return crypted

    else:
        print("You can't use params that have different type than string or list.")
        raise TypeError


def CryptMessage(string):
    """ Returns a list with crypted version of the message. """

    crypted = []
    for char in string:
        crypted.append(list.index(char))
    return crypted

def DecryptMesage(numbers):
    """ Returns a list with decrypted version of the message. """

    # if the list transfered as paramter contains characters will crash the program
    # the list must contains digits to be decoded
    for iter in numbers:
        if type(iter) == chr:
            print("Wrong data type in list, cant decrypt characters...")
            raise TypeError

    decrypted = str()
    for number in numbers:
        decrypted += list[number]
    return decrypted



