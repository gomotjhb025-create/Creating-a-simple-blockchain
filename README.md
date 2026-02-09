# Creating a Simple Blockchain

This small project is a beginner-friendly implementation of a minimal proof-of-work blockchain in Python. It is intended as a starting point for learning how blockchains work: how blocks are structured, how hashes link blocks together, and how a simple mining loop (proof-of-work) is implemented.

Contents
- `blockchain.py`: Minimal blockchain implementation containing `Block` and `Blockchain` classes. The script creates a genesis block and mines three example blocks when run directly.

What this project demonstrates
- Block structure: each `Block` stores a block number, timestamp, payload (`info`), `prevash` (previous block hash), a `minework` nonce, and a `hash` computed from those fields.
- Hashing: the block's hash is produced with SHA-256 over a canonical JSON representation of the block's fields.
- Proof-of-Work mining: `mine_the_block(difficulty)` increments the nonce and recomputes the hash until the hash has `difficulty` leading zeros.
- Chain validation: `is_chain_valid()` recomputes hashes and checks previous-hash links to detect tampering.

How to run
1. Ensure you have Python 3.8+ installed.
2. From the project folder, run:

```powershell
& C:/Users/gonts/AppData/Local/Python/pythoncore-3.14-64/python.exe .\blockchain.py
```

What you'll see
- The script prints messages while mining each block, the final chain validity check, and block details (number, timestamp, payload, hash, previous hash).

Notes and suggestions for learning
- Difficulty: the `difficulty` value in `Blockchain.__init__` controls how many leading zeros are required. Increasing it will greatly increase mining time — useful for experimenting with how proof-of-work scales.
- Experiment: try tampering with a block's `info` or `minework` and re-run `is_chain_valid()` to see how validation detects changes.
- Extensions: add transactions pool, Merkle tree for transactions, block rewards, or a simple network gossip layer to explore distributed consensus.

License
- This repository is for learning and does not include a license file. Add one if you plan to publish or reuse the code in other projects.

