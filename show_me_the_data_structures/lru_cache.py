class LRU_Cache(object):

    def __init__(self, capacity ):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}
        self.lru = []

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            self.lru.append(key)        
            return(self.cache.get(key))        
        if len(self.cache) >= self.capacity:
            if key == self.least_used():
                return -1

        return -1




    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.       
        if key not in self.cache and self.capacity > len(self.cache):
            self.cache.update({key:value})
            return(f' {key} updated')
        if self.capacity <= len(self.cache):      
            self.cache.popitem()
            return('at capacity')
      
        
        
            

        
    def least_used(self):
        c, least  = len(self.lru), 0
        for x in self.lru:
            if self.lru.count(x) <= c :
                c = self.lru.count(x)
                least = x
        return least

        

        

four_cache = LRU_Cache(5)

print(four_cache.set(1, 1))
print(four_cache.set(2, 2))
print(four_cache.set(3, 3))
print(four_cache.set(4, 4))
print(four_cache.get(1))       # returns 1
print(four_cache.get(2))       # returns 2
print(four_cache.get(9))      # returns -1 because 9 is not present in the cache
print(four_cache.set(5, 5) )
print(four_cache.set(6, 6))

print(four_cache.get(3)) 
# print(four_cache.get(5))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# questions to ask. Does the cache only work on get? 
# my solution returns -1 for 5 cause it was used only for a set just like 3 which is to return -1 