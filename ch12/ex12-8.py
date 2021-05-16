# 12.8 간단한 병렬 프로그램 수행

# findrobots.py

import gzip
import io
import glob

def find_robots(filename):
    '''
    단일 로그 파일의 robots.txt가 접근한 모든 호스트를 찾는다.
    '''
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f,encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fileds[0])
    return robots

def find_all_robots(logdir):
    '''
    전체 파일 시퀀스와 모든 호스트를 찾는다.
    '''
    files = glob.glob(logdir+'/*.log.gz')
    all_robots = set()
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots

if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)


# findrobots.py

import gzip
import io
import glob
from concurrent import futures

def find_robots(filename):
    '''
    단일 로그 파일의 robots.txt가 접근한 모든 호스트를 찾는다.
    '''
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f,encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fileds[0])
    return robots

def find_all_robots(logdir):
    '''
    전체 파일 시퀀스와 모든 호스트를 찾는다.
    '''
    files = glob.glob(logdir+'/*.log.gz')
    all_robots = set()
    with futures.ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots

if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)



# 토론

from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor() as pool:
    ...
    do work in parallel using pool
    ...


# 많은 작업을 하는 함수
def work(x):
    ...
    return result

# 병렬화하지 않은 코드
results = map(work, data)

# 병렬화 구현
with ProcessPoolExecutor() as pool:
    results = pool.map(work, data)


# 임의의 함수
def work(x):
    ...
    return result

with ProcessPoolExecutor() as pool:
    ...
    # 풀에 작업을 등록하는 예제
    future_result = pool.submit(work, arg)

    # 결과 얻기(종료될 때까지 실행을 멈춘다.)
    r = future_result.result()
    ...


def when_done(r):
    print('Got:', r.result())

with ProcessPoolExecutor() as pool:
    future_result = pool.submit(work, arg)
    future_result.add_done_callback(when_done)
