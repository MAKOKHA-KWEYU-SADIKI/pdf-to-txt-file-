with open("text.txt","r") as f:
    content=f.read()
    word=content.split()
  #  print(word,len(word))
  #  t=set[word]
    t=set(word)
    l=[]
    for n in t :
        if n==n:
            l.append(n)
    print(len(l),"repeated words")

    print(len(word),"word in this file")
f.close()