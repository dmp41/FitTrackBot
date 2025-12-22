from datetime import datetime


async def calculate_calories(user_dict):
    BMR = 0
    k = 0
    birth_date = datetime.strptime(user_dict['birthday'], "%Y.%m.%d").date()
    today = datetime.now().date()

    user_dict['age'] = today.year - birth_date.year

    if user_dict['gender'] == '👨 Мужской':

        BMR = 10 * user_dict['weight'] + 6.25 * user_dict['height'] - user_dict['age'] + 5

    if user_dict['gender'] == '👩 Женский':

        BMR = 10 * user_dict['weight'] + 6.25 * user_dict['height'] - user_dict['age'] - 161

    if user_dict['activity'] == '🛋️  Сидячий образ жизни':
        k = 1.2

    if user_dict['activity'] == '🚶‍♂ Легкая активность':
        k = 1.375

    if user_dict['activity'] == '🏋️‍♂ Средняя активность':
        k = 1.55

    if user_dict['activity'] == '💪 Высокая активность':
        k = 1.725

    if user_dict['activity'] == '🦸‍♂ Очень высокая активность':
        k = 1.9

    TDEE = BMR * k

    MASS = TDEE + 450

    return {'one': BMR,'two':TDEE,'three':MASS}

