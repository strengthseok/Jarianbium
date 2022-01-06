import time
import sys
import pyautogui as au


# 자리안비움으로 사용
# 파라미터는 3개로 사용
# exe 파일 생성 원할시. 해당 폴더로 접근해서 명령어 실행 -> pyinstaller main.py -F(실행파일만 생기는 옵션)


def Jarianbium():
    # au.PAUSE = 1              # 코드당 1초의 간격으로 실행 파라미터
    au.FAILSAFE = False         # 오류실패 장치
    sec = 300                   # 체크간격 시간
    x_target, y_target = 1, 1   # 기본 좌표

    if len(sys.argv) == 2:
        sec = int(sys.argv[1])
    if len(sys.argv) == 4:
        sec = int(sys.argv[1])
        x_target = int(sys.argv[2])
        y_target = int(sys.argv[3])

    print("======= Parameters ========")
    print("Check time:" + str(sec))
    print("Click target x,y:" + str(x_target) + "," + str(y_target))
    print("===========================")
    print("Program start...")

    while True:
        x1, y1 = au.position()
        time.sleep(sec)
        x2, y2 = au.position()

        if x1 == x2 and y1 == y2:
            print("Click Tracking:" + time.strftime('%H시 %M분 %S초'))
            au.click(x=x_target, y=y_target, button='left', clicks=1)
            au.moveTo(x1, y1)
        else:
            pass


if __name__ == '__main__':
    Jarianbium()
