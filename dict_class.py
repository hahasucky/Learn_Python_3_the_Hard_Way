my_Dict = {'a': 'seokhee', 'b': "byunghyun",
"c": "messi" }

his_Dict = {'a': 'seokhee',"c": "messi" ,'b': "byunghyun"}
his_Dict.__delitem__('a')
output = his_Dict.pop('a', 'no a??')
print(output)
