from typing import Dict, List

from pydj.di.internal.register_info import RegisterInfo

beans_groups: Dict[str, List[RegisterInfo]] = {}

def get_collected_group(group: str) -> List[RegisterInfo]:
    return beans_groups.get(group, [])
