import random
total_iterations = [True]*216000
p=0
q=0
r=0
s=0
for i in total_iterations:
    if random.random() < 0.026*0.1108:
        p+=1
    if random.random() < 0.026*0.3612:
        q+=1
    if random.random() < 0.026*0.1047:
        r+=1
    if random.random() < 0.026*0.4232:
        s+=1
print(p,q,r,s)
print("..........")


S = 2250

# vi, vj, vk, vl = 1656, 1940, 480, 508
vi = p/2#int(input("enter the volume and press enter"))
vj = q/4#int(input("enter the volume and press enter"))
vk = r/2#int(input("enter the volume and press enter"))
vl = s/4#int(input("enter the volume and press enter"))

ratio_i = vi/(S)
ratio_j = vj/(S)
ratio_k = vk/(S)
ratio_l = vl/(S)
print(ratio_i, ratio_j, ratio_k, ratio_l)

def round_up_to_5(n):
    return -(-n // 5) * 5
summation = ratio_i + ratio_j + ratio_k + ratio_l
Co =round_up_to_5(((1.5*12)+5)/(1-summation))
print('Cycle length')
print(Co, summation)
G = Co - 12
print(summation, Co, G)

gt_i = round_up_to_5(G*ratio_i)
gt_j = round_up_to_5(G*ratio_j)
gt_k = round_up_to_5(G*ratio_k)
gt_l = round_up_to_5(G*ratio_l)

print(gt_i, gt_j, gt_k, gt_l)


