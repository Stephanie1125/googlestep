# Description of programs

1. **[solver_all_liu.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_all_liu.py)**

   Try all possible path and calculate all the distances and find the minimum distance.

   Only work for small tsp_size(N) —> N=16 not working

   | tsp_size (N) | distance |
   | :----------: | :------: |
   |    **5**     |   3292   |
   |    **8**     |   3779   |

2. **[solver_greedy_liu.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_greedy_liu.py)**

   Similar with the program [solver_greedy.py](https://github.com/Stephanie1125/google-step-tsp/blob/gh-pages/solver_greedy.py) but we start with the shortest distance path

   | tsp_size (N) | distance |
   | :----------: | :------: |
   |      5       |   3418   |
   |      8       |   3832   |
   |      16      |   5844   |
   |      64      |  10188   |
   |     128      |  12465   |
   |     512      |  25404   |
   |     2048     |  44509   |

3. **[solver_google_opt.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_google_opt.py)**

   Using google API (google or_tools)

   Just want to check the result obtained from google TSP 

   (And google or_tools method almost beat everything —> cheated : P)

   Just for fun :)

   | tsp_size (N) | distance  |
   | :----------: | :-------: |
   |    **5**     | **3289**  |
   |    **8**     | **3775**  |
   |    **16**    | **4486**  |
   |      64      |   8587    |
   |   **128**    | **11016** |
   |   **512**    | **20612** |
   |   **2048**   | **40193** |

4. **[solver_opt_2.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_opt_2.py)**

   apply opt_2 algorithm

   | tsp_size (N) | distance |
   | :----------: | :------: |
   |      5       |   3292   |
   |      8       |   3832   |
   |      16      |   4670   |
   |      64      |   9543   |
   |     128      |  11922   |
   |     512      |  22722   |
   |     2048     |  44509   |

5. **[solver_or_opt.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_or_opt.py)**

   apply or_opt algorithm

   | tsp_size (N) | distance |
   | :----------: | :------: |
   |      5       |   3292   |
   |      8       |   3779   |
   |      16      |   4494   |
   |      64      |   9735   |
   |     128      |  14303   |
   |     512      |  27627   |
   |     2048     |  56983   |

6. **[solver_mix_opt.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_mix_opt.py)**

   apply both opt_2 and or_opt algorithms

   | tsp_size (N) | distance |
   | :----------: | :------: |
   |      5       |   3292   |
   |      8       |   3779   |
   |      16      |   4494   |
   |      64      |   9446   |
   |     128      |  11254   |
   |     512      |  21749   |
   |     2048     |  42801   |

7. **[solver_mix_opt2.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_mix_opt2.py)**

   use the path obtained from **[solver_greedy_liu.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_greedy_liu.py)** as initial input path and then apply both opt_2 and or_opt algorithms on the initial path.

   Yeah :) this method beat the **[solver_google_opt.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_google_opt.py)** for input_3.csv !!!

   | tsp_size (N) |     distance     |
   | :----------: | :--------------: |
   |      5       |       3292       |
   |      8       |       3779       |
   |      16      |       4494       |
   |    **64**    |     **8404**     |
   |     128      |      11272       |
   |     512      |      20918       |
   |     2048     | runtime too long |

8. **[solver_mix_random.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_mix_random.py)**

   use random initail path and then apply both opt_2 and or_opt algorithms on the initial path.

   —> different time will get different result (random)

   —> rewrite the result at solution_6.csv if we get better result

   | tsp_size (N) | distance |
   | :----------: | :------: |
   |     2048     |  42379   |

   ​

