# 2022 夏季学期 Rust 课堂笔记 

<center><div style='height:2mm;'></div><div style="font-family:华文楷体;font-size:14pt;">未央软-11  鲁睿<div style='height:2mm;'>   </div></center>

## Tutorial

### 习题评讲

+ 使用元组实现相当于解包压包

+ 使用 ``a.inter().map(|x| x * 2).collect()`` 等价于 

  ```rust
  let ret - vec![];
  for x in &a{
    rec.push(x * 2);
  }
  ```

+ 随机数的选取，如果不希望抽重，使用随机种子打乱然后顺序取

+ ``json`` 是传输数据格式中非常重要的格式：字符串、字典、数字，标准中没有注释，最后没有逗号。

+ general 的工作一定有人写，合并命令行参数第三方库 ``merge``

+ f64 没有实现偏序关系 Ord ，这是因为 NaN 不满足全序关系，从而 NaN 与所有数比较都是 false

### OJ 相关知识

请求和响应，前端属于客户端，不涉及跨主机访问

### HTTP 请求

例子：https://www/baidu.com/

GET:

HOST: www.baidu.com

Content-Type: html

#### HTTP 响应

一个例子：

HTTP 200 OK

Content-Type: application

#### json 序列化与反序列化

#[derive: deserialize]

result 转成 json 文件

#### 互斥锁

yse std::sync::{Arc, Mutex};

保证数据只能被一个线程加以修改，但要防止死锁（情况如下）

```rust
let lock_a = A.luck().unwrap();
let lock_b = B.luck().unwrap();
```

在上锁的时候，所有错误不要出现恐慌

#### 不同提交隔离

一个小段子：C艹中的 \<deque\> 中分配内存出错时，没有出现内存错误的异常

## Lecture 5

### 泛型

C 语言中没有泛型，如 ``quicksort() bisearch()`` 没有对数据类型进行泛化，而是交给程序员进行处理（手动传入 ``compare()`` 函数）

Rust 中第一个泛型，将类型作为参数，变成泛型枚举类型

```rust
enum Result<T, E> {
  Ok(T),
  Err(E),
}
```

python 不需要泛型，其有底层 ``Object`` 类型，并且是动态语言

对上述泛型枚举类型，在实现相应方法的时候其函数返回值也是 ``<T, E>``，其也可以使用参数作为传入

```rust
fn foo<T, U>(x: T, y: U){
  // ...
}
```

### 特型(trait)

一定程度上对应**面向对象编程的多态性**，对于下一段美观打印、同时比较多个参数结构体实现代码：

```rust
struct Point { 
  x: i32, 
  y: i32, 
}
impl Point {
	fn format(&self) -> String {
		format!("({}, {})", self.x, self.y)
	}
	fn equals(&self, other: Point) -> bool {
	self.x == other.x && self.y == other.y
  }
}
```

可以抽象出共同特点(trait)，相当于 C艹 中的虚函数

```rust
// write trait
trait PrettyPrint {
  fn format(&self) -> String;
}
// write actual function
impl PrettyPoint for Point {
  fn format(&self) -> String {
    format!("({}, {})", self.x, self.y)
  }
}
```

C++ 中标准库由快速排序和插入排序混合版实现

python java 使用 Tim-Sort 归并排序

C++ 背上了很大的历史包袱，每次遇到问题都需要加入新的概念

特型约束的泛型类型示例

```rust
enum Result<T, E> {
	Ok(T),
	Err(E), 
}
trait PrettyPrint {
	fn format(&self) -> String; 
}
impl<T: PrettyPrint, E: PrettyPrint> PrettyPrint for Result<T, E> {
	fn format(&self) -> String {
    match *self {
      Ok(t) => format!("Ok({})", t.format()),
      Err(e) => format!("Err({})", e.format()), 
    }
  }
}
```

特型可以拿到其“子特型”的方法

```rust
trait Parent {
  fn foo(&self) {
    // ...
  }
}
trait Child: Parent {
  fn bar(&self) {
    self.foo();
  }
}
```

``#[derive(Debug)]`` 能够让对应的数据结构获得相应实现，不用重新编写，共有以下自动**核心特性**

```rust
Clone, Copy, Debug, Default, Eq
Hash, Ord, PatialEq, PartialOrd
```

特型的自动获得需要满足其所有成员都能自动获得指定的特型，如 Eq 不能在包含 f32 的结构体类型上自动获得，因为 f32 不是 Eq 的（浮点数中的 NAN  与任意数比较都是错误的，**不满足全序关系中的自反性**）

