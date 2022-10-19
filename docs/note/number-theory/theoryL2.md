# 初等数论
> 未央软-11  鲁睿


## 第2章 同余式



### 1. 完全剩余系

#### 定理1

$$
设m_1 > 0，m_2>0，(m_1,m_2)=1，而x_1，x_2分别通过模数m_1，m_2的完全剩余系，\\则m_2x_1+m_1x_2通过模数m_1m_2的完全剩余系.
$$

#### 定理2（1948，Chowla）

$$
设n>2，并设a_1,\ldots ,a_n和b_1,\ldots,b_n分别是模数n的一组完全剩余系,\\则a_1b_1,\ldots,a_nb_n不是模数n的一组完全剩余系.
$$

#### 模数m剩余类环（抽象代数）

$模数m的剩余类之间可以定义运算.在任给的两个模数m的剩余类C_i,C_j中各取一代表i,j.$

$而令i+j（或i\cdot j）所在的剩余类为C_{<i+j>}（或C_{<i\cdot j>}），则C_{<i+j>}仅与C_i,C_j有关，$

$而与所选择的代表无关，故可定义C_i,C_j之间的加法和乘法为：$

$C_i\bigoplus C_j=C_{<i+j>}，C_i\bigodot C_j=C_{<i\cdot j>}.$

$C_0,\ldots,C_{m-1}对上述加法和乘法成环，叫做模数m剩余类环$.



### 2. 同余类（群，环，域）

$设m\in **\mathbb Z**_{>0}，a\in \mathbb Z，记\overline a = \{x\in \mathbb Z | x\equiv a\pmod m\}称为模m的一个同余类.$

$若(a,m)=1，则称\overline a为模m的一个缩同余类.欧拉函数\varphi(m)即表示缩同余类的个数.$

$\displaystyle \mathbb Z=\overline 0 \bigcup\overline1\bigcup\cdots\bigcup\overline{m-1}$



##### 基本性质

$a,b,c\in \mathbb Z_{m}$

1. $\overline a + \overline b = \overline b + \overline a$

2. $(\overline a + \overline b ) + \overline c = \overline a + (\overline b + \overline c)$
3. （零元）$\overline 0 + \overline a = \overline a $
4. （逆元）$\overline a + \overline{-a} = \overline 0$（这定义了减法）
5. $\overline a \cdot\overline b = \overline b \cdot \overline a$
6. $(\overline a \cdot \overline b)\cdot \overline c=\overline a\cdot(\overline b \cdot \overline c)$
7. （幺元）$\overline 1 \cdot \overline a = \overline a$
8. $(\overline a +\overline b)\cdot \overline c=\overline a\cdot \overline c + \overline b \cdot \overline c$

在缩同余类中，可以定义除法：

定义$Z_m^*$为所有缩同余类的集合.	则$Z_m^*$对乘法封闭(why?)，且每个元素均可逆，因此$Z_m^*$是乘法交换群.

$(a,m)=1\Leftrightarrow \exists \overline b, \overline a \cdot \overline b = \overline 1$

这是因为：$\exists x, ax+my=1.$ 故$ax\equiv 1\pmod m$

* 如果有2-4，则称为**群**. 如果有1，则称为**交换群**.

* 如果有1-4，6-8，则称为**环**. 如果有5，则称为**交换环**.

* **域**为交换除环.（每个**非零元**都有乘法逆元的交换环）

##### 推广性质

1. （消去律）（由于乘法逆元的存在）$若\overline a\cdot\overline c = \overline b \cdot \overline c，\overline c\in \mathbb Z_m^*，则\overline a = \overline b.$

2. $若m=p为素数，\overline a \cdot \overline b =0，则\overline a = 0或\overline b =0.$

3. (Wilson定理) $(p-1)!\equiv 1\pmod p$

   $假设p\neq 2，\: \overline a\in\{\overline 1, \cdots, \overline {p-1}\}，则\overline{a^{-1}}\in\{\overline 1, \cdots, \overline {p-1}\}$

   $易知：\overline a \neq \overline b\Leftrightarrow \overline{a^{-1}}\neq\overline{b^{-1}}$

   $若\overline a =\overline{a^{-1}}，则\overline{a^2}=\overline 1.$

   $因此，(\overline a+\overline1 )(\overline a-\overline1)=\overline 0.$

   $因此\overline a = \overline 1 或\overline a = \overline {-1}.$

   $\displaystyle因此\overline 1\cdots\overline{p-1}=\overline1\cdot\overline{-1}\cdot\large\prod_{i=1}^{\frac{p-3}{2}}(\overline{a_i}\cdot\overline{a_{i}^{-1}})=\overline{-1}.$


4. 环$Z_m$中元素$\bar a$可逆当且仅当$\bar a$是$Z$的模$m$缩同余类，即$(a,m)=1$.
5. $Z_m$是域当且仅当$m$是素数.





### 3. 缩系

#### 欧拉函数$\varphi(n)$

##### 定义

>  $\varphi(n)定义为0,1,\ldots,n-1中与n互素的数的个数.$

##### 性质

* $设m>1，(a,m)=1，则a^{\varphi(m)}\equiv 1\pmod m$
* $若(m_1,m_2)=1，则\varphi(m_1m_2)=\varphi(m_1)\varphi(m_2).$
* $对一般的m,n,设(m,n)=d,则有\varphi(mn)=\varphi(m)\varphi(n)\frac{d}{\varphi(d)}$
* $若a\mid b,则\varphi(a)\mid \varphi(b)$
* $设n的标准分解n=p_1^{\alpha1}...p_k^{\alpha k}，则\varphi(n)=n(1-\frac{1}{p_1})...(1-\frac{1}{p_k}).$
* $\displaystyle设n\geq1，则有\sum_{d \mid n}\varphi(d)=n.$

##### 莱梅猜想

$不存在合数n,使得\varphi(n)\mid n-1.$

##### 性质

若$\{r_1,\cdots,r_{\varphi(m)}\}$是模$m$的缩系，则$\{r_1^{-1},\cdots,r_{\varphi(m)}^{-1}\}$也是模$m$的缩系.

##### 推广

（$Fermat$小定理：$a^p\equiv a\pmod p$.）

因此，有限域$Z_p$中的$p$个元素均是方程$x^p-x=0$的解.（这里的$x$是指一个同余类）

应用下面的$Lagrange$定理，我们有：$x^p-x=x(x-1)\cdots(x-(p-1))$，

比较$x$的系数可得：$-1\equiv(p-1)!\pmod p$，此即$Wilson$定理.



### 4. 一次同余式

#### 定义

设$f(x)=a_nx^n+\cdots+a_1x+a_0$，其中$n>0,a_i(i=0,1,\cdots,n)$是整数，又设$m>0$，则

$f(x)\equiv 0\pmod m$叫做模数$m$的同余式.若$\langle a_n\rangle_m\ne 0$，则$n$叫做该同余式的系数.

若$x_0$满足$f(x_0)\equiv 0\pmod m$，则$x\equiv x_0\pmod m$叫做同余式的解.不同的解是指互不同余的解.

#### 定理

1. $设(a,m)=1,m>0,则同余式ax\equiv b(mod\: m)恰有一个解：x\equiv ba^{\varphi(m)-1}(mod\: m)$

2. $设(a,m)=d,m>0,则同余式ax\equiv b(mod\:m)有解的充要条件是d\mid b.$

3. $若d\mid b,则上式恰有d个解.$ 

4. 推广到一般情形：

   $设k\geq 1,则同余式a_1x_1+\cdots+a_kx_k+b\equiv 0(mod\: m)有解的充要条件是(a_1,\cdots,a_k,m)\mid b$



### 5. 模数是素数的同余式

#### Lagrange定理

##### 定义

