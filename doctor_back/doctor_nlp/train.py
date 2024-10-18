# train.py
import numpy as np
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from dataset_loader import load_data
from preprocess_data import preprocess_data
from model import create_model

if __name__ == "__main__":
    # 加载训练集和验证集数据
    train_data = load_data('train')
    val_data = load_data('val')

    # 提取训练集和验证集的句子
    train_sentences = train_data['sentence'].tolist()
    val_sentences = val_data['sentence'].tolist()

    # 合并训练集和验证集的句子，以生成统一的词汇表
    combined_sentences = train_sentences + val_sentences

    # 使用 TfidfVectorizer 构建词汇表，并对训练集和验证集进行向量化
    vectorizer = TfidfVectorizer(max_features=30000)  # 可以根据实际情况调整 max_features
    vectorizer.fit(combined_sentences)  # 基于合并后的句子生成词汇表

    # 对训练集和验证集进行词向量化
    X_train = vectorizer.transform(train_sentences)
    X_val = vectorizer.transform(val_sentences)

    '''
    使用LabelEncoder将关系标签y_train['r']和y_val['r']转换为整数编码。
    LabelEncoder可以将分类标签（例如“临床表现”、“药物治疗”等）转换为数值表示。
    '''
    label_encoder = LabelEncoder()
    y_train_encoded = label_encoder.fit_transform(train_data['r'])
    y_val_encoded = label_encoder.fit_transform(val_data['r'])

    # 获取输入特征维度和关系类别数量
    # input_shape表示LSTM的输入形状
    input_shape = (1, X_train.shape[1])  # 1为时间步数，词汇表维度为features
    num_classes = len(set(y_train_encoded))  # 关系类别数量

    # 将输入数据重塑为三维数组以适应LSTM的输入要求
    # 输入格式：(样本数, 时间步数, 特征数量)
    X_train_reshaped = np.reshape(X_train.toarray(), (X_train.shape[0], 1, X_train.shape[1]))
    X_val_reshaped = np.reshape(X_val.toarray(), (X_val.shape[0], 1, X_val.shape[1]))

    # 创建LSTM模型
    model = create_model(input_shape, num_classes)

    # 训练模型
    '''
    - X_train_reshaped和y_train_encoded是训练集的输入和标签
    - X_val_reshaped和y_val_encoded是验证集的输入和标签
    - epochs表示训练轮数
    - batch_size表示每个批次处理的样本数量
    '''
    model.fit(X_train_reshaped, y_train_encoded,
              validation_data=(X_val_reshaped, y_val_encoded),
              epochs=10,  # 可根据实际需求调整
              batch_size=32)  # 可根据实际需求调整

    # 保存训练好的模型为Keras格式
    model.save('medical_relationship_model.keras')
