# model.py
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np


def create_model(input_shape, num_classes):
    """创建LSTM模型"""
    model = models.Sequential()

    # LSTM层
    # 添加输入层，指定输入数据的形状
    model.add(layers.Input(shape=input_shape))
    # 添加一个128个单元的LSTM层，return_sequences=False表示该层只返回最后一个时间步的输出
    model.add(layers.LSTM(128, return_sequences=False))

    # 全连接层
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(num_classes, activation='softmax'))  # 使用softmax输出多分类结果

    # 编译模型
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model


if __name__ == "__main__":
    from preprocess_data import preprocess_data
    from dataset_loader import load_data

    # 加载和预处理数据
    train_data = load_data('train')
    X_train, y_train = preprocess_data(train_data)

    # 获取输入特征维度和类别数量
    input_shape = (1, X_train.shape[1])  # 添加timesteps维度
    num_classes = len(set(y_train['r']))  # 关系类别数量

    # 重塑输入数据
    X_train_reshaped = np.reshape(X_train.toarray(), (X_train.shape[0], 1, X_train.shape[1]))

    # 创建模型
    model = create_model(input_shape, num_classes)

    # 输出模型概述
    model.summary()
