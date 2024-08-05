def test_function():
    def inner_function():  # 2
        print("Я в области видимости функции test_function")

    inner_function() # функция ничего не возвращает


# inner_function()
# Вызов функци inner_function() вне функции test_function приводит к появлению ошбики -
# NameError: name 'inner_function' is not defined
test_function() # функция работает
