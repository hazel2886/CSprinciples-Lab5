from flask import Flask, request, redirect, render_template
from selection import CourseSelection

app = Flask(__name__)

courses = CourseSelection(0, 0, 0, 0)

@app.route('/')
def hello_please_select_course(): 
    return 'Congrats! You have made it to High School. Please create a schedule for school. (Remeber that each course you choose is assoiated with a different subject. As well as having a certain amount of points assosiated with it. No going back once you have chosen the courses in which you will take for the next year.) Choose wisely. Good Luck.!'

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
    answers = ['calculus', 'AP physics', 'AP World', 'AP Lit']

    if request.method == 'GET':
        return render_template('question_2.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            courses.add('math')
        if selected == answers[1]:
            courses.add('history')
        if selected == answers[2]:
            courses.add('sceince')
        if selected == answers[3]:
            courses.add('english')
                    
        return redirect('/question/3')
    

@app.route('/question/3', methods = ['GET', 'POST'])
def third_question():
    answers = ['AP Psycology', 'AP Computer Science', 'St. John\'s Math', 'Creative Writing']

    if request.method == 'GET':
        return render_template('question_3.html', answers = answers)
    
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
        
        return redirect('/question/4')
    
@app.route('/question/4', methods = ['GET', 'POST'])
def fourth_question():
    answers = ['Model UN', 'forensics', 'robotics', 'Journalism']

    if request.method == 'GET':
        return render_template('question_4.html', answers = answers)
    
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
        
        return redirect('/question/5')
    
@app.route('/question/5', methods = ['GET', 'POST'])
def fifth_question():
    answers = ['boxing', 'CPR training class', 'football', 'soccer']

    if request.method == 'GET':
        return render_template('question_5.html', answers = answers)

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
        
        return redirect('/result')
    
@app.route('/result')
def result():
    return 'Based on the coures you have selected your main course will be.... ' + courses.sort() + '!'
        
if __name__ == '__main__':
    app.run()