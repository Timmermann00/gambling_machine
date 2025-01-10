from gambling_machine.game import define_win_multiplier

def test_define_win_multiplier_apple():
    result_list = [["Apple", "Apple", "Apple"], ["Orange", "Apple", "Orange"], ["Orange", "Apple", "Grapefruit"]]
    result = define_win_multiplier(result_list)
    assert result == 2

def test_define_win_multiplier_orange():
    result_list = [["Orange", "Orange", "Orange"], ["Orange", "Apple", "Orange"], ["Orange", "Apple", "Grapefruit"]]
    result = define_win_multiplier(result_list)
    assert result == 3

def test_define_win_multiplier_grapefruit():
    result_list = [["Grapefruit", "Grapefruit", "Grapefruit"], ["Orange", "Apple", "Orange"], ["Orange", "Apple", "Grapefruit"]]
    result = define_win_multiplier(result_list)
    assert result == 5

def test_define_win_multiplier_no_fruit():
    result_list = [["Orange", "Apple", "Grapefruit"], ["Orange", "Apple", "Orange"], ["Orange", "Apple", "Grapefruit"]]
    result = define_win_multiplier(result_list)
    assert result == 0