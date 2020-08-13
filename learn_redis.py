import redis

class Base(object):
    def __init__(self, host, port=6379, db=0):
        self.r = redis.StrictRedis(host=host, port=port, db=db)

class TestList(Base):

    def test_push(self, *args):
        self.r.lpush('test:lst', *args)
    
    def test_pop(self):
        return self.r.lpop('test:lst')
    

    def query_lst(self):
        return self.r.lrange('test:lst', 0, -1)

class TestSet(Base):

    def test_sadd(self, *args):
        self.r.sadd('test:set', *args)
    
    def test_srem(self, *elements):
        return self.r.srem('test:set', *elements)
    

    def query_set(self):
        return self.r.smembers('test:set')


if __name__ == "__main__":
    test_lst = TestList('192.168.211.45')
    test_set = TestSet('192.168.211.45')
