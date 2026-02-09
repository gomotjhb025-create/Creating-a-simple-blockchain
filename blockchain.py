import hashlib  # import hashlib: provides hashing algorithms (e.g. SHA-256); executed at module import time; used to compute block hashes for integrity
import datetime  # import datetime: provides current date/time; executed at module import time; used to timestamp blocks when they're created
import json  # import json: used to convert block data to a canonical string for hashing; executed at import time


class Block:  # define a Block class to represent a single blockchain block; class definition executes at import time
    def __init__(self, blknum, info, prevash):
        # store the block number provided when the Block instance is created; runs whenever a Block is instantiated
        self.blknum = blknum
        # record the creation timestamp as an ISO-like string; evaluated at Block instantiation to capture creation time
        self.timestamp = str(datetime.datetime.now())
        # store the payload/transaction information for this block; set at instantiation
        self.info = info
        # store the hash of the previous block in the chain; provided when adding/creating a block so continuity can be validated
        self.prevash = prevash
        # initialize the nonce / mining work counter; starts at 0 when the block object is created and is incremented during mining
        self.minework = 0
        # compute the initial hash based on the current fields (including minework=0); this runs at instantiation to have a starting hash value
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # create a deterministic JSON string of the block's critical fields; runs whenever we need the canonical representation for hashing
        block_creation_string = json.dumps({
            "blocknumber": self.blknum,
            "timestamp": self.timestamp,
            "info": self.info,
            "prevash": self.prevash,
            "minework": self.minework
        }, sort_keys=True)
        # compute and return the SHA-256 hex digest of the canonical string; this is the block's cryptographic fingerprint used for validation
        return hashlib.sha256(block_creation_string.encode()).hexdigest()

    def mine_the_block(self, difficulty):
        # target is a string of leading zeros of length == difficulty; this defines the mining goal and is evaluated when mining is invoked
        target = "0" * difficulty

        # loop until the block's hash has the required number of leading zeros
        # each iteration updates the nonce (minework) and recalculates the hash; this is the core proof-of-work routine
        while self.hash[:difficulty] != target:
            # increment the nonce so the next hash attempt differs; runs many times during mining
            self.minework += 1
            # recalculate the hash with the updated nonce; runs immediately after incrementing the nonce
            self.hash = self.calculate_hash()

        # when the loop exits the hash meets the difficulty target; print a confirmation message; useful for demonstration and debugging
        print(f"this block has been mined:{self.hash}")


class Blockchain:  # define a Blockchain class to hold the chain and related operations; class defined at import time
    def __init__(self):
        # create the chain list and initialize it with the genesis block; runs when a Blockchain instance is created
        self.chain = [self.create_genesis_block()]
        # set the mining difficulty (number of leading zeros required); configured at initialization and used by add_block
        self.difficulty = 4

    def create_genesis_block(self):
        # return the first block in the chain with a fixed previous-hash value; called during Blockchain initialization
        return Block(0, "Block genesis", "0")

    def get_latest_block(self):
        # return the last block in the chain list; used when linking a new block to the chain; runs when called
        return self.chain[-1]

    def add_block(self, new_block):
        # set the incoming block's previous-hash to the hash of the latest block; ensures the chain links together; runs before mining
        new_block.prevash = self.get_latest_block().hash
        # perform proof-of-work on the new block using the blockchain difficulty; this mutates new_block.minework and new_block.hash
        new_block.mine_the_block(self.difficulty)
        # append the mined block to the chain list; runs after successful mining to include the block in the blockchain
        self.chain.append(new_block)

    def is_chain_valid(self):
        # iterate over the chain (starting at 1 because 0 is genesis) to validate each block's integrity and linkage
        for i in range(1, len(self.chain)):
            # get the current and previous blocks for comparison; executed for every index in the loop
            current = self.chain[i]
            previous = self.chain[i - 1]
            # recompute the current block's hash and compare with stored hash to detect tampering; runs for validation checks
            if current.hash != current.calculate_hash():
                # if hashes differ, the block's content was modified after mining; validation fails
                return False
            # verify the stored prevash matches the previous block's hash to ensure linkage; runs for chain continuity validation
            if current.prevash != previous.hash:
                return False
        # if all checks pass, the chain is valid
        return True


if __name__ == "__main__":
    # create a Blockchain instance when script is executed directly; this block executes only in direct-run mode
    Final_Blockchain = Blockchain()

    # mining and adding block 1: print status then create and add the block; these lines run during the script's main sequence
    print("Mining block 1...")
    Final_Blockchain.add_block(Block(1, {"amount": 100}, ""))

    # mining and adding block 2
    print("Mining block 2...")
    Final_Blockchain.add_block(Block(2, {"amount": 50}, ""))

    # mining and adding block 3
    print("mining block 3...")
    Final_Blockchain.add_block(Block(3, {"amount": 200}, ""))

    # print whether the blockchain is valid after adding blocks; validation runs is_chain_valid() which performs integrity checks
    print("\nBlockchain valid? " + str(Final_Blockchain.is_chain_valid()))

    # iterate over the chain and print block details for inspection; this runs after mining to show stored values
    for block in Final_Blockchain.chain:
        print("\n------------------------------")
        print(f"Block number: {block.blknum}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Info: {block.info}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.prevash}")