현재 제 가상환경의 파이썬 버전은 3.13.1 입니다.
추가적으로 버전 업그레이드를 해야하나 궁금했는데
개개인 가상환경으로 구축해서 쓰기 때문에 따로 업그레이드는 필요 없습니다!!
혹시 모를 충돌에 대비해 적어두겠습니다!

파이썬 버전
김이준 - 3.13.1
박현기 -
정이학 - 

[pyenv로 파이썬 버전 관리하기 용이합니다 :) 이건 개개인 선택하여 설치하세요~~]

현재 프로젝트에서 필요한 패키지는 모두 설치하고 업데이트하여 진행해주세요!

source .venv/bin/activate

pip3 install --upgrade pip

pip3 install -r requirements.txt

touch run.py config.py wsgi.py form.conf

mkdir app && cd app

touch __init__.py models.py routes.py
mkdir views && cd views

touch answers.py choices.py images.py questions.py users.py

위에 있는 모든 명령어 진행하여 가상환경 접속 후 코드 짜주시면 됩니다!! 


