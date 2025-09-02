from sqlalchemy import create_engine
import pandas as pd 
from google import genai
import re
import gradio as gr

engine = create_engine("mysql+mysqlconnector://root:HASSAN123321hassan@127.0.0.1:3307/supermarket")
client = genai.Client(api_key="AIzaSyD4IcFq0ctSfJcocvc_5E5IDN6OEq9aeKg")  

def get_sql_query(question):
    prompt = f"""You are an expert SQL generator. 
The database schema is as follows: 

Tables:
1. Customers
   - customer_id (INT, PK)
   - first_name (VARCHAR)
   - last_name (VARCHAR)
   - email (VARCHAR)
   - phone (VARCHAR)
   - address (VARCHAR)
   - created_at (TIMESTAMP)

2. Categories
   - category_id (INT, PK)
   - category_name (VARCHAR)
   - description (TEXT)

3. Products
   - product_id (INT, PK)
   - product_name (VARCHAR)
   - category_id (INT, FK to Categories)
   - price (DECIMAL)
   - stock_quantity (INT)
   - description (TEXT)

4. Suppliers
   - supplier_id (INT, PK)
   - supplier_name (VARCHAR)
   - contact_name (VARCHAR)
   - phone (VARCHAR)
   - email (VARCHAR)
   - address (VARCHAR)

5. Orders
   - order_id (INT, PK)
   - customer_id (INT, FK to Customers)
   - order_date (DATE)
   - total_amount (DECIMAL)
   - status (VARCHAR)

6. OrderDetails
   - order_detail_id (INT, PK)
   - order_id (INT, FK to Orders)
   - product_id (INT, FK to Products)
   - quantity (INT)
   - price (DECIMAL)

7. Inventory
   - inventory_id (INT, PK)
   - product_id (INT, FK to Products)
   - supplier_id (INT, FK to Suppliers)
   - supply_date (DATE)
   - quantity (INT)
   - cost_price (DECIMAL) 

Instructions:
- Always use the correct table and column names above.  
- Write valid MySQL SQL queries only.  
- If a question is about counts, sums, or joins, use the appropriate tables (e.g., OrderDetails for quantities sold).  
- Wrap your SQL code in ```sql ... ``` blocks.  
Question: {question}"""  
    response = client.models.generate_content(
       model = "gemini-1.5-flash",
       contents = prompt
    )
    sql_query = response.candidates[0].content.parts[0].text
    match = re.search(r"```sql(.*?)```", sql_query, re.DOTALL)
    if match:
      sql_query = match.group(1).strip()
    else:
      sql_query = sql_query.strip()
    return question,sql_query

def sql_answer(sql_query):
   df = pd.read_sql(sql_query, engine)
   return df

def generate_answer(question,answer):
   prompt = f"generate a human response for this question {question} with its answer {answer}"
   response = client.models.generate_content(
      model="gemini-1.5-flash",
      contents= prompt
    )
   text = response.candidates[0].content.parts[0].text
   return text.strip()   

def ask_question(question):
    
    q, sql = get_sql_query(question)
    
    
    try:
        df = sql_answer(sql)
    except Exception as e:
        return f"Error running SQL: {e}", "", ""
    
    
    answer_text = generate_answer(question, df.iloc[0,0] if not df.empty else "No results")
    

    return sql, df.to_html(index=False), answer_text

with gr.Blocks(title="Chat with Supermarket DB") as demo:
    gr.Markdown("## 🛒 Ask questions about your Supermarket database in plain English")
    
    with gr.Row():
        question_input = gr.Textbox(label="Your Question", placeholder="e.g., How many customers are in the database?", lines=2)
    
    with gr.Row():
        sql_output = gr.Textbox(label="Generated SQL", interactive=False)
        answer_output = gr.HTML(label="Query Result (Table)")
    
    answer_text_output = gr.Textbox(label="Answer in plain English", interactive=False)
    
    submit_btn = gr.Button("Ask")
    
    submit_btn.click(
        fn=ask_question,
        inputs=question_input,
        outputs=[sql_output, answer_output, answer_text_output]
    )

demo.launch()














