from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()



    #1 Проверка, что нельзя добавить уже имеющуюся книгу в списке
    def test_add_new_book_add_existing_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1

    #2 Проверка, что рэйтинг выставляется
    def test_set_book_rating_set_rating_five(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        rating = collector.get_books_rating()
        assert rating.get('Гордость и предубеждение и зомби') == 5

    #3 Проверка, что можно получить рэйтинг книги по ее имени
    def test_get_book_rating_rating_is_returned(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        rating = collector.get_book_rating('Гордость и предубеждение и зомби')
        assert rating

    #4 Проверка, что список get_books_with_specific_rating не содержит книг с невыбранным рэйтингом
    def test_get_books_with_specific_rating_specific_list_is_not_empty(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 10)

        specific_rating_list = collector.get_books_with_specific_rating(5)
        assert 'Что делать, если ваш кот хочет вас убить' not in specific_rating_list

    #5 Проверка, что метод get_books_rating возвращает словарь
    def test_get_books_rating_dict_is_returned(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_books_rating()

    #6 Проверка, что книга добавляется в список избранного
    def test_add_book_in_favorites_book_added_to_favourites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    #7 Проверка, что книга удаляется из избранного
    def test_delete_book_from_favorites_book_is_removed(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    #8 Проверка, что метод get_list_of_favorites_books возвращает пустой список, если ни одной книги не было добавлено в избранное
    def test_get_list_of_favorites_books_with_zero_books_added(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []