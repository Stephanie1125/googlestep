**Liu, Stephanie, Hsin-Wen**

**Google STEP homework — second week June 3rd**

***

**宿題その1**

***

**行列積を求めるプログラムを書いて、行列のサイズNと実行時間の関係を調べてみよう**

**Write code to calculate C = A \* B, where A, B and C are matrices of size N * NMeasure the execution time of your code for various Ns, and plot the relationship between N and the execution time**

GitHub URL: https://github.com/Stephanie1125/googlestep/tree/master/week2

Please check  [week2_hw.py](https://github.com/Stephanie1125/googlestep/blob/master/week2/week2_hw.py "week2_hw.py") for graphing program of the relationship between N=0 to 100 and the program execution time. Also please check the [README.md](https://github.com/Stephanie1125/googlestep/blob/master/week2/README.md "README.md") for more details of the matrix programs in [My Github](https://github.com/Stephanie1125/googlestep/tree/master/week2 "mygithub") of week two's homework-1. 

Programs are all mainly written in python3. (may add some programs written in some other programming languages for practicing new skills afterward)

***

**宿題その2**

***

**木構造を使えばO(log N)、ハッシュテーブルを使えばO(1)で検索・追加・削除を実現することができて、これだけ見ればハッシュテーブルのほうがはるかに優れているように見える。ところが、現実の大規模なデータベースでは、（もちろんいろいろなものがあるが）ハッシュテーブルではなく木構造が使われることが多い。その理由を考えよ。**

**The complexity of searching / adding / removing an element is O(1) with a hash table, whereas the complexity is O(log N) with a tree. This means that a hash table is more efficient than a tree. However, large-scale database systems used in a real world tend to prefer a tree to a hash table. Consider reasons why a tree is more preferred than a hash table for those database systems.**

​	Usually for evaluation of one's program, we will consider about two parts, first is the program execution running time and the second part is the memery space. As for hash table, you have to build the initial hash table with the approximate size of the input data you may have to use in your program. If the hash table you built doesn't have enough space for storing data, you have to rebuild and resize the table again and all the elements you first put in your first table should be rehashed again and it will take O(n) time, it depends on the size of your input data. 

​	For example, I first build a hash table with size of 10 and i put number 0~ 9 in my hash table (the space is full) and then i want to add element number 10 into my hash table, I have to rebuild another hash table with size 11 and rehash the number 0 ~ 10 into my new hash table, which takes O(n) if the time in this case (adding/ insertion).  On the other hand, for tree data structure, you don't have to know the size of the input data in advance.

​	Also, hash function may have highly chance to map the data into the same hash table index if we have large amount of input data. We will use array of linked list to connect the data in the same index. In this case, it will take O(n) to insert the data in the same index which may already have some data stored in it. (you have to add the data at the end of the array linked list to one index in the hash table), same idea for the removing data case. Not to mention that for using the hash table, data stay unsorted, so for the searching part, you have to go through all the data in the array linked list in order to find the one data you want to search after you know which index number it supposes to be in the hash table, which will take O(n) time. On the other hand, tree structure's data is sorted in some rule (go right if the data is larger than the root and go left if it is smaller than the root), it will take O(log N) in the case of binary search tree on the average.

​	As a result, if we consider the problem that hash table may have if it is a large scale database system, a tree is more preferred than a hash table because that for execution running time O(log N) is much faster than the O(n), also if we consider about the memory space, the space for tree data structure is the same as the data numbers, and for the hash table, we may have to use more space to build the initial hash table to avoid the case that you have to rebuild a new hash table.

***

**宿題その3 (余裕がある人のみ）**

***

**キャッシュの管理をほぼO(1)で実現できるデータ構造を考えよ**

**Design a cache that achieves the following operations with O(1)When a pair of  is given, find if the given pair is contained in the cache or notIf the pair is not contained, insert the pair into the cache after evicting the least recently accessed pair**











