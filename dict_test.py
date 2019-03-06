# 브랜드 별로 핫한 아이템 묶어 놓기

# dict 정의
brand_to_hot_item_dict = {
'Nike': ['regista', 'magician', 'new_air'],
'Apple': ['macbookair13', 'macbookpro17'],
}

del(brand_to_hot_item_dict['Nike'])
nike_list = brand_to_hot_item_dict.get('Nike', "No Nike in the base.")
apple_list = brand_to_hot_item_dict['Apple']

print(nike_list, apple_list)
