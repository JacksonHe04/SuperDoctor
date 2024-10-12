import os
import mysql.connector
import jsonlines

# 连接MySQL数据库
cnx = mysql.connector.connect(
    user='root',
    password='vsmvpvp10MS',
    host='localhost',
    database='MedicalStore'
)
cursor = cnx.cursor()

# 指定包含.jsonl文件的目录路径
directory_path = './'

# 遍历目录中的所有.jsonl文件
for filename in os.listdir(directory_path):
    if filename.endswith('.jsonl'):
        file_path = os.path.join(directory_path, filename)
        table_name = os.path.splitext(filename)[0]  # 获取文件名作为表名

        # 创建表，不把id作为主键
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS `{table_name}` (
            `auto_id` INT AUTO_INCREMENT PRIMARY KEY,  -- 新的自增主键
            `id` INT,  -- 保留jsonl中的id
            `sentence` TEXT,
            `h` VARCHAR(255),
            `t` VARCHAR(255),
            `r` VARCHAR(255)
        )
        """
        cursor.execute(create_table_query)

        # 读取JSON Lines文件并插入数据
        with jsonlines.open(file_path) as reader:
            for obj in reader:
                # 获取JSON对象中的各个字段
                id_value = obj.get('id', 0)  # 使用0作为默认id值
                sentence_value = obj.get('sentence', '')
                h_value = obj.get('h', '')
                t_value = obj.get('t', '')
                r_value = obj.get('r', '')

                # 插入数据到MySQL数据库
                insert_query = f"""
                INSERT INTO `{table_name}` (`id`, `sentence`, `h`, `t`, `r`)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (id_value, sentence_value, h_value, t_value, r_value))

# 提交事务
cnx.commit()

# 关闭游标和连接
cursor.close()
cnx.close()