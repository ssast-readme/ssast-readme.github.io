# 2022 夏季学期 Rust 课堂笔记 

<center><div style='height:2mm;'></div><div style="font-family:华文楷体;font-size:14pt;">未央软-11  鲁睿<div style='height:2mm;'>   </div></center>

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
