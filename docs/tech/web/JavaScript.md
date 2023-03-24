# JavaScript

作者：陆离马鹿

## 5.1 JS语言结构

### 5.1.1 字符集

> Js支持Unicode字符集，可以使用几乎所有的拉丁文、亚洲符号文字和汉字来书写程序
> 

### 5.1.2 符号 Token

> 符号（Tokens）包括标识符、字面量、标点符以及模板
符号组成语句和语句块
> 
1. 标识符
由Unicode组成的符号，它可以是变量名、函数名、以及保留字
2. 字面量
直接表示程序中的某些数据的符号，包括Null、Boolean、Number、String以及正则表达式（RegularExpression）等
3. 标点符
表达式中连接标识名与字⾯量的运算符以及表示结构的花括号、⼩括号、中括号、点、分号、逗号、冒号等。
4. 模板
模板字⾯量，⼀种JavaScript⽀持的特殊的字符串语法

```jsx
/*function, greeting, message,return是标识符,
'Hello', 'world', 'everyone'是字⾯量*/
function greeting(message = 'world') {
return 'Hello ' + message;
}

const message = greeting('everyone');
console.log(message);
```

### 5.1.3 空白符

> 空白符指Token之间可以插入的所有字符，包括空格、换行和制表符
> 

### 5.1.4 语句和语句块

- 语句由Token组成
- 分号代表语句的终止
- 一个或多个语句可以组成语句块
- 语句块以花括号标记起始和结束

### 5.1.5 换行

通常符号与符号之间，也能插入⼀个或多个换行符，但有⼀些特殊情况不允许换行

- return和返回值之间
- break/continue和label名之间
- 变量和`++`、`--`后缀运算符之间
- throw 和异常对象之间
- 箭头函数的参数列表和箭头`=>`之间
- yield和迭代值之间
- async和异步函数声明、函数表达式、方法名之间

### 5.1.6 作用域

- 语句块：块级作用域
- 函数：函数作用域
- 模块：模块作用域

```jsx
块级作⽤域
let i = 1;
{
	let i = 2;
	console.log(i);//2
}
console.log(i)//1

//函数作用域
const bar='bar'
function foo() {
	const bar='foobar'
	console.log(bar);
}
foo();//foobar
console.log(bar);//bar
```

### 5.1.7 变量声明

1. var
- ES5及之前的早期版本
- 无块级作用域
- 声明提升（hoist）

```jsx
var a=10;

function foo(){
	console.log(a,i);//undifine,undifined
	var a=20;
	for(var i=0;i<a;i++){
		//do sth.
	}
	console.log(a,i);//20,20
}

foo();
```

1. let
- 块级作用域
- 暂存死区（DTZ）

```jsx
{
	let x=10;
	console.loh('x is'+x);//x is 10
}

consloe.log(typeof x);//error

let x=10;

function foo(){
	console.log(x);//undifined
	var x=20;
	return x*x;
}
```

1. const
- 块级作用域
- 暂存死区（DTZ）
- 绑定值不可变

```jsx
const BUFFER_SIZE=1024;
const buffer=new ArrayBuffer(BUFFER_SIZE);

console.log(buffer);

const data=new Uint16Array(buffer);
const data2=new Uint8Array(buffer);

data[0]=0xff06;

console.log(data2[0],data2[1]);
```

## 5.2 JS数据类型

JS数据类型

- 原始类型，共有7种：
number,string,null,undefined,boolean,bigint,symbol(独一无二的值)
- 非原始类型

### 5.2.1 typeof

```jsx
console.log(
	typeof null, //ojbect
	typeof undefined, //undefined
	typeof 10, //number
	typeof 'abc', //string
	typeof true, //boolean
	typeof Symbol(), //symbol
	typeof 2n, //bigint,原始类型
	typeof Object(), //object,非原始类型
);

function add(x,y){
	return x+y;
}

console.log(typeof add);//function
```

### 5.2.2 隐式类型转换

