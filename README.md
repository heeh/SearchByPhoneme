# Extractor v1.0 (한국어 검색기반 문자열 추출기)

* 한국어 음소/음절/단어를 포함하는  문자열 추출
* 단어단위, 음절단위, 음소단위 검색이 가능합니다.
* 사용법  
  $ python extractor.py

* 튜토리얼
  1. 입력파일 설정: extractor.py 소스 내부의 변수 f부분 수정
  2. 출력파일 설정: extractor.py 소스 내부의 변수 g부분 수정
  3. 음소검색: 초성, 중성, 혹은 종성을 명시한후 if 조건 추가. 문의사항은 이메일로 부탁드려요.
  4. 음절 / 단어 검색: wrongwords.txt에 매칭하고자 하는 단어 입력
  5. python extractor.py 실행

* 예시
  * 음소검색 기반 추출1: 종성으로 'ㅅ'을 지니는 모든 라인 추출. (햇, 겟, 갓네, )
  * 음소검색 기반 추출2: 초성과 중성은 'ㅉ'와 'ㅣ' 이고 종성은 모든 음소가능한 라인 추출(찍, 찐, 찜, ...)
  * 음절검색 기반 추출: '쟎'이 포함된 모든 라인 추출(했쟎아, 있쟎아, ...)
  * 단어검색 기반 추출: "조으" 로 시작되는 모든 라인 추출(조으냐, 조으네, ...)

* 파일설명
  * extractor.py: 추출기 파일
  * wrongwords.txt: 검색하고자 하는 음절 혹은 단어 모음(라인별로 구별)
  * foo.txt: 입력파일 예시
  * foo.txt.fix: 출력파일 예시
  * unicodeSort.sh: wrongwords.txt 정렬(선택사항)



# Extractor v1.0  
## Korean string extractor(By searching phonemes, syllables, or words)

* Extracts korean words which contain phonemes(onset, nucleus, or coda), syllables, or words.
* Usage
  $ python extractor.py

* Tutorial
  1. Input file: Modify the variable 'f' in extractor.py.
  2. Output file: Modify the variable 'g' in extractor.py.
  3. Phoneme-based Search: You have to modify extractor.py. E-mail me if you are lost.
  4. Syllable or Word based search: Add words to wrongwords.txt
  5. Execute python extractor.py

* 예시
  * Phoneme-based Search 1: Retrieve whole lines which contain coda 'ㅅ'. (햇, 겟, 갓네, )
  * Phoneme-based Search 2: Retrieve whole lines which contain onset'ㅉ' and nucleus'ㅣ'. (찍, 찐, 찜, ...)
  * Syllable-based Search : Extract whole lines which contain '쟎'. (했쟎아, 있쟎아, ...)
  * Word-based Search     : Extract whole lines which start with "조으". (조으냐, 조으네, ...)

* Files
  * extractor.py: A file contains main function
  * wrongwords.txt: A files contains syllables or words to be searched.(By line)
  * foo.txt: input example
  * foo.txt.fix: output example
  * unicodeSort.sh: A file which sorts wrongwords.txt(Not so important)
