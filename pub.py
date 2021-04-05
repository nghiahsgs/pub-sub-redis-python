import redis
import time
r = redis.Redis(host='127.0.0.1',port = 6379)
dem = 0
while True:
  p = r.publish(channel ='channel3',message="nghiahsgs%s"%dem)
  dem+=1
  time.sleep(1)
