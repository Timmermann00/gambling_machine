from gambling_machine.game import define_win_multiplier

def test_define_win_multiplier_apple():
    resultList = [["Apple", "Apple", "Apple"], ["Orange", "Apple", "Orange"], ["Orange", "Apple", "Orange"]]
    result = define_win_multiplier(resultList)
    assert result == 2