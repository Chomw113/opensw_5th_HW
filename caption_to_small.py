inStr, outStr = "", ""
ch = ""
count, i = 0, 0

if __name__=="__main__":
    inStr = input("문자열을 입력하세요 : ")
    count = len(inStr)

    for i in range(0, count):
        ch = inStr[i]

##2019038019 조민우##
        
        if(ord(ch) >= ord("A") and ord(ch) <= ord("Z")):
            newCh = ch.lower()
            
##대문자를 소문자로 바꿔주는 명령
            
        elif(ord(ch) >= ord("a") and ord(ch) <= ord("z")):
            newCh = ch.upper()

##소문자를 대문자로 바꿔주는 명령

        else :
            newCh = ch

##영어 외에는 그대로 출력
            
        outStr += newCh

    print("대소문자 변환결과 --> %s" %outStr)
    
