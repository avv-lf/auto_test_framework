import pytest
from utils.file_handler import write_csv_report, read_csv_file, CaseParseError
import os

def test_write_and_read_csv(tmp_path):
    # 临时文件
    csv_file = tmp_path / "report.csv"
    data = [
        {"case_id": "case001", "name": "登录接口", "result": "PASS", "cost": "0.02"},
        {"case_id": "case002", "name": "查询接口", "result": "FAIL", "cost": "0.05"}
    ]
    headers = ["case_id", "name", "result", "cost"]
    # 写
    write_csv_report(str(csv_file), data, headers)
    # 读
    res = read_csv_file(str(csv_file))
    assert len(res) == 2
    assert res[0]["case_id"] == "case001"

def test_csv_missing_key(tmp_path):
    # 缺key场景，预期抛出CaseParseError
    csv_file = tmp_path / "tmp.csv"
    data = [{"case_id": "case001", "name": "登录接口"}]
    headers = ["case_id", "name", "result"]
    with pytest.raises(CaseParseError):
        write_csv_report(str(csv_file), data, headers)
