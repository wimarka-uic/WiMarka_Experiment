def splitSpecialCharacters(text):
    return (
        text.replace('"', ' " ')
        .replace(",", " , ")
        .replace(".", " . ")
        .replace("!", " ! ")
        .replace("?", " ? ")
        .replace(";", " ; ")
        .replace(":", " : ")
        .replace("(", " ( ")
        .replace(")", " ) ")
        .strip()
    )


def printFindings(tokenList, tokenLenghts):
    print(f"Tokens: {len(tokenList)}")
    print(f"Unique Tokens: {len(set(tokenList))}")
    print(f"Max Tokens: {max(tokenLenghts)}")
    print(f"Min Tokens: {min(tokenLenghts)}")
    print(f"Avg Tokens: {sum(tokenLenghts) / len(tokenLenghts)}\n")


def getTokens(EXP):

# for source texts

    E1_PATHS = [
        "Simple_Declarative",
        "Simple_Interrogative",
        "Simple_Imperative",
        "Simple_Exclamatory",
        "Compound_Declarative",
        "Compound_Interrogative",
        "Compound_Imperative",
        "Compound_Exclamatory",
        "Complex_Declarative",
        "Complex_Interrogative",
        "Complex_Imperative",
        "Complex_Exclamatory",
        "Complex_Compound_Declarative",
        "Complex_Compound_Interrogative",
        "Complex_Compound_Imperative",
        "Complex_Compound_Exclamatory",
    ]

    E2_PATHS = ["BIK", "CEB", "HIL", "ILO", "PAM", "PAG", "TGL", "WAR"]

    E1_TOKENS = []
    E1_LENGTHS = []
    E2_TOKENS = []
    E2_LENGHTS = []

    if EXP == 0:

        for path in E1_PATHS:

            CAT_TOKENS = []
            CAT_LENGTHS = []

            file_path = f"Experiment_1/{path}/EN.txt"
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    line = splitSpecialCharacters(line)
                    tokens = line.strip().split()
                    E1_LENGTHS.append(len(tokens))
                    CAT_LENGTHS.append(len(tokens))
                    
                    for token in tokens:
                        E1_TOKENS.append(token)
                        CAT_TOKENS.append(token)

                print(f"{path}")
                printFindings(CAT_TOKENS, CAT_LENGTHS)

        print("Experiment 1 Findings:")
        printFindings(E1_TOKENS, E1_LENGTHS)

    if EXP == 1:

        for path in E2_PATHS:

            CAT_TOKENS = []
            CAT_LENGTHS = []

            for j in range(1, 4):

                SUB_TOKENS = []
                SUB_LENGTHS = []

                file_path = f"Experiment_2/{path}/{path}{j}.txt"
                with open(file_path, "r", encoding="utf-8") as file:
                    for line in file:

                        line = splitSpecialCharacters(line)
                        tokens = line.strip().split()
                        E1_LENGTHS.append(len(tokens))
                        CAT_LENGTHS.append(len(tokens))
                        SUB_LENGTHS.append(len(tokens))
                        
                        for token in tokens:
        
                            E2_TOKENS.append(token)
                            CAT_TOKENS.append(token)
                            SUB_TOKENS.append(token)

                    print(f"{path} - {j}")
                    printFindings(SUB_TOKENS, SUB_LENGTHS)

                    if j == 3:
                        break

            print(f"{path}")
            printFindings(CAT_TOKENS, CAT_LENGTHS)

        print("Experiment 2 Findings:")
        printFindings(E2_TOKENS, E1_LENGTHS)


getTokens(0)
