# 第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
from time import sleep, time
import redis

# r = redis.StrictRedis('127.0.0.1',port=6379,db=0)
# print(r)
# # r.set('name','wushuang')
# print(r.get('name'))
codes = ['dddda','assss','sass','dddda']
# r.set('codes',codes)
# print(r.get('codes'))

pool = redis.ConnectionPool(host='127.0.0.1',port=6379,decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('age',2,ex=1,nx=True)
print(r.get('age'))
# sleep(2)
# r.set('age',200,ex=1,nx=True)
# print(r.get('age'))
# print(r.set('age',30,xx=True))
# print(r.get('age'))
print(r.setnx("fruit","fruit..."))
print(r.setnx("fruit","fruit..."))
for code in codes:
    r.sadd('codes',code)
print(r.scard('codes'))
print(r.smembers('codes'))

for c in codes:
    r.lpush("name1",c)
# print(r.smembers("name1"))
print(r.lrange("name1",0,-1))
