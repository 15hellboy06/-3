# TODO Напишите функцию для поиска индекса товара
def find_first_item_index(items_list, find_item):
    """
    Находит индекс первого вхождения элемента в списке.

    Args:
        items_list: Список товаров.
        find_item: Товар, который нужно найти.

    Returns:
        Индекс первого вхождения товара, если товар найден, иначе None.
    """
    try:
        return items_list.index(find_item)
    except ValueError:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_item_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
