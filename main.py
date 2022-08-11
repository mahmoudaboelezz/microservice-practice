from mylib.logic import wiki


print(wiki('Ahmed Zewail'))
if 'Ahmed Hassan Zewail' in wiki('Ahmed Zewail'):
    print('Yes')