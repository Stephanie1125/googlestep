# Description of programs

1. **[solver_all_liu.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_all_liu.py)**

   Try all possible path and calculate all the distances and find the minimum distance.

   Only work for small tsp_size(N) —> N=16 not working

   | tsp_size (N) |    distance     |
   | :----------: | :-------------: |
   |    **5**     | **3291.621721** |
   |    **8**     | **3778.715416** |

2. **[solver_greedy_liu.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_greedy_liu.py)**

   Similar with the program [solver_greedy.py](https://github.com/Stephanie1125/google-step-tsp/blob/gh-pages/solver_greedy.py) but we start with the shortest distance path

   | tsp_size (N) |   distance   |
   | :----------: | :----------: |
   |      5       | 3418.101599  |
   |      8       | 3832.290094  |
   |      16      | 5843.912856  |
   |      64      | 10187.554517 |
   |     128      | 12465.051408 |
   |     512      | 25404.242145 |
   |     2048     | 44508.500299 |

3. **[solver_google_opt.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_google_opt.py)**

   Using google API (google or_tools)

   Library Import Error occurred —> Not sure if this is working or not

   Just want to check the result obtained from google TSP but this program cannot run due to library import problems.

4. **[solver_opt_2.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_opt_2.py)**

   apply opt_2 algorithm

   | tsp_size (N) |    distance     |
   | :----------: | :-------------: |
   |    **5**     | **3291.621721** |
   |      8       |   3832.290094   |
   |      16      |   4670.266134   |
   |      64      |   9543.278792   |
   |     128      |  11922.389313   |
   |     512      |  22722.036516   |
   |     2048     |  44508.500299   |

5. **[solver_or_opt.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_or_opt.py)**

   apply or_opt algorithm

   | tsp_size (N) |    distance     |
   | :----------: | :-------------: |
   |    **5**     | **3291.621721** |
   |    **8**     | **3778.715416** |
   |    **16**    | **4494.417962** |
   |      64      |   9735.256086   |
   |     128      |  14302.956710   |
   |     512      |  27626.930162   |
   |     2048     |  56982.682842   |

6. **[solver_mix_opt.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_mix_opt.py)**

   apply both opt_2 and or_opt algorithms

   | tsp_size (N) |     distance     |
   | :----------: | :--------------: |
   |    **5**     | **3291.621721**  |
   |    **8**     | **3778.715416**  |
   |    **16**    | **4494.417962**  |
   |      64      |   9445.796954    |
   |   **128**    | **11253.668891** |
   |     512      |   21749.244644   |
   |     2048     |   42801.432451   |

7. **[solver_mix_opt2.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_mix_opt2.py)**

   use the path obtained from **[solver_greedy_liu.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_greedy_liu.py)** as initial input path and then apply both opt_2 and or_opt algorithms on the initial path

   | tsp_size (N) |     distance     |
   | :----------: | :--------------: |
   |    **5**     | **3291.621721**  |
   |    **8**     | **3778.715416**  |
   |    **16**    | **4494.417962**  |
   |    **64**    | **8403.532157**  |
   |     128      |   11271.988369   |
   |   **512**    | **20917.757077** |
   |     2048     | runtime too long |

8. **[solver_mix_random.py](https://github.com/Stephanie1125/googlestep/blob/master/week6/liuweek6tsp/solver_mix_random.py)**

   use random initail path and then apply both opt_2 and or_opt algorithms on the initial path.

   —> different time will get different result (random)

   —> rewrite the result at solution_6.csv if we get better result

   | tsp_size (N) |     distance     |
   | :----------: | :--------------: |
   |   **2048**   | **42378.641570** |

   ​

