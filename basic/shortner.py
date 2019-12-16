from hashlib import blake2b



class Urlx():
   
    def short(self, num=None):
        id = blake2b(str(num).encode(), digest_size=3).hexdigest()
        return  ''.join(id)

