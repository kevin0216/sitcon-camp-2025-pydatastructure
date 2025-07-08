import json

# 請讓這個有問題的程式碼能夠輸出找不到檔案
# ... 處應該加上什麼來 catch 找不到檔案的錯誤
...
with open("not_exist", "r") as f:
    ex_dict = json.load(f)
...
