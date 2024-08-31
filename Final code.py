import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

quiz_data = [
    {
        "question": "What is the first SDG goal?",
        "options": ["No Poverty", "Zero Hunger", "Good Health and Well-being", "Quality Education"],
        "answer": "No Poverty"
    },
    {
        "question": "Which SDG goal focuses on climate action?",
        "options": ["Life on Land", "Climate Action", "Affordable and Clean Energy", "Life Below Water"],
        "answer": "Climate Action"
    },
    {
        "question": "Due to these changes in climate, the number of weather, climate and water-related disasters has increased by a factor of five over the past 50 years, causing over __________________ deaths and US$3.64 trillion in losses",
        "options": ["2 million", "3 million", "4 million", "7 million"],
        "answer": "2 million"
    },
    {
        "question": "Which resource is South Africa’s most important export?",
        "options": ['Copper', 'Diamond', 'Silver', 'Gold'],
        "answer": "Gold"
    },
    {
        "question": "On _____________, the United Nations marks its very first International Day of Clean Energy",
        "options": ['January 26 2024', '27th December 2023', '13th November 2023', 'None of the above'],
        "answer":"January 26 2024"
    },
    {
        "question": "According to IPCC, warming beyond ______ degrees could have irreversible and irreparable consequences.",
        "options": ['2', '1.7', '1.5', 'None of the above'],
        "answer": "1.5"
    },
    {
        "question": "________________ has always been an integral part of the sustainable development agenda.",
        "options": ['Education for all', 'Climate Action', 'Eradicate Poverty', 'None of the above'],
        "answer": 'Education for all'
    },
    {
        "question": "Sustainable Development Goal _______ aims to “protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, and halt and reverse land degradation and halt biodiversity loss”.",
        "options": ['13', '14', '15', '16'],
        "answer": '15'
    },
    {
        "question": "In which year the term 'Sustainable Development' came into existence?",
        "options": ['1987', '1980', '1978', '1992'],
        "answer": '1980'
    },
    {
        "question": "The United Nations Commission on Sustainable Development (CSD) was established by the UN General Assembly in the year _____________",
        "options": ['1992', '1993', '1994', '1995'],
        "answer": '1992'
    },
    {
        "question": "Which of the following is not included in the parameters of sustainable development?",
        "options": ['Carrying capacity', ' Inter and Intra-generation equity', 'Gender disparity and diversity', 'None of the above'],
        "answer": 'None of the above'
    },
    {
        "question": "Any contaminated components that seep into the soil, filtration, and are transferred into the underground reservoir are referred to as _____________",
        "options": ['Water Pollution', 'Land Contamination', 'Noise Pollution', 'Air Pollution'],
        "answer": 'Land Contamination'
    },
    {
        "question": "The alternative name for landscaping is:",
        "options": ['decrease', 'restoration', 'topsoil removal', 'none of the above'],
        "answer": 'restoration'
    },
    {
        "question": "According to the United Nations, the following are the significant issues of social progress:",
        "options": ['instruction', 'public health', 'living standards', 'all of these'],
        "answer": 'all of these'
    },
    {
        "question": "United Nations (UN) era of schooling for sustainable growth is from:",
        "options": ['2002-11', '2003-12', '2004-13', '2005-14'],
        "answer": '2005-14'
    }
]

class SDGQuizGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SDG Goal Quiz Game")
        self.geometry("849x724")

        try:
            bg_image = Image.open("C:/Users/har22/.vscode/sdgbgr.jpg")
            bg_photo = ImageTk.PhotoImage(bg_image.resize((849, 724)))
        except Exception as e:
            messagebox.showerror("Error", "Unable to load background image: {e}")
            self.destroy()
            return

        self.canvas = tk.Canvas(self, width=1600, height=900)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=bg_photo, anchor="ne")
        self.bg_photo = bg_photo

        self.current_question = 0
        self.score = 0

        self.display_quiz()
        self.add_exit_button()
        self.show_start_screen()

    def show_start_screen(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        title_label = tk.Label(self, text="😊 Welcome to the SDG Goal Quiz Game 😊", font=("Segoe UI Variable Display", 21, "bold"))
        self.canvas.create_window(400, 150, window=title_label)
        start_button = tk.Button(self, text="🚀 Start Quiz", font=("Arial", 16), command=self.start_quiz)
        self.canvas.create_window(500, 200, window=start_button)

    def start_quiz(self):
        self.current_question = 0
        self.score = 0
        self.clear_screen()
        self.display_quiz()

    def display_quiz(self):
        question_data = quiz_data[self.current_question]
        self.question_label = tk.Label(self, text=question_data["question"], font=("Segoe UI Variable Display", 20), wraplength=790)
        self.canvas.create_window(400, 100, window=self.question_label)

        self.option_buttons = []
        for i, option in enumerate(question_data["options"]):
            button = tk.Button(self, text=option, font=("Segoe UI", 13), command=lambda opt=option: self.check_answer(opt))
            self.canvas.create_window(400, 200 + i * 50, window=button)
            self.option_buttons.append(button)

    def check_answer(self, selected_option):
        correct_answer = quiz_data[self.current_question]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "That's correct!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer is: {correct_answer}")

        self.current_question += 1
        if self.current_question < len(quiz_data):
            self.clear_screen()
            self.display_quiz()
        else:
            self.show_final_score()

    def clear_screen(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

    def show_final_score(self):

        self.clear_screen()
        score_text = f"🎉Your final score is: {self.score} / {len(quiz_data)}🎉"
        self.score_label = tk.Label(self, text=score_text, font=("Ink Free", 24), bg="#FFFFFF")
        self.canvas.create_window(400, 100, window=self.score_label)

        feedback_label = tk.Label(self, text="Please provide your feedback below:", font=("Segoe UI Variable Display", 18))
        self.canvas.create_window(400, 200, window=feedback_label)

        self.feedback_textbox = tk.Text(self, height=5, width=50, font=("Segoe UI", 12))
        self.canvas.create_window(400, 300, window=self.feedback_textbox)

        submit_feedback_button = tk.Button(self, text="Submit Feedback", font=("Ink Free", 16), command=self.submit_feedback)
        self.canvas.create_window(400, 420, window=submit_feedback_button)
   
        restart_button = tk.Button(self, text="Play Again", font=("Ink Free", 16), command=self.restart_game)
        self.canvas.create_window(400, 470, window=restart_button)

        exit_button = tk.Button(self, text="Exit", font=("Ink Free", 16), command=self.quit)
        self.canvas.create_window(400, 520, window=exit_button)


    def restart_game(self):
        self.current_question = 0
        self.score = 0
        self.clear_screen()
        self.display_quiz()

    def add_exit_button(self):
        exit_button = tk.Button(self, text="Exit", font=("Arial", 16), command=self.quit)
        self.canvas.create_window(700, 550, window=exit_button)

    def submit_feedback(self):
        feedback = self.feedback_textbox.get("1.0", tk.END).strip()
        if feedback:
            print("User Feedback:", feedback) 
            messagebox.showinfo("Thank You", "Thank you for your feedback!")
        else:
            messagebox.showwarning("Empty Feedback", "Please enter your feedback before submitting.")          

if __name__ == "__main__":
    game = SDGQuizGame()
    game.mainloop()