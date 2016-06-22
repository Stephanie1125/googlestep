# Description of programs

***

## 宿題その1

***

**ページランクを実装してみましょう先ほどの人間関係のグラフを、簡単に読める形式にして [ここ](https://github.com/Stephanie1125/googlestep/tree/master/week4/sample_inputs) に上げておきます。 medium_data.txt がさっきのデータです。C言語だとhashmap的なデータ構造のライブラリがないので、ちょっと面倒度がアップしますが、たぶん書ける範囲だと思います。 できればのあるC++の方がおすすめですPythonとかRubyとかが楽でおすすめです**

**Implement the pagerank algorithm. Here’s [the sample inputs](https://github.com/Stephanie1125/googlestep/tree/master/week4/sample_inputs) you can use, including the relation graph in the previous slide (medium_data.txt).I recommend to use a laguage which has map/hashmap/dict or something like that -- specifically, like Python, Ruby. Implementing in plain C language might be a bit difficult because of the lack of these data structures, though it’s not impossible. Probably you can use C++ and  instead.**

***











***

## 宿題その2（1,2 行で十分です）

***

**このページランクアルゴリズムは、繰り返しを無限に行えば必ず収束しますか？もし収束しないなら、どういう解決策が考えられますか？**

**Does the pagerank algorithm I described converge always? If not, what can we do to make sure it converge?**

***

The pagerank algorithm will not converge always in all cases and the following is some examples cases that won't converge no matter how long the process of PageRank algorithm is running.![CaseNotConvergeforPageRank](CaseNotConvergeforPageRank.png)

We can tell that the cases are all form infinite loops or cycles. As a result, to make sure the model we apply converge, we should avoid infinite loops and cycles.

***

**実際にこのページランクアルゴリズムを使うとして、繰り返しはどのぐらいで止めるべきでしょうか？ （実用上はもちろん無限に繰り返すということはできないので、どこで止めるかという判断が必要になります）**

**When you use this algorithm in practice, you need to decide when to finish the iteration. How do you decide it?**

***

We finish the iteration process when the model is converge, which means that all nodes will have the same scores as its previous scores. As a result, we can compare scores for each process with its previous result, if two processes scores for every nodes are the same, it means the model is converge and we can finish the iteration process.

***

