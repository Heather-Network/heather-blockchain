from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "heather_harvester heather_timelord_launcher heather_timelord heather_farmer heather_full_node heather_wallet".split(),
    "node": "heather_full_node".split(),
    "harvester": "heather_harvester".split(),
    "farmer": "heather_harvester heather_farmer heather_full_node heather_wallet".split(),
    "farmer-no-wallet": "heather_harvester heather_farmer heather_full_node".split(),
    "farmer-only": "heather_farmer".split(),
    "timelord": "heather_timelord_launcher heather_timelord heather_full_node".split(),
    "timelord-only": "heather_timelord".split(),
    "timelord-launcher-only": "heather_timelord_launcher".split(),
    "wallet": "heather_wallet heather_full_node".split(),
    "wallet-only": "heather_wallet".split(),
    "introducer": "heather_introducer".split(),
    "simulator": "heather_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
