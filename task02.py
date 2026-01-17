def atm_operation(balance: int, action: str, amount: int) -> int:
    if amount < 0:
        return 'Manfiy summa mumkin emas'

    if action == "deposit":
        return balance + amount

    if action == "withdraw":
        if amount > balance:
            return 'balans yetarli emas'
        return balance - amount


result = atm_operation(100000, 'deposit', 50000)
print(result)
