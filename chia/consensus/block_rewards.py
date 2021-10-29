from chia.util.ints import uint32, uint64
import math

# 1 heather coin = 1,000,000,000,000 = 1 trillion ling.
_mojo_per_chia = 1000000000000
_blocks_per_year = 1681920  # 32 * 6 * 24 * 365
_base_reward = 2199023255552

def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 7/8 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times due to fluctuations in difficulty. They will likely
    come early, if the network space and VDF rates increase continuously.
    We start off at 2,199,023,255,552 which is 2^41 (about 2.2 heather) and half year 2, then half again year 4, then
    half again year 8 etc. after 5 halfings we drop to zero, but don't panic, that's year 64
    right shift >> to half...
    """

    if height == 0:
        return uint64(int((7 / 8) * (_base_reward << 16)))
    elif height < 1 * _blocks_per_year:
        return uint64(int((7 / 8) * _base_reward))
    elif height < 3 * _blocks_per_year:
        return uint64(int((7 / 8) * (_base_reward >> 1)))
    elif height < 7 * _blocks_per_year:
        return uint64(int((7 / 8) * (_base_reward >> 2)))
    elif height < 15 * _blocks_per_year:
        return uint64(int((7 / 8) * (_base_reward >> 3)))
    elif height < 31 * _blocks_per_year:
        return uint64(int((7 / 8) * (_base_reward >> 4)))
    elif height < 63 * _blocks_per_year:
        return uint64(int((7 / 8) * (_base_reward >> 5)))
    else:
        return uint64(0)


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height.
    """

    if height == 0:
        return uint64(int((1 / 8) * (_base_reward << 16)))
    elif height < 1 * _blocks_per_year:
        return uint64(int((1 / 8) * _base_reward))
    elif height < 3 * _blocks_per_year:
        return uint64(int((1 / 8) * (_base_reward >> 1)))
    elif height < 7 * _blocks_per_year:
        return uint64(int((1 / 8) * (_base_reward >> 2)))
    elif height < 15 * _blocks_per_year:
        return uint64(int((1 / 8) * (_base_reward >> 3)))
    elif height < 31 * _blocks_per_year:
        return uint64(int((1 / 8) * (_base_reward >> 4)))
    elif height < 63 * _blocks_per_year:
        return uint64(int((1 / 8) * (_base_reward >> 5)))
    else:
        return uint64(0)
