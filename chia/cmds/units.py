from typing import Dict

# The rest of the codebase uses ling everywhere.
# Only use these units for user facing interfaces.
units: Dict[str, int] = {
    "heather": 10 ** 12,  # 1 heather (HEATHER) is 1,000,000,000,000 ling (1 trillion)
    "ling:": 1,
    "colouredcoin": 10 ** 3,  # 1 coloured coin is 1000 colouredcoin ling
}
