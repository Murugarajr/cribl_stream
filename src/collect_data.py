"""
This script will read Cribl API client and get the response for POST request ('/system/capture-Capture live
incoming data) data and do necessary filtering, transformation(TO DO)

Author: Raj Rengaraj
Version: 0.1
Date: 14/10/2022
"""

import json
from typing import Any, Dict
from clients import CriblAPIClient

POST_DICT = {
    "filter": "",
    "level": 0,
    "maxEvents": 1,
    "stepDuration": 0,
    "workerId": "80d87a74-9042-4a9e-a634-f552df2cd475",
    "workerThreshold": 0,
}

cribl_client = CriblAPIClient()


def build_preview_data(post_data: Dict[str, Any]) -> Any:
    raw_data = json.dumps(cribl_client.post_preview(post_data))
    return json.loads(raw_data)


if __name__ == "__main__":
    preview_data = build_preview_data(post_data=POST_DICT)
    print(preview_data)
