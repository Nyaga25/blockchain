import datetime
from hashlib import sha256
from operator import le


class Block:
    def __init__(self) -> None:
        self.index = 0
        self.timestamp = datetime.datetime.now().strftime("%x")
        self.data = ""
        self.previous_hash = ""
        self.hash = ""


class Blockchain:
    def __init__(self) -> None:
        self.block_array = []

    def add_block(self, block: Block):
        if len(self.block_array) == 0:
            block.index = 1
            block.previous_hash = ""
            block.hash = self.calculate_hash(block)
            self.block_array.append(block)
        else:
            previous_block = self.block_array[len(self.block_array) - 1]
            block.index = previous_block.index + 1
            block.previous_hash = previous_block.hash
            block.hash = self.calculate_hash(block)
            self.block_array.append(block)

    def calculate_hash(self, block: Block):
        block_data = (
            str(block.index) + str(block.timestamp) + block.data + block.previous_hash
        )
        return sha256(block_data.encode("ascii")).hexdigest()

    def print_blocks(self):
        for block in self.block_array:
            print("Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous hash:", block.previous_hash)
            print("Hash:", block.hash)
            print("")

    def verify(self):
        blockchain_ok = True
        for i in range(len(self.block_array)):
            if self.block_array[i].index == 1:
                self.block_array[i].hash = self.calculate_hash(self.block_array[i])
                continue
            else:
                self.block_array[i].hash = self.calculate_hash((self.block_array[i]))
                if self.block_array[i].previous_hash == self.block_array[i - 1].hash:
                    continue
                else:
                    blockchain_ok = False
                    break
        return blockchain_ok


block1 = Block()
block1.data = "some transaction"

block2 = Block()
block2.data = "cash transaction"

block3 = Block()
block3.data = "nazbits"

blockchain = Blockchain()
blockchain.add_block(block1)
blockchain.add_block(block2)
blockchain.add_block(block3)

blockchain.block_array[0].data = ""
# change some data in a block
blockchain.print_blocks()
print(blockchain.verify())
