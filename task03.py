def calculate_tax(salary: int) -> dict:
    if salary <= 5_000_000:
        tax = 0
        rate = '0%'
    elif salary <= 10_000_000:
        tax = (salary - 5_000_000) * 12 // 100
        rate = '12%'
    elif salary <= 20_000_000:
        tax = (salary - 10_000_000) * 18 // 100
        rate = '18%'
    else:
        tax = (salary - 20_000_000) * 25 // 100
        rate = '25%'

    net = salary - tax

    return {
        'gross': salary,
        'tax': tax,
        'net': net,
        'rate': rate
    }


print(calculate_tax(8_000_000))