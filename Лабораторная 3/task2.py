# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    """
    Находит общих участников в двух группах.

    Args:
        group1: Строка с участниками первой группы (разделены separator).
        group2: Строка с участниками второй группы (разделены separator).
        separator: Разделитель между участниками (по умолчанию ',').

    Returns:
        Список общих участников, отсортированный в алфавитном порядке.
    """
    group1_list = group1.split(separator)
    group2_list = group2.split(separator)
    common_participants = sorted(list(set(group1_list) & set(group2_list)))  # Используем множества для эффективности
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(f"Общие участники (с разделителем '|'): {common_participants}")


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники (с разделителем ','): {common_participants}")
# TODO Провеьте работу функции с разделителем отличным от запятой
