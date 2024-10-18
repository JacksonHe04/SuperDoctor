# preprocess_data.py
import jieba  # 导入jieba库用于中文分词
from sklearn.feature_extraction.text import TfidfVectorizer  # 导入TF-IDF向量化工具
import pandas as pd  # 导入pandas库用于数据处理


# 对句子进行分词的函数
def tokenize_sentence(sentence):
    # 使用jieba对句子进行分词，并将结果用空格连接成字符串
    return " ".join(jieba.lcut(sentence))


# 对数据进行预处理的函数
def preprocess_data(data):
    """
    在DataFrame数据集中新增一个名为tokenized_sentence的列
    data['sentence']表示 data 中的一个sentence列
    apply方法用于将函数tokenize_sentence应用到sentence列中的每个元素上
    tokenize_sentence将句子切分为单词或词元（tokens）
    处理后的结果会被存储在列tokenized_sentence中
    """
    data['tokenized_sentence'] = data['sentence'].apply(tokenize_sentence)

    # 使用TF-IDF对文本进行向量化
    vectorizer = TfidfVectorizer()  # 初始化TF-IDF向量化器
    # fit_transform方法会先根据输入的文本数据，学习词汇表和IDF权重
    # 将分词后的句子的列转换为TF-IDF向量，便于机器学习模型的训练和预测
    X = vectorizer.fit_transform(data['tokenized_sentence'])

    # 返回向量化后的文本数据和原始数据中的'h', 't', 'r'列
    return X, data[['h', 't', 'r']]


if __name__ == "__main__":
    # 从dataset_loader.py导入load_data函数
    from dataset_loader import load_data

    # 加载数据
    train_data = load_data('train')  # 加载训练集数据
    val_data = load_data('val')  # 加载验证集数据
    test_data = load_data('test')  # 加载测试集数据

    print("已将数据从数据库加载到DataFrame！")

    # X_train是分词后的句子的文本向量，y_train是其他三个列（标签）
    # 对训练集、验证集和测试集进行预处理
    X_train, y_train = preprocess_data(train_data)  # 预处理训练集数据
    X_val, y_val = preprocess_data(val_data)  # 预处理验证集数据
    X_test, y_test = preprocess_data(test_data)  # 预处理测试集数据

    # 输出处理后数据的维度
    print(f"训练集文本向量维度: {X_train.shape}")  # 打印训练集文本向量的维度
    # 获取并打印训练集文本向量的第二个维度
    second_dimension = X_train.shape[1]
    print(f"这意味着从训练集中分词后共产生了{second_dimension}个词汇！")
    print(f"验证集文本向量维度: {X_val.shape}")  # 打印验证集文本向量的维度
    print(f"测试集文本向量维度: {X_test.shape}")  # 打印测试集文本向量的维度

