# Beautiful Soup 4

> 作者：lurf21

为了更好的阅读体验，建议[点击下载本文档的 `ipynb` 格式](BeautifulSoup4.ipynb)。

## 环境准备

在开始之前，你需要先安装 Beautiful Soup 4。


```python
! pip install beautifulsoup4
```

可以通过一下代码检测你是否安装成功：


```python
import bs4
bs4.__version__
```


    '4.11.1'

Beautiful Soup 4 对 HTML/XML 文件的解析是依赖于解析器的，支持 Python 标准库中的 HTML 解析器，还支持第三方的解析器 lxml 和 html5lib。下表列出了不同解析器的优缺点，你可以根据需求选择合适的解析器，并使用 pip 或其他方式安装。

| 解析器               | 使用方法                                                     | 优点                                                         | 缺点                                 |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------ |
| Python’s html.parser | `BeautifulSoup(markup, "html.parser")`                       | 1.Python 标准库内置 2.速度不错 3.容错性不错                  | 不如 lxml 快，不如 html5lib 容错性好 |
| lxml’s HTML parser   | `BeautifulSoup(markup, "lxml")`                              | 1.极快的速度 2.容错性不错                                    | 需要安装额外的C语言库                |
| lxml’s XML parser    | `BeautifulSoup(markup, "lxml-xml")`/`BeautifulSoup(markup, "xml")` | 1.极快的速度 2.目前唯一支持的 XML 解析器                     | 需要安装额外的C语言库                |
| html5lib             | `BeautifulSoup(markup, "html5lib")`                          | 1.极佳的容错性（以浏览器的方式解析文档）2.生成 HTML5 格式文档 | 速度慢                               |



如果你图方便，可以选择 Python 内置的解析器，其速度和容错性也足以满足大多数需求；如果你追求速度，那么 lxml 一定是不二之选；如果待解析的 HTML 文件非常复杂，需要较高容错性，那么选择 html5lib ;如果你要解析的是 XML，就只能选择 lxml 了。

另外需要注意的是，不同解析器对同一文档的解析结果仍可能不同，若文档存在不符合标准的语法，那么它被不同解析器解析后可能会生成不同结构的树型文档。因此，在团队合作中最好将使用的解析器进行说明并统一。

## 基本使用

首先，我们传入字符串或文件句柄到 `BeautifulSoup` 构造方法中，我们便可以轻松得到 `soup` 对象。在这个过程中，字符串/文档被转换为 Unicode，并且 HTML 实例都被转换成 Unicode 编码。


```python
from bs4 import BeautifulSoup
soup = BeautifulSoup("<html>data</html>")
soup
```


    <html><body><p>data</p></body></html>

## 对象的种类

Beautiful Soup 将复杂 HTML 文档转换成一个复杂的树形结构，每个节点都是 Python 对象，所有对象可以归纳为4种: `Tag` ， `NavigableString` ， `BeautifulSoup` ， `Comment` 。我们下面来逐一介绍。

### Tag

`Tag` 对象和原生 HTML 或 XML 文档中的 tag 相同。


```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
type(tag)
```


    bs4.element.Tag

Tag 中最重要的属性有 name 和 attributes。每个 tag 都有它自己的名字，可以用 `.name` 方法获取。


```python
tag.name
```


    'b'

如果改变了 tag 的 name，那将影响所有通过当前 Beautiful Soup 对象生成的文档:


```python
tag.name = "blockquote"
soup
```


    <html><body><blockquote class="boldest">Extremely bold</blockquote></body></html>

一个 tag 可能有多个属性。tag `<b class="boldest">` 有一个 `class` 的属性，值为 `boldest` 。tag 的属性的操作方法与字典类似：


```python
tag['class']
```


    ['boldest']

也可以用 `.attrs` 方法获取所有属性。


```python
tag.attrs
```


    {'class': ['boldest']}

tag 的属性可以被添加，删除或修改。


```python
tag['class'] = 'verybold'
tag['id'] = 1
print(tag)

del tag['class']
del tag['id']
print(tag.get('class'))
```

    <blockquote class="verybold" id="1">Extremely bold</blockquote>
    None


