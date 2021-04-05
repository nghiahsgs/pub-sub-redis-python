#from multiprocessing import Process
import redis
r = redis.Redis(host='127.0.0.1',port = 6379,charset='utf-8',decode_responses=True)
#def sub():
p = r.pubsub()
p.subscribe("channel3")
#p.subscribe("channel2")
#print(p.get_message())
#'''
for message in p.listen():
        print(message)
#'''
#sub()
#Process(target=sub, args=()).start()
#print("end")
