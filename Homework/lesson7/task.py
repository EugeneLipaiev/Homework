import random

words = [
    'Abuse', 'Adult', 'Agent', 'Anger', 'Apple', 'Award', 'Basis', 'Beach', 'Birth', 'Block', 'Blood', 'Board', 'Brain',
    'Bread', 'Break', 'Brown', 'Buyer', 'Cause', 'Chain', 'Chair', 'Chest', 'Chief', 'Child', 'China', 'Claim', 'Class',
    'Clock', 'Coach', 'Coast', 'Court', 'Cover', 'Cream', 'Crime', 'Cross', 'Crowd', 'Crown', 'Cycle', 'Dance', 'Death',
    'Depth', 'Doubt', 'Draft', 'Drama', 'Dream', 'Dress', 'Drink', 'Drive', 'Earth', 'Enemy', 'Entry', 'Error', 'Event',
    'Faith', 'Fault', 'Field', 'Fight', 'Final', 'Floor', 'Focus', 'Force', 'Frame', 'Frank', 'Front', 'Fruit', 'Glass',
    'Grant', 'Grass', 'Green', 'Group', 'Guide', 'Heart', 'Henry', 'Horse', 'Hotel', 'House', 'Image', 'Index', 'Input',
    'Issue', 'Japan', 'Jones', 'Judge', 'Knife', 'Laura', 'Layer', 'Level', 'Lewis', 'Light', 'Limit', 'Lunch', 'Major',
    'March', 'Match', 'Metal', 'Model', 'Money', 'Month', 'Motor', 'Mouth', 'Music', 'Night', 'Noise', 'North', 'Novel',
    'Nurse', 'Offer', 'Order', 'Other', 'Owner', 'Panel', 'Paper', 'Party', 'Peace', 'Peter', 'Phase', 'Phone', 'Piece',
    'Pilot', 'Pitch', 'Place', 'Plane', 'Plant', 'Plate', 'Point', 'Pound', 'Power', 'Press', 'Price', 'Pride', 'Prize',
    'Proof', 'Queen', 'Radio', 'Range', 'Ratio', 'Reply', 'Right', 'River', 'Round', 'Route', 'Rugby', 'Scale', 'Scene',
    'Scope', 'Score', 'Sense', 'Shape', 'Share', 'Sheep', 'Sheet', 'Shift', 'Shirt', 'Shock', 'Sight', 'Simon', 'Skill',
    'Sleep', 'Smile', 'Smith', 'Smoke', 'Sound', 'South', 'Space', 'Speed', 'Spite', 'Sport', 'Squad', 'Staff', 'Stage',
    'Start', 'State', 'Steam', 'Steel', 'Stock', 'Stone', 'Store', 'Study', 'Stuff', 'Style', 'Sugar', 'Table', 'Taste',
    'Terry', 'Theme', 'Thing', 'Title', 'Total', 'Touch', 'Tower', 'Track', 'Trade', 'Train', 'Trend', 'Trial', 'Trust',
    'Truth', 'Uncle', 'Union', 'Unity', 'Value', 'Video', 'Visit', 'Voice', 'Waste', 'Watch', 'Water', 'While', 'White',
    'Whole', 'Woman', 'World', 'Youth',
]
computer = random.choice(words)
computer = list(computer.lower())

user = list(input("Type your word "))

for i in range(len(user)):
    if computer[i] == user[i]:
        user[i] = "!"
    elif user[i] in computer:
        user[i] = "?"
    else:
        user[i] = "."

result = "".join(user)





"""
Комп'ютер загадує слово зі списку words і пропонує користувачеві відгатати його за шість спроб.

Користувач вводе слово, а комп'ютер "відповідає" на нього таким чином:
- яккщо літера не зістрічається в загаданому слові, на її місці комп'ютер ставить крапку (.);
- якщо літера зустрічається, але на іншому місці - знак питання (?);
- якщо литера є і знаходиться на правильній позиції - знак оклику (!).

Приклад. Загадане слово - "Agent". Користувач вводить "Angel", відповідь комп'ютера повинна бути:
<<< !???.  # 1 літера - вірно; 2,3,4 - є такі, але на інших позиціяї; 5 літера в слові відсутня

Якщо користувач не відгадав слово за 6 спроб - програма завершується і коп'ютер виводить загадане слово.

!!! Зверніть увагу, що літери в словах можуть повторюватись:
Якщо користувач вводить "focus", то для загаданого "Class" потрібно вивести "..?.!" - остання літера вірна


-------------------- Додатково --------------------
1. Зробити гру регістронезалежною (не важливо, маленькі чи великі літери вводяться).
2. Зробити валідацію того, що вводить користувач: лише 5 літер латінецею
   (якщо користувач ввів щось невірне - ця спроба не рахується і комп'ютер лише пропонує ввести ще раз).
3. Ввести в гру підрахунок балів - на свій розсуд. Врахуйте, чи вгадана літера, чи на правильному місці, з якої спроби,
                                                                                                                   тощо.
"""