import torch
from cka import cka_score, CKA_Minibatch

# 批大小，多少批，迭代次数

bs = 64
split = 20
n_epoch = 20

x1 = torch.rand(bs * split, 128)
x2 = 2 * x1 + torch.randn(x1.shape) * 1

cka_minibatch = CKA_Minibatch()
for epoch in range(n_epoch):
    perm = torch.randperm(bs*split) # 生成索引数据，随机打断的顺序，再进行赋值，可以打乱原来的
    x1 = x1[perm]
    x2 = x2[perm]
    for i in range(split):
        b1 = x1[i*bs:(i+1)*bs]
        b2 = x2[i*bs:(i+1)*bs]
        cka_minibatch.update(b1, b2)
    score = cka_minibatch.compute()
    print(f'Minibatch CKA at epoch {epoch}: {score.item()}')

print('Full CKA:', cka_score(x1, x2).item())



