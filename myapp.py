def sentence_maker(phrase):
    introgatives = ("how", "who", "why")
    capitilized=phrase.capitalize()
    if phrase.startswith(introgatives):
        return "{}? ".format(capitilized)
    else:
        return "{}.".format(capitilized)
result=[]
while True:
   inputfield=input("say something:")
   if inputfield =="\end":
     break;
   else:
       (result.append(sentence_maker(inputfield)))
print(",".join(result))



