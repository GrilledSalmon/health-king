from app import user_collection
from bcrypt import hashpw, gensalt


id_list = ['연어', '곰', '호랑이', '두꺼비', '학', '고양이', '강아지', '용']
password_list = ['1234', '1234', '1234', '1234', '1234', '1234', '1234', '1234']

name_list = id_list
for id, password, name in zip(id_list, password_list, name_list):
    if user_collection.find_one({'id' : id}): # 중복 검사
        continue
    hashed_pw = hashpw(password.encode(), gensalt())    
    doc = {'id' : id, 'password' : hashed_pw, 'name' : name, 'activity' : []}
    user_collection.insert_one(doc)
