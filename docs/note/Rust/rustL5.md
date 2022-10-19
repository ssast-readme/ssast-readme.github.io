# 2022 夏季学期 Rust 课堂笔记 

<center><div style='height:2mm;'></div><div style="font-family:华文楷体;font-size:14pt;">未央软-11  鲁睿<div style='height:2mm;'>   </div></center>

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

