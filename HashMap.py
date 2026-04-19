import enum
class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for i in range(capacity)]
    
    def __len__(self):
        return self.size
    
    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return True
        return False

    def put(self, key, value):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
        self.size += 1
        

    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError("Key not found!")

    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError("Key not found!")

    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    def bucket(self):
        return [bucket for bucket in self.buckets]

    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0

        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity
        return hash_result

maps = HashMap(3)
maps.put("name", "Ugochukwu Chidera")
maps.put("name2","Ugochukwu Adaeze")
maps.put("name3", "Ugochukwu Chiziterem")
maps.put("name4", "Ugochukwu Onyeonoro")
maps.put("final_name", "Ogechukwu Onyeonoro")

print(maps.__len__(), maps.__contains__("name4"))
maps.remove("name2")
print(maps.get("name"))
print(maps.__len__(), maps.__contains__("name4"))
print(maps.keys(), maps.values(), maps.items(), maps.bucket())
