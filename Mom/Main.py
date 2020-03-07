def find_median_five(L):
	S=[]
	S=L
	A,M,B=[],[],[]#small, middle, large
	p=S[0]
	
	for a in L:
		if a<p:A.append(a)
		elif a==p:M.append(a)
		else:B.append(a)
	if len(A)>=len(L)/2:return find_median_five(A)
	elif len(A)+len(M)<len(L)/2:return find_median_five(B)
	else: return p
	
def MoM(L, k): # L의 값 중에서 k번째로 작은 수 리턴
	if len(L) == 1: # no more recursion
		return L[0]
	i = 0
	A, B, M, medians = [], [], [], []
	while i < len(L) and i+4 <= len(L):
		medians.append(find_median_five(L[i: i+5]))
		i=i+5
	if i < len(L) and i+4 >= len(L):
		medians.append(find_median_five(L[i:]))
	
	mom = MoM(medians,len(medians)/2)
	for v in L:
		if v < mom: A.append(v)
		elif v > mom: B.append(v)
		else: M.append(v)

	if len(A)>=k: return MoM(A,k)
	elif len(A)+len(M)<k: return MoM(B,k-len(A)-len(M))
	else: return mom

n,k=input().split()
n=int(n)
k=int(k)# n과 k를 입력의 첫 줄에서 읽어들인다
L=input().split()

#현재 Atom에서는 input()이 작동하지 않으므로 직접 n,k,L의 값을 입력해야만 정상 작동한다.

for i in range(len(L)):
	L[i]=int(L[i])# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
print(MoM(L, k))
