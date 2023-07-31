# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.


text = 'Князь Князь Князь Князь Князь Князь Князь Князь Василий сдержал обещание и помог сыну Друбецкой — Борису. Его перевели в гвардии семеновский полк.' \
       'Вскоре Анна прибыла к своим богатым родственникам Ростовым, воспитывавшим ее Бориса. Он пока оставался в Москве для обмундирования.' \
       'У Ростовых были именинницы — две Натальи — мать и дочь. С утра в дом приезжали гости,' \
       'все обсуждали неподобающее поведение сына старого князя Безухова. Даже в Москве узнали,' \
       'что Пьер с Долоховым достали где-то медведя, посадили в карету и повезли по актрисам. Далее подоспела полиция,' \
       'а они поймали квартального, привязали его спина к спине с медведем и пустили в Мойку.' \
       'Также обсуждали те обстоятельства, что у Безухова законных детей нет, а незаконных — человек двадцать.' \
       'Пьер из них любимый, потому Безухов писал государю о Пьере. Наследником состояния графа должен стать либо ближайший' \
       'родственник — князь Курагин, либо сын Пьер.' \
       'Ростовы производят приятное впечатление: графиня Ростова, красивая женщина восточного типа, ласково и учтиво принимала гостей.' \
       'Ее добродушный и веселый муж хлопотал, чтобы прием в честь именин был роскошным. В доме царит радушие.'

for_replace = "+-—.,;:!?,'""—"

for i in for_replace:
    text = text.replace(i, "")
text = text.lower().split(" ")

result = {}

for i in text:
    result[i] = result.setdefault(i, 0) + 1
print(result)

words = sorted(result.items(), key=lambda v: v[1], reverse=True)
print("Десятка самых частых встречаемых слов: ", end='')

for i in range(10):
    print(f"{words[i][0]}, " if i < 9 else f"{words[i][0]}.", end='')