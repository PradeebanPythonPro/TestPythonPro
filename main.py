from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista di domande con risposte corrette
questions = [
    {
        'question': 'Il nome vero di Goku è:',
        'options': ['Kakarot', 'Nappa', 'Jiren', 'Trunks'],
        'answer': 'Kakarot'
    },
    {
        'question': 'Come si chiama il pianeta dove si svolge la saga di Freezer?',
        'options': ['Terra', 'Pianeta dei Kaio', 'Namecc', 'Konoha'],
        'answer': 'Namecc'
    },
    {
        'question': 'Qual è la trasformazione più potente di Goku in Dragon Ball Z?',
        'options': ['Super Saiyan 1', 'Super Saiyan 4', 'Super Saiyan 3', 'Super Saiyan Blue'],
        'answer': 'Super Saiyan 3'
    },
    {
        'question': 'Chi è il creatore originale di Dragon Ball?',
        'options': ['Akira Toriyama', 'Eiichiro Oda', 'Masashi Kishimoto', 'Tite Kubo'],
        'answer': 'Akira Toriyama'
    },
    {
        'question': 'Chi è il principale antagonista nella saga di Dragon Ball GT?',
        'options': ['Freezer', 'Cell', 'Majin Bu', 'Baby'],
        'answer': 'Baby'
    },
    {
        'question': 'Qual è il nome della tecnica di combattimento più potente di Vegeta?',
        'options': ['Kamehameha', 'Final Flash', 'Spirit Bomb', 'Galick Gun'],
        'answer': 'Final Flash'
    },
    {
        'question': 'Chi è il dio della distruzione dell\'universo 7 in Dragon Ball Super?',
        'options': ['Whis', 'Beerus', 'Champa', 'Zeno'],
        'answer': 'Beerus'
    },
    {
        'question': 'Qual è il nome del secondo figlio di Goku?',
        'options': ['Goten', 'Gohan', 'Trunks', 'Piccolo'],
        'answer': 'Goten'
    },
    {
        'question': 'Chi è il miglior amico di Goku?',
        'options': ['Piccolo', 'Vegeta', 'Krillin', 'Yamcha'],
        'answer': 'Krillin'
    },
    {
        'question': 'Chi è il guerriero leggendario della razza Saiyan, destinato a comparire ogni 1000 anni?',
        'options': ['Goku', 'Vegeta', 'Broly', 'Bardak'],
        'answer': 'Broly'
    },
]

# Creiamo una lista di tuple contenenti domanda e opzioni
question_options = [(question['question'], question['options'], f"question_{index}") for index, question in enumerate(questions)]

# Punteggio massimo
max_score = 0

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('quiz'))  # Reindirizza alla pagina del quiz
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global max_score
    total_questions = len(questions)  # Calcola il numero totale delle domande
    if request.method == 'POST':
        # Calcolo del punteggio
        score = 0
        for index, question in enumerate(questions):
            user_answer = request.form.get(f'question_{index}')
            if user_answer == str(question['answer']):  # Confronto le risposte come stringhe
                score += 1
        
        # Aggiorna il punteggio massimo
        if score > max_score:
            max_score = score

        return render_template('score.html', score=score, max_score=max_score, total_questions=total_questions)

    return render_template('quiz.html', question_options=question_options, max_score=max_score)


@app.route('/developer')
def developer():
    return "Sviluppato da [Il Tuo Nome]"


if __name__ == '__main__':
    app.run(debug=True)
