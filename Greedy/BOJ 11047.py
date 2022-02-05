
N,K = map(int, input().split()) # N, K 값을 입력 받는다. 

coinList = [] # N개의 동전을 저장할 리스트
coinNum = 0 # 필요한 동전 개수 
cnt = 0 # K를 동전의 가치로 나눈 몫 

for i in range(N) :
    coin = int(input())
    coinList.append(coin)
    
coinList.reverse() # 입력 받은 동전 리스트를 역차적으로 배열 

for i in coinList :
    cnt = K // i
    if cnt >= 1 : 
        coinNum += cnt 
        K = K - cnt * i 


print(coinNum)
    