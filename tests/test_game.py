from gambling_machine.game import define_win_multiplier

def test_define_win_multiplier_apple():
    resultList = [["Apple", "Apple", "Apple"], ["Orange", "Apple", "Orange"], ["Orange", "Apple", "Grapefruit"]]
    result = define_win_multiplier(resultList)
    assert result == 2

def test_define_win_multiplier_orange():
    resultList = [["Orange", "Orange", "Orange"], ["Orange", "Apple", "Orange"], ["Orange", "Apple", "Grapefruit"]]
    result = define_win_multiplier(resultList)
    assert result == 3

def test_define_win_multiplier_grapefruit():
    resultList = [["Grapefruit", "Grapefruit", "Grapefruit"], ["Orange", "Apple", "Orange"], ["Orange", "Apple", "Grapefruit"]]
    result = define_win_multiplier(resultList)
    assert result == 5

def test_define_win_multiplier_no_fruit():
    resultList = [["Orange", "Apple", "Grapefruit"], ["Orange", "Apple", "Orange"], ["Orange", "Apple", "Grapefruit"]]
    result = define_win_multiplier(resultList)
    assert result == 0