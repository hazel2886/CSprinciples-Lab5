from flask import Flask, request, redirect, render_template
from selection import CourseSelection

app = Flask(__name__)

courses = CourseSelection(0, 0, 0, 0)

@app.route('/')
def hello_please_select_course(): 
    return 'hello please select course!'

@app.route('/image')
def serve_image():
    return render_template('image.hmtl')

@app.route('/select')
def select():
    return list(courses.subjects.items)
                
@app.route('/reset')
def reset():
    courses.clear()
    return 'the selecting course has been reset!'

@app.route('/question/1', methods = ['GET','POST'])
def first_question():
    answers = ['math', 'history', 'science', 'english']

    if request.method == 'GET':
        return render_template('question_1.html', answers = answers)
    
    if request.method == 'POST': 
        selected = request.form['selected']
        if selected == answers[0]:
            courses.add('math')
        if selected == answers[1]:
            courses.add('history')
        if selected == answers[2]:
            courses.add('science')
        if selected == answers[3]:
            courses.add('english') 

        return redirect('/question/2')
            
@app.route('/question/2', methods = ['GET', 'POST'])
def second_question():
    answers = ['calculus', 'algebra', 'geometry', 'AP world', 'AP US', 'Global', 'Physics', 'Chemistry', 'AP physics', 'AP chemistry']

    if request.method == 'GET':
        return render_template('question_2.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            courses.add('math')
        if selected == answers[3]:
            select_course.add('history')
        if selected == answers[3]:
            select_course.add('sceince')
        if selected == answers[4]:
            select_course.add('english')
                    
        return redirect('/class')
                    
@app.route('/course')
def select_course():
    return 'congrats you are in ' + select_course() + '!'
        
if __name__ == '__main__':
    app.run()