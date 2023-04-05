# Мультиклассовый классификатор

Данные  
http://archive.ics.uci.edu/ml/datasets/Image+Segmentation  

Число и АХ нейронов 1-го скрытого слоя  
40, logistic

Число и АХ нейронов 2-го скрытого слоя  
40, logistic

Число и АХ нейронов 3-го скрытого слоя  
20, logistic  

Число и АХ нейронов 4-го скрытого слоя  
10, logistic  

Режим обучения  
Stochastic

Возможные классы  
GRASS  
PATH  
WINDOW  
CEMENT  
FOLIAGE  
SKY  
BRICKFACE  

Результат на валидационной выборке

precision        recall     f1-score     support

           0       1.00      1.00      1.00       229
           1       0.99      0.95      0.97       216
           2       0.93      0.80      0.86       229
           3       0.93      0.89      0.91       226
           4       0.99      0.84      0.91       235
           5       1.00      0.99      1.00       217
           6       1.00      0.99      0.99       223

   micro avg       0.98      0.92      0.95      1575