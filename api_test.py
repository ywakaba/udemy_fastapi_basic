import requests
import json
from datetime import datetime

def main():
    url = "http://localhost:8000/contacts"
    current_datetime = datetime.now().isoformat() # JSON変換できる様にISO形式に変換
    body = {
        "id": 1,
        "name": "山田さん",
        "email": "user@example.com",
        "url": "https://example.com/",
        "gender": 2, 
        "message": "メッセージです",
        "is_enabled": True,
        "created_at": current_datetime
        }
    
    # 辞書型->JSONに変換してPOST通信
    res = requests.post(url, json.dumps(body))
    print(res.json())
    
if __name__ == "__main__": # 直接実行された時だけ動く(__name__変数がmainとして生成)
    main()