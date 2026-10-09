import re


def extract_token(text: str) -> str | None:
    """
    从文本中提取token
    :param text: 包含token的原始文本，例如 resp: token=abc123456; expires=1752221111
    :return: 提取出来的token字符串，没有匹配到返回None
    """
    pattern = r"token=([^;]+)"
    res = re.search(pattern, text)
    if res:
        return res.group(1)
    return None


def check_email(email: str) -> bool:
    """
    校验邮箱格式是否合法
    :param email: 待校验邮箱字符串
    :return: 合法返回True，不合法返回False
    """
    pattern = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
    res = re.match(pattern, email)
    return res is not None


def extract_all_url(text: str) -> list:
    """
    批量提取文本内所有http/https链接
    :param text: 原始文本
    :return: 所有url组成的列表，无匹配返回空列表
    """
    pattern = r"(?:https|http)://[\w./?=&-]+"
    url_list = re.findall(pattern, text)
    return url_list


if __name__ == "__main__":
    # 自测demo
    print(extract_token("resp: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9; expires=1752221111"))
    print(check_email("test@petstore.com"))
    print(extract_all_url("访问地址：https://api.test.com/user?name=test，备用：http://demo.org"))
