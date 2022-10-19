# 初等数论
> 未央软-11  鲁睿


## 第3章 数论函数
### 1. $pot_pn$
#### 定义

$对于给定的素数p，设p^m\mid n且p^{m+1}\nmid n，则pot_pn=m.$

#### 性质

1. $pot_p(mn)=pot_p(m)+pot_p(n)$

2. $pot_pm^k=kpot_pm$

3. $\displaystyle pot_p(n!)=\sum_{t=1}^{\infin}[\frac{n}{p^t}]$

4. $对于给定的素数p和0<r<p^c,c>0,有pot_p(C_{p^c}^{r})=c-pot_pr$



### 2. $M\ddot{o}bius$函数$\mu(n)$

#### 定义

>  $设n=p_1^{l_1}\cdots p_s^{l_s}为n的标准分解式$
>
>  $\mu(n)=\left\{\begin{matrix}(-1)^s,l_1=\cdots=l_s=1\\ 0,有某个l_i>1\end{matrix}\right.$
>
>  $而当n=1时，\mu(n)=1.$

#### 性质1

$$\displaystyle 如果n\geq1，则有\sum_{d\mid n}\mu(d)=\lfloor\frac{1}{n}\rfloor=I_n$$

#### 性质2

$$
利用\varphi(n)=n(1-\frac{1}{p_1})\cdots(1-\frac{1}{p_s})，可以推出\varphi(n)=\sum_{d\mid n}\mu(d)\frac{n}{d}.
$$

### 3. 数论函数的狄利克雷乘积

#### 定义

> $设f(n),g(n)是两个数论函数，它们的狄利克雷乘积h(n)也是一个数论函数，由下式给出：$

> $\displaystyle h(n)=\sum_{d\mid n}f(d)g(\frac{n}{d})$

#### 定理1

$任给数论函数f(n),g(n),k(n),$

$则有f(n)*g(n)=g(n)*f(n)和(f(n)*g(n))*k(n)=f(n)*(g(n)*k(n))$

#### 定理2

$设I(n)=\lfloor\frac{1}{n}\rfloor,则对所有数论函数f(n),f(n)*I(n)=I(n)*f(n)=f(n).I(n)为单位数论函数$

#### 定理3

$设数论函数f(n),满足f(1)\neq0,则存在唯一的数论函数f^{-1}(n)，称为f(n)的狄利克雷逆函数,使得$

$f(n)*f^{-1}(n)=f^{-1}(n)*f(n)=I(n)$

$\displaystyle且f^{-1}(n)由下面的公式给出：f^{-1}(n)=\frac{-1}{f(1)}\sum_{d\mid n,d<n}f(\frac{n}{d})f^{-1}(d)$



全体$f(1)\neq0$的数论函数组成一个Abel群，记为D.



### 4. $M\ddot{o}bius$反演公式

#### 定义

我们知道：

$\displaystyle n = \sum_{d\mid n}\varphi(d)=\sum_{d\mid n}\varphi(\frac{n}{d})$

$\displaystyle \varphi(n)=\sum_{d\mid n}\mu(d)\frac{n}{d} = \sum_{d\mid n}\mu(\frac{n}{d})d$

一般地，

$\displaystyle若数论函数f(n)和g(n)满足:f(n)=\sum_{d\mid n}g(d)，$

$称f(n)为g(n)的M\ddot{o}bius变换，g(n)为f(n)的M\ddot{o}bius逆变换.$

$由定义知，n是\varphi(n)的M\ddot{o}bius变换，\varphi(n)是n的M\ddot{o}bius逆变换.$

#### 定理

$\displaystyle 若任意两个数论函数f(n)和g(n)满足等式f(n)=\sum_{d\mid n}g(d),则有$

$\displaystyle g(n)=\sum_{d\mid n}\mu(d)f(\frac{n}{d})$

反过来，后者成立时，前者也成立.

#### 定理的证明

$设对任意的正整数n，数论函数e(n)=1.$

$若f(n)=g(n)*e(n)，则f(n)*\mu(n)=g(n)*e(n)*\mu(n)=g(n)*(e(n)*\mu(n))=g(n)*I(n)=g(n)$

后半部分证明同理.



### 5. 积性函数

#### 定义

$如果数论函数f(n)不恒等于0，且当(m,n)=1时，f(mn)=f(m)f(n)，则f(n)叫做积性函数.$

$如果一个积性函数，对所有m，n，均有f(mn)=f(m)f(n)，则叫做完全积性函数.$



#### 性质1

> $如果f(n)是一个积性函数，则f(1)=1.$

证明：$\forall n，(n,1)=1.故f(n)=f(n)\cdot f(1).又因f(n)不恒等于0，故f(1)=1.$

#### 性质2

> $如果f(n)和g(n)是积性函数，那么f(n)*g(n)也是积性函数.$

证明：

> 引理：$设(m,n)=1，如果t_1通过m的全部因子，t_2通过n的全部因子，则t=t_1t_2通过mn的全部因子.$



$\displaystyle 回到原题.设h(n)=f(n)*g(n)，(m,n)=1.则h(mn)=\sum_{t\mid mn}f(t)g(\frac{mn}{t}).$

$\displaystyle 令t=t_1t_2，t_1\mid m,t_2\mid n，由引理，h(mn)=\sum_{t\mid mn}f(t)g(\frac{mn}{t})$

$\displaystyle =\sum_{t_1\mid m}\sum_{t_2\mid n}f(t_1)f(t_2)g(\frac{m}{t_1})g(\frac{n}{t_2})=\sum_{t_1\mid m}f(t_1)g(\frac{m}{t_1})\cdot\sum_{t_2\mid n}f(t_2)g(\frac{n}{t_2})=h(m)h(n).$



#### $\sigma_{\alpha}(n)$

$记f_{\alpha}(n)=n^{\alpha}，这里\alpha是任一实数，是一个完全积性函数.$

$\displaystyle设\sigma_{\alpha}(n)=\sum_{d\mid n}f_{\alpha}(d)，则\sigma_{\alpha}(n)是一个积性函数，但不是完全积性函数.（因为\sigma_{\alpha}(n)=f_{\alpha}(n)*e(n)）$

$\displaystyle \sigma_0(n)=\sum_{d\mid n}1=d(n).d(n)表示n的因数个数.$

$\sigma_1(n)表示n的全部因子的和，一般记为\sigma(n).$

##### 性质

$设n=p_1^{\alpha_1}\ldots p_k^{\alpha_k}，则\sigma_{\alpha}(n)=\sigma_{\alpha}(p_1^{\alpha_1})\ldots\sigma_{\alpha}(p_k^{\alpha_k})$

$而\sigma_{\alpha}(p_j^{\alpha _j})=1+p_j^{\alpha}+\ldots+p_j^{\alpha_j\alpha}$

$\alpha=0时，\sigma_{\alpha}(p_j^{\alpha _j})=\alpha_j+1.$

$\alpha \neq0时,\sigma_{\alpha}(p_j^{\alpha _j})=\frac{p_j^{\alpha(\alpha_j+1)-1}}{p_j^{\alpha}-1}.$

$ 于是，\sigma_{\alpha}(n)=\left\{\begin{matrix}\Pi_{j=1}^{k}\frac{p_j^{\alpha(\alpha_j+1)-1}}{p_j^{\alpha}-1},\alpha\neq 0,\\ \Pi_{j=1}^{k}(\alpha_j+1),\alpha=0.\end{matrix}\right.$

#### 性质3

$设h(n)=f(n)*g(n)，且g(n)和h(n)都是积性函数，那么f(n)也是积性函数.$

$由此可知，若g(n)是一个积性函数，则g(n)的狄利克雷逆函数也是一个积性函数.$

#### 性质4

$设f(n)是一个积性函数，那么f(n)是一个完全积性函数的充分必要条件是f^{-1}(n)=\mu(n)f(n).$

#### 性质5

$设f(n)是一个积性函数，若对素数的方幂p^{\alpha}(\alpha\geq1)有f(p^{\alpha})=f(p)^{\alpha}，则f(n)是完全积性函数.$



### 6. Lucas序列和Fibonacci序列

#### 定义

$\Large u_n=\frac{\alpha^n -\beta^n}{\alpha - \beta},n=0,1\cdots$

$\Large v_n=\alpha^n + \beta^n,n=0,1\cdots$

$其中\alpha, \beta为以下整系数二次方程的两个根：$

$x^2-Px+Q=0,\:(P,Q)=1.$

我们把$u_n$和$v_n$都叫做Lucas序列.这类序列在整数的分解、不定方程等方面有用.

$若P=1,Q=-1,则为Fibonacci序列.(F_0=F_1=1)$



#### 性质1 恒等式

1. $F_0+F_1+F_2+\cdots+F_n=F_{n+2}-1$

2. $F_0^2+F_1^2+\cdots+F_n^2=F_nF_{n+1}$

3. $F_0+F_2+\cdots+F_{2n}=F_{2n+1}$

4. $F_1+F_3+\cdots+F_{2n-1}=F_{2n}-1$

5. $F_n=F_mF_{n-m}+F_{m-1}F_{n-m-1}$(***)

6. $F_{n-1}F_{n+1}=F_n^2+(-1)^{n-1}$



#### 性质2 数论性质

1. $\gcd(F_{n-1},F_n)=1$

2. $\gcd(F_m,F_n)=F_{\gcd(m,n)}$（利用性质1-5、2-1）

3. $n\mid m \Leftrightarrow F_n\mid F_m$（***）
