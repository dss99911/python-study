from setuptools import setup, find_packages

# deploy
#   - 개발모드 디플로이 : python setup.py develop
#   - env에 설치 : python setup.py install
#   - source distribution(zip source on dist foloder) : python setup.py sdist
#       - https://docs.python.org/3/distutils/sourcedist.html
#   - build distribution :
#       `python setup.py bdist` or `python setup.py bdist_egg` or `python setup.py bdist --formats=zip`
#       - compress source code
#       - make entrypoint shell script
#       - bdist_egg를 하면, 압축 풀었을 때, 절대 경로의 폴더가 안나오고, python파일이 바로 나옴. 이 걸 쓰는게 좋을듯.

setup_requires = [
    # setup.py 자신을 위해 필요한 패키지. ex) setuptools_git
]

install_requires = [
    # 버전 확인에는 pip freeze 명령을 사용하면 됩니다. 패키지 이름의 대소문자는 중요하지 않습니다.
    'markdown==2.3.1',
    'pyyaml==3.10',
    'pillow==2.1.0',
    'lxml==3.2.3',
    'beautifulsoup4==4.3.1',
]

# # 비공개 모듈 설치
# dependency_links = [
#     'git+https://github.com/django/django.git@stable/1.6.x#egg=Django-1.6b4',
# ]

setup(
    name='python-study',
    version='0.1',
    description='python study',
    author='hyun',
    author_email='dss99911@gmail.com',
    packages=find_packages(exclude=['test', 'study', 'pip']),  # find_packages() 함수는 폴더를 뒤져서 패키지들의 목록을 만들어 줍니다
    install_requires=install_requires,
    setup_requires=setup_requires,
    # dependency_links=dependency_links,
    # scripts=['manage.py'],
    entry_points={  # 콘솔 스크립트 설치
        'console_scripts': [
            'publish = flowdas.books.script:main',
            'scan = flowdas.books.script:main',
            'update = flowdas.books.script:main',
        ],
    },
)