**Debug** 特型用于输出调试信息，如 

```rust
#[derive(Debug)]
struct Point { x: i32, y: i32, }
let origin = Point { x: 0, y: 0 };
// println!("The origin is: {:?}", origin);
```

**Default** 特型用于定义一个默认值，如 0 或者 ""

**Eq 和 PartialEq** 等价关系和部分等价关系，都有对称性和传递性，前者还有自反性

**Hash** 表示可哈希的类型，H 类型是抽象的哈希状态，可以计算哈希值，而如果同时出现了 Eq 特型，需要满足以下重要性质

x == y -> hash(x) == hash(y) 

**PartialOrd 和 Ord** 表示偏序和全序，都有反对称性和传递性，前者还要满足完全性（对所有的 a 和 b，有 a <= b 或者 b <= a 成立），后者可以按照字典序排序

**关联类型的需求**：例如，图的表示：邻接矩阵/链表

**Sized 和 ?Sized** 前者表示在编译时固定大小，后者大小是动态的（如 [T], str），一般跟指针相关的泛型才会出现后者（如 Box<T>）

特型甚至可以为所有类型写，如 i32，但不推荐。为了写一个特型实现的 impl 代码段，要么拥有该特性，要么拥有该类型。

**Drop** 表示可以销毁的特型，但一般情况下不需要手动实现 Drop

### 特型对象

考虑以下特型和实现

**静态**分发：在编译的时候给定了相应特性的函数

**动态**分发：在运行的时候决定相应特性的函数，但只有运行之后才能使用，其他情况只能当成一个特型来使用，编译器不知道对应的类型信息（已经被抹去）

**对象安全性**，需要满足一定条件，关联函数要求除接收方之外，其他地方都不能出现 Self 类型（否则获取到对应的类型），不能以 Sized 为超特型，接收方是引用或者指针形式的类型（Self, Box\<Self\>）

> 课件上问题：不可变的引用是可以 Clone 的。

### 生命周期

考虑以下情况：

1. 获取了一项资源。
2. 乙方通过引用借用了甲方的这项资源。
3. 甲方对这项资源使用完毕，对它进行释放。
4. 乙方还保留着对这项资源的引用，并开始使用它。
5. 乙方挂了……

如何保证第 3 步和第 4 步的顺序关系？一般情况下，引用具有隐式的生命周期，不需要额外关注，但也可以**显式**地指定生命周期

```rust
fn bar<'a>(x: &'a i32) {
	// ...
}
```

``fn borrow_x_or_y<'a>(x: &'a str, y: &'a str) -> &'a str; `` 保证引用 x 和 y 的生命周期至少会和返回的引用生命周期一样长，若只需要前者和返回值的生命周期一样长，则可以分开为 'a 与 'b ``fn borrow_p<'a, 'b>(p: &'a str, q: &'b str) -> &'a str; ``，如以下编译期间会报错

```rust
struct Pizza(Vec<i32>);
struct PizzaSlice<'a> {
  pizza: &'a Pizza, // <- references in structs must
  index: u32, // ALWAYS have explicit lifetimes
}
  let s2; {
  let p2 = Pizza(vec![1, 2, 3, 4]);
  s2 = PizzaSlice { pizza: &p2, index: 2 };
  // no good - why?
}
drop(s2); // to undo NLL
```

如果结构体或者枚举类型的成员是引用，那么就需要显式地指定生命周期

```rust
struct Foo<'a, 'b> {
  v: &'a Vec<i32>,
	s: &'b str, 
}
```

## Lecture 6

> **所有权**是 rust 语言**资源管理**的灵魂，**特型**是 rust 语言**灵活运用**的灵魂。

> **共享不修改，修改不共享——rust 设计哲学**

### 项目管理

####  模块系统

+ 包 (packages)：Cargo 的一项功能，可以让用户构建、测试、分享箱。
+ 箱 (crates)：也叫单元包，是由**模块构成的一棵树**，能够产生一个库或者可执行文件。
+ 模块 (modules)：与 use 配合，**控制路径**的组织结构、作用域和访问权限。
+ 路径 (paths)：命名项目的方式，这里的项目可以指结构体、函数、模块等。

在模块中加上 ``pub`` 关键字便可以让其他用户访问，模块相当于 C艹 中的 namespace，模块之间可以嵌套，如下

