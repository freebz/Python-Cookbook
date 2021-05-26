# 13.6 외부 명령을 실행하고 결과 얻기

import subprocess
out_bytes = subprocess.check_output(['netstat','-a'])


out_text = out_bytes.decode('utf-8')


try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output       # 에러 이전에 생성된 결과
    code      = e.returncode   # 반환 코드


out_bytes = subprocess.check_output(['cmd','arg1','arg2'],
                                    stderr=subprocess.STDOUT)


try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'], timeout=5)
except subprocess.TimeoutExpired as e:
    ...


out_bytes = subprocess.check_output('grep python | wc > out', shell=True)



# 토론

import subprocess

# 전송할 텍스트
text = b'''
hello world
this is a test
boodbye
'''

# 파이프와 함께 명령 실행
p = subprocess.Popen(['wc'],
          stdout = subprocess.PIPE,
          stdin = subprocess.PIPE)

# 데이터를 전송하고 결과 얻기
stdout, stderr = p.communicate(text)

# 텍스트로 해석하기 위한 디코딩
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')