> $设p是一个素数，f(x)=a_nx^n+\ldots+a_1x+a_0，n>0，a_n\neq 0(mod\:p)是一个整系数多项式.
> $$则同余式f(x)\equiv 0(mod\:p)最多有n个解.$

> 事实上，$f(x)=0$在**任何域中**都至多有$n$个解.

##### 证明

我们断言：在有限域$Z_p$中考虑上述方程，若$f(x)=0$有一个根$x_0$，则必然有：**$f(x)=(x-x_0)h(x)$**.

> 这个引理很像我们当初证明代数学基本定理时的方法（实际上复数域也是域，方法都是可借鉴的）

这是因为：设$x_0$是$f(x)=a_nx^n+\cdots+a_1x+a_0=0$的一个根，则：

考虑$g(x)=f(x+x_0)=a_n(x+x_0)^n+\cdots+a_1(x+x_0)+a_0=a_nx^n+a_{n-1}'x^{n-1}+\cdots+a_1'x+a_0'$.

其中$a_0'=a_nx_0^n+\cdots+a_1x_0+a_0=f(a_0)=0$.	

因此，$g(x)=a_nx^n+\cdots+a_1x=x(a_nx^{n-1}+\cdots+a_1)$.反代回$f(x)$，我们有：

$f(x)=(x-x_0)h(x)$.	由此可证明$Lagrange$定理.

##### 推论

若该同余式解的个数大于n，那么$p\mid a_i，i=0,1,\ldots,n$

##### 应用

> $对于任意素数p，多项式f(x)=(x-1)(x-2)\cdots (x-p+1)-x^{p-1}+1的所有系数被p整除.$

###### 证明

$设g(x)=(x-1)(x-2)\cdots(x-p+1)，则1,\cdots,p-1是同余式g(x)\equiv0(mod\:p)的p-1个解.$
$由Fermat小定理，1,\cdots,p-1也是同余式h(x)=x^{p-1}-1\equiv0(mod\:p)的p-1个解.$
$故同余式f(x)\equiv g(x)-h(x)(mod\:p)有p-1个解,而f(x)是p-2次的多项式，因此其所有系数被p整除.$

> $注意到f(x)的常数项是(p-1)!+1，因此我们证明了Wilson定理.$



#### Wolstenholme定理

$在上面构造的g(x)中，g(x)=x^{p-1}-s_1x^{p-2}+s_2x^{p-3}+\cdots-s_{p-2}x+(p-1)!(*)\\$

$\displaystyle其中s_j(j=1,2,\cdots,p-2)是整数，且s_{p-2}=\sum_{k=1}^{p-1}\frac{(p-1)!}{k}.$

$由Lagrange定理知，p\mid s_j(j=1,2,\cdots,p-2)，在(*)中令x=p，$

$由于g(p)=(p-1)!，故p^{p-1}-s_1p^{p-2}+\cdots-ps_{p-2}=0.$

$因为p>3，对上式取模p^3得：ps_{p-2}\equiv 0(mod\:p^3).于是s_{p-2}\equiv0(mod\:p^2)$.

等价表述：$\displaystyle\sum_{k=1}^{p-1}\frac{1}{k}\equiv0(mod\:p).$

### 6. 孙子剩余定理及其应用

$考察同余方程组x\equiv b_1(mod\: m_1),\cdots,x\equiv b_k(mod\: m_k),其中m_1,\cdots,m_k是k个两两互质的正整数.$

设$m=m_1\cdots m_k,M_i=\frac{m}{m_i}$,则同余方程组恰有**唯一解**$x\equiv b_1\cdot M_1^{'}M_1+\cdots+b_k\cdot M_k^{'}M_k(mod\: m)$

