from app.model.db import pets
from app.service.sorters import sort_pets


def test_sort_pets():
    unsorted1 = [pets(Name='a'), pets(Name='c'), pets(Name='d'), pets(Name='b')]
    sort_pets(unsorted1)
    assert [p.Name for p in unsorted1] == ['a', 'b', 'c', 'd']

    unsorted2 = [pets(Name='a'), pets(Name='b')]
    sort_pets(unsorted2)
    assert [p.Name for p in unsorted2] == ['a', 'b']

    unsorted3 = []
    sort_pets(unsorted3)
    assert [p.Name for p in unsorted3] == []

    unsorted4 = [pets(Name='a')]
    sort_pets(unsorted4)
    assert [p.Name for p in unsorted4] == ['a']
