from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

# mac_dict = ChainMap(bread, meat, sauce, vegetables, toppings)
# st = input().split(',')
# total = 0
# for i in st:
#     total += mac_dict[i]
# ln = len(str(total)) + 7
# lens = len(max(st, key=len))
# for k, v in Counter(sorted(st)).items():
#     print(f'{k}{(lens - len(k)) * " "} x {v}')
#     if ln < len(f'{k}{(lens - len(k)) * " "} x {v}'):
#         ln = len(f'{k}{(lens - len(k)) * " "} x {v}')
# print(f'{ln * "-"}')
# print(f'ИТОГ: {total}р')

st = 'булочка с кунжутом,обычная булочка,ржаная булочка,куриный бифштекс,говяжий бифштекс,рыбный бифштекс,сливочно-чесночный,кетчуп,горчица,барбекю,чили,лук,салат,помидор,огурцы,сыр,яйцо,бекон,булочка с кунжутом,обычная булочка,ржаная булочка,куриный бифштекс,говяжий бифштекс,рыбный бифштекс,сливочно-чесночный,кетчуп,горчица,барбекю,чили,лук,салат,помидор,огурцы,сыр,яйцо,бекон,булочка с кунжутом,обычная булочка,ржаная булочка,куриный бифштекс,говяжий бифштекс,рыбный бифштекс,сливочно-чесночный,кетчуп,горчица,барбекю,чили,лук,салат,помидор,огурцы,сыр,яйцо,бекон,булочка с кунжутом,обычная булочка,ржаная булочка,куриный бифштекс,говяжий бифштекс,рыбный бифштекс,сливочно-чесночный,кетчуп,горчица,барбекю,чили,лук,салат,помидор,огурцы,сыр,яйцо,бекон,булочка с кунжутом,обычная булочка,ржаная булочка,куриный бифштекс,говяжий бифштекс,рыбный бифштекс,сливочно-чесночный,кетчуп,горчица,барбекю,чили,лук,салат,помидор,огурцы,сыр,яйцо,бекон,булочка с кунжутом,обычная булочка,ржаная булочка,куриный бифштекс,говяжий бифштекс,рыбный бифштекс,сливочно-чесночный,кетчуп,горчица,барбекю,чили,лук,салат,помидор,огурцы,сыр,яйцо,бекон,булочка с кунжутом,обычная булочка,ржаная булочка,куриный бифштекс,говяжий бифштекс,рыбный бифштекс,сливочно-чесночный,кетчуп,горчица,барбекю,чили,лук,салат,помидор,огурцы,сыр,яйцо,бекон,булочка с кунжутом,обычная булочка,ржаная булочка,куриный бифштекс,говяжий бифштекс,рыбный бифштекс,сливочно-чесночный,кетчуп,горчица,барбекю,чили,лук,салат,помидор,огурцы,сыр,яйцо,бекон,булочка с кунжутом,обычная булочка,ржаная булочка,куриный бифштекс,говяжий бифштекс,рыбный бифштекс,сливочно-чесночный,кетчуп,горчица,барбекю,чили,лук,салат,помидор,огурцы,сыр,яйцо,бекон,булочка с кунжутом,обычная булочка,ржаная булочка,куриный бифштекс,говяжий бифштекс,рыбный бифштекс,сливочно-чесночный,кетчуп,горчица,барбекю,чили,лук,салат,помидор,огурцы,сыр,яйцо,бекон'

ings = ChainMap(bread, meat, sauce, vegetables, toppings)
# c = Counter(input().split(','))
c = Counter(st.split(','))
lines = [f'{i.ljust(len(max(c, key=len)))} x {j}' for i, j in sorted(c.items())]
total = f'ИТОГ: {sum(ings[i] * j for i, j in c.items())}р'

print(*lines, '-' * len(max(lines + [total], key=len)), total, sep='\n')