from bank import bankOper

def test_deposit():
    totalBalance, updatedBalance = bankOper(200000, 30000, 0)
    print("Total balance:", totalBalance)
    print("Updated balance:", updatedBalance)
    assert totalBalance == 230000
    assert updatedBalance == 230000

def test_withdraw():
    totalBalance, updatedBalance = bankOper(100000, 40000, 10000)
    print("Total balance:", totalBalance)
    print("Updated balance:", updatedBalance)
    assert totalBalance == 140000
    assert updatedBalance == 130000