```rust
mod english {
  pub mod greetings { /* ... */ }
  pub mod farewells { /* ... */ }
}
mod chinese {
  pub mod greetings { /* ... */ }
  pub mod farewells { /* ... */ }
}
```

可以把模块写成单独的文件 ``lib.rs``，用于整合所有的模块

```rust
// lib.rs
mod english;
// english.rs
pub mod greetings { /*...*/ }
```

也可以用目录来组织模块，把模块当做目录名使用

还可以在 Cargo 中使用自己编写的箱

```rust
[dependencies]
myfoo = { git = "https://github.com/me/foo-rs" }
mybar = { path = "../rust-bar" }
```

#### Cargo 相关

**单元测试**直接附着在源代码中，``#[test]``，**集成测试**放在 ``tests/*.rs`` 中，**基准测试程序**放在 ``benches/*.rs``（类似作坊中的基准模块）

``feature`` 是在构建时做选择性的开关（与 ``bug`` 不同）

使用 rust 语言，Cargo 编写脚本

```rust
[package]
build = "build.rs"
```

可以将自己写的软件包发布到 crate.io ，原子性的库。

### 语法补充

#### 属性

#! [no_std] 禁用标准库，#[derive(Debug)] 自动获得特型

#[inline(always)] 提示编译器内联优化，\#[cfg(target_os = "linux")] 定义条件编译。

inter procedure o

#### 操作符

运算类 > 操作类 > 位运算类 > 逻辑类，其背后的原因是 a + b == c 应该被理解为 (a + b) == c，后者是源于逻辑二元运算存在**短路情况**

使用特型来重载操作符，定义在 std::ops 下，有如下重载操作符：Neg, Not, Deref, DerefMut | Mul, Div, Mod | Add, Sub...

#### 类型转换

使用 **From 和 Into 实现自定义类型转换**，前者实现之后后者会自动实现，例如实现**对数转换**

```rust
impl Into<f64> for Log2 {
    fn into(self) -> f64 {
        // return log_2 of the value
        self.0.ln() / std::f64::consts::LN_2
    }
}
// 调用取得对数
    let log2_4: f64 = Log2(4.0).into();
    let log2_8: f64 = Log2(8.0).into();
```

#### 命名规范

##### 标识符

+ CamelCase：类型、特型

+ snake_case：箱、模块、函数、方法、变量

+ SCREAMING_SNAKE_CASE：常量和静态变量

+ T（单个大写字母）：类型参数

+ 'a（撇 + 短的小写名字）：生命周期参数

##### 构造函数和转换函数

+ new, new_with_stuff：构造函数

+ from_foo：转换构造函数

+ as_foo：低开销非消耗性转换

+ to_foo：高开销非消耗性转换

+ into_foo：消耗性转换

### 智能指针

#### Box\<T\> 

用于在堆上分配空间存放数据，其拥有 T 类型的对象，其指针是唯一的，类似 C艹 中的 ``std::unique_ptr``，是动态分配

#### std::rc::Rc\<T\>

是 **Referenced counted** 的缩写，代表指针的别名个数

共享所有权的指针类型，相当于 C艹 中的 ``std::shared_ptr``，并且其一直符合 rust 的借用规则，当且仅当引用计数为 1 时才能修改

```rust
let mut shared = Rc::new(6);
println!("{:?}", Rc::get_mut(&mut shared)); // ==> Some(6)
let mut cloned = shared.clone(); // ==> Another reference
println!("{:?}", Rc::get_mut(&mut shared)); // ==> None
println!("{:?}", Rc::get_mut(&mut cloned)); // ==> None
```

gc 垃圾回收机制，如果有各种变量相互引用形成**一种环**，就不能释放，导致空间的浪费：

+ A 有一个 B 的 Rc，B 也有一个 A 的 Rc，两者的引用计数都是 1。

+ 由于构成了环，两个对象都不会被释放，从而引起内存泄露。

可以使用**弱引用**来避免（与 C艹 中的 ``weak_ptr`` 类似） ，Rc::downgrade() 降级成 Weak。

> 对于图 (V, E)，对顶点拥有**所有权**，但是对于边来说，不能拥有对顶点的所有权，可以使用**弱引用**来实现

但这样会引入双重计数，增加开销。

#### std::cell::Cell\<T\>

为 Copy 类型提供内部可变性的格子类型，用 get() 从 Cell 中取值，用 set() 更新 Cell 的值。

#### std::cell::RefCell\<T\>

