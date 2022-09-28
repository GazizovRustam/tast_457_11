def main():
    strInput = 'i o i '.split()
    getMaxLetter(strInput)

def getMaxLetter(strInput):
    index = 1
    top = 0
    n_ch = ''

    for n in range(index, len(strInput)):
        if strInput[n] == strInput[index]:
            n_ch = strInput[n]

            top = top + 1

            index = index + 1
    print(n_ch, top)
    # for n in range(len(strInput)):
    #
    #     if strInput[n]

if __name__ == "__main__":
    main()