Name = 'Good day'
Day = 'is a perfect day to learn some python'
Mood = 'thanks for joining the beetroot'

beetroot_index = Mood.find("beetroot")
python_index = Day.find("python")

Day_1 = Day[:2].capitalize() + Day[2:31] + Day[python_index:].upper()
Mood_1 = Mood[:6].title() + Mood[6:beetroot_index] + Mood[beetroot_index:].title()
print(
    Name, end="!\n" +
    Day_1 + ".\n" +
    Mood_1 + "!")