# Wonderland Programming Realms

*A gamified programming learning experience inspired by Alice in Wonderland.*

## About

Wonderland Programming Realms is an interactive desktop quiz game that turns learning programming concepts into an immersive adventure. Inspired by *Alice in Wonderland*, the application allows users to create adventurer profiles and explore themed realms that teach fundamental concepts in **Python, C++, Web Development, and Data Science**.

Through storytelling, gamified quizzes, persistent player profiles, and performance analytics, the project aims to make programming education engaging and interactive.

---

## Features

### Persistent Player Profiles

Users can create and manage adventurer profiles. Game progress, statistics, scores, and playtime are saved locally using JSON and CSV files.

### Four Programming Realms

🐍 **Python Rabbit Hole** – Python fundamentals such as operators, data types, list comprehensions, and functions.

👑 **C++ Looking Glass** – Key C++ topics including memory management, pointers, and function overloading.

🎩 **Mad Tea Party** – Web development concepts such as HTML, CSS, and JavaScript.

📊 **Queen's Croquet Ground** – Introductory data science tools like NumPy and Pandas.

### Gamified Quiz System

Players answer multiple-choice questions across three difficulty levels: **Easy, Medium, and Hard**, with immediate feedback.

### Player Dashboard

Displays player statistics including:

* Total score
* Completed realms
* Playtime
* Difficulty-wise performance
* Favourite realm

### Python Spellbook

An interactive section demonstrating advanced Python concepts:

* Recursion
* Lambda functions
* List comprehensions
* Map / Filter / Reduce
* Regular expressions
* Exception handling

### Data Analytics

Optional integration with **Pandas** and **Matplotlib** allows players to visualise performance and export analytical reports.

### Interactive GUI

The application uses **Tkinter** to provide a responsive desktop interface.

---

## Technologies Used

### Core Technologies

* Python 3.6+
* Tkinter (GUI framework)
* JSON (profile storage)
* CSV (game statistics)

### Optional Libraries

* Pandas
* NumPy
* Matplotlib
* Pillow (image handling)

### Python Standard Library

* `re`
* `functools`
* `datetime`

---

## Installation

### Prerequisites

* Python 3.6 or higher
* pip (Python package installer)

### Clone the repository

```bash
git clone https://github.com/YOURUSERNAME/wonderland-programming-realms.git
cd wonderland-programming-realms
```

### Optional: Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install optional dependencies

```bash
pip install pandas numpy matplotlib
```

For image support:

```bash
pip install Pillow
```

### Run the application

```bash
python alice_game.py
```

---

## Project Structure

```
wonderland-programming-realms
│
├── alice_game.py
├── wonderland_questions.json
├── README.md
│
├── screenshots
│
└── requirements.txt
```

User data is stored locally:

Mac / Linux

```
~/.wonderland_data/
```

Windows

```
%APPDATA%\Wonderland\
```

---

## Learning Goals

This project explores how programming education can be enhanced through **interactive design and gamification**.

Key technical concepts demonstrated:

* Object-oriented programming in Python
* GUI development using Tkinter
* Persistent data storage using JSON and CSV
* Modular application structure
* Quiz-based educational design
* Performance analytics and data visualisation

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

## License

This project is licensed under the **MIT License**.

---

## Acknowledgements

Inspired by *Alice's Adventures in Wonderland* by **Lewis Carroll**.

Developed as part of a programming project at **MPSTME, NMIMS University** under the supervision of **Prof. Nilima Agarwal**.

---

✨ *Enjoy exploring the Wonderland of code!* 🐇
