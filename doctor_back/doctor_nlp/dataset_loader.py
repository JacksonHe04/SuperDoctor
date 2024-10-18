# dataset_loader.py
import pymysql
import pandas as pd
from sqlalchemy import create_engine

# 数据库连接设置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'vsmvpvp10MS',
    'db': 'MedicalStore',  # 数据库名称
    'charset': 'utf8mb4'
}


# 从指定的数据表中加载数据
def load_data(table_name):
    # 创建数据库连接
    engine = create_engine(f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['db']}?charset={db_config['charset']}")

    # 构造SQL查询语句，用于从指定的数据库表中选择所有列，放在query中
    query = f"SELECT auto_id, sentence, h, t, r FROM {table_name}"

    # 使用pandas的read_sql方法执行SQL查询，将查询结果直接读入DataFrame中
    data = pd.read_sql(query, engine)
    print(f"pandas成功从{table_name}中加载数据！")

    return data


if __name__ == "__main__":
    # 加载训练集、验证集和测试集数据
    train_data = load_data('train')
    val_data = load_data('val')
    test_data = load_data('test')

    # 输出数据的基本信息
    print(f"训练集的行数和列数: {train_data.shape}")
    print(f"验证集的行数和列数: {val_data.shape}")
    print(f"测试集的行数和列数: {test_data.shape}")
