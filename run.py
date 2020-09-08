import kiwi

# train_config = '/home/snchen/project/openkiwi/experiments/train_nuqe.yaml'
# kiwi.train(train_config)

predict_config = '/home/snchen/project/openkiwi/experiments/predict_nuqe.yaml'
kiwi.predict(predict_config)
evaluate_config = '/home/snchen/project/openkiwi/experiments/evaluate_nuqe.yaml'
kiwi.evaluate(evaluate_config)
