from urllib.parse import urljoin

import responses

from tgtg import ALL_BUSINESS_ENDPOINT, BASE_URL, TgtgClient


@responses.activate
def test_get_items_success():
    data = [
        {
            "id": "88",
            "created_by": "88",
            "category_id": "1",
            "latitude": "55.65004170",
            "longitude": "12.20162040",
            "business_name": "Asia House - Hedehusene",
            "todays_stock": "6",
            "is_open": "1",
            "img_path": "https://images.tgtg.ninja/user/1468224399_GT8Gn0MCoH_scale.jpg",
            "pickup_day_offset": "0",
            "current_window_pickup_start_utc": "2019-09-22 19:20:00",
            "current_window_pickup_end_utc": "2019-09-22 19:25:00",
        }
    ]
    responses.add(
        responses.GET,
        urljoin(BASE_URL, ALL_BUSINESS_ENDPOINT),
        json={"info": data, "msg": "OK", "status_code": 1},
        status=200,
    )
    client = TgtgClient()
    client.get_all_business()
    assert client.get_all_business() == data
