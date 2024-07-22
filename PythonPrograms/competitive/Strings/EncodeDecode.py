class EnDecoder:

    def encode(self, data: []) -> str:
        counter = 0
        mergedString = ""
        breakpoints = ""
        for string in data:
            mergedString += string;
            counter += len(string)
            breakpoints += ',' + str(counter)

        return mergedString + '#' + breakpoints

    def decode(self, data: str):
        beginIndex = 0
        endindex = 0
        result = []
        fullstring, breakpoints = data.split("#")
        for i in str(breakpoints).split(","):
            if i != "":
                endindex = int(i)
                temp = str(fullstring)[beginIndex:endindex]
                beginIndex = endindex
                result.append(temp)
        return result


data = ["list", "lint", "love", "you"]

encoder = EnDecoder()
encoded = encoder.encode(data)
print(encoded)
decoded = encoder.decode(encoded)
print(decoded)
print(encoded, decoded, end='\n')
