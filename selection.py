class CourseSelection:
    def __init__(self, english: int, history: int, math: int, science: int):
        self.courses = {
            'english': english,
            'history': history,
            'math': math,
            'science': science
        }

    def add(self, course: str) -> None:
        if course == 'english':
            self.courses['english'] = self.courses.get('AP lit, English, Brit lit') + 3
        if course == 'hsitory':
            self.courses['history'] = self.courses.get('AP world, US history') + 2
        if course == 'englsih':
            self.courses['math'] = self.courses.get('pre calc, Ap calc, geometry, algegra') + 4
        if course == 'science': 
            self.courses['science'] = self.courses.get('physics, chemistry') + 2

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
