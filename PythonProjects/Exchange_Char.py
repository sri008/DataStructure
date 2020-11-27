exchange={'G':'C','C':'G','T':'A','A':'U'}
b=input()
for k,v in exchange.items():
    if k==b:
        print(v,"")
        break
    else:
        continue