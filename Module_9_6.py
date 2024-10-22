def all_variants(text):
    for i in range(len(text)):
        for v in range(i, len(text)):
            yield text[i:v + 1]


a = all_variants("abc")
for i in a:
    print(i)