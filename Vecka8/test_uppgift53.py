from uppgift53 import prime_factors


def test_factor_36():
    assert prime_factors(36) == [2, 2, 3, 3]


def test_factor_10001():
    assert prime_factors(10001) == [73, 137]


def test_factor_779351():
    assert prime_factors(779351) == [779351]


def test_factor_1024():
    assert prime_factors(1024) == [2] * 10
