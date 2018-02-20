# This file is the demo for a simple blockchain
# Author: Dr. Wei Yuan
# Time: 2018-02-20
# Email: weiy1991@{163.com, sjtu.edu.cn}
# Site: Shanghai Jiao Tong University

import hashlib as hasher

class Block:
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()
	

	def hash_block(self):
		sha = hasher.sha256()
		sha.update((str(self.index) + 
				str(self.timestamp) + 
				str(self.data) +
				str(self.previous_hash)).encode('utf-8'))
		return sha.hexdigest()


import datetime as date

def create_genesis_block():
	return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
	this_index = last_block.index + 1
	this_timestamp = date.datetime.now()
	this_data = "Hey! I'm block" + str(this_index)
	this_hash = last_block.hash
	return Block(this_index, this_timestamp, this_data, this_hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(num_of_blocks_to_add):
	block_to_add = next_block(previous_block)
	blockchain.append(block_to_add)
	previous_block = block_to_add

	print("Block %d has been add to the blockchain!", block_to_add.index)
	print("Hash: {}".format(block_to_add.hash))










