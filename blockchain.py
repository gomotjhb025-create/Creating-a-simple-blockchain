import hashlib
import datetime
import json 

class Block: 
    def __init__(self, blknum, info, prevash):
        self.blknum = blknum 
        self.timestamp = str(datetime.datetimenow())
        self.info = info 
        self.prevash = prevash 
        self.minework = 0 
        self.hash = self.calculate_hash() 

    def calculate_hash(self):
        block_creation_string = json.dumps({"blocknumber": self.blknum,
                                            "timestamp": self.timestamp,
                                            "info": self.info,
                                            "prevash": self.prevash,
                                            "minework": self.minework},sort_keys=True) 
        return hashlib.sha256(block_creation_string.encode()).hexdigest() 
    
    def mine_the_block(self, difficulty):
        target = "0" * difficulty 

        while self.hash[:difficulty] != target: 
            self.minework += 1
            self.hash = self.calculate_hash() 

        print(f"this block has been mined:{self.hash}") 

class Blockchain:
    def __init__(self): 
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4 
    
    def create_genesis_block(self):
        return Block(0, "Block genesis", "0") 
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block): 
        new_block.prevash = self.get_latest_block().hash 
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1,len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1] 
            if current.hash != current.calculate_hash(): 
                return False 
            if current.prevash != previous.hash:
                return False 
        return True 
    
if __name__ == "__main__":
    Final_Blockchain = Blockchain()