### NavigableString

字符串常被包含在 tag 内。Beautiful Soup 用 `NavigableString` 类来包装 tag 中的字符串：


```python
print(type(tag.string))
tag.string
```

    <class 'bs4.element.NavigableString'>
    
    'Extremely bold'

通过 `str()` 方法可以直接将 `NavigableString` 对象转换成Unicode字符串：


```python
unicode_string = str(tag.string)
type(unicode_string)
```


    str

字符串是不能直接被编辑的，但是可以通过 `replace_with()` 方法来替换字符串：


```python
tag.string.replace_with("No longer bold")
tag
```


    <blockquote>No longer bold</blockquote>

### BeautifulSoup

`BeautifulSoup` 对象将已解析的文档作为一个整体表示。大多数时候可以把它看作 `Tag` 对象。你可以通过一些操作将两个已解析的文档进行合并：


```python
doc = BeautifulSoup("<document><content/>INSERT FOOTER HERE</document", "xml")
footer = BeautifulSoup("<footer>Here's the footer</footer>", "xml")
doc.find(text="INSERT FOOTER HERE").replace_with(footer)
doc
```


    <?xml version="1.0" encoding="utf-8"?>
    <document><content/><footer>Here's the footer</footer></document>

`BeautifulSoup` 对象并不是真正的 HTML 或 XML 的 tag，但可以使用它的 `.name` 方法, `BeautifulSoup` 对象包含了一个值为 `[document]` 的特殊属性。


```python
soup.name
```


    '[document]'

### Comments and other special strings

虽然上述三种对象可以几乎覆盖 HTML 和 XML 中的所有内容，但仍然会存在一些其他的特殊对象，比如注释。


```python
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
type(comment)
```


    bs4.element.Comment

该 `Comment` 对象只是一种特殊类型 `NavigableString`：


```python
comment
```


    'Hey, buddy. Want to buy a used parser?'

## Navigating the tree

以“三姐妹”的文档为例：


```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')
```

### Going down

#### Navigating using tag names

一个 Tag 可能包含多个字符串或其它的 Tag，这些都是这个 Tag 的子节点。Beautiful Soup 提供了许多操作和遍历子节点的方法。

操作文档树最简单的方法就是告诉它你想获取的 tag 的 name。如果想获取 `<head>` 标签，只要用 `soup.head` ：


```python
soup.head
```


    <head><title>The Dormouse's story</title></head>

如果你想获取某个 tag 的子节点，可以重复调用该方法，比如 `soup.head.title` ：


```python
soup.head.title
```


    <title>The Dormouse's story</title>

#### `.contents` and `.children`

tag 的 `.contents` 属性可以将 tag 的子节点以列表的方式输出：


