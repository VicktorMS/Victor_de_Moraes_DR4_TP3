import os
import re
from constants import QUESTIONS

activities_dir = "src/questions"
os.makedirs(activities_dir, exist_ok=True)

def sanitize_filename(name):
    name = re.sub(r'[^a-zA-Z0-9\s]', '', name)
    name = re.sub(r'\s+', '_', name)
    return name.lower()

def generate_question_files(questions):
    for i, question in enumerate(questions, start=1):
        filename = sanitize_filename(question)
        file_path = os.path.join(activities_dir, f"{filename}_{i}.py")
        file_content = f"""
# {i} - {question}
{'#'*24}
def main():
    print("Esta é a questão: {question}")
"""
        with open(file_path, "w") as file:
            file.write(file_content.strip())
        print(f"Arquivo '{file_path}' criado com sucesso.")

generate_question_files(QUESTIONS)
