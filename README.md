# Extractor v1.0 (heehcs@gmail.com)

* 주어진 한글파일에 대해서 맞춤법이 틀렸을 확률이 높은 줄을 추출하는 프로그램입니다.
* 단어단위, 음절단위, 음소단위 검색이 가능합니다.
* 사용법
  1. 입력파일 설정: extractor.py 소스 내부의 변수 f부분 수정
  2. 출력파일 설정: extractor.py 소스 내부의 변수 g부분 수정
  3. 음절 / 단어 검색: wrongwords.txt에 매칭하고자 하는 단어 입력
  4. 음소검색: 초성, 중성, 혹은 종성을 명시한후 if 조건 추가
  5. $ python extractor.py