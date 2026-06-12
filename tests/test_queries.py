from unittest.mock import MagicMock
from queries import shortest_path, top_hub, two_hop_neighbour

def test_shortest_path_returns_length():
    mock_driver = MagicMock()
    mock_driver.execute_query.return_value = (
        [{"result": 3}],
        None,
        None
    )
    result = shortest_path(mock_driver, "PER", "SYD")
    assert result == 3

def test_top_hub_returns_ranked_pairs():
    mock_driver = MagicMock()
    fake_records = [
        {"Airport": "Perth", "Connections": 42},
        {"Airport": "Sydney", "Connections": 38},
    ]
    mock_driver.execute_query.return_value = (
        fake_records,
        None,
        None
    )
    result = top_hub(mock_driver)
    assert result == [("Perth", 42), ("Sydney", 38)]

def test_two_hop_neighbours():
    mock_driver = MagicMock()
    fake_records = [
        {"Reachable": "Sydney"},
        {"Reachable": "Melbourne"}
    ]
    mock_driver.execute_query.return_value = (
        fake_records,
        None,
        None
    )
    result = two_hop_neighbour(mock_driver, "PER")
    assert result == ["Sydney", "Melbourne"]