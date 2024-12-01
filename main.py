import os
import importlib
import sys

sys.path.insert(0, os.path.abspath("src"))

def main():
    questions = {}
    questions_dir = "src/questions"

    for filename in os.listdir(questions_dir):
        if filename.endswith(".py"):
            question_num = filename.split("_")[-1].replace(".py", "")
            module_name = f"questions.{filename[:-3]}"
            try:
                module = importlib.import_module(module_name)
                questions[question_num] = module.main
            except ModuleNotFoundError as e:
                print(f"Erro ao importar o módulo {module_name}: {e}")

    question_number = input("Digite o número da questão para executar (1, 2, 3...): ")

    if question_number in questions:
        questions[question_number]()
    else:
        print(f"Questão {question_number} não encontrada.")

if __name__ == "__main__":
    main()
