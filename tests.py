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
        assert len(collector.get_books_rating()) == 2,f"number 2 expected, got: {len(collector.get_books_rating())}"

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_add_new_book_add_existing_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1,f"number 1 expected, got: {len(collector.get_books_rating())}"

    def test_set_book_rating_set_rating_five(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        rating = collector.get_books_rating()
        assert rating.get('Гордость и предубеждение и зомби') == 5

    def test_set_book_rating_set_rating_more_than10(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_rating('Гарри Поттер и философский камень', 15)
        rating = collector.get_books_rating()
        assert rating.get('Гарри Поттер и философский камень') == 1

    def test_set_book_rating_set_rating_zero(self):
        collector = BooksCollector()

        collector.add_new_book('Не читайте эту книгу')
        collector.set_book_rating('Не читайте эту книгу', 0)
        rating = collector.get_books_rating()
        assert rating.get('Не читайте эту книгу') == 1

    def test_set_book_rating_book_off_the_list_rating_is_not_set(self):
        collector = BooksCollector()

        collector.set_book_rating('Такой книги нет в списке', 5)
        rating = collector.get_books_rating()
        assert rating.get('Такой книги нет в списке') == None

    def test_get_book_rating_rating_is_returned(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        rating = collector.get_book_rating('Гордость и предубеждение и зомби')
        assert rating

    def test_get_books_with_specific_rating_specific_list_is_not_empty(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 10)

        specific_rating_list = collector.get_books_with_specific_rating(5)
        assert 'Что делать, если ваш кот хочет вас убить' not in specific_rating_list

    def test_get_books_rating_dict_is_returned(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        rating = collector.get_books_rating()
        assert rating.get('Гордость и предубеждение и зомби')


    def test_add_book_in_favorites_book_added_to_favourites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_book_off_the_dict_is_not_added(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        assert 'Гарри Поттер и философский камень' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_is_removed(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_with_zero_books_added(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []