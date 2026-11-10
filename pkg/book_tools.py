
import json


def read_books(file_name: str) -> list:
    """讀取 JSON 書籍資料。

    file_name：要讀取的 JSON 檔案名稱。
    回傳：包含書籍資料的 list。
    """
    with open(file_name, "r", encoding="UTF-8") as file:
        books = json.load(file)

    return books


def write_books(books: list, file_name: str) -> None:
    """將書籍資料寫入 JSON 檔案。

    books：要匯出的書籍列表。
    file_name：要寫入的 JSON 檔案名稱。
    回傳：無。
    """
    with open(file_name, "w", encoding="UTF-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def search_books(books: list, keyword: str) -> list:
    """依照書名關鍵字查詢書籍。

    books：全部書籍資料。
    keyword：使用者輸入的查詢關鍵字。
    回傳：符合條件的書籍列表。
    """
    result = [
        book for book in books
        if keyword.lower() in book["title"].lower()
    ]

    return result


def show_books(books: list) -> None:
    """顯示書籍資料。

    books：要顯示的書籍列表。
    回傳：無。
    """
    if not books:
        print("目前沒有書籍資料")
        return

    print(f"{'編號':>4}  {'書籍編號':<8} {'書名':<18} {'作者':<10} {'價格':>10}  狀態")

    for index, book in enumerate(books, 1):
        status = "已借出" if book["borrowed"] else "可借閱"

        print(
            f"{index:>4}  {book['id']:<8} "
            f"{book['title']:<18} {book['author']:<10} "
            f"{book['price']:>10,}  {status}"
        )
