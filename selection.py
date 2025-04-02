class CourseSelection:
    def __init__(self, english: int, history: int, math: int, science: int):
        self.courses = {
            'english': english,
            'history': history,
            'math': math,
            'science': science,
        }

    def add(self, course: str) -> None:
        if course == 'english':
            self.courses['english'] = self.courses.get('english') + 1
        if course == 'history':
            self.courses['history'] = self.courses.get('history') + 1
        if course == 'math':
            self.courses['math'] = self.courses.get('math') + 1
        if course == 'science': 
            self.courses['science'] = self.courses.get('science') + 1

    def sort(self) -> str:
        score = 0 
        result = ''
        for course, points in self.courses.items():
            if points > score:
                result = course
                score = points

        return result

    def clear(self) -> None:    
        self.courses = {
            'english': 0,
            'history': 0, 
            'math': 0,
            'science': 0,
        }