可为任意类型提供内部可变性，当 borrow() 一个 RefCell\<T\> 时，得到的是 Ref\<T\>，而不是 &T。

#### const T 和 *mut T

相当于 C 语言的裸指针。

### 常用库

+ 正则表达式: reges
+ 日志: log （源于航海，各种级别分开，error, warning）
+ 日期: chrono 
+ HTTP 客户端: reqwest
+ 增强错误处理: thiserror , anyhow
+ 数据库: rusqlite, r2d2

### 数据库

#### 分类

**数据库**是以一定方式存储在一起、能够给多个用户共享、具有尽可能小的冗余度、与应用程序彼此独立的数据集合。

+ 关系数据库：**创建在关系模型基础上的数据库**，给予集合代数
  + Oracle 国外数据库，早些年中国各大银行使用，现在国产化
  + ProsgreSQL
    + MySQL
    + SQLite

<img src="https://pic.imgdb.cn/item/6310b37c16f2c2beb17decd6.jpg" style="zoom:50%;" />

+ 非关系型数据库
  + 文档数据库（json 转换为二进制文件），如 MongoDB
  + 键值数据库（类似 HashMap），如 LevelDB

#### 操作

数据查询：**选择、投影、连接、并、交、差**

Excel 表中 vlookup 函数用于合并数据，指定键值

数据操作：**新增、删除、修改、查询**

#### SQL 简介

常用命令：

+ 创建表格 CREATE TABLE 
+ 查询数据 SELECT
+ 插入数据 INSERT
+ 更新数据 UPDATE
+ 删除数据 DELETE
+ 删除表格 DROP TABLE

DBA IT 认证，Oracle 数据管理库职业

#### 在 rust 中使用 SQL

软件包 rusqlite 

```rust
fn main() -> Result<()> {
  let conn = Connection::open_in_memory()?;
  conn.execute(
    "CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    data BLOB
    )",
    (), // empty list of parameters.
  )?;
}
```

还可以与 Web 框架联合使用

创建数据库连接池，将连接池作为 Data\<T\> 传给请求处理代码

## Lecture 7

> 当今许多设备都是多核的，并发是现代语言必须具备的特性，

### 闭包

#### 概念与类型推导

闭包的概念和匿名函数、lambda 函数相似，其可以绑定在变量上：

```rust
let square = |x: i32| -> i32 { x * x };
println!("{}", square(3));
// => 9
```

类型可以推导，参数类型和返回值类型都可以不显示地给出

```rust
let square_v4 = |x: u32| { (x * x) as i32 };
let square = |x| { x * x };
println!("{}", square(-2.4));
// => 5.76
```

#### 捕捉

闭包还可以包含其所在的环境（可以调用外面的参数，称为**捕捉**）

```rust
let magic_num = 5;
let magic_johnson = 32;
let plus_magic = |x: i32| x + magic_num;
```

闭包绑定后如果尝试借用，如果在上述代码后面加入以下代码，借用编译器则会报错

```rust
let more_magic = &mut magic_num; // Err!
```

#### 移动闭包

可以使用 ``{...}``  让闭包超过作用域来恢复，调用函数和被调用函数 Caller, Callee，也可以使用 ``move`` 关键字强制闭包获得环境变量的所有权，为**移动闭包**

```rust
fn make_closure(x: i32) -> Box<dyn Fn(i32) -> i32> {
  let f = move |y| x + y;
  Box::new(f)
}
let f = make_closure(2);
println!("{}", f(3));
// => 5
```

#### 特型闭包

闭包与所有权，只能调用一次，满足 rust 借用规则。与所有权相似，闭包也具有闭包特型，``Fn, FnMut, FnOnce`` 分别代表借用、可变借用、所有权

如何正确地返回闭包？如下，使用动态的生命周期以及移动语义解决

```rust
fn box_up_your_closure_and_move_out() -> Box<dyn Fn(i32) -> i32> {
  let local = 2;
  Box::new(move |x| x * local)
}
```

Lambda 函数本质上是 C++/Rust 在调用处创建一个未知名字的类/结构体，然后传入环境的相关值，最后调用一个未知名字的函数。

### 并发

#### 线程进程、并发并行概念

二进制可执行文件在执行之后，成为进程，在 CPU 中存放：**寄存器，堆，栈，操作系统指令**。

**Program Point** 指向进程下一个指令（在X86 中称为 PC）

线程是**轻量级**，有 CPU 存放的寄存器、堆、栈、操作系统指令单元，但内存是相互共享的，但不引入通信的开销（网络、进程通信）

