# 初等数论
> 未央软-11  鲁睿


##  第1章 整数的唯一分解定理
### 1. Bezout定理

***

$$
\forall a, b \in \mathbb N^*,\:\exists m, n \in \mathbb Z,\:s.t.\:(a,b)=ma+nb\\
\forall a_1,...a_n\in \mathbb N^*,\exists x_1,...x_n \in \mathbb Z,\:s.t.(a_1,...a_n) = \sum_{i=1}^n a_ix_i
$$



### 2. 多项式表示素数可行吗？

$$
\forall x_0, 不存在整系数多项式f(x)=a_nx^n+...+a_1x+a_0\:(a_n\neq 0),\\s.t.\:x取所有\geq x_0 的整数时，f(x)都是整数.
$$

***

#### proof

$$
设f(x_0)=p是素数,对整数y,有f(x_0 + py)-f(x_0)=pM,即f(x_0+py)=p(M+1)\\
\because 最多有3n个y使得f(x_0+py) = 0,\:p,\:-p\\
\therefore 对充分大的y,\:f(x_0+py)不是素数.
$$

### 3. Mersenne数

$$
设p是素数，则形如2^p-1的数叫Mersenne数，记作M_p.
$$

***

#### 定理

> $设p是奇素数，q是M_p的一个素因子，则q=2kp+1$

#### proof

$$
引理：设a，b\in\mathbb N^*，s>1，则(s^a-1,s^b-1)=s^{(a,b)}-1\\
\because q是素数 \: \therefore q\mid2^{q-1}+1.\:又由于q\mid2^p-1，所以\\
q \mid (2^{q-1}-1,2^p-1)=2^{(p,q-1)}-1\\
\because q>1，\:\therefore(p,q-1)>1，\:\therefore p\mid q-1\\
又因为q-1是偶数，所以q=2kp+1.
$$

#### 应用

1. $可以看到，求偶完全数等价于Mersenne素数.是否有无穷多个p使得M_p是素数，是数论中尚未解决的难题.$

2. $Mersenne素数在一些应用学科（例如代数编码）中有应用.$



### 4. Fermat数

> $F_n=2^{2^n}+1$

#### 定理

> $\forall m \neq n, (F_m,F_n)=1.$

#### proof

$$
由归纳法可得，\forall n， F_n=F_{n-1}F_{n-2}...F_1F_0+2.\\
设d\mid F_m， \:d\mid F_n，则d\mid2.\:而d必为奇数，故d=1.
$$

#### 应用

$在数字信号处理中，用Fermat数给出的数论变换，可用来计算整数序列的卷积.$



### 5. 完全数

> $\displaystyle若n\in \mathbb N^*，\sigma(n) = \sum_{d\mid n}d = 2n，则d为完全数$

#### 定理

$n是偶完全数\iff n=2^{p-1}(2^p-1)，其中p和2^{p-1}都是素数.$

#### 难题

* 是否存在奇完全数？



### 6. 抽屉原理的应用

$$
设1\leq a_1 < a_2 <...<a_{n+1}\leq 2n，则\exists\:1\leq i < j \leq n+1，s.t.a_i \mid a_j.
$$

#### proof

$$
记a_i=2^{\lambda_i}b_i，\lambda_i\geq0，2\nmid b_i. 其中b_i<2n.\\
由于1到2n中恰有n个奇数，故b_1,...b_{n+1}中必有两个相同.\:设b_i=b_j，则有a_i\mid a_j.
$$



### 7. 素数分布

#### 命题1

> $证明：\forall n \geq3，n和n!之间必有素数.$

##### proof

$考虑n!-1.\:易知：1,2,...n均与之互素.故n!-1的素因子必然在n+1到n!-1之间.$



#### 命题2(unsolved)

>$证明：\forall n \in \mathbb N^*，n到2n之间必有素数.(Bertrand-Chebyshev)$



### 8. 带余除法定理

#### 命题1

> $取一组不为0的整数a_1,...a_n，记d=(a_1,a_2,...a_n).\:S=\{a_1x_1+...+a_nx_n|x_i\in\mathbb Z\}$
>
> $证明：S是所有d的倍数组成的集合.$

##### proof

$显然S\subset \{d的倍数\}.$
$所以只需证明\{d的倍数\}\subset S.进一步地，只需d\in S$
$取d^{'}是S中的最小正整数.则d^{'}\geq d. 假设d^{'}>d，则\exists a_i，d^{'} \nmid a_i.$
$\therefore \exists  q,r,\:s.t.a_i=d^{'}q+r,0<r<d^{'}.$
$于是r = a_i-d^{'}q\in S.又由于r<d^{'}，故与d^{'}的最小性矛盾！$
$\therefore S是所有d的倍数组成的集合.$