- 字符串与数值相加时，数值被转换为字符串
- 字符串参与非加法数学运算时，字符串被转换为数值
- 布尔值与数值进行运算时，true视为1，false视为0
- 布尔值与字符串进行相加时，布尔值被视为字符串
- 更多规则参考 [ECMA-262](https://www.ecma-international.org/ecma-262/#sec-type-conversion)

```jsx
const a = 10, b = 'abc', c = 1;
console.log(a + b + c);//10abc1

const a=123,b='456',c=1;
console.log(a+b-c);//123455

const a=123,b='abc',c=1;
console.log(a+b-c);//NaN(未定义或不可表达的值)

const a=true,b=false;
console.log(a+1,b*3);//2 0

const a=true,b=false;
console.log(a+'',b+'foobar');
//'true',falsefoobar
```

### 5.2.3 比较

- 值用==操作符比较时，会出发隐式类型转换
- 值用===操作符比较时，不会触发隐式类型转换
- 一般原则是除了与null比较外，尽量用===
- 具体比较规则参考 [ECMA-262](https://www.ecma-international.org/ecma-262/#prod-RelationalExpression)

```jsx
console.log(true==1,true===1);//true,false
```

### 5.2.4 显式类型转换

通过调用方法`Number`、`String`、`Boolean`等可以将值显式转换类型

```jsx
console.log(Number('123')===123);//true
```

### 5.2.5 值类型和引用类型

- 原始类型默认是值类型
- 非原始类型默认是引用类型

```jsx
let x=20,y=30;

function foo(a,b){
	a++;
	b++;
	console.log([a,b]);//21 31 值类型,局部变量
}

foo(x,y);
console.log([x,y]);//20 30

const ojb={x:20,y:30};
function foo_2(obj){
	obj.x++;
	obj.y++;
	console.log(obj);//21 31
}

foo_2(obj);
//引用类型,函数内改变值对函数外有影响
console.log(obj);//{x:21,y:31}
```

## 5.3 JS原始类型 I

### 5.3.1 Null和Undifined

Null和Undefine是Javascript中的两种原始类型，它们分别只有一个值。

- Null的值为null
- Undifined的值为undefined
- 在非严格比较下，null==undefined

```jsx
let foo;//变量标识符被声明而没有初始化
console.log(foo);//undefined

function bar(a,b){
	return [a,b]
}
console.log(bar(1));//[1,undefined], bar的第二个参数没有传入实参

let sum=0;
function addSum(num) {
	sum+=num;
}
//addsum没有return值
console.log(addSum(10));//undifined

//访问p对象不存在的z属性
let p={x:1,y:2};
console.log(p.z);//undifind
```

### 5.3.2 Number

Number类型表示整数和浮点数

- 是符合[IEEE 754](https://baike.baidu.com/item/IEEE%20754)标准的64位浮点数
- 整数有二进制、八进制、十进制和十六进制表示法
- 可以用科学计数法表示
- 精确表示的整数范围从 $-2^{53}+1\sim 2^{53}+1$    ch
- 常量Number.MAX_SAFE_INTERGER

```jsx
0b101//二进制
0o777//八进制
0x7f//十六进制
3e9//科学计数法
Number.isSafeInterger(int k);//函数返回false或true
```

### 5.3.3 浮点数

浮点数可以表示小数

- 规范规定浮点数的整数部分如果是0，0可以省略
- 浮点数也可以使用科学计数法
- 最大浮点数 Number.MAX_VALUE
- 最小浮点数 Number.MIN_VALUE
- 浮点数精度 Number.EPSILON
- 无穷大数 Infinity

```jsx
.3//相当于0.3
Number.MAX_VALUE //1.7976931348623157e+308
Number.MIN_VALUE //5e-324
Number.EPSILON //2.220446049250313e-15

//大于小于MAX/MIN的都为infinity,数除零也为infinity
```

### 5.3.4 运算精度问题

浮点数运算存在精度问题

- 不可用相等比较浮点数

```jsx
console.log(0.1+0.2===0.3);//false

//正确做法:
function floatEqual(a,b){
	return Math.abs(a-b)<Number.EPSILON;
}

console.log(floatEqual(0.1+0.2,0.3);//true
```

### 5.3.5 NaN

符号NaN表示Not-a-Number。在计算的过程中，遇到无法表示为数值的情况，计算结果就会是`NaN`

- 如果两个数值是NaN，它们的比较结果是不等的
- Number.isNaN 判断
- ⽤ Object.is 比较

```jsx
n1=NaN;
n2=NaN;
Object.is(n1,n2);
```

### 5.3.6 +0与-0

- 数值0有+0和-0两种形态，这两个值如果比较的话是相等的。但是如果它们作为除数进行运算，分别会得到`+Infinity`和`-Infinity`
- 同样，如果⼀个有限的正数除以`Infinity`和`-Infinity`分别得到+0和-0

## 5.4 JS原始类型 II

### 5.4.1 Boolean

Boolean类型表示逻辑真和逻辑假，它只有两个可选的值，分别是字面量`true`和`false`

- JS的比较操作符返回布尔类型的结果
- 做布尔判断时存在隐式类型转换
- +0、-0、NaN、空串、undefined、null 转为 false

```jsx
const TRUE=true,
			FALSE=false;

console.log(typeof TRUE,typeof FALSE);//boolean,boolean

if(true) {
	console.log('Something should print');
}

while(false) {
	console.log('Something should not print');
}

const result=(6*7==42);
console.log(result);//true
```

### 5.4.2 String

JS使用⼀对单引号 ' 或⼀对双引号 " 来表示字符串，单引号和双引号中间不能有换行。

- 支持特殊转义符和Unicode转义符
- 由于HTML标签属性用双引号,所以JS字符串通常推荐用单引号

```jsx
var text='This is a\n text.';//转义字符
var html='<p class="sth">a <em>paragraph</em></p>';

console.log(text);
console.log(html);

var text_2='\u5947\u821e\u56e2';//其他转义字符
console.log(text_2);//"奇舞团"
```

### 5.4.3 处理字符

字符串可以使用spread操作符展开成字符数组。可以使用`codePointAt`方法来获得某位字符的Unicode码位

- Unicode码位位以多字节Unicode编码表示⼀个字符
- `String.fromCodePoint`方法可以将码位还原为字符串

```jsx
console.log(str.codePointAt(0));//str为一字符串
const str=String.fromCodePoint(126978,126979);
```

### 5.4.4 类型转换

字符串可以与其他类型数据相互操作

- +操作符触发其他类型的隐式类型转换
- Number.parseInt与Number.parseFloat
- 显式类型转换
- 对象的toString方法

```jsx
console.log([1+2,'1'+2,'1'-2]);
//[3."12",-1]

console.log(Number.parseInt('100abc',2));//4
console.log(Number('0b100');

console.log(Number,parseFloat('12.3e10xx'));
//123000000000

var foo={
	toString(){
		return 'foo';
	}
};
console.log(foo+'bar'));//foobar
```

> `Number.parseInt`与`Number.parseFloat`均会忽略串中无法转换的末尾部分
> 

### 5.4.5 常用操作

字符串内置常用操作方法

- 字符串连接 +
- 大小写转换 `toUpperCase, toLowerCase`
- 逆序 `split(’k’)`以k字符为分界将字符串分为两半，`reverse()`逆转
- 截取 `slice(a,b),substr(a,b)`
- 查找 `indexOf(x)`
- 替换 `replace(a,b)`

```jsx
const a='hello';
const b='WORLD';
const c='!';

console.log(a+' '+b+c);//字符串连接,hello WORLD!
console.log(a.toUpperCase()+' '+b.toLowerCase()+c);//HELLO world!
console.log(a.split('').reverse().join(''));//olleh
console.log(a.slice(2,3),a.substr(2,3));//截取子串
//l llo

const d=a+' '+b+c;
console.log(d.indexOf(b));//字符串查找
//6
console.log(d.replace(a,a.toUpperCase());//"HELLO WORLD"
```

### 5.4.6 多行文本

ES6之后，JS支持以⼀对反引号```表示多行文本，同时也是模板字符串

```jsx
const tpl1 =`我所做的馅饼 
						 是全天下
						 最好吃的`;
console.log([tpl1, typeof tpl1]);
{
let who = '⽉影', what = '⽉饼';
const tpl2 = `${who}所做的${what} 
						是全天下 
						最好吃的`;
console.log(tpl2);
}
```

## 5.5 JS原始类型 III

### 5.5.1 Symbol

ES6及之后的版本中引⼊的新原始数据类型，Symbol可以创建唯⼀标识。

- 作为对象的key
- `Symbol.for` 创建全局标识
- `Symbol.keyFor` 从全局标识中拿到对应的key

```jsx
const id1=Symbol('foo');
const id2=Symbol('foo');
console.log(id1===id2);//false

const foo=Symbol.for('foobar');
const bar=Symbol.for('foobar');
console.log(foo==bar);//true 因为是全局的

const foo=Symbol.for('foobar');
console.log(Symbol.keyFor(foo));//forbar 获得key
```

### 5.5.2 私有属性

新的语言标准中private field有些不理想，所以也可以采⽤Symbol来定义私有属性

```jsx
const size = Symbol('size');
class Collection {
	constructor() {
		this[size] = 0;
	}
	add(item) {
		this[this[size]] = item;
		this[size]++;
	}

	static sizeOf(instance) {
		return instance[size];
	}
}
```

### 5.5.3 内置Symbol

ES6内置了一些有用的Symbol，可以用来控制对象的一些内部行为

- Symbol.iterator 迭代器
- Symbol.toPrimitive
- Symbol.toStringTag

### 5.5.4 BigInt

BigInt是JavaScript新的原始类型，可以精确表示大于$2^{53}-1$的整数

- BigInt字面量：数字+n
- BigInt运算：不能与Number直接进行运算
- 显式类型转换：BigInt与Number相互转换

### 5.5.5 BigInt内置方法

BigInt提供了两个内置方法可以转换为width位的有符号或无符号BigInt值

- BigInt以计算机补码表示负数
- BigInt.asIntN转换为对应的有符号整数
- BigInt.asUintN转换为对应的无符号整数

## 5.6 JS函数 I

### 5.6.1 函数声明

可以通过function关键字来声明一个函数

- 函数声明没有块级作用域
- 函数声明会被提升（hoist）在声明函数之前调用也是正确的，因为编译时声明会被提前

```jsx
//不带参数的函数
function foo() {
	console.log('foo bar');
}
//带两个参数的函数
function add(x, y=0) {
	return x+y;
}

//可选参数
function sum(x=0,...rest){
	return rest.reduce((a,b)->a+b,x);
}
//解构参数
function vectorLength({x=0,y=0,z=0}={}) {
	return Math.hypot(x,y,z);
}
const v={x:3,y:4,z:0};
console.log(vectorLength(v));//5
```

### 5.6.2 函数表达式

函数也是对象，因此我们可以把一个函数赋给一个变量，可以将函数作为对象使用

- 函数表达式不会被提升（hoist）
- 函数表达式可以具名也可以匿名

```jsx
const factorial=function f(n){
	if(typeof n==='number')n=BigInt(n);
	if(n<=1n) return 1n;
	return n*f(n-1n);//具名的f只能在内部访问
}
console.log(factorial(100));//外部只能使用factorial
```

### 5.6.3 箭头函数

匿名函数表达式还可以写为箭头函数

- 单行的箭头函数可以省略花括号与return
- 只有一个参数的箭头函数可以省略圆括号
- 箭头函数不能具名，也没有this上下文

```jsx
const radAngles=angles.map(angle->MATH.PI*angle/100);
const sum=arr.reduce((x,y))->x+y);
```

### 5.6.4 执行上下文（闭包）

函数有执行上下文，运行时会产生“闭包”

- 闭包时运行时由函数调用产生的
- 通过闭包可访问执行上下文中的数据
- 如果产生闭包的引用被销毁，闭包被销毁

```jsx
function sayHelloTo(person){
	return function(){
		console.log(`hello ${person}!`);
	}
}

let greeting_1=sayHelloTo('Tom');
let greeting_2=sayHelloTo('Jerry');

greeting_1();//Hello Tom!
greeting_2();//Hello Jerry!

greeting_1=null;
greeting_2=null;//greeting_1,greeting_2环境/闭包
```

## 5.7 JS函数 II

### 5.7.1 this上下文

函数的this上下文，指函数的实际调用者对象。在函数体内部，可以通过 `this` 对象访问函数调用this上下文。

```jsx
const personn={
	firstname:'三',
	lastname:'张',
	getFullName:function(){
		return this.lastName+' '+this.firstName;
	},
};

console.log(person.firstName);//三
console.log(person.lastName);//张
console.log(person.getFullName()));//张三

person.sayHelloTo=function(){
	console.log(`Hello ${this.lastName}!`);
}
person.sayHelloTo();//Hello 张!
setTimeout(person.sayHelloTo,100);//调用者不是person,因此this.lastname不存在
//Hello undefined!
```

- 箭头函数
    - 箭头函数没有this上下文，利用这一特性，可以让箭头函数访问外部作用域的this上下文
    
    ```jsx
    const person={
    	firstName:'三',
    	lastName:'张',
    	getFullName(){
    		return this.lastname+' '+this.firstName;
    	},
    sayHelloTo(){
    	setTimeout(()->console.log(`Hello ${this.lastName}!`),100);
    	//()->没有this上下文,为外层的this	
    	}
    };
    person.sayHelloTo();//Hello 张！
    ```
    

### 5.7.2 动态绑定

函数的this上下文在函数调用时可以动态指定，方法是通过函数的call、apply或bind方法来调用

`function.call`

```jsx
function getFullName(){
	return this.firstName+' '+this.lastName;
}

const person={firstName:'三',lastName:'张'};
console.log(getFullName.call(person));//三 张

const logger={
	type:'info',
	count:0,
	log:function(message){
		console[this.type](message,++this.count);
	},
};

//call,apply,bind不光能绑定this上下文,还能绑定部分参数
setInterval(//定时器
	logger.log.bind(logger,'heart beat'),1000);//logger.log的调用者默认是global
```

### 5.7.3 Function类

函数对象是Function类的实例，可以通过Function类动态创建

```jsx
const add=new Function('x','y','return x+y');
console.log(add(1,2));//2

const tpl="{foo:'bar'}";
//tpl不是规范的JSON字符串,无法使用JSON.parse解析
const obj=(new Function(`return ${tpl}`))();
console.log(obj);//{foo:'bar'}
```

## 5.8 JS对象 I

### 5.8.1 构造

对象构造可以用字面量，也可以用构造器，或者用原型。对象是最基础的复合类型，它是一组属性的集合

- 通过字面量构造
- 通过构造器构造
- 通过原型构造

```jsx
//字面量
{
	let mtObj={
		name:"akira",
		birthday:"12-29"
	};
}

//构造器
{
	let myObj=new Object();
	myObj.name='akira';
	myObj.birthday='12-29';
}

//原型
{
	myObj=Object.create({name:"akira",
	birthday:"12-29"});
}
```

- 构造器与类

JAvaScript是面向对象的编程语言，对象默认的构造器是Object，可以定义函数作为构造器或者定义class

```jsx
//函数作为构造器
{
	function Vector2D(x,y){
		this.x=x;
		this.y=y;
	}
	const v=new Vector2D(3,4);
}
//定义class
{
	class Vector2D{
		constructor(x,y){
			this.x=x;
			this.y=y;
		]
	}
	const v=new Vector2D(3,4);
}
```

### 5.8.2 属性定义

对象的属性名可以是字符串或Symbol。对象属性定义的key可以用合法标识符、字符串或方括号`[]` 中的表达式。如果是表达式，计算出的值应该是字符串或者Symbol

```jsx
const data_1={
	foo:'foo',
	bar:'bar'
};

const data_2={
	'foo-bar':'foo bar',//foo-bar不能作属性名,但加上影号成为字符串则可以
};

const foo='foo';
const data_3={
	[foo+'bar']:'foobar',
};

console.log(data_1);//{foo:'foo',bar:'bar'}
console.log(data_2);//{'foo-bar':'foo bar'}
console.log(data_3);//{foobar:'foobar'}

const id=Symnol('id');
const obj={[id]:'message'};
console.log(obj);//{Symbol(id):"message"}
```

### 5.8.3 属性访问

对对象指定属性的访问，有两种方式，如果属性名是合法的标识符，那么可以使用`.`操作符访问。如果属性名不是合法标识符，比如不符合标识符命名的字符串或Symbol，或者属性名需要经过计算，那么我们可以通过`[ ]` 操作符访问。

```jsx
const id=Symbol('id');
const data={
	'foo-bar':'foor-bar',
	[id]:'message',
	'12':'result',
};
console.log(data['foo-bar'],data[id],data[3*4]);
//foo-bar message result
//使用key访问

//[]允许动态计算表达式的值作为属性名
//对于动态转换数据结构很有帮助
const students=['张三','李四','王五'];
const scores=[70,100,80];
const results={};

for(let i=0;i<studets.length;i++){
	results[students[i]]=scores[i];
}
```

### 5.8.4 属性遍历

除了通过对象属性名（key）访问对应的值，我们科研对属性的key或value分别进行遍历

- 用`for…in`遍历
- 用`for…of`遍历

```jsx
const scores={
	'张三':80,
	'李四':100,
	'王五':60,
};
for(let name in scores){
	console.log(name,scores[name]);
//分别输出张三,80,李四,100,王五,60
}

const scores={
	'张三':80,
	'李四':100,
	'王五':60,
};
for(let [name,score] of Object.entries(scores)){
	console.log(name,score);
	//分别输出张三,80 李四,100 王五,60
}
```

### 5.8.5 增删改

对象属性可以动态添加，直接给对象属性复制就可以，要将已有属性删除，可以用delete操作，通过in操作符，可以判断一个属性是否在对象上存在

```jsx
const date={}

//添加属性
data.foo='foo';
data['foo-bar']='foo-bar';

delete data.foo;//删除属性

console.log(data.foo,data['foo-bar']);//undifined foo-bar
console.log('foo' in data,'foo-bar' in data);//false true
```

### 5.8.6 原型

原型是对象上的特殊的属性，对象可以通过原型来共享数据。

- 通过Object.create共享
- 通过构造器共享

```jsx
//通过Object.create共享
//将已有对象作为create的参数
{
	const o={foo:'foo'};
	const a=Object.create(o);
	const b=Object.create(o);
	a.bar='bar1';
	b.bar='bar2';
	console.log(a.foo,a.bar);//foo,bar1
	console.log(b.foo,n.bar);//foo,bar2
}

//通过构造器的prototype属性访问原型
{
	function Foo(message='foo'){
		this.foo=message;
	}
	Foo.prototype.bar='bar';//构造器设置prototype
	const a=new Foo('foo1'),
				b=new Foo('foo2');
	console.log(a.foo,a.bar);//foo1,bar
	console.log(b.foo,b.bar);//foo2,bar
}
```

### 5.8.7 原型链

在JavaScript中，几乎所有对象都可以访问它的构造器上的原型对象，而这个原型对象本身又可以访问它自身的构造器上的原型对象，依次类推，就构成⼀个链式结构，被称为原型链

```jsx
function Animal() {}
	Animal.prototype={
	eat() {console.log("I'm eating");}
}
function Person() {}
Person.prototype=new Animal();

Person.prototype.speak=function() {
	console.log('I can say something');
}
function Student(name) {
	this.name=name;
}
Student.prototype=new Person();
Student.prototype.study=function() {
	console.log("I'm learning...");
}

const student=new Student('张三');
console.log(student.eat(),student.speak(),student.study());
```

### 5.8.8 类继承

原型链在JavaScript中起到了类继承的作用，而ES6之后，我们也可以直接用class的语法来实现类继承。

## 5.9 JS对象 II

### 5.9.1 访问器

根据对象的其他属性或者别的数据的改变而改变的一类属性

- 访问器属性-对象可定义访问器属性（Accessor Property）
    - 使用get/set定义
    - 使用defineProperty/defineProperties定义
    
    ```jsx
    class Vector2D{
    	constructor(x,y){
    		this.x=x;
    		this.y=y;
    	}
    	get length(){
    		return Math.sqrt(this.x**2+this.y**2);
    	}
    	set length(len){
    		const clase=len/this.length;
    		this.x*=scale;
    		this.y*=scale;
    	}
    }
    
    const v1=new Vector2D(3,4)l
    console.log(v1.x,v1.y,v1.length);//3,4,5
    
    v1.length*=2;
    console.log(v1.x,v1.y,v1.length);//6,8,10
    ```
    

### 5.9.2 描述符

是一类特殊的对象，用来描述属性的访问特性，通过`defineProperty`/`definePropertities`定义属性可以指定属性描述符

| 描述符 | 类型 | 说明 |
| --- | --- | --- |
| configurable | boolean | 可删除 |
| writable | boolean | 可写 |
| enumerable | boolean | 可枚举 |
| value | any | 值 |
| get | function | getter |
| set  | function | setter |
- `defineProperties`-通过defineProperties和属性描述符定义属性
    - 动态添加在对象上的普通属性默认是可删除、可写、可枚举的
    - 定义在class上的普通属性默认是可删除、可写、不可枚举的
    - 可以使用`Object.getOwnPropertyDescriptors`来获取属性描述符
    
    ```jsx
    const obj={};
    
    Object.defineProperties(obj,{
    	foo:{
    		value:'foo',
    		wraitable:true,
    		configurable:true,
    	},
    	bar:{
    		get(){return 'bar'},
    	}
    });
    
    console.log(obj.foo,obj.bar);//foo bar
    obj.foo='foo2';
    console.log(obj.foo,obj.bar);//foo2 bar
    delete obj.foo;
    console.log(obj.foo,obj.bar);//undefined bar
    ```
    

### 5.9.3 解构

除了传参之外，对象的初始化和赋值也是可以解构的

- 可以用属性名来解构
- 也可以在解构的同时重新命名
- 除了一般对象，数组也可以解构

```jsx
{
	const obj={foo:'foo',bar:'bar'};
	const {foo,bar}=obj;
	console.log(foo,bar);//foo,bar
}
{
	const obj={x:{y:1},z:2};
	const {x:{y},z}=obj;//解构的嵌套
	console.log(y,z);//1,2
}
{
	const obj={foo:1,bar:2};
	for(let [key,value] of Object.entries(obj)){
		console.log(key,value);
	}//foo,1 bar,2
}
```

| Object | ✔️ | ArrayBuffer | ❌ |
| --- | --- | --- | --- |
| Function | ✔️ | Promise | ✔️ |
| Array | ✔️ | DataView | ❌ |
| Date | ✔️ | Map | ❌ |
| Regex | ✔️ | Set | ❌ |
| Error | ❌ | TypedArray | ❌ |
| Math | ❌ | Proxy | ❌ |

# 6 Javascript与Web开发

## 6.1 DOM基础

### 6.1.1 认识DOM

了解DOM的基本概念

### 6.1.1.2 DOM

Document Object Model（文档对象模型），允许程序或脚本语言（如JavaScript）来操作HTML/XML文档的接口

- BOM: Browser Object Model（浏览器对象模型）
    - BOM没有统一的标准，但是window的一些子对象有对应的标准 （DOM、HTML、CSS等）
- DOM的基本概念：文档树、节点、元素、根节点和根元素（每一棵文档树只会有一个根节点和一个根元素）
    - 获取根节点和根元素
    
    ```jsx
    Node.getRootNode();
    node.parentElement; //递归地获取根元素
    ```
    
- 获取Document、HTML、Window
  
    ```jsx
    //获取document
    node.ownerDocument;//document || null
    
    //获取html元素
    document.documentElement;
    
    //获取window对象
    document.defaultView;//window || null
    document.parentWindow;//非标准 IE only
    ```
    

### 6.1.2 常用DOM接口

认识DOM的常用接口，常用属性和常用方法

- 节点Node：常用接口，常用属性和常用方法
- 元素Element：继承Node接口，常用属性、常用方法
- HTML Element：继承Elment接口、常用属性
- Event：常用属性、常用方法

### 6.1.3 操作DOM

### 6.1.3.1 DOM的获取

- 根据元素特征
    - 根据ID获取`document.getElementById(’main’);`
    - 根据classname获取`document.getElementByClassName(’list’);`
    - 根据tagname获取`document.getElementByTagName(’li’);`
    - 根据name获取`document.getElementByName(’btn01’);`
- 通过CSS选择器获取
    - 根据ID选择器获取
    - 根据类选择器获取
    - 根据标签选择器获取
    - 根据属性选择器获取
    - 根据复杂的CSS选择器获取
- `HTMLCollection & NodeList`
- 获取子节点
    - `p.firstChild`
    - `p.lastChild`
    - `p.childNodes`
- 获取父节点
    - `xx.parentElement`
    - `xx.parentNode`
- 获取兄弟节点
    - `xx.previousSibling`
    - `xx.previousElementSibling`
    - `xx.nextSibling`
    - `xx.nextElementSibling`

### 6.1.3.2 创建节点并插入DOM

```jsx
//创建节点
let a= document.createElement('a');
//设置文本
a.textContent='link to so.com';
//设置属性
a.href='https://www.so.com';//property方式
a.setAttribute('target','_blank');//attribute方式
//设置样式
a.style.cssText='color:red';//cssText方式
a.tyle.fontSize='40px'//属性方式
//插入DOM
document.body.appendChild(a);
```

- 批量插入子节点

```jsx
//批量插入DOM
for(let i=0;i<10;i++){
	let p=document.createElement('p');
	p.textContent=`这是第${i+1}个`;
	//appendChild执行了10次,DOM重绘了10次
	document.body.appendChild(p);
}
```

```jsx
//利用DocumentFragment
let frag=document.createDocumentFragment();
for(let i=0;i<10;i++){
	let p=document.createElement('p');
	p.textContent=`这是第${i+1}个`;
//没有实际插入DOM,不触发重绘
	frag.appendChild(p);
}
//只插入一次DOM,触发一次重绘
document.obdy.appendChild(frag);

//fragment本身并不会被插入DOM
console.log(frag.parentNode);//null
//只会将子节点全部插入DOM并将fragment清空
console.log(frag.children);//HTMLCollection[]

```

```jsx
//利用ParentNode.append()方法(IE不支持)
let arr=[];
for(let i=0;i<10;i++){
	let p=document.createElement('p');
	p.textContent=`这是第${i+1}个`;
	arr.push(p);
}document.body.append(...arrr);
//document.body.append.apply(document,body,arr);
```

`ParentNode.append()` 插入文本

```jsx
let p=document.createElement('p');
p.textContent='这是一个段落';
document.body.append('这是段落前的文本',p,'这是段落后的文本');
```

- 插入到指定结点之前

```jsx
let p=documen.getElementById('p');
let text=document.createTextNode('这是一段文本');
document.body.insertBefore(text,p);
```

- 替换已有的节点

```jsx
let p=document.getElementById('p');
let text=document.createTextNode('则是一段文本');
document.body.replaceChild(text,p);
```

- 移除节点

```jsx
let p=document.et ElementById('p');
p.parentNode.removeChild(p);
```

### 6.1.3.3 属性相关的其他操作

```jsx
let p=document.getElementById('p');
//属性判断
console.log(p.hasAttribute('title'));//false
console.log(p.hasAttribute('id'));//true

//属性获取
console.log(p.getAttribute('title'));//null
console.log(p.getAttribute('id'));//'p'

//属性移除
p.removeAttribute('id');
```

### 6.1.3.4 事件

- 事件的监听

```jsx
let btn=document.getElementById('btn1');
//写法1
btn.addEventListener('click',unction(ev){
	console.log(`点击位置:[${ev.ageX},${ev.pageY}]`)
],{
		passive:false,//是否允许ev.preventDefault()取消事件
		apture:false,//是否在捕获阶段触发
		once:false,//是否只触发一次
});
```

- 事件的解除

```jsx
let btn=document.getElementById('btn1');
function handler(ev){
	console.log(`点击位置:[${ev.pageX},${ev.ageY}]`)
}

//事件绑定
btn.addEventListener('click',handler,false);
//事件解除
btn.removeEventLisener('click',handler,false);

//注意1:解除事件的函数必须和绑定时指向同一个
btn.removeEventLisener('click',function handler(ev){
	console.log(`点击位置:[${ev.pageX},${ev.ageY}]`)
},false);//解除失败

//注意2:尽可能保持结束事件时第三个参数与绑定时相同
btn.removeEventLisener('click',handler,true);
```

### 6.1.3.5 DOM事件的阶段

1. 捕获阶段
2. 目标阶段
3. 冒泡阶段
- 事件代理：利用事件冒泡的原理

```jsx
let num=0;
document.body.addEventListener('click',function(ev){
	switch(ev.target.id){
		case'btn1':
			num++;
			break;
		case'btn2':
			num--;
			break;
		case'btn3':
			num*=2;
			break;
		case'div':
			num=0;
			break;
	}
	console.log(num);
},false);
```

- 冒泡事件与不冒泡事件
    - 冒泡事件
        - click
        - mousedown
        - mouseup
    - 不冒泡事件
        - mouseenter 鼠标移入
        - mouseleave 鼠标移出

## 6.2 JS动画基础

### 6.2.1 动画基础

- 构成动画的两大要素
    - （静态）画面：图片/文字，CSS，Canvas，SVG
    - （动态）事件：时间轴，时间节点，延时，缓动
- 帧 Frame：帧数、帧频（Frame Per Second）
    - 关键帧、过渡帧
- 时间轴 Timeline

### 6.2.2 时间管理

### 6.2.2.1 时间的获取

Date

- `new Date().getTime()`/ `+new Date()` 相对于1970.1.1至今的毫秒数
- `Date.now()` 不需要实例化

performance

- `window.performance.now()` 浮点数，从网页打开到运行`performance.now()`的毫秒数

|  | Date | performance |
| --- | --- | --- |
| 精度 | 毫秒 | 微秒 |
| 受系统时间影响 | ✔️ | ❌ |
| 兼容性 | all | ie10+ |

### 6.2.2.2 延时执行

`setTimeout`

```jsx
//设置定时器
let timer=setTimeout(fn,delay);
//清除定时器
clearTimeout(timer);
```

`requestAnimationFrame(raf)`

```jsx
//注册回调
//在浏览器下一次渲染之前执行fn
let requestId-requestAnimationFrame(fn);
//撤销注册
cancelAnimationFrame(requesttId);
```

|  | setTimeout | raf |
| --- | --- | --- |
| 触发时机 | 一定时间之后 | 浏览器下次渲染 |
| 延时间隔 | 调用时指定，但不准确 | 不可控，需自己判断 |
| 丢帧 | ✔️ | ❌ |
| 兼容性 | all | ie10+ |
- 其他延时方案
    - `setInterval` `clearInterval`  不会自动停下
    - `setImmediate(NodeJS/IE)`
    - `process.nextTick(NodeJS)`

### 6.2.3 动画实现

### 6.2.3.1 动画策略

动画策略的选择

- 非均匀动画：不进行时间判断，只依赖延时方法执行的次数
    - 优点：实现简单，动画总帧数稳定
    - 缺点：帧频不稳定，所以在视觉上不均匀，存在延迟时会拖慢整个动画进度

```jsx
let x=0;
function frame(){
	x+=17;
	if(x<1000){
		requestAnimationFrame(frame);
	}else{
		x=1000;
	}
	console.log(x);
}
frame();
```

- 均匀动画
    - 丢帧保时：没有关键帧的设定，只依赖延时方法执行时的时间戳
        - 优点：动画在时间上完全均匀
        - 缺点：如果间隔过长，会导致关键动画部分的丢失
    
    ```jsx
    let x=0;
    function frame(){
    	let time=performance.now();
    	x=Math.min(1000,time-startTime);
    	if(x<1000){
    		requestAnimationFrame(frame);
    	}
    	console.log(x);
    }
    let startTime=performance.now();
    frame();
    ```
    
    - 延时保帧：在丢帧保时的基础上，设置必须播放的关键帧
        - 优点：兼具非均匀动画和丢帧保时策略的优点
        - 缺点：逻辑复杂，实现成本略高
        
        ```jsx
        let x=0;
        function frame(){
        	let time=performance.now();
        	let lastX=x;
        	x=Math.min(1000,time-startTime);
        	if(x>nextKeyFrame){
        		if((x-lastX)>100{//权衡点1,x是否越过关键帧太多
        			startTime+=(x-nextKeyFrame);//权衡点2,是否需要把起始时间往后拨
        			x=nextKeyFrame;
        		}
        	}
        	if(x<1000){
        		requestAnimationFrame(frame);
        	}
        	console.log(x);
        }
        
        let startTim=performance.now();
        let nextKeyFrame=50;
        frame();
        ```
        

### 6.2.3.2 缓动

调节动画过程的速度变化

- 缓动函数
    - 线性 linear
    - 缓出 ease-out
    - 缓入 ease-in
    - 缓入缓出 ease-in-out
    - 分布(后动：先显示再位移) step-end
    - 分布(先动) step-start

## 6.3 事件

### 6.3.1 事件概念

1. 事件类型：是一个字符串，又是也称为事件名称
2. 事件目标：一个对象，事件发生在改对象上或者事件与该对象有关。必须明确事件的类型和目标

> 最常见的事件目标`Windows`、`Document`、`Element`
> 
1. 事件处理程序或事件监听器：一个函数，负责处理或响应事件。应用通过浏览器注册自己的事件处理程序，指定事件类型和事件目标
2. 事件对象：是与特定事件关联的对象，包含有关该事件的细节。有`type` 和`target`属性
3. 事件传播：一个过程，有些会冒泡
4. 默认动作：事件处理程序可以取消默认动作

### 6.3.2 事件分类

1. 设备相关输入事件：直接与特定输入设备相关

`mousedown,mousemove,mouseup,touchstart,touchmove,touchend,keydown,keyup`

1. 设备无关输入事件：不与特定输入直接相关

`click,imput,pointerdown,pointermove,pointerup` 对某些设备相关输入事件的输入无关替代

1. 用户界面事件：UI事件是高级时间，通常在HTML表单元素上触发

`focus,change,submit`

1. 状态变化事件：由网络或浏览器活动触发，表示某种生命周期或状态相关的变化

`load,DOMContentLoaded,online,offline,popstate`

1. API特定事件：HTML及相关规范定义的Web API包含各自的事件类型

### 6.3.3 注册事件处理程序

1. 注册事件处理程序的方式：设置作为事件目标的对象或文档元素的一个属性/把处理程序传给这个对象或元素的`addEvventListener()`方法
2. 设置事件处理程序属性（JS）：把事件目标的一个属性设置为关联的事件处理程序函数
   事件处理程序属性的名字常由on和事件名组成（区分大小写，必须全部小写）：`onclick,onchange,onload,onmouseover`
   
    ```jsx
    //设置window对象的onload属性为一个函数
    //这个函数是事件处理程序,会在文档加载完成时被调用
    wndow.onload=function(){
    	//查找一个个<form>元素
    	let form=document.querySelector("form#shipping");
    	//在这个表单上注册一个事件处理程序
    	//在表单被提交之前会调用这个函数。假设其他地方定义了isFormValid()
    	form.onsubmit=function(event){//当用户提交表单时
    		if(!isFormValid(this)){
    			event.preventDefault();//无效则组织提交
    		}
    	};
    };
    ```
   
    事件处理程序属性的一个缺点：这种方式假设事件目标对每种时间最多只有一个处理程序。`addEventListener`注册更好,不会重写从此前注册的处理程序
   
3. 设置事件处理程序属性（HTML）：文档元素的事件处理程序属性也可以直接在HTML文件中作为对应HTML标签的属性来定义。属性值为一段JavaScript字符串,为事件处理程序函数的函数体

```jsx
<button onclick="console.log('Thank you');>Please Click</button>
```

1. `addEventListener()`：接受3个参数，分别为事件类型（字符串，不包含前缀”on“），调用的函数，指定出发时间处理程序阶段的参数

> `onclick`属性和调用`addEventListener`不相冲突，且能多次使用`addEventListener`在同一个对象上位同一个事件注册多个处理程序，并按照注册的顺序被调用
> 

```jsx
<button id="mybutton">Click me</button>
<script>
	let b=document.querySelector("#mybutton");
	b.onclick=function(){ console.log("Thanks for clicking me!");};
	b.addEventListener("click",()->{console.log("Thanks again!");});
</script>
```

> `removeEventListener()`方法用来从对象上移除事件处理程序
> 

### 6.3.4 调用事件处理程序

1. 事件处理程序的参数：调用时会接收到一个唯一的Event对象参数，包含属性为：
- type 发生事件的类型
- target 发生事件的对象
- currentTarget 注册此程序的对象
- timeStamp 事件发生的时间戳
- isTrusted 浏览器派发事件：True，JavaScript派发：False
1. 事件处理程序的上下文：
- 通过设置属性注册事件处理程序时（`target.onclick=...`），在事件处理函数的函数体，this关键字引用的是注册时间处理程序的对象（`target`）
- 使用`addEventListener()`注册时，处理程序在被调用的时候以事件目标作为其`this`值。不过这不适用于箭头函数形式的处理程序，箭头函数中this的值始终等于定义它的作用域的this值
1. 事件处理程序的返回值
- 老旧的代码中存在返回值，返回值通常用于告诉浏览器不要执行与事件相关的默认动作
1. 调用顺序
- ⼀个事件目标可能会为一种事件注册多个处理程序。当该事件发生时，浏览器会按照注册处理程序的顺序调用它们。即便混合使用addEventListener()和设置对象的onclick属性，结果仍然如此

### 6.3.5 事件传播

1. 概述：
- 如果事件的目标是Window或其他独立对象，浏览器对这个事件的响应就是简单地调用该对象上对应的事件处理程序。如果事件目标是Document或其他文档元素，就没有那么简单了
1. 事件冒泡：
- 注册在目标元素上的事件处理程序被调用后，多数事件都会沿DOM树向上“冒泡”。目标父元素的事件处理程序会被调用。然后注册在目标祖父元素上的事件处理程序会被调用。就这样⼀直向上到Document对象，然后再到Window对象
- 因此可以在文档元素的公共祖先元素上注册一个事件处理程序
- 例外：`focus,blur,scroll`事件、`load`到document对象就会停止冒泡，window对象的`load`事件处理程序只会在整个文档加载完毕之后才会被触发
1. 事件捕获
- `addEventListener()`的第3个参数是`true/{capture:true}` 表示该程序注册为捕获事件处理程序，捕获程序递归向下调用，下到事件目标的父元素

### 6.3.6 取消默认动作

- `preventDefault()` 取消关联的默认动作
- `stopPrepagantion()` 取消事件传播，但同一对象的其他处理程序仍可用，可在捕获阶段、事件目标本身、冒泡阶段起作用
- `stopImmediatePropagation()` 还会阻止在同一个对象上注册的后续事件处理程序的执行

### 6.3.7 自定义事件

- `CustomEvent()` 构造函数创建自定义事件对象，参数为表示事件类型的字符串，指定对象属性的对象，`detail`属性：事件的内容
- 将此对象传给`dispatchEvent()`

```jsx
//派发一个自定义事件,通知UI自己正忙着
document.dispatchEvent(new CustomEvent("busy",{detail:true}));

//执行网络操作
fetch(url)
	.then(handleNetworkResponse)
	.catch(handleNetworkError)
	.finally(()->{
		//无论网络请求成功还是失败,都再派发一个事件,通知UI自己现在已经不忙了
		document.dispatchEvent(new CustomEvent("busy",{detail:false}));
	});
//在代码其他地方为"busy"事件注册一个处理程序,并通过其显示或隐藏转轮图标,告诉用户忙与闲
document.addEventListener("busy",(e)->{
	if(e.detail){
		showSpinner();
	}else{
		hideSpinner();
	}
});
```

## 6.4 Web组件

### 6.4.1 使用Web组件

```jsx
//Web组件实在JavaScript中定义的
<script src="components/card-component.js"></script>
//Web组件要定义自己的HTML标签名
<card-component img="..."></card-component>
//Web组件可以接收有标识的子组件
<card-component img="...">
	<span slot="title"/>
	<span slot="text"/>
</card-component>
```

### 6.4.2 DocumentFragment节点

- `document.createDocumentFragment()`
- 可以临时充当一组同辈节点的父节点
- 像文档中插入`DocumentFragment`时，其本身不会被插入，实际上插入的是它的子节点

### 6.4.3 自定义元素

```jsx
//创建自定义的类,扩展HTMLElment元素
class CardComponent extends HTMLElement{};
//创建自定义HTML标签,必须包含连字符
customElement.define("card-component",CardComponent);//为了将来HTML拓展时不与用户的自定义标签冲突
```

### 6.4.4 自定义元素：生命期方法

- `constructor()`：创建自定义元素时调用
- `connectedCallback()：`自定义元素被插入文档时
- `disconnectCallback()：`自定义元素从文档中被移除时调用
- `attributeChangedCallback(attributeName,oldValue,newValue)：`指定的自定义元素属性被设置或修改时调用