$其中M_i^{'}M_i\equiv 1(mod\:m_i)(i=1,\cdots,k)$.

> 注：我们并不要求每个$m_i$都是<u>素数</u>.

#### 证明

证明是构造性的，需要用到“**叠加原理**”.

对每个$1\leq i\leq k$，考虑同余方程组

$\begin{cases}x\equiv 1\pmod {m_i},\\[2ex]x\equiv 0\pmod {m_j},(j\neq i)\end{cases}$

令$M_i=\dfrac{m_1\cdots m_k}{m_i}$，则$x$必然是$M_i$的倍数.	因此上面的同余方程组归结于：$M_iy\equiv 1\pmod {m_i}$.

由$(M_i,m_i)=1$可知，该方程必有一解$y=M_i'$.	即$x=M_iM_i'$.

现在考虑所有$M_iM_i'$的一个线性组合$A=b_1M_1M_1'+\cdots+b_kM_kM_k'$，易知$A$是方程组的一个解.

下面证明唯一性.	设令有一解$B$，则$A\equiv B\pmod {m_i},\forall i$.

因此$A\equiv B\pmod {m_1\cdots m_k}$. 故唯一性得证.

#### 性质

$若m_1,m_2,\cdots,m_k是k个两两互素的正整数,m=m_1\cdots m_k,则同余式f(x)\equiv 0(mod\:m)有解的充要条件是$

$同余式f(x)\equiv 0(mod\:m_i)(i=1,\cdots,k)的每一个有解.并且，若用T_i表示f(x)\equiv 0(mod\: m_i)的解数，T表示$

$f(x)\equiv 0(mod\:m)的解数,则T=T_1T_2\cdots T_k.$



### 7. 模数是素数幂的同余式(to be continued)



### 8. 整数的剩余表示

#### 定义

$设m_1>0,\cdots,m_k>0,(m_i,m_j)=1,0<i<j\leq k,一个整数x对于模数m_1,\cdots,m_k$

$的剩余表示是指序列(\langle x\rangle_{m_1},\langle x\rangle_{m_2},\cdots,\langle x\rangle_{m_k})，记作x\leftrightarrow (\langle x\rangle_{m_1},\langle x\rangle_{m_2},\cdots,\langle x\rangle_{m_k})$

#### 定理

$设m_1>0,\cdots,m_k>0,(m_i,m_j)=1,0<i<j\leq k.两个整数x,x'对于模数$

$m_1,\cdots,m_k的剩余表示相同的充分必要条件是x\equiv x'(mod\:M)，这里M=m_1\cdots m_k$



$设Z_l=\{0,1,\cdots,l-1\}表示l的最小非负剩余组成的集合，设m_1>0,\cdots,m_k>0,(m_i,m_j)=1，$

$0<i<j\leq k,0\leq x<m_1\cdots m_k，则集合S=\{x|0\leq x<m_1\cdots m_k\}与集合$

$S_1=\{(a_1,\cdots,a_k)|a_j\in Z_{m_j},j=1,\cdots,k\}之间存在一一对应.$



$设x和y的剩余表示分别为(\langle x\rangle_{m_1},\langle x\rangle_{m_2},\cdots,\langle x\rangle_{m_k})和(\langle y\rangle_{m_1},\langle y\rangle_{m_2},\cdots,\langle y\rangle_{m_k})，则有$

$1. \langle x \pm y\rangle_{M}的剩余表示为(\langle\langle x\rangle_{m_1}\pm \langle y\rangle_{m_1}\rangle_{m_1},\langle\langle x\rangle_{m_2}\pm \langle y\rangle_{m_2}\rangle_{m_2},\cdots,\langle\langle x\rangle_{m_k}\pm \langle y\rangle_{m_k}\rangle_{m_k})$

$2. \langle x\cdot y\rangle_{M}的剩余表示为(\langle\langle x\rangle_{m_1}\langle y\rangle_{m_1}\rangle_{m_1},\cdots,\langle\langle x\rangle_{m_k}\langle y\rangle_{m_k}\rangle_{m_k})$



#### 应用

这里乘法和加法无需进位，特别是乘法无需进位，这在计算机的制造和使用上，将带来很大的方便。
