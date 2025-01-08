def parse_rules():
    R = int(input())
    rules = {}
    for _ in range(R):
        s1, _, s2, _, s3 = input().split()
        if (s1, s2) not in rules:
            rules[(s1, s2)] = s3
    return rules

def parse_test_case():
    C = int(input())
    tokens = []
    for _ in range(C):
        token_certs = {}
        while True:
            pair = input().split()
            if pair[0] == "END":
                break
            k, cer = pair[0], float(pair[1])
            token_certs[k] = cer
        tokens.append(token_certs)
    return tokens

def combine_tokens(tokens, rules):
    while len(tokens) > 1:
        new_tokens = []
        for i in range(len(tokens) - 1):
            s1, s2 = list(tokens[i].keys())[0], list(tokens[i + 1].keys())[0]
            if (s1, s2) in rules or (s2, s1) in rules:
                if (s1, s2) in rules:
                    new_cer = tokens[i][s1] * tokens[i + 1][s2]
                else:
                    new_cer = tokens[i][s2] * tokens[i + 1][s1]
                new_tokens.append({rules[(s1, s2)]: new_cer})
            else:
                return "GAMEOVER"
        tokens = new_tokens
    return list(tokens[0].keys())[0]

def main():
    rules = parse_rules()
    T = int(input())
    for _ in range(T):
        tokens = parse_test_case()
        result = combine_tokens(tokens, rules)
        print(result)

if __name__ == "__main__":
    main()
# Generator time: 51.0822 seconds