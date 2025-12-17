
from src.sorting import bubble_sort, quick_sort

def test_sort():
    data = [{"Score":90},{"Score":70}]
    assert bubble_sort(data,"Score")[0]["Score"] == 70
    assert quick_sort(data,"Score")[0]["Score"] == 70
