set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {7, 8, 9, 10, 11}


#1
res = set_a.union(set_b, set_c)
print(res)


#2
res_a_b = set_a.difference(set_b)
res_b_c = set_b.difference(set_c)
res_a_c = set_a.difference(set_c)

# print(res_a_b)
# print(res_b_c)
# print(res_a_c)


#3
# res_a_b = set_a.union(set_b)
# res_b_c = set_b.union(set_c)
# res_c_a = set_c.union(set_a)
# print(res_a_b)


#4
if {1, 2} & set_a:
    print("True")
else:
    print("False")


if {1, 2} & set_b:
    print("True")
else:
    print("False")


if {1, 2} & set_c:
    print("True")
else:
    print("False")


#5
res_1 = {x for x in res if x % 2 == 0}
res_2 = {x for x in res if not x % 2 == 0}
print(res_1)
print(res_2)


####
dict_a = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    'key_4': 'value_4',
    'key_5': 'value_5'
}

dict_b = {
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8',
    'key_9': 'value_9',
    'key_10': 'value_10'
}

dict_c = {
    'key_4': 'value_4',
    'key_5': 'value_5',
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8'
}


#1
res = {**dict_a, **dict_b}
print(res)


#2
keys_d_a = dict_a.keys()
value_d_b = dict_b.values()
res = dict(zip(keys_d_a,value_d_b))
print(res)


#3
res = dict(zip(value_d_b,keys_d_a))
print(res)


#4
res = {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3', 'key_4': 'value_4', 'key_5': 'value_5', 'key_6': 'value_6' , 'key_7': 'value_7', 'key_8': 'value_8', 'key_9': 'value_9', 'key_10': 'value_10'}

res_1 = {}
for key,val in res.items():
    number = int(key.split("_")[-1])
    if number % 2 != 0:
        res_1[key] = val
print(res_1)


#5
set_a = set(dict_a.items())
set_b = set(dict_b.items())
set_c = set(dict_c.items())
res = {
    'dict_a': len(set_a & set_c),
    'dict_b': len(set_b & set_c)
}
print(f'res = {res}')
