from googletrans import Translator, LANGUAGES
import datetime

def translate_english_to_korean():
    # Translator 객체 생성
    translator = Translator()
    
    # 번역할 영어 문서 파일 경로
    file_path = r'C:\Users\highk\pypy50\9. 영어로된 문서를 한글로 자동번역\영어파일.txt'
    
    try:
        # 파일 읽기
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # 영어에서 한국어로 번역 실행
        translated = translator.translate(text, dest='ko')
        
        # 번역 결과 출력
        print(f"번역 결과: {translated.text}")
        
        # 파일 저장 경로 및 이름 설정 (현재 디렉토리, 파일명에 생성 날짜 추가)
        current_date = datetime.datetime.now().strftime("%Y%m%d")
        new_file_path = f'C:\\Users\\highk\\pypy50\\9. 영어로된 문서를 한글로 자동번역\\번역결과_{current_date}.txt'
        
        # 번역된 텍스트 파일로 저장
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            new_file.write(translated.text)
            print(f"번역된 결과가 다음 경로에 저장되었습니다: {new_file_path}")
    except ValueError as ve:
        print("올바르지 않은 언어 코드가 사용되었습니다. 사용 가능한 언어 목록을 확인하세요.")
        print(f"사용 가능한 언어 목록: {LANGUAGES}")
    except Exception as e:
        print(f"번역 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    translate_english_to_korean()
