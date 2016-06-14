# Description of program

***

## 1. [week3_hw_bug.py](https://github.com/Stephanie1125/googlestep/blob/master/week3/week3_hw1_bug.py)

**電卓のプログラムで「✕」「/」に対応せよ例： 3.0 + 4 × 2 − 1 / 5細かい仕様は適宜定義してよい**

**Write code to do calculations of numbers, including numbers addition, subtraction, multiplication, and division. Also, this program should be able to calculate decimals, such as 0.5, 5.8, 6.5…etc**

**[ヒント:]**

**1回目の評価で「x」「/」を処理 3.0 + 4 × 2 − 1 / 5 ⇒ 3.0 + 8 − 0.2**

**2回目の評価で「+」「−」を処理 3.0 + 8 − 0.2 ⇒ 3.6**

***

According to the hint, we do the calculation with the following step:

1. Calculate the part with「x」and「/」

    ```Num1``` + ```Num2 × Num3``` − ```Num4 / Num5``` ⇒ ```Num1``` + ```Num6``` − ```Num7``` 

   where, ```Num6 = Num2 × Num3``` and ```Num7 = Num4 / Num5```

2. Calculate the part with「+」and「-」

   ```Num1``` + ```Num6``` − ```Num7``` 

As a result, I wrote the following codes inside the **readNumber(line, index)** function:

```
if index < len(line) and line[index] == 'x':
    number = float(line[index-1]) * float(line[index+1])
    index += 2
if index < len(line) and line[index] == '/':
    number = float(line[index-1]) / float(line[index+1])
    index += 2
```

By doing this, I can save the result of  ```Num2 × Num3``` as ```Num6``` in the list  ```tokens``` , which plays an important role in the **evaluate(tokens)** function.

This program works fine with all the inputs which can do the calculation of「x」and「/」part first and then do the「+」and「−」part afterward.

**However, there are some bugs in this program.**

In some situation, this program is not working. 

For example,

if we enter **"4x5/4"** ⇒ the result will be "1.25" because the program only do the **"5/4"**

if we enter **"1.5x2"** ⇒ the result will be **"10"** because the program only do the **"5x2"**

if we enter **"1.5x1.5"** ⇒ the result will be **Invalid character found: .**

### இдஇ Oh no, SO MANY BUGS  இдஇ （泣きそう…） ###

So here comes the debug part and i wrote the second program.

***

## 2. [week3_hw_fixbug.py](https://github.com/Stephanie1125/googlestep/blob/master/week3/week3_hw1_fixbug.py)

So the reason that bugs appear is that I didn't think about the priority and the performance of calculating numbers very clear. So I decided to think it over again.

### **もう一度考え直してみますね =͟͟͞͞( •̀д•́)( •̀д•́)**

so for the calculation of numbers, here is the things and roles:

1. the decimals should be one number. ⇒ 3.6, 5.8 …. etc
2. if we met 「x」and「/」, we should calculate it first. 「x」and「/」have the same priority.
3. Then the「+」and「−」, we should calculate it in the end.

for the example,

**"4x5/4"** : we should do the calculation of 「x」first and then「/」⇒ the result should be 20/4 = 5

**"1.5x2"** ⇒ we should take 1.5 as one number ⇒ the result should be 3.0

**"1.5x1.5"** ⇒  we should take 1.5 as one number ⇒ the result should be 2.25

As a result, we cannot put the multiplication and division program inside the **readNumber(line, index)** because it will affect the decimals and also the priority of the「x」and「/」.

We should write it as the way we write the Pulse and Minus function. 

### **And the bugs all fixed.｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡**













