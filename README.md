🛒 AI-Powered Supermarket SQL Assistant

Project Overview
This project enables users to interact with a supermarket MySQL database using natural language. By leveraging Google Gemini AI, Python, and Gradio, the application generates SQL queries from plain English questions, executes them, and provides both tabular results and human-readable answers. It demonstrates the integration of AI with databases for practical, real-world applications.

🚀 Features

Natural Language to SQL: Ask questions in plain English; Gemini AI generates accurate SQL queries.

Automatic Query Execution: SQL is executed directly on the MySQL supermarket database.

Human-Readable Answers: AI generates plain-language summaries of query results.

Interactive Web Interface: Built with Gradio, displaying SQL, results, and answers.

Database Schema-Aware: Supports all tables in the supermarket schema (Customers, Products, Orders, OrderDetails, Suppliers, Inventory, Categories).

🛠️ Tech Stack

Python 3.10+

MySQL: Relational database backend

SQLAlchemy: Database connection & query execution

Google Gemini API: Natural language to SQL generation & answer summarization

Pandas: Data manipulation

Gradio: Interactive web interface

⚙️ Installation

Clone the repository

git clone https://github.com/yourusername/supermarket-ai-sql.git
cd supermarket-ai-sql


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Set up MySQL database

Create the supermarket database and tables as defined in the schema.

Add sample data (optional for testing).

Set API key for Gemini

export GEMINI_API_KEY="your_api_key"   # Linux/Mac
set GEMINI_API_KEY="your_api_key"      # Windows

📝 Usage

Run the application:

python ChatWithDB.py


Open the Gradio interface in your browser.

Enter your question in plain English, e.g.:

“How many customers are in the database?”

“Which product has the highest sales?”

“Which supplier provided the most products?”

View generated SQL, query results, and human-readable answers.

📊 Screenshots

(Add screenshots of your Gradio app here to make it visually appealing)

💡 Example Questions

“Who is the top-spending customer and how much did they spend?”

“List all products with stock below 10 units.”

“Show total revenue per product category.”

📂 Repository Structure
/ChatWithDB.py       # Main application script
/requirements.txt    # Python dependencies
/README.md           # Project documentation

⚖️ License

This project is licensed under the MIT License.
