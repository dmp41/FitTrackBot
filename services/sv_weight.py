from datetime import datetime


async def calculate_weight(new_weight):
    new_weight = int(new_weight)
    old_weight = 100
    last_weight = 90
    target = 70
    today = datetime.now().date()

    last_change = last_weight - new_weight
    all_change = old_weight - new_weight
    target_change = new_weight - target

    return {'today': today, 'new_w': new_weight, 'target': target, 'last_change': last_change,
            'all_change': all_change, 'target_change': target_change}