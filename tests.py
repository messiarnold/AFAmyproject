import subprocess

# task_progress menu for the progress bar, add your tasks here
task_progress = {
    'task_1': 0,
    'task_2': 0,
    'task_2.1':0,
    'task_2.2':0,
    'task_2.3':0,
    'task_2.4':0,
    'task_12': 0,  
    'task_13': 0,  
}


# a function that checks for input and empty code
def check_for_input_and_empty_code(code,task):
    if code == '':
        feedback = 'אתה צריך להכניס קוד'
        task_progress[task] = 0
        return feedback
    if 'input(' in code:
        feedback = 'התוכנית לא אמורה לקחת קלט'
        task_progress[task] = 0
    else:
        feedback = ''
    return feedback


# functions that evaluate all the tasks:
def evaluate_task_1(code):
    feedback = check_for_input_and_empty_code(code,'task_1')
    if feedback != '':
        return feedback
    else:
        try:
            result = subprocess.run(['python','-c',code],text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if result.returncode == 0:
                output = result.stdout.strip()
                if 'hello world' in output.lower():
                    task_progress['task_1'] = 100
                    feedback = "!הצלחת במשימה" 
            else:
                feedback = 'למסך hello world לא הודפס'
                task_progress['task_1'] = 0
        except SyntaxError:
            feedback = 'טעית בכתיבה של הקוד'
            task_progress['task_1'] = 0
        except Exception as e:
            feedback = f"Error: {str(e)}\n{print(e)}"           
    return feedback

def evaluate_task_2(code):
    feedback = check_for_input_and_empty_code(code,'task_2')
    if feedback != '':
        return feedback
    else:
        try:
            result = subprocess.run(['python','-c',code],text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if result.returncode == 0:
                output = result.stdout.strip()
                if '41' in output:
                    feedback = 'הצלחת במשימה'
                    task_progress['task_2'] = 100
                else:
                    feedback = 'לא הצלחת אולי החישוב לא נכון'
                    task_progress['task_2'] = 0                    
        except SyntaxError:
            feedback = 'יש לך טעות בכתיבה של הקוד'
            task_progress['task_2'] = 0
        except Exception as e:
            feedback = f"Error: {str(e)}\n{print(e)}"           
    return feedback

def evaluate_task_2_1(code):
    feedback = ''
    if code == '':
        feedback = 'לא הכנסת קוד'
        return feedback
    else:
        try:
            user_input = "admin"  
            result = subprocess.run(['python', '-c', code], input=user_input, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                output = result.stdout.strip().lower()
                if 'welcome' in output and 'admin' in output:
                    feedback = '!הצלחת במשימה'
                    task_progress['task_2.1'] = 100
            else:
                feedback = 'לא הודפסה הודעת ברוכים הבאים'
                task_progress['task_2.1'] = 0
        except SyntaxError:
            feedback = 'יש לך טעות בכתיבה של הקוד'
            task_progress['task_2.1'] = 0
        except Exception as e:
            task_progress['task_2.1'] = 0
            feedback = f"Error: {str(e)}\n{e}"
    return feedback
       
def evaluate_task_2_2(code):
    feedback = ''
    if code == '':
        feedback = 'לא הכנסת קוד'
        return feedback
    else:
        try:
            user_input = "123456789" 
            result = subprocess.run(['python', '-c', code], input=user_input, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                output = result.stdout.strip().lower()
                print(output)
                if '1234567891' in output:
                    feedback = '!הצלחת במשימה'
                    task_progress['task_2.2'] = 100
            else:
                feedback = 'לא הודפסה תעודת הזהות בתוספת הספרה 1'
                task_progress['task_2.2'] = 0
        except SyntaxError:
            feedback = 'יש לך טעות בכתיבה של הקוד'
            task_progress['task_2.2'] = 0
        except Exception as e:
            task_progress['task_2.2'] = 0
            feedback = f"Error: {str(e)}\n{e}"
    return feedback

def evaluate_task_2_3(code):
    feedback = ''
    if code == '':
        feedback = 'לא הכנסת קוד'
        task_progress['task_2.3'] = 0
        return feedback
    if 'input(' in code and 'int(' not in code:
        feedback = 'כנראה ששכחת להמיר למספר את הקלט'
        task_progress['task_2.3'] = 0
    else:
        try:
            user_input = "249" 
            result = subprocess.run(['python', '-c', code], input=user_input, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                output = result.stdout.strip()
                if '5' in output:
                    feedback = '!הצלחת במשימה'
                    task_progress['task_2.3'] = 100
            else:
                feedback = 'לא הודפס הממוצע'
                task_progress['task_2.3'] = 0
        except SyntaxError:
            feedback = 'יש לך טעות בכתיבה של הקוד'
            task_progress['task_2.3'] = 0
        except Exception as e:
            task_progress['task_2.3'] = 0
            feedback = f"Error: {str(e)}\n{e}"
    return feedback

def evaluate_task_2_4(code):
    feedback = check_for_input_and_empty_code(code,'task_2.4')
    if feedback != '':
        return feedback
    else:
        result = subprocess.run(['python', '-c', code], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            output = result.stdout.strip()
            if '0' in output and '1' in output and '2' in output and '3' in output and '5' in output and '8' in output and '6765' in output:
                feedback = 'הצלחת במשימה'
                task_progress['task_2.4'] = 100
            elif '0' in output and '1' in output:
                feedback = 'לא כל המספרים הודפסו'
                task_progress['task_2.4'] = 100
            else:
                feedback = 'לא הודפסו עשרים המספרים הראשונים בסדרת פיבונאצי'
                task_progress['task_2.4'] = 0
        else:
            feedback = 'שגיאה בעת הרצת הקוד'
            task_progress['task_2.4'] = 0
    return feedback
            
def evaluate_task_12(code):
    try:
        if 'input(' in code:
            feedback = "התוכנית לא אמורה לקחת קלט"
        else:
            exec_globals = {}
            exec_locals = {}
            exec(code, exec_globals, exec_locals)

            if 'addition' in code and 'subtraction' in code:
                result_addition = exec_locals['addition'](2, 3)
                result_subtraction = exec_locals['subtraction'](5, 2)
                feedback = f"Addition result: {result_addition}, Subtraction result: {result_subtraction}"
                if result_addition != 5:
                    feedback = 'פונקציית ההוספה שלך לא עובדת'
                    task_progress['task_12'] = 50 
                if result_subtraction != 3:
                    feedback = 'פונקציית החיסור שלך לא עובדת'
                    task_progress['task_12'] = 50 
                if result_subtraction != 3 and result_addition != 5:
                    feedback = "שתי הפונקציות שלך לא עובדות"
                    task_progress['task_12'] = 0
                if result_addition == 5 and result_subtraction == 3:
                    feedback = "!!הפונקציות שלך עובדות הצלחת במשימה" 
                    task_progress['task_12'] = 100
            else:
                feedback = "אין לך בקוד פונקציית חיבור ופונקציית חיסור או שלא קראת לפונקציות בשמות הנכונים"
                task_progress['task_12'] = 0
    except SyntaxError as e:
        feedback = "יש לך טעות בכתיבה של הקוד"
        task_progress['task_12'] = 0
    except Exception as e:
        feedback = f"Error: {str(e)}\n{print(e)}"
    return feedback

def evaluate_task_13(code):
    if code == '':
        feedback = 'אתה צריך להכניס קוד'
        return feedback
    try:
        simulated_input_1 = "10c"  
        simulated_input_2 = "50f" 
        result_1 = subprocess.run(['python', '-c', code], input=simulated_input_1, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result_2 = subprocess.run(['python', '-c', code], input=simulated_input_2, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result_1.returncode == 0 and result_2.returncode == 0:
            output_result_1 = result_1.stdout.strip()
            output_result_2 = result_2.stdout.strip()
            if "50" in output_result_1 and "10" in output_result_2:
                feedback = "הצלחת במשימה"
                task_progress['task_13'] = 100
            elif "50" in output_result_1 and "10" not in output_result_2: 
                task_progress['task_13'] = 50
                feedback = "המרה מפרנייט לצלזיוס לא עובדת"
            elif "50" not in output_result_1 and "10" in output_result_2: 
                task_progress['task_13'] = 50
                feedback = "המרה מצלזיוס לפרנהייט לא עובדת"
            else:
                task_progress['task_13'] = 0
                feedback = "התוכנית שלך לא נכונה אולי טעית בנוסחה"
        else:
            task_progress['task_13'] = 0
            feedback = "שגיאה בעת הרצת הקוד אולי טעית בכתיבה של הקוד" 
    except SyntaxError as e:
        feedback = "יש לך טעות בכתיבה של הקוד"
        task_progress['task_13'] = 0
    return feedback