#매주 1회 작성해야하는 보고서가 있따 보고서는 항상 아래와 같다
#- n주차 주간보고 -
#부서 :
#이름 :
#업무요약 :
#1주차부터 50주차까지의 파일을 만들어라
#파일명은 1주차.txt
for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding = "utf8") as repo:
        repo.write("- {0}주차 주간보고 -\n부서:\n이름 :\n업무요약 :".format(i))