```python
head_tag = soup.head
print(head_tag.contents)
title_tag = head_tag.contents[0]
title_tag.contents
```

    [<title>The Dormouse's story</title>
    
    ["The Dormouse's story"]

`BeautifulSoup` 对象也有子节点，在这个例子中，`<html>`标签就是它的一个子节点：


```python
print(len(soup.contents))
soup.contents[0].name
```

    1
    
    'html'

需要注意的是，string 对象没有 `.contents` 属性。

你可以通过 `.children` generator 来遍历所有子节点：


```python
for child in title_tag.children:
    print(child)
```

    The Dormouse's story


#### `.descendants`

`.descendants` 属性可以对 tag 的所有子孙节点进行递归遍历：


```python
for child in head_tag.descendants:
    print(child)
```

    <title>The Dormouse's story</title>
    The Dormouse's story


#### `.string`

如果一个 tag 仅有一个子节点,那么这个 tag 也可以使用 `.string` 方法得到子节点。


```python
title_tag.string
```


    "The Dormouse's story"

如果包含了多个子节点，那么就会返回 `None` ：


```python
print(soup.html.string)
```

    None


#### `.strings` and `stripped_strings`

如果 tag 包含了多个子节点，可以使用 `.strings` 或 `stripped_strings` 来获取所有子节点：


```python
for string in soup.strings:
    print(repr(string))
```

    "The Dormouse's story"
    '\n'
    '\n'
    "The Dormouse's story"
    '\n'
    'Once upon a time there were three little sisters; and their names were\n'
    'Elsie'
    ',\n'
    'Lacie'
    ' and\n'
    'Tillie'
    ';\nand they lived at the bottom of a well.'
    '\n'
    '...'
    '\n'


`stripped_strings` 的作用是清除空格和空行：


```python
for string in soup.stripped_strings:
    print(repr(string))
```

    "The Dormouse's story"
    "The Dormouse's story"
    'Once upon a time there were three little sisters; and their names were'
    'Elsie'
    ','
    'Lacie'
    'and'
    'Tillie'
    ';\nand they lived at the bottom of a well.'
    '...'


### Going up

#### `.parent`

`.parent` 属性用来获取 tag 的父节点：


```python
title_tag = soup.title
title_tag.parent
```


    <head><title>The Dormouse's story</title></head>

文档的根节点是 `BeautifulSoup` 对象，它的父节点是 `None` ：


```python
html_tag = soup.html
print(type(html_tag.parent))
print(soup.parent)
```

    <class 'bs4.BeautifulSoup'>
    None


#### `.parents`

`.parents` 属性可以对 tag 的所有父节点进行递归遍历：


```python
link = soup.a
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
```

    p
    body
    html
    [document]


### Going sideways

我们使用一个简单的例子：


```python
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'lxml')
print(sibling_soup.prettify())
```

    <html>
     <body>
      <a>
       <b>
        text1
       </b>
       <c>
        text2
       </c>
      </a>
     </body>
    </html>


因为 `<b>` 标签和 `<c>` 标签是同一层：他们是同一个元素的子节点，所以 `<b>` 和 `<c>` 可以被称为兄弟节点。一段文档以标准格式输出时，兄弟节点有相同的缩进级别。在代码中也可以使用这种关系。

#### `.next_sibling` and `.previous_sibling`

`.next_sibling` 和 `.previous_sibling` 属性可以来查询兄弟节点：


```python
print(sibling_soup.b.previous_sibling)
sibling_soup.b.next_sibling
```

    None
    
    <c>text2</c>


```python
print(sibling_soup.c.next_sibling)
sibling_soup.c.previous_sibling
```

    None
    
    <b>text1</b>

值得注意的是，实际文档中的 tag 的 `.next_sibling` 和 `.previous_sibling` 属性通常可能是空白。

#### `.next_siblings` and `.previous_siblings`

`.next_siblings` 和 `.previous_siblings` 属性可以对 tag 的所有兄弟节点进行递归遍历：


```python
for sibling in soup.a.next_siblings:
    print(repr(sibling))
```

    ',\n'
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    ' and\n'
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    ';\nand they lived at the bottom of a well.'

```python
for sibling in soup.find(id="link3").previous_siblings:
    print(repr(sibling))
```

    ' and\n'
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    ',\n'
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    'Once upon a time there were three little sisters; and their names were\n'


### Going back and forth

#### `.next_element` and `.previous_element`

`.next_element` 属性指向解析过程中下一个被解析的对象，结果可能与 `.next_sibling` 相同，但通常不同。


```python
last_a_tag = soup.find("a", id="link3")
print(last_a_tag.next_sibling)
last_a_tag.next_element
```

    ;
    and they lived at the bottom of a well.
    
    'Tillie'

`.previous_element` 属性则指向解析过程中上一个被解析的对象。


```python
print(last_a_tag.previous_element)
last_a_tag.previous_element.next_element
```

     and


    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

#### `.next_elements` and `.previous_elements`

`.next_elements` 和 `.previous_elements` 迭代器就可以向前或向后访问文档的解析内容，就好像文档正在被解析一样：


```python
for element in last_a_tag.next_elements:
    print(repr(element))
```

    'Tillie'
    ';\nand they lived at the bottom of a well.'
    '\n'
    <p class="story">...</p>
    '...'
    '\n'


## Searching the tree

与遍历文档树相比，我们更常用的是搜索文档树。其中最重要的两个方法就是 `.find()` 和 `.find_all()` ，我们将在接下来主要介绍它们。我们仍然用之前的例子：


```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')
```

### Kinds of filters

在介绍 `find_all()` 方法之前，我们首先来了解一些常用的 filter。

#### A string

传入一个字符串参数，将会查找与字符串完整匹配的内容，默认为 UTF-8 编码：


```python
soup.find_all('b')
```


    [<b>The Dormouse's story</b>]

#### A regular expression

传入正则表达式，将会调用 `re.search()` 方法，并返回匹配的结果：


```python
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
```

    body
    b


#### A list

传入列表，将会返回与列表中任一元素匹配的内容：


```python
soup.find_all(["a", "b"])
```


    [<b>The Dormouse's story</b>,
     <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
     <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
     <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#### `True`

`True` 可以匹配任何值，但不会返回字符串节点：


```python
for tag in soup.find_all(True):
    print(tag.name)
```

    html
    head
    title
    body
    p
    b
    p
    a
    a
    a
    p


#### A function

你还可以自定义一个函数，接收一个元素参数，并返回一个布尔值。下面是一个例子：


```python
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
soup.find_all(has_class_but_no_id)
```


    [<p class="title"><b>The Dormouse's story</b></p>,
     <p class="story">Once upon a time there were three little sisters; and their names were
     <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
     <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
     <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
     and they lived at the bottom of a well.</p>,
     <p class="story">...</p>]

你可以发挥想象力，创造更多满足自己需要的 filter。

### `find_all()`

```python
find_all(name, attrs, recursive, string, limit, **kwargs)
```

下面我们来解释一下各个参数的意义：

#### `name` 参数

查找所有名为 `name` 的 tag。


```python
soup.find_all("title")
```


    [<title>The Dormouse's story</title>]

#### keyword 参数

如果一个指定名字的参数不是搜索内置的参数名，搜索时会把该参数当作指定名字 tag 的属性来搜索，如果包含一个名字为  id 的参数，Beautiful Soup 会搜索每个 tag 的 id 属性.


```python
soup.find_all(id=True)
```


    [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
     <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
     <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

使用多个指定名字的参数可以同时过滤 tag 的多个属性：


```python
soup.find_all(href=re.compile("elsie"), id='link1')
```


    [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

有些 tag 属性在搜索不能使用，比如 HTML5 中的 data-* 属性，但是可以通过 `find_all()` 方法的 `attrs` 参数定义一个字典参数来搜索包含特殊属性的 tag：


```python
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(attrs={"data-foo": "value"})
```


    [<div data-foo="value">foo!</div>]

#### `string` 参数

通过 `string` 参数搜索文档中的字符串内容。同样接受不同的 filter。


```python
print(soup.find_all(string="Elsie"))
print(soup.find_all(string=["Tillie", "Elsie", "Lacie"]))
soup.find_all(string=re.compile("Dormouse"))
```

    ['Elsie']
    ['Elsie', 'Lacie', 'Tillie']
    
    ["The Dormouse's story", "The Dormouse's story"]

#### `limit` 参数

`limit` 参数指定搜索的最大数量。对于大文档，如果我们不需要所有的结果，那么这个参数是非常有用的。


```python
soup.find_all("a", limit=2)
```


    [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
     <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>

#### `recursive` 参数

`find_all()` 方法默认搜索所有子孙节点，如果只想搜索当前节点的直接子节点，可以设置 `recursive`


```python
print(soup.html.find_all("title"))
soup.html.find_all("title", recursive=False)
```

    [<title>The Dormouse's story</title>]
    
    []

### Calling a tag is like calling `find_all()`

由于 `find_all()` 几乎是 Beautiful Soup 中最常用的搜索方法，所以定义了简写方法。下面左右的代码是等价的：


```python
soup.find_all("a") == soup("a")
```


    True

### `find()`

```python
find(name, attrs, recursive, string, **kwargs)
```

当我们只想要一个搜索结果时，使用 `find()` 方法或许是更好的选择。`find()` 方法在找不到匹配对象时，返回 `None`。

除了 `find()` 和 `find_all()` 方法，Beautiful Soup 还提供了十个用于搜索的 API，它们是 `find_parents()`, `find_parent()`, `find_next_siblings()`, `find_next_sibling()`, `find_previous_siblings()`, `find_previous_sibling()`, `find_all_next()`, `find_next()`, `find_all_previous()`, `find_previous()`.它们的用法和参数都 `find_all()` 类似，通过函数名也可以大致知道它们的作用，相信你可以很快掌握它们的用法。

`find()` 和 `find_all()` 方法虽然很常用，用来搜索一些结构简单的文档非常方便，但是如果你想搜索一个结构非常复杂的文档，那么 `find()` 和 `find_all()` 方法是不够的。

比如，在一些场景下，你想搜索的 tag 可能除了包含的内容，和其他一些 tag 完全一样，包括 tag 的名字和其他的属性，但是它们的内容不都是你想要的。这时如果你用 `find_all()` 方法，得到的结果并不尽人意，同时筛选起来也非常困难。对于这种情况，我的建议是打开浏览器开发者模式，然后查看 HTML 源码，厘清你想要的 tag 和其他内容的父子、兄弟等层级关系，最后用 `find()` 和 `find_all()` 结合上面提到的其他十个 API 来搜索。总之，灵活应用这些搜索的 API 能使你对文档的解析更快也更轻松。

### CSS 选择器

Beautiful Soup 支持大部分的 CSS 选择器，详见 http://www.w3.org/TR/CSS2/selector.html， 在 Tag 或 BeautifulSoup 对象的 `.select()` 方法中传入字符串参数， 即可使用 CSS 选择器的语法找到 tag。对于熟悉CSS选择器语法的人来说这是个非常方便的方法。具体用法可以参考官方文档，在此不再赘述。

## Modifying the tree

Beautiful Soup 的强项是文档树的搜索，但同时也可以方便的修改文档树

### 修改 Tag 的名称和属性

在 Tag 的部分已经讲解过，请参考前面对应内容。

### 修改 `.string`

给 tag 的 `.string` 属性赋值，就相当于用当前的内容替代了原来的内容：


```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
tag = soup.a
tag.string = "New link text."
tag
```


    <a href="http://example.com/">New link text.</a>

### `.append()`

向 tag 中添加内容，就像 Python 列表的 `append()` 方法一样：


```python
soup = BeautifulSoup("<a>Foo</a>")
soup.a.append("Bar")

print(soup)
soup.a.contents
```

    <html><body><a>FooBar</a></body></html>
    
    ['Foo', 'Bar']

### `extend()`

按顺序向 tag 中添加列表。


```python
soup = BeautifulSoup("<a>Soup</a>", 'html.parser')
soup.a.extend(["'s", " ", "on"])

print(soup)
soup.a.contents
```

    <a>Soup's on</a>
    
    ['Soup', "'s", ' ', 'on']

### `NavigableString()` 和 `.new_tag()`

`NavigableString()` 可以添加一段文本内容到文档中：


```python
from bs4 import NavigableString
soup = BeautifulSoup("<b></b>")
tag = soup.b
tag.append("Hello")
new_string = NavigableString(" there")
tag.append(new_string)
tag.contents
```


    ['Hello', ' there']

如果想要创建一段注释，或 `NavigableString` 的任何子类，只要调用 NavigableString 的构造方法：


```python
from bs4 import Comment
new_comment = soup.new_string("Nice to see you.", Comment)
tag.append(new_comment)
tag
tag.contents
```


    ['Hello', ' there', 'Nice to see you.']

创建一个 tag 最好的方法是调用工厂方法 `BeautifulSoup.new_tag()`：


```python
soup = BeautifulSoup("<b></b>")
original_tag = soup.b

new_tag = soup.new_tag("a", href="http://www.example.com")
original_tag.append(new_tag)
print(original_tag)

new_tag.string = "Link text."
original_tag
```

    <b><a href="http://www.example.com"></a></b>
    
    <b><a href="http://www.example.com">Link text.</a></b>

### `insert()`

`insert()` 方法与 `append()` 方法类似，区别是不会把新元素添加到父节点 `.contents` 属性的最后，而是把元素插入到指定的位置：


```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
tag = soup.a

tag.insert(1, "but did not endorse ")
print(tag)
tag.contents
```

    <a href="http://example.com/">I linked to but did not endorse <i>example.com</i></a>
    
    ['I linked to ', 'but did not endorse ', <i>example.com</i>]

### `insert_before` 和 `insert_after`

在当前 tag 或字符串之前或之后插入内容：


```python
soup = BeautifulSoup("<b>stop</b>")
tag = soup.new_tag("i")
tag.string = "Don't"
soup.b.string.insert_before(tag)
soup.b
```


    <b><i>Don't</i>stop</b>


```python
soup.b.i.insert_after(soup.new_string(" ever "))
print(soup.b)
soup.b.contents
```

    <b><i>Don't</i> ever stop</b>
    
    [<i>Don't</i>, ' ever ', 'stop']

### `clear()`

清空 tag 中的内容：


```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
tag = soup.a

tag.clear()
tag
```


    <a href="http://example.com/"></a>

### `extract()`

将当前 tag 或字符串从文档树中移除，并返回移除的内容：


```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a
i_tag = soup.i.extract()

print(a_tag)
print(i_tag)
print(i_tag.parent)
```

    <a href="http://example.com/">I linked to </a>
    <i>example.com</i>
    None


### `decompose()`

将当前节点从文档树中移除并完全销毁：


```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a
i_tag = soup.i
soup.i.decompose()

a_tag
```


    <a href="http://example.com/">I linked to </a>

可以用 `.decomposed` 属性检查节点是否已经被销毁。


```python
print(i_tag.decomposed)
a_tag.decomposed
```

    True
    
    False

### `replace_with()`

移除文档树中的某段内容，并用新 tag 或文本节点替代它：


```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a

new_tag = soup.new_tag("b")
new_tag.string = "example.com"
a_tag.i.replace_with(new_tag)

print(a_tag)

bold_tag = soup.new_tag("b")
bold_tag.string = "example"
i_tag = soup.new_tag("i")
i_tag.string = "net"
a_tag.b.replace_with(bold_tag, ".", i_tag)

a_tag
```

    <a href="http://example.com/">I linked to <b>example.com</b></a>
    
    <a href="http://example.com/">I linked to <b>example</b>.<i>net</i></a>

### `wrap()`

对指定的 tag 元素进行包装，并返回包装后的结果：


```python
soup = BeautifulSoup("<p>I wish I was bold.</p>")
soup.p.string.wrap(soup.new_tag("b"))

soup.p.wrap(soup.new_tag("div"))
```


    <div><p><b>I wish I was bold.</b></p></div>

### `unwrap()`

将包装的 tag 元素从包装的 tag 中移除，常用来进行标记的解包：


```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
a_tag = soup.a

a_tag.i.unwrap()
a_tag
```


    <a href="http://example.com/">I linked to example.com</a>

## 输出

### Pretty-printing

`prettify()` 方法将 Beautiful Soup 的文档树格式化后以 Unicode 编码输出，每个 XML/HTML 标签都独占一行，十分优雅。


```python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
print(soup.prettify())
```

    <html>
     <body>
      <a href="http://example.com/">
       I linked to
       <i>
        example.com
       </i>
      </a>
     </body>
    </html>


`BeautifulSoup` 对象和它的 tag 节点都可以调用 `prettify()` 方法:


```python
print(soup.a.prettify())
```

    <a href="http://example.com/">
     I linked to
     <i>
      example.com
     </i>
    </a>


需要注意的是，由于这种输出方法会添加换行符和空白字符，所以不要用它去 reform 文档。它的意义在于让你较为清晰的看清楚文档的结构。

### Output formatters

Beautiful Soup 输出是会将 HTML 中的特殊字符转换成 Unicode，比如 &lquot：


```python
soup = BeautifulSoup("&ldquo;Hello World!&rdquo; he said.")
str(soup)
```


    '<html><body><p>“Hello World!” he said.</p></body></html>'

你也可以将 Unicode 编码转换为 UTF-8 编码：


```python
soup.encode("utf8")
```


    b'<html><body><p>\xe2\x80\x9cHello World!\xe2\x80\x9d he said.</p></body></html>'

在输出过程中，你可以通过设置 `formatter` 属性来指定输出的格式。由于这部分在实际工程中应用并不多，如果你想进一步学习，请参考官方文档或阅读源代码。

### `get_text()`

如果只想得到 tag 中包含的文本内容，那么可以调用 `get_text()` 方法，这个方法获取到 tag 中包含的所有文版内容包括子孙 tag 中的内容，并将结果作为 Unicode 字符串返回：


```python
markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
soup = BeautifulSoup(markup)

soup.get_text()
```


    '\nI linked to example.com\n'

可以通过参数指定 tag 的文本内容的分隔符：


```python
soup.get_text("|")
```


    '\nI linked to |example.com|\n'

还可以去除获得文本内容的前后空白字符：


```python
soup.get_text("|", strip=True)
```


    'I linked to|example.com'

或者使用 `.stripped_strings` generator，获得文本列表后手动处理列表：


```python
[text for text in soup.stripped_strings]
```


    ['I linked to', 'example.com']

## 编码

Beautiful Soup 会自动检测文档的编码，并将文档转换为 Unicode。如果你安装了 Python 库 `charset-normalizer`， `chardet` 或 `cchardet`，猜测编码的准确率会大幅提高。你可以通过传入 `from_encoding` 参数来指定编码方式。

同时需要注意，无论输入文档的编码方式是什么，Beautiful Soup 的输出编码均为 UTF-8。

## 解析部分文档

`SoupStrainer` 类可以定义文档的某段内容，这样搜索文档时就不必先解析整篇文档，只会解析在 `SoupStrainer` 中定义过的文档。创建一个 `SoupStrainer` 对象并作为 parse_only 参数给 BeautifulSoup 的构造方法即可。

下面我们给出三个例子：


```python
from bs4 import SoupStrainer

only_a_tags = SoupStrainer("a")

only_tags_with_id_link2 = SoupStrainer(id="link2")

def is_short_string(string):
    return string is not None and len(string) < 10
only_short_strings = SoupStrainer(string=is_short_string)
```


```python
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

print(BeautifulSoup(html_doc, "html.parser", parse_only=only_a_tags).prettify())
print(BeautifulSoup(html_doc, "html.parser", parse_only=only_tags_with_id_link2).prettify())
print(BeautifulSoup(html_doc, "html.parser", parse_only=only_short_strings).prettify())
```

    <a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>
    <a class="sister" href="http://example.com/lacie" id="link2">
     Lacie
    </a>
    <a class="sister" href="http://example.com/tillie" id="link3">
     Tillie
    </a>
    <a class="sister" href="http://example.com/lacie" id="link2">
     Lacie
    </a>
    Elsie
    ,
    Lacie
    and
    Tillie
    ...

## Debug

如果想知道 Beautiful Soup 到底怎样处理一份文档，可以将文档传入 diagnose() 方法，Beautiful Soup 会输出一份报告，说明不同的解析器会怎样处理这段文档，并标出当前的解析过程会使用哪种解析器。通过如下方式开始使用：

```python
from bs4.diagnose import diagnose
```

## 参考及更多学习资源

以上就是关于 Beautiful Soup 4 的全部内容了，希望能在解析文档的过程中帮助你。下面列出了一些参考资料和更多的学习资源：

- [Beautiful Soup Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [HTML 语言基础](https://docs.net9.org/languages/html/)
- [Python爬虫利器之Beautiful Soup的用法](https://cuiqingcai.com/1319.html)