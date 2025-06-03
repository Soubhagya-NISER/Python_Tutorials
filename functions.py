def fun(message):
    word = message.split()
    print (word)
    o = ''
    emojis = {
        ":)" : "+",
        ":(" : "-"
    }
    for i in word:
        o += emojis.get(i,i)+" "
    return o

m = input(">")
p = fun(m)
print(p)