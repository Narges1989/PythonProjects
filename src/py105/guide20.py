from typing import Any

from to_do import TODO


def guide20(hard_drive: dict[str, dict[str, Any]]) -> str:
    Min_File_size = 100000
    for key,file_spec in hard_drive.items():
        if file_spec['size'] < Min_File_size:
            Min_File_size = file_spec['size']
            result = file_spec['extension']
    return result