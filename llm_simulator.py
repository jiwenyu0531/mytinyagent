import numpy as np
import random
import string


def get_llm_response(message):
    return "".join(random.choices(string.ascii_letters + string.digits + " ", k=50))


def get_text_embedding(text):
    embedding = np.random.rand(768)  # 生成 768 维随机浮点数向量（范围 [0,1]）
    return embedding
