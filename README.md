[pyenv로 파이썬 버전 관리하기 용이합니다 :) 이건 개개인 선택하여 설치하세요~~]

현재 프로젝트에서 필요한 패키지는 모두 설치하고 업데이트하여 진행해주세요!

source .venv/bin/activate

pip3 install --upgrade pip

pip3 install -r requirements.txt

위에 있는 모든 명령어 진행하여 가상환경 접속 후 코드 짜주시면 됩니다!! 
프로젝트에 필요한 폴더 및 파이썬파일의 경우 만들어 두었습니다! 

https://www.notion.so/Flask-mini-project-Day1-177caf5650aa802081f0d97fb7c69c2a

위 접속하시어 확인 부탁드립니다 :) 잘해보아용~!

<h2>설문조사 주제 : '흑백요리사' 설문조사!</h2> 

<!-- 1. 가장 먹어보고싶은 쉐프 top5 -->
<p><strong>1. 가장 먹어보고싶은 쉐프 top5</strong></p>
<ul>
    <li>쉐프 1</li>
    <li>쉐프 2</li>
    <li>쉐프 3</li>
    <li>쉐프 4</li>
    <li>쉐프 5</li>
</ul>

<!-- 2. 가장 먹어보고싶은 요리 top5 -->
<p><strong>2. 가장 먹어보고싶은 요리 top5</strong></p>
<ul>
    <li>요리 1</li>
    <li>요리 2</li>
    <li>요리 3</li>
    <li>요리 4</li>
    <li>요리 5</li>
</ul>

<!-- 3. 가장 아쉬웠던 순간 top3 -->
<p><strong>3. 가장 아쉬웠던 순간 top3</strong></p>
<ul>
    <li>상황 1</li>
    <li>상황 2</li>
    <li>상황 3</li>
</ul>

<!-- 4. 다음 시즌에 나오면 좋은 쉐프 [객관식] -->
<p><strong>4. 다음 시즌에 나오면 좋은 쉐프</strong> (객관식)</p>
<input type="checkbox" id="chef1" name="chef" value="chef1">
<label for="chef1">쉐프 A</label><br>
<input type="checkbox" id="chef2" name="chef" value="chef2">
<label for="chef2">쉐프 B</label><br>
<input type="checkbox" id="chef3" name="chef" value="chef3">
<label for="chef3">쉐프 C</label><br>

<!-- 5. 개선사항 [주관식] -->
<p><strong>5. 개선사항</strong> (주관식)</p>
<textarea name="improvements" rows="4" cols="50"></textarea>