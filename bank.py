def bankOper(balance, deposit, withdraw):
    totalBalance = balance + deposit
    updatedBalance = totalBalance - withdraw
    return totalBalance, updatedBalance