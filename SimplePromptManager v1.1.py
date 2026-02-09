"""
SimplePromptManager.py - Менеджер промптов для нейросетей

Функционал:
1. Хранение промптов в структурированном виде
2. Поиск по тегам
3. Интерактивный интерфейс

Автор: [JDM-enjoyer]
Версия: 1.0
Дата: 2026-01-31
"""

# === БАЗА ДАННЫХ ПРОМПТОВ ===
import json
with open("prompts_database.json", "r", encoding="utf-8") as file:
    prompts_database = json.load(file)

# Функция для поиска промпта основываясь на наличии в БД нужного тега для него и добавление результата в переменную для вывода
def find_prompts_by_tags(tag):
    result = []
    for prompt in prompts_database:
        if tag in prompt["tags"]:
            result.append(prompt)
    return result

# Список для отслеживания всех тегов в БД 
available_tags = []
for prompt in prompts_database:
    for tag in prompt["tags"]:
        available_tags.append(tag)
unique_tags = list(set(available_tags))
    
# Проверка ввода с предложением доступных тегов и вводом данных, а также проверка для завершения поиска    
while True:
    tag_input = input(f"Доступные теги: {", ".join(unique_tags)} \n Введите тег (Enter для выхода): ").lower()
    if tag_input.lower() in ["выход", "exit", ""]:
        break
    result = find_prompts_by_tags(tag_input)
    
# Проверка соотвествия тега промпту и вывод или же повтор поиска пока работает цикл while
    if result:
        for found_prompt in result:
            print(f"{found_prompt['name']}\n{found_prompt['prompt']}")
            print("=" * 84)
    else:
        print("Ничего не найдено.")

    