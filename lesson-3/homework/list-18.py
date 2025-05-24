def issublist(mainlist,  sublist):
    main_str = ','.join(map(str,mainlist))
    sub_str = ','.join(map(str, sublist))
    return sub_str in main_str

given_list = ['s', 'a', 'n', 'k', 'u', 't', 'm']
sublist = ['n', 'k', 'u']

print(issublist(given_list, sublist))
