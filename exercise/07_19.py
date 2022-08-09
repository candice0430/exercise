'''
第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
'''
from base64 import encode
import hashlib
import hmac
from hashlib import sha256
import os

from numpy import isin

def encrype_pwd(password,salt=None):
    if not salt:
        salt = os.urandom(8)
    print('salt:',salt)
    assert len(salt) == 8
    assert isinstance(salt,bytes)
    assert isinstance(password,str)

    result = password
    for _ in range(10):
        result = hmac.HMAC(password.encode(),salt,sha256).digest()
    return salt+result

def check_pwd(pwd,res):
    pwd1 = encrype_pwd(pwd,res[:8])
    if res == pwd1:
        print('密码正确')
    else:
        print('密码错误')

# res = encrype_pwd('Aa123456.')
res = encrype_pwd('Aa123456.')
print(res)
check_pwd('Aa123456.',res)
check_pwd('aa123456.',res)


def md5_pwd(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    print(md5.hexdigest())
    print(len(md5.hexdigest()))

def sha1_pwd(pwd):
    s = hashlib.sha1()
    s.update(pwd.encode('utf-8'))
    print(s.hexdigest())
    print(len(s.hexdigest()))

def hmac_pwd(key,pwd):
    mac = hmac.new(key,pwd.encode('utf-8'),hashlib.md5)
    mac.digest()
    print(mac.hexdigest())


# md5_pwd('Aa123456.')
# sha1_pwd('Aa123456.')
# hmac_pwd(b'hello','Aa123456.')