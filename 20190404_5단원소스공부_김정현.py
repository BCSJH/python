#!/usr/bin/env python
# coding: utf-8

# In[1]:


#5-20
a= 5 #변수 선언
if(a>3):#a가 3보다 크면
    print("Hello World")
    print("Hello TEAMLAB")
if(a>4):#a가 4보다 크면
    print("Hello World")
    print("Hello TEAMLAB")
#여기까지 실행됨
    
if(a>5):#a가 5보다 크면
    print("Hello World")
    print("Hello TEAMLAB")


# In[2]:


#5-21
def print_hello():
    print("Hello World")
    print("Hello TEAMLAB")
a=5
if(a>3):
    print_hello()
if(a>4):
    print_hello()
#여기까지 출력됨    
    
if(a>5):
    print_hello()


# In[4]:


#5-22
import math#math를 사용하겠다.
a=1; b=-2; c=1#변수 선언

print((-b + math.sqrt(b**2 - (4*a*c)) )/(2*a))#sqrt를 사용해 함수로 계산하기
print((-b - math.sqrt(b**2 - (4*a*c)) )/(2*a))


# In[6]:


#5-23
import math#math 사용

def get_result_quadratic_equation(a,b,c):#함수를 만들어 return 하기
    values = []#배열
    values.append((-b + math.sqrt(b**2 - (4*a*c)) )/(2*a))
    values.append((-b - math.sqrt(b**2 - (4*a*c)) )/(2*a))
    return values#반환

print(get_result_quadratic_equation(1,-2,1))#값 계산 출력


# In[ ]:





# In[8]:


#5-1
def calculate_rectangle_area(x,y):
    return x*y

rectangle_x=10
rectangle_y=20
print("사각형 x의 길이 : ", rectangle_x)
print("사각형 y의 길이 : ", rectangle_y)

#넓이 구하는 함수 호출
print("사각형의 넓이",calculate_rectangle_area(rectangle_x,rectangle_y))


# In[10]:


#5-2
#각각의 함수 적기
def f(x):
    return 2*x+7
def g(x):
    return x**2#제곱

x=2#x값 선언
print(f(x) + g(x) + f(g(x))+g(f(x)))#출력


# In[45]:


#5-4
#넓이 구하는 함수들
def a_rectangle_area():
    print(5*7)
    
def b_rectangle_area(x,y):
    print(x*y)
    
def c_rectangle_area():
    print(5*7)
    
def d_rectangle_area(x,y):
    print(x*y)
    
a_rectangle_area()
b_rectangle_area(5,7)
print(c_rectangle_area())#35 출력
print(d_rectangle_area(5,7))#대입해서 값 출력

#none값은 왜나오는 건지 모르겠음


# In[12]:


#5-5
#함수 만들기
def f(x):
    y=x
    x=5#x값 바꾸기
    return y*x#반환

x=3#x값 선언
print(f(x))
print(x)


# In[13]:


#5-6
def spam(eggs):
    eggs.append(1)#기존 eggs(ham)에 aggs라는 배열에 1추가
    
    eggs=[2,3]#새로운 객체 생성
    
ham = [0]
spam(ham)
print(ham)


# In[16]:


#5-7
def test(t):
    print(x)
    t=20
    print("In Function:",t)
    
x=10
test(x)
print("In Main:",x)
print("In Main:",t)
#t는 test함수에 있는 변수라서 지역변수임
#그래서 t를 찾을 수 없음


# In[19]:


#5-8
#함수
def f():
    s="I love London!"
    print(s)
    
s="I love Paris!"
f() #함수를 먼저 호출했기 때문에 함수속에서 London 출력
print(s) #함수는 전역변수기 때문에 영향을 미치지 않음


# In[20]:


#5-9
def f():
    global s
    s="I love London!"
    print(s)
    
s="I love Paris"
f()
print(s)#global은 함수 내에서 사용가능하기 때문에 s에 다 영향을 미침


# In[21]:


#5-11
def calculate(x,y):
    total = x+y#값 할당되어 함수 안 total은 지역변수
    print("In Function")
    print("a:",str(a),"b:",str(b),"a+b",str(a+b),"total",str(total))
    return total

a=5#지역변수
b=7
total=0 #전역변수
print("In Program -1")
print("a:",str(a),"b:",str(b),"a+b",str(a+b))

sum = calculate(a,b)
print("After Calculation")
print("Total:",str(total),"sum:",str(sum))#지역 변수는 전역 변수에 영향을 주지 않음


# In[23]:


#5-12
def factorial(n):#함수 선언
    if n==1:
        return 1
    else:
        return n *factorial(n-1)
    #1이 아닐때까지 함수 속 함수를 사용해 값 계산한 것을 불러와서 곱한 것을 출력
    
    
print(factorial(int(input("Input Number for Factorial Calculation:"))))
#사용사로부터 입력을 받아 factorial 함수 n의 변수로 값을 넣어줌


# In[24]:


#5-12
#함수 선언
def print_something(my_name,your_name):
    print("Hello{0}, My name is {1}".format(your_name,my_name))
    
print_something("Sungchul","TEAMLAB")
print_something(your_name="TEAMLAB",my_name="Sungchul")
#함수의 변수에 값을 딱딱 지정해서 해줘도 결과는 같은


# In[25]:


#5-13
def print_something_2(my_name,your_name="TEAMLAB"):
    print("Hello {0},My name is {1}".format(your_name,my_name))
    
print_something_2("Sungchul","TEAMLAB")
#이미 your_name에 값이 지정되어 있지만 그것을 무시하고 넣어줄수있고
print_something_2("Sungchul")
#이미 your_name이 TEAMLAB이라고 지정되어있어서 한가지만 써도 상관없음


# In[51]:


def asterisk_test(a, b, *args):
    return a + b + sum(args)

print(asterisk_test(1, 2, 3, 4, 5))
#1,2는 제대로 들어가고 나머지들은 전부다 args에 넣어주는것임 (*args가 가변인수)


#이 부분이 오류가 나서 다른 곳에서 실행했습니다.
#다른 컴퓨터에서는 됩니다.
#왜 오류가 나는지 모르겠습니다.
#어쨋든 소스상 문제는 없습니다...


# In[48]:


#5-15
def asterisk_test(a, b, *args):
    return args

print(asterisk_test(1, 2, 3, 4, 5)) 
#*args가 가변인수


# In[37]:


#5-16
def asterisk_test_2(*args):
    x,y,z = args#변수에 각각의 값이 들어감
    return x,y,z

#언패킹 됨
print(asterisk_test_2(3,4,5))#가변 인수의 개수를 정확히 알고 있을 경우로


# In[40]:


#5-17
def asterisk_test_2(*args):
    x,y,*z = args#변수에 각각의 값이 들어감 z는 가변인수라서 나머지 값이 다 들어감
    return x,y,z

#언패킹 됨
print(asterisk_test_2(3,4,5,10,20))#가변 인수의 개수가 다를 경우


# In[42]:


#5-18
def kwargs_test(**kwargs):#kwargs는 키워드 가변 인수
    print(kwargs)
    print("First value is {first}".format(**kwargs))
    print("second value is {second}".format(**kwargs))
    print("third value is {third}".format(**kwargs))

    #**를 두개쓰면 개별 변수로 들어감
kwargs_test(first=3,second=4,third=5)


# In[44]:


#5-19
lL0O = "1234"
for i in 10:
    print("Hello")
#for문에서 오류 뜸


# In[ ]:




