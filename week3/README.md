# Description of program

***

### **宿題その1**

***

**電卓のプログラムで「*」「/」に対応せよ例： 3.0 + 4 * 2 − 1 / 5細かい仕様は適宜定義してよい**

**Write code to do calculations of numbers, including numbers addition, subtraction, multiplication, and division. Also, this program should be able to calculate decimals, such as 0.5, 5.8, 6.5…etc**

**[ヒント:]**

**1回目の評価で「x」「/」を処理 3.0 + 4 × 2 − 1 / 5 ⇒ 3.0 + 8 − 0.2**

**2回目の評価で「+」「−」を処理 3.0 + 8 − 0.2 ⇒ 3.6**

***

## 1. [week3_hw1.py](https://github.com/Stephanie1125/googlestep/blob/master/week3/week3_hw1.py) 

 For the calculation of numbers, here is the things and roles:

1. the decimals should be one number. ⇒ 3.6, 5.8 …. etc
2. if we met 「x」and「/」, we should calculate it first. 「x」and「/」have the same priority.
3. Then the「+」and「−」, we should calculate it in the end.

for the example,

**"4x5/4"** : we should do the calculation of 「x」first and then「/」⇒ the result should be 20/4 = 5

**"1.5x2"** ⇒ we should take 1.5 as one number ⇒ the result should be 3.0

**"1.5x1.5"** ⇒  we should take 1.5 as one number ⇒ the result should be 2.25

***

### **宿題その2（チャレンジしたい人向け）**

***

**さらに括弧に対応せよ Add parentheses: ()**

**例： (3.0 + 4 × (2 − 1)) ÷ 5**

***

## 2. [week3_hw2.py](https://github.com/Stephanie1125/googlestep/blob/master/week3/week3_hw2.py)

If we add parentheses as input in our program.

for the calculation of numbers, here is the roles:

1. the decimals should be one number. ⇒ 3.6, 5.8 …. etc
2. if we met () , we should calculate it first, parentheses hold higher priority than  the「x」and「/」
3. 「x」and「/」have the same priority.
4. we should calculate「+」and「−」, in the end.

In this program, we use the evaluate function from [week3_hw1.py](https://github.com/Stephanie1125/googlestep/blob/master/week3/week3_hw1.py) and change the function name to calculate function. This function do the calculation part in the input and also it will first calculate the part inside parentheses. In the evaluate function, we call the calculate function and then in this function, we use a stack to make sure we calculate the part inside parentheses first.

The stack deal with the parentheses and I first pop() the item from the list "tokens" 
as a result the order in the stack will be reversed( because we pop the items from the "tokens")
So if we want to do the calculation, we should take the reverse order to make sure we are doing the right calculation.(like 3/5 is not equal 5/3 so the order is very important!)

Also the reason I use the stack list is because I want to calculate the part with parentheses first and then put it back to the tokens list. The following is an example to explain how this program working. 

***

**if I input : (1+2)/3**

in the tokens list: </br>
**tokens= [{type: lpar}, {type:num, num: 1},{type: plus}, {type:num, num: 2}, {type: rpar}, {type: div}, {type: num, num: 3}]**

--> we pop item to stack 

**tokens = [] empty** </br>
**stack= [{type: num, num: 3}, {type: div}, {type: rpar}, {type:num, num: 2},{type: plus}, {type:num, num: 1},{type: lpar}]**

and we also record the index number of '(' and ')' because we want to calculate the () part first.

``calculate_part = stack[rpar_index + 1:lpar_index]``

—> [{type:num, num: 2},{type: plus}, {type:num, num: 1}] —> (2+1)

``calculate_part.reverse()`` 

—> [{type:num, num: 1},{type: plus}, {type:num, num: 2}] —> reverse it back (1+2) —> get 3

 And after we calculate the part with parentheses, we put it back into the tokens list. (get rid of parentheses)
We also put the remain part inside stack back to tokens list. 
as a result,

**tokens list: [{type:num, num: 3} {type: div}, {type: num, num: 3}] ---> 3/3 = 1**

and then we can call the calculate function and get the final result :)







