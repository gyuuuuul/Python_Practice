#turtle 모듈을 불러오고 turtle 대신 t를 기호로 사용한다.
import turtle as t

#그림이 그려지는 속도를 설정한다. (0.4로)
t.speed(0.4)

# 버블 정렬과 turtle 속성을 지정해주는 함수
def bubble_sort(orig_lst): 
  lst = [ (x, "blue") for x in orig_lst ] #막대그래프 높이와 색깔을 묶어 lst에 저장
  n = len(lst)
  t.pensize(3) #선의 굵기를 3픽셀로 바꾼다.(원래 선은 너무 얇아서...)
  draw(lst, width) #밑에서 설정할 draw함수. 막대그래프를 그린다. width는 밑에서 설명하지만, 막대 너비.
  swapped = True  #swapped는 두 숫자를 교환한다는 의미.
  while swapped:  #swapped가 True일 때. 즉, 더 이상 교환할 것 없을 때까지.
    swapped = False  
    for i in range(n-1):  
        if lst[i+1][0] < lst[i][0]: #input에서 i+2번째 숫자가 i+1숫자보다 작을때. (i는 0부터)
            lst[i], lst[i+1] = lst[i+1], lst[i] #위의 두 숫자를 교환한다.
            lst[i] = (lst[i][0], "green")  #더 작은 막대그래프(앞으로 옮겨진)를 초록색으로
            swapped = True
            con = input() #아무거나 input하면 1회 시행을 한다.
            t.home() #화면은 그대로 두고 화살표 원위치로
            t.clear() #화면은 지우지만 화살표는 그대로 둔다.
            draw(lst,width) #1회 시행으로 순서가 달라진 막대그래프들을 그린다.
  newLst = [ x[0] for x in lst ] #정렬이 완료된 lst에서 숫자만을 빼서 새로운 리스트를 만든다.
  return newLst 

# 선택 정렬과 turtle 속성을 지정해주는 함수 (위와 동일한 건 생략)
def selection_sort(orig_lst):  
  lst = [ (x, "blue") for x in orig_lst ]
  n = len(lst)
  t.pensize(3)
  draw(lst, width)
  for i in range(n-1): #input에서 i+1번째 숫자 를 택하자.
    tmp = i
    for j in range(i+1, n): #그 숫자 뒤에 있는 모든 수들과 비교할 것이다.
      if lst[tmp][0] > lst[j][0]: #뒤에 있는 모든 수 중 제일 작은 'j'를 찾았다. tmp에 대입
        tmp = j
    lst[tmp], lst[i] = lst[i], lst[tmp] #제일 작은 막대와 i+1번째 막대 교환
    lst[tmp] = (lst[tmp][0], "green") # 두 막대를 둘다 초록색으로 칠하자.
    lst[i] = (lst[i][0], "green")
    con = input()
    t.home()
    t.clear()
    draw(lst,width)
    for j in range(n): #초록색으로 칠해진 막대를 다 파란색으로 만들자.
      lst[j] = (lst[j][0], "blue")
  newlst = [x[0] for x in lst]
  return newlst

 #turtle로 막대를 그리는 함수 
def draw(lst, width): 
  for x in lst:
    height = x[0] #막대 높이
    t.color(x[1]) #막대 색(파랑 or 초록)
    t.forward(width) #너비만큼 x축으로 전진
    t.left(90) #왼쪽으로 90도(이하생략)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.penup() #펜을 든다. 즉, 이동해도 선을 그리지 않는다,
    
    t.forward(width) #너비만큼 이동
    t.pendown() #펜을 내린다. 그리는 상태.

#input(),split()은 압력받은 값을 공백을 기준으로 분리하여 변수에 차례대로 저장하는 역할
#list(map(int, a))에서 map은 a의 모든 요소를 정수로 리스트에 집어넣어주는 역할
original_lst = list(map(int, input("정렬될 리스트 : ").split()))

width = 30 #막대그래프 너비를 30으로 하자.
sel = int(input("사용할 정렬 알고리즘\n1. 버블정렬\n2. 선택정렬\n입력 : ")) #버블정렬은 1번, 선택정렬은 2번으로 선택하자.
if sel==1:
  newLst = bubble_sort(original_lst)
elif sel==2:
  newLst = selection_sort(original_lst)

print ("정렬된 리스트 : ", newLst) #정렬이 완료된 리스트를 print하자.
