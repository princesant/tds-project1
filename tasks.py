import os
import subprocess
import json
import sqlite3
import openai
from datetime import datetime

openai.api_key = os.getenv("AIPROXY_TOKEN")  # Securely load API key

def execute_task(task):
    """Parses task description and executes the corresponding function."""
    if "install uv" in task and "datagen.py" in task:
        return install_uv_and_run_datagen(task)
    elif "format" in task and "prettier" in task:
        return format_markdown(task)
    elif "count" in task and "Wednesdays" in task:
        return count_wednesdays()
    elif "sort contacts" in task:
        return sort_contacts()
    elif "recent log" in task:
        return extract_recent_logs()
    elif "index markdown" in task:
        return index_markdown_files()
    elif "email sender" in task:
        return extract_email_sender()
    elif "credit card" in task:
        return extract_credit_card()
    elif "similar comments" in task:
        return find_similar_comments()
    elif "total sales" in task:
        return calculate_gold_ticket_sales()
    else:
        raise ValueError("Unsupported task")

def install_uv_and_run_datagen(task):
    """Install 'uv' if required and run datagen.py"""
    subprocess.run(["pip", "install", "uv"], check=True)
    user_email = task.split()[-1]
    subprocess.run(["python", "datagen.py", user_email], check=True)
    return "Datagen script executed"

def format_markdown(task):
    """Formats Markdown using prettier"""
    subprocess.run(["npx", "prettier@3.4.2", "--write", "/data/format.md"], check=True)
    return "Markdown formatted"

def count_wednesdays():
    """Counts number of Wednesdays in /data/dates.txt"""
    with open("/data/dates.txt", "r") as f:
        dates = [line.strip() for line in f.readlines()]
    
    count = sum(1 for date in dates if datetime.strptime(date, "%Y-%m-%d").weekday() == 2)
    
    with open("/data/dates-wednesdays.txt", "w") as f:
        f.write(str(count))
    
    return f"Counted {count} Wednesdays"

# Other functions (sorting JSON, log extraction, etc.) go here...

