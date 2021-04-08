import ast

endProgram = 0;

# Function returns flattened JSON object
def flatten_json(jsonObject):

    flatJObject = {}

    # Flattens if key-value pair is nested
    def flatten(x, key = ''):
        if type(x) is dict:
            for c in x:
                flatten(x[c], key + c + '.')

        else:
            flatJObject[key[:-1]] = x

    flatten(jsonObject)

    return flatJObject



if __name__ == '__main__':
    # Accepts JSON Object input from command line
    while endProgram == 0:
        jsonInput = str(input("Enter JSON Object (or Enter 'Quit' to exit program): "))
        if jsonInput == 'Quit':
            endProgram = 1
            exit(-1)
        jsonInput = ast.literal_eval(jsonInput)
        print(flatten_json(jsonInput))


