from typing import Any, Dict, cast

from requests import Session, Response
from config import BASE_URL, AUTH_TOKEN


def _url_join(*args: str) -> str:
    return "/".join((a.strip("/") for a in args))


preview_url = _url_join(BASE_URL, "api", "v1", "system", "capture")
header = {"Authorization": "Bearer " + AUTH_TOKEN}  # type: ignore


class CriblAPIClient:
    def __init__(self) -> None:
        self.preview_url = _url_join(preview_url)

        self._session = Session()
        self._session.headers.update(header)

    @staticmethod
    def _parse_response_data(response: Response) -> Dict[str, Any]:
        response.raise_for_status()
        return cast(Dict[str, Any], response.json())

    def post_preview(self, post_data: Dict[str, Any]) -> Dict[str, Any]:
        return self._parse_response_data(
            self._session.post(self.preview_url, json=post_data, stream=True, timeout=None)
        )
