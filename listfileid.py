import gdown

def get_gdrive_folder_file_list(folder_url):
    """使用 gdown 取得共用資料夾內所有檔案與 ID"""
    try:
        print("正在讀取 Google Drive 資料夾資訊...")
        
        # skip_download=True 僅掃描結構、不下載實體檔案
        items = gdown.download_folder(
            url=folder_url,
            quiet=True,
            skip_download=True
        )
        
        if not items:
            print("無法讀取資料夾或資料夾為空。")
            return []

        print(f"\n成功取得檔案清單（共 {len(items)} 個項目）：\n")
        print(f"{'檔案名稱 / 路徑':<45} | {'檔案/目錄 ID':<35}")
        print("-" * 82)
        
        file_list = []
        for item in items:
            file_name = getattr(item, 'path', getattr(item, 'name', 'Unknown'))
            file_id = getattr(item, 'id', 'N/A')
            
            file_list.append({"name": file_name, "id": file_id})
            print(f"{file_name:<45} | {file_id:<35}")
            
        return file_list

    except Exception as e:
        print(f"存取失敗，錯誤訊息：{e}")
        return []

if __name__ == '__main__':
    # 填入您的 Google Drive 共用資料夾網址
    FOLDER_URL = "https://drive.google.com/drive/folders/1yYPSvaoUg4gk6xSm2SgIvRudev3foxAd?usp=sharing"
    get_gdrive_folder_file_list(FOLDER_URL)