并发是程序同时有多个正在运行的线程，而并行是指多个处理单元，要求更高，真正意义的同时处理。

#### 并发执行

考虑下面代码，假设两个线程，一个执行 ``foo()``，一个执行 ``bar()`` 

```rust
let mut x = 0;
fn foo() {
  let mut y = &mut x; *y = 1;
  println!("{}", *y); // foo expects 1
}
fn bar() {
  let mut z = &mut x; *z = 2;
  println!("{}", *z); // bar expects 2
}
```

这两个线程的执行顺序不是每次都能保证的，如果将两个函数当做两台 ATM 机，则会发生严重的后果。

并发编程的难点：**数据共享**、**数据竞争**、**同步**（保证所有线程都有正确的世界观，共享缓冲区）、**死锁**

死锁发生有四个条件：**互斥、持有资源、非抢占、等待成环**

一个形象的例子：

*N* 个哲学家坐在一张圆桌周围，交替地进行吃饭和思考。每个哲学家需要一双筷子用来吃饭，但是一共只有 *N* 根筷子，每两个哲学家之间有一根。

哲学家的行为用算法描述如下：

+ 拿起他左侧的那根筷子（获取一个资源的锁）。
+ 拿起他右侧的那根筷子（获取一个资源的锁）。
+ 吃饭（使用资源）。
+ 将两根筷子放回原处（释放资源的锁）。

对所有哲学家来说，依据算法，所有人都拿到左侧的筷子，而此时桌上没有筷子，从而所有人卡在第二步

### 线程

Rust 标准库提供了线程 ``std::thread``，每个线程有自己的栈和状态，使用闭包来指定线程的行为

#### 线程句柄

```rust
use std::thread;
let handle = thread::spawn(|| {
  "Hello, world!"
});
println!("{:?}", handle.join());
```

![](https://lr-tsinghua11.github.io/img/video_editor/blackboard.png)

``join()`` 会阻塞当前线程的执行，直到句柄对应的线程终止，其返回 ``Ok`` 或者 ``Err``

``thread::park()`` 可以暂停自己的执行，之后可以通过现成的 ``unpark()`` 来继续执行

#### 线程与所有权

线程的创建也要满足所有权的规则（包括闭包和所有权的规则），例如使用 ``move`` 来创建移动闭包，获得所有权

```rust
use std::thread;
for i in 0..10 {
  thread::spawn(move || {
  	println!("I'm #{}!", i);
}
```

### 共享线程状态

Rust 类型系统包含要求满足并发承诺的特型

+ Send 表示可以在线程间安全转移

+ Sync 表示可以在线程间（通过引用）安全共享

Send 类型可以将它的所有权在线程间转移，如果一种类型没有实现 Send，那么它只能留在原来的线程里。

Sync 类型在多个线程使用时不会引发内存安全问题，基本所有类型都是 Sync 的。以下为一个共享线程状态示例

```rust
use std::thread;
use std::time::Duration;
fn main() {
  let mut data = vec![1, 2, 3];
  for i in 0..3 {
    thread::spawn(move || {
      data[i] += 1;
    });
  }
  thread::sleep(Duration::from_millis(50));
}
```

此时 data 有多个所有者，使用 ``Arc<T>`` ，代表原子性的引用计数指针（Atomic Reference-Counted），但如果只是在初始化加入 Arc，编译也不通过。

Arc 也不具有内部可变性，需要添加**互斥锁**（Mutual Exclusion），保证它包含的值只有一个线程能够访问；如果一个线程锁定了互斥锁，但是发生了恐慌，此时该互斥锁进入中毒状态，该锁不会被释放

高并发任务、超算比赛主要资源共享，Open Np，消息传递 npi

### 通道

通道（channels）可以用来**同步线程之间的状态**，用于在线程之间传递消息，也可以用来提醒其他现成关于数据就绪、事件已经发行的情况

``std::sync::mpsc`` 实现多生产者、单消费者的通信功能

**同步：**不同进程之间是需要等待的，**异步：**发送的东西放入（相当于无限大的）缓冲区，相互之间不需要等待

使用 ``channel<T>()`` 函数创建一对连接的 ``(Sender<T>, Receiver<T>)``

``go`` 语言有 ``GC`` 机制，导致编程开销大

对哲学家筷子问题，可以使用最后一个哲学家用相反方向拿筷子或者传递令牌规定拿筷子的哲学家。
