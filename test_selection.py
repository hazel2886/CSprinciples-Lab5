from selection import CourseSelection

def test_selection():
    courses = CourseSelection(0, 0, 0, 0)
    courses.add('history')
    courses.add('science')
    courses.add('math')
    courses.add('history')

    assert courses.sort() == 'history'

def test_english_selection():
    courses =CourseSelection(0, 0, 0, 0)
    courses.add('english')
    courses.add('science')
    courses.add('math')
    courses.add('english')

    assert courses.sort() == 'english'