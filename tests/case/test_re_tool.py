from utils.re_tool import extract_token, check_email, extract_all_url

def test_extract_token():
    # 正常场景
    text1 = "resp: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9; expires=1752221111"
    assert extract_token(text1) == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    # 无token场景
    text2 = "resp: no token here"
    assert extract_token(text2) is None

def test_check_email():
    assert check_email("test@petstore.com") is True
    assert check_email("test#petstore.com") is False

def test_extract_all_url():
    text = "访问地址：https://api.test.com/user?name=test，备用：http://demo.org"
    assert extract_all_url(text) == ["https://api.test.com/user?name=test", "http://demo.org"]
