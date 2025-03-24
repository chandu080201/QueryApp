![MasterQuery App](https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif)

# 🚀 MasterQuery App - Generative AI for SQL Automation

## 🌟 Overview
MasterQuery App is an **AI-powered SQL automation tool** that seamlessly translates **natural language** queries into **SQL commands**. Leveraging **Google Gemini Pro** and **LangChain**, this tool simplifies database interaction with a user-friendly **Streamlit interface**.

## 🔥 Features
✅ Converts **English queries** to **SQL commands** using **Google Gemini Pro**  
✅ Retrieves data from an **SQLite database**  
✅ Provides an interactive **Streamlit-based UI**  
✅ Loads **environment variables** securely using `dotenv`  
✅ **Effortless execution** of SQL queries with real-time response  

## 🏗️ Project Architecture
```
📂 MasterQuery-App/
│-- 📄 app.py            # Main Streamlit App
│-- 📄 sql.py            # SQL Query Handling
│-- 📄 requirements.txt  # Dependencies
│-- 📄 students.db       # SQLite Database
│-- 📄 .env              # Environment Variables
```

## ⚡ Quick Setup & Installation
```bash
# Clone the repository
$ git clone https://github.com/your-repo/MasterQuery-App.git

# Navigate to project directory
$ cd MasterQuery-App

# Install dependencies
$ pip install -r requirements.txt

# Create a .env file and add your Google API Key
GOOGLE_API_KEY=your_api_key_here

# Run the application
$ streamlit run app.py
```

## 🛠️ Tech Stack
- **Python** 🐍
- **Streamlit** 🎨
- **Google Gemini Pro** 🤖
- **SQLite** 🗄️
- **LangChain** 🔗

## 🚀 How It Works
1️⃣ Enter your **natural language** question in the input box.  
2️⃣ The app **converts** it into an **SQL query** using **Google Gemini Pro**.  
3️⃣ The SQL command is **executed** on the SQLite database.  
4️⃣ The **results** are displayed in real-time! 🎉

## 🎯 Example Queries
| English Query | Generated SQL |
|--------------|--------------|
| How many students are there? | `SELECT COUNT(*) FROM STUDENT;` |
| Show all students in Data Science class. | `SELECT * FROM STUDENT WHERE CLASS='Data Science';` |

## 📸 Screenshot
![MasterQuery UI](https://via.placeholder.com/800x400.png?text=MasterQuery+App+UI)

## 🤝 Contributing
Contributions are **welcome**! If you have ideas for improvement, feel free to **fork** the repo and submit a **pull request**.

## 📜 License
This project is licensed under the **MIT License**.

---
**🚀 MasterQuery App - Making SQL Queries Effortless!**
