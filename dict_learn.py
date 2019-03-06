#나이키 품종
nike_dict = {
'나이키':
{
'베놈': {'265': 12, '260' : 2, '220': 3},
'레지스타': {'265': 12, '260' : 2, '220': 3},
}
}
target_brand = input("which brand to search in this storage")
if not 브랜드_나이키_품종_재고_사전.__contains__(target_brand):
    print("다른 창고 조회해보세요.")
print(브랜드_나이키_품종_재고_사전['나이키']['베놈'].__delitem__('220'))
print(브랜드_나이키_품종_재고_사전)

#
딕션 = {'a': [1,2], 'b': [2,3], 'c': [3,4],  'd': [4,5]}
딕션_2 = {'a': [1,2], 'b': [2,3],}
#print(브랜드_나이키_품종_재고_사전.__getitem__('나이키'))
#for i in 브랜드_나이키_품종_재고_사전:
#    print(i)

#딕션_이터_오브젝트 = 딕션.__iter__()
#print(next(딕션_이터_오브젝트))
#print(next(딕션_이터_오브젝트))

#dict_length =딕션.__len__()
#print(dict_length)

#print(딕션.get('e', 'donna \'e\''))

#print(type(딕션.items())) #dict_items 객체

# 1. 그 키 값이 없었다면 그 키와 해당 값을 딕셔너리에 어싸인 하라 /
# 2. 만약 있다면 딕셔너리.get(k, d) k의 값을 반환하라

딕션.setdefault('e', [7,8])
print(딕션)
print(딕션.get('e'))

딕션_3 = {'a': [8,9], 'd': [10,11]}
딕션_3.update(딕션_2)
print(딕션_3)
