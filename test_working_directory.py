import os

"""
파일 이름, 파일 경로
test.py를 생성하고 아래 코드를 실행하면 파일 이름과 경로가 출력됩니다. 
realpath()는 심볼릭 링크 등의 실제 경로를 찾아주며, 
abspath는 파일의 절대경로를 리턴합니다.
"""
print(__file__)
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))

"""
현재 파일의 디렉토리(폴더) 경로
아래 코드들은 파일이 있는 폴더의 경로를 구하는 2가지 방법입니다. 
os.getcwd()는 폴더 경로(current working directory)를 리턴합니다. 
os.path.dirname()는 파일의 폴더 경로를 리턴합니다.
"""
print(os.getcwd())
print(os.path.dirname(os.path.realpath(__file__)) )

"""
현재 디렉토리에 있는 파일 리스트
listdir()는 인자로 넘겨준 경로의 파일 리스트를 리턴합니다.
"""
print(os.listdir(os.getcwd()))

"""
작업 디렉토리 변경
chdir은 작업 디렉토리를 변경해줍니다.
"""
print("before: %s"%os.getcwd())
os.chdir("D:/workspace_python/")
print("after: %s"%os.getcwd())
os.chdir("D:\workspace_python\pyqt_erp_application")
print("after: %s"%os.getcwd())

"""
특정 경로에 대해 절대 경로 얻기
os.path.abspath(path)
"""
print(os.path.abspath("dbconnection/db_pool.py"))
print(os.path.abspath("db_pool.py"))

"""
경로 중 디렉토리명만 얻기
os.path.dir(path)
경로 중 파일명만 얻기
os.path.basename(path)
"""
print(os.path.dirname('D:\workspace_python\pyqt_erp_application\dbconnection/db_pool.py'))
print(os.path.basename('D:\workspace_python\pyqt_erp_application\dbconnection/db_pool.py'))

"""
경로 중 디렉토리명과 파일명 나누어 얻기
os.path.split(path) 디렉토리명, 파일명

파일 경로를 리스트로 얻기
os.path.sep(OS별 파일 경로 나는 문자)를 이용해 split합니다.

파일의 크기
os.path.getsize(path)
"""
dir, file = os.path.split('D:\workspace_python\pyqt_erp_application\dbconnection/db_pool.py')
print(dir, file, sep="\n")
print('D:\workspace_python\pyqt_erp_application\dbconnection\db_pool.py'.split(os.path.sep))
print(os.path.getsize("D:\workspace_python\pyqt_erp_application\dbconnection\db_pool.py"))
