
from pkg.book_tools import read_books, show_books, search_books, write_books


def main() -> None:
    """執行書籍管理系統。"""
    try:
        books = read_books("books.json")

    except FileNotFoundError:
        print("找不到 books.json，程式無法啟動。")
        return

    except ValueError:
        print("books.json 格式錯誤，程式無法啟動。")
        return

    except OSError:
        print("無法讀取 books.json，程式無法啟動。")
        return

    print(f"成功讀取 {len(books)} 筆書籍資料。")

    while True:
        print("\n--- 簡易書籍管理系統 ---")
        print("1. 顯示全部書籍")
        print("2. 新增書籍")
        print("3. 查詢書籍")
        print("4. 變更借閱狀態")
        print("5. 顯示最後 3 筆書籍與統計")
        print("6. 匯出書籍資料")
        print("7. 離開系統")
        print("------------------------")

        choice = input("請選擇功能：")

        if choice == "1":
            print("\n--- 全部書籍 ---")
            show_books(books)

        elif choice == "2":
            while True:
                book_id = input("請輸入書籍編號：").strip()

                if book_id == "":
                    print("書籍編號不可為空，請重新輸入。")
                    continue

                duplicated = False

                for book in books:
                    if book["id"] == book_id:
                        duplicated = True
                        break

                if duplicated:
                    print("書籍編號已存在，請重新輸入。")
                else:
                    break

            while True:
                title = input("請輸入書名：").strip()

                if title == "":
                    print("書名不可為空，請重新輸入。")
                else:
                    break

            while True:
                author = input("請輸入作者：").strip()

                if author == "":
                    print("作者不可為空，請重新輸入。")
                else:
                    break

            while True:
                price_text = input("請輸入價格：").strip()

                try:
                    price = int(price_text)

                    if price > 0:
                        break
                    else:
                        print("價格須為大於 0 的整數，請重新輸入。")

                except ValueError:
                    print("價格須為大於 0 的整數，請重新輸入。")

            new_book = {
                "id": book_id,
                "title": title,
                "author": author,
                "price": price,
                "borrowed": False
            }

            books.append(new_book)
            print("新增成功。")

        elif choice == "3":
            while True:
                keyword = input("請輸入書名關鍵字：").strip()

                if keyword == "":
                    print("關鍵字不可為空，請重新輸入。")
                else:
                    break

            result = search_books(books, keyword)

            if result:
                print("\n--- 查詢結果 ---")
                show_books(result)
            else:
                print("查無符合的書籍")

        elif choice == "4":
            book_id = input("請輸入書籍編號：").strip()

            found = False

            for book in books:
                if book["id"] == book_id:
                    book["borrowed"] = not book["borrowed"]

                    status = "已借出" if book["borrowed"] else "可借閱"

                    print(
                        f"「{book['title']}」的狀態已變更為：{status}"
                    )

                    found = True
                    break

            if not found:
                print("查無此書籍編號")

        elif choice == "5":
            if not books:
                print("目前沒有書籍資料")

            else:
                recent_books = books[-3:]

                print("\n--- 最後 3 筆書籍 ---")
                show_books(recent_books)

                total_count = len(books)
                borrowed_count = 0
                total_price = 0

                for book in books:
                    total_price += book["price"]

                    if book["borrowed"]:
                        borrowed_count += 1

                available_count = total_count - borrowed_count
                average_price = total_price / total_count

                print("\n--- 書籍統計 ---")
                print(f"書籍總數：{total_count}")
                print(f"可借閱：{available_count}")
                print(f"已借出：{borrowed_count}")
                print(f"價格合計：{total_price:,} 元")
                print(f"平均價格：{average_price:.2f} 元")

        elif choice == "7":
            print("系統已退出")
            break

        elif choice == "6":
            try:
                write_books(books, "output.json")
                print(f"已匯出 {len(books)} 筆書籍資料至 output.json。")

            except OSError:
                print("匯出失敗，無法寫入 output.json。")

        else:
            print("選項錯誤，請重新選擇")


main()
