# Python and Javascript

## Why Python
- Easy syntax
- Readable
- Popular


``` JS
var x = 2
var y = 2

funciton addTwoNumbers(a, b) {
    if (a === 5) {
        console.log("can't do 5")
    } else if (a === 9) {
        console.log("can't do 9 either")
    } else {
    sum = a + b
    console.log(sum)
    return sum
    }
}

addTwoNumbers(x, y)

```

``` Python
x = 2
y = 2

def add_two_numbers(a, b):
    if a == 5:
        print("can't do 5")
    elif a == 9:
        print("can't do 9 either")
    else:
        sum = a + b
        print(total)
        return total

add_two_numbers(x, y)
```


### Differences
| Java Script               | Python                     |
| -----------               | ---------------------------|
| function                  | def                        |
| {}                        | :                          |
| console.log               | print                      |
| variable declaration      | no declaration             |
| doesn't care about indent | cares greatly about indent |
| camalCase                 | snake_case, PascalCase     |


# Data Types

|Java Script | Python     | Java Script Literal | Python Literal |
| ---------- | ---------- | ------------------- | -------------- |
| string     | list       | " " or ' ' or \` \` |  " " or ' '    |
| boolean    | ...        | true or false       | True or False  |
| array      | list       | [ ... ]             | [ ... ]        |
| integers   | numbers    | 1, 2, 3             | 1, 2, 3        |
| floats     | numbers    | 1.0, 2.0, 3.0       | 1.0, 2.0, 3.0  |
| objects    | dictionary | { }                 | { }            |

|Java Script | Python        |
| ---------- | ------------- |
| arr.push   | list.append() |
| arr.pop()  | list.pop()    |