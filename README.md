📄 README.md
# 🎓 Super GPA Calculator System

A modular Python-based GPA management system designed to simulate a real university-style academic record system. It supports semester, yearly, and cumulative GPA calculations with weighted grading, persistent student storage, and automatic report generation with historical archiving.

## 🚀 Features

- **Student Management**: Add students with multiple academic terms and courses.
- **GPA Calculations**:
  - Semester GPA (specific term)
  - Year GPA (all terms in a year)
  - Cumulative GPA (all terms across student's history)
- **Weighted Grading**: Supports regular (1.0x), honors (1.1x), and AP (1.2x) courses, capped at 4.0.
- **Persistent Storage**: JSON database with corruption safety, atomic writes, and automatic backups.
- **Report Generation**: Formatted text reports saved to `new_reports/`, auto-archived to `past_reports/` with timestamps.
- **CSV Export**: Export course data to CSV after GPA calculation for easy analysis.
- **Input Validation**: Robust error handling for grades (A-F), credits (>0), course types, and unique student IDs.
- **Command-Line Interface**: Simple menu-driven system with built-in help.
- **Modular Design**: Separated concerns across files for maintainability.

## 📁 Project Structure

```
super-gpa-calculator/
│
├── main.py          # CLI interface, user input handling, menu system
├── gpa.py           # GPA calculation engine (weighted/unweighted)
├── storage.py       # JSON database management, report archiving
├── utils.py         # Report formatting, CSV export, date utilities
│
├── data/
│ ├── students.json  # Persistent student database
│ └── backup/        # Automatic backups on corruption
│
├── new_reports/     # Latest generated reports (text & CSV)
├── past_reports/    # Archived reports with timestamps
│
└── README.md        # This documentation
```

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.6 or higher (no external libraries required).

### Installation
1. Download or clone the project files into a directory.
2. Ensure Python is installed: `python3 --version`.
3. Run the application: `python3 main.py`.

Directories (`data/`, `new_reports/`, `past_reports/`) are created automatically on first run.

## 📖 Usage Guide

### Starting the Application
Run `python3 main.py` to launch the CLI menu.

### Main Menu Options
1. **Add Student**: Create a new student record.
   - Enter name and unique ID.
   - Add academic terms (e.g., "Fall 2026").
   - For each term, add courses: name, grade (A-F), credits (>0), type (regular/honors/ap).
   - Type "done" to finish courses/terms.
2. **View Students**: List all stored students by ID and name.
3. **Calculate GPA**: Select a student and compute GPA.
   - Choose: Semester (specific term), Year (all terms in a year), or Cumulative (all terms).
   - Reports are generated, saved, and archived.
   - Option to export course data to CSV.
4. **Help**: Display in-app usage instructions and GPA rules.
5. **Exit**: Quit the application.

### GPA Calculation Example
- **Course 1**: Math, A, 3 credits, regular → 4.0 × 1.0 × 3 = 12 points
- **Course 2**: Science, B, 4 credits, honors → min(3.0 × 1.1, 4.0) × 4 = 4.0 × 4 = 16 points
- **Total**: 28 points / 7 credits = **4.0 GPA**

### Data Storage
- Student data persists in `data/students.json`.
- Reports in `new_reports/` are archived to `past_reports/` on new calculations.
- Automatic backups created if JSON corruption is detected.

## 🔧 Technical Details

- **GPA Scale**: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0
- **Weighting Formula**: `min(grade_points × weight, 4.0) × credits`
- **Storage Safety**: Atomic JSON writes prevent corruption; backups on read errors.
- **Report Filtering**: Shows only relevant courses based on GPA type.
- **CSV Format**: Columns: Semester, Course Name, Grade, Credits, Type, Weight

## 📝 Changelog

- **v1.0**: Initial release with semester/year GPA, basic storage.
- **v1.1**: Added cumulative GPA, CSV export, input validation, help menu, improved README.

## 🤝 Contributing

Enhance the system with:
- GUI (Tkinter/Flask)
- PDF report generation (reportlab)
- Database migration (SQLite)
- Unit tests (unittest/pytest)
- Advanced features (GPA trends, course prerequisites)

Pull requests welcome!

## 📄 License

MIT License - Free to use and modify.
  - course type (regular, honors, AP)
  - weight multiplier

---

## 🗂 Persistent Storage
- JSON-based lightweight database (`students.json`)
- Supports multiple students
- Structured academic term storage

---

## 📄 Report System
- Auto-generates GPA reports
- Saves latest report to:

```
new_reports/report.txt
```

- Automatically archives old reports into:

```
past_reports/
```

- Timestamp-based versioning for audit history

---

# ▶️ How to Run

## 1. Install Python
Ensure Python 3.10+ is installed.

## 2. Run the program

```bash
python main.py
🧭 Main Menu

When launched:

===== SUPER GPA SYSTEM =====
1. Add Student
2. View Students
3. Calculate GPA
4. Exit
📊 GPA Calculation Options

After selecting a student:

1. Semester GPA
2. Year GPA
📌 Semester GPA

Calculates GPA for a single academic term.

Example:

Fall 2026
📌 Year GPA

Calculates GPA across all terms in a given year.

Example:

Fall 2026 + Spring 2026 → 2026 Year GPA
🧮 GPA Scale
Standard 4.0 Scale
Grade	Points
A	4.0
B	3.0
C	2.0
D	1.0
F	0.0
Weighted System
Course Type	Multiplier
Regular	1.0
Honors	1.1
AP	1.2
Final GPA is capped at 4.0 (university standard model)
📦 Example students.json
{
  "1001": {
    "name": "Mark Johnson",
    "id": "1001",
    "created_at": "2026-05-10T20:15:00",
    "terms": [
      {
        "semester": "Fall 2026",
        "courses": [
          {
            "name": "Math",
            "grade": "A",
            "credits": 3,
            "type": "honors",
            "weight": 1.1
          },
          {
            "name": "Computer Science",
            "grade": "B",
            "credits": 4,
            "type": "ap",
            "weight": 1.2
          }
        ]
      }
    ]
  }
}
🏗 Architecture Overview
Separation of Concerns
File	Responsibility
main.py	CLI + application flow
gpa.py	GPA calculation logic
storage.py	JSON database + file handling
utils.py	report formatting
Data Flow
User Input
   ↓
main.py (controller)
   ↓
storage.py (save/load JSON)
   ↓
gpa.py (calculate GPA)
   ↓
utils.py (format report)
   ↓
file output (reports/)
📄 Report Example Output
==========================================
           SUPER GPA SYSTEM
==========================================

Student: Mark Johnson
ID: 1001
Generated: 2026-05-10 20:15:00

MODE: YEAR GPA (2026)

COURSES:

Fall 2026:
  Math | Grade: A | Credits: 3 | Type: honors
  CS   | Grade: B | Credits: 4 | Type: ap

------------------------------------------
FINAL GPA: 3.742
==========================================
🧠 Design Philosophy
No stored GPA values (always computed dynamically)
JSON used as lightweight database layer
Modular architecture (engine vs storage vs UI)
Scalable toward real university registrar systems
Supports multi-term academic tracking
🔮 Future Enhancements

This system can be extended into:

🏫 Academic upgrades
cumulative GPA across all years
transcript generator (PDF export)
dean’s list / honor roll detection
academic probation rules
📊 Visualization
GPA trend graphs
semester comparison charts
🌐 Full system upgrade
web dashboard (Flask / React)
login system per student
database migration (SQLite/Postgres)
📜 License

Educational / personal use project.

⚙️ Author Notes

This project is structured to simulate:

university GPA systems
registrar database logic
academic reporting pipelines

---

If you want next step, I can turn this into a:

### 🔥 “Real University Portal System”
with:
- web UI dashboard
- login/auth system
- database backend (SQLite)
- transcript PDF generator
- GPA analytics charts

Just tell me 👍