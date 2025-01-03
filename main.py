def introspection_info(obj):
    info = {}

    # Тип объекта
    info['type'] = type(obj).__name__

    # Атрибуты объекта
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Методы объекта
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Модуль, к которому объект принадлежит
    info['module'] = obj.__class__.__module__

    # Дополнительные свойства объекта (если есть)
    info['other_properties'] = {}

    if isinstance(obj, (int, float, complex)):
        info['other_properties']['is_integer'] = isinstance(obj, int)
    elif isinstance(obj, str):
        info['other_properties']['length'] = len(obj)
    elif isinstance(obj, (list, tuple, set, dict)):
        info['other_properties']['length'] = len(obj)

    return info


# Пример использования
number_info = introspection_info(42)
print(number_info)
