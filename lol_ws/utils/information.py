import json, yaml, os

# 현재 파이썬 파일 위치 기준으로 상대 경로 설정
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)
CONFIG_PATH = os.path.join(BASE_DIR, "config")

class ConfigLoader:

    def load_file_info(self, filepath: str) -> list:
        filepath = os.path.join(CONFIG_PATH, filepath)
        if filepath.endswith('.json'):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        else:
            raise ValueError("지원하지 않는 파일 형식입니다.")
        
        return data
    
if __name__ == '__main__':
    print(CONFIG_PATH)
    cofigloader = ConfigLoader()
    print(cofigloader.load_file_info('items.yaml'))