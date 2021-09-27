# ItemRecommender

Item Recommender based association rules mined on a dataset of transactions

# How To Use

1. Run [association.py](https://github.com/erick576/ItemRecommender/blob/master/association.py) and enter your preferred min support and confidence (Ex : min_sup = 0.02, min_conf = 0.7)
2. See association rules generated in [walmart_trans.csv](https://github.com/erick576/ItemRecommender/blob/master/walmart_trans.csv). These rules will be used to reccomend items for new transactions
3. Run [reccomendItem.py](https://github.com/erick576/ItemRecommender/blob/master/reccomendItem.py) and enter a new transaction (Ex : '2345, 3245, 34556')
4. The program should output items that are reccomended to you based on the items you just bought

# Example Output
![Output](https://user-images.githubusercontent.com/46385457/134830959-8c97e9ca-5879-45df-8746-8ab2112b803f.PNG)
