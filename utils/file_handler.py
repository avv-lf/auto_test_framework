import csv
import os
from typing import List, Dict


# ---------------------- 自定义框架异常类 ----------------------
class RequestError(Exception):
    """接口请求异常，http请求相关错误抛出"""
    pass


class CaseParseError(Exception):
    """用例解析异常，读取/解析用例文件出错抛出"""
    pass


# ---------------------- csv写测试报告函数 ----------------------
def write_csv_report(file_path: str, data_list: List[Dict], fieldnames: List[str]) -> None:
    """
    写入csv测试报告
    :param file_path: csv文件路径
    :param data_list: 字典列表，每一个字典代表一行用例结果
    :param fieldnames: 表头字段列表
    :raises CaseParseError: 数据格式不匹配、写入失败抛出
    """
    try:
        # 自动创建目录
        dir_path = os.path.dirname(file_path)
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # =========新增：校验每一行字典，必须包含所有表头key，缺key直接抛错=========
        for row in data_list:
            missing_keys = [k for k in fieldnames if k not in row]
            if missing_keys:
                raise KeyError(f"{missing_keys}")

        with open(file_path, "w", encoding="utf-8-sig", newline="") as f:
            # extrasaction="raise"：字典出现表头以外key，直接抛KeyError
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="raise")
            writer.writeheader()
            writer.writerows(data_list)
    except KeyError as e:
        # 字典key和fieldnames不匹配时触发（缺key / 多余key都会触发）
        raise CaseParseError(f"csv字段校验失败，key异常: {e}") from e
    except csv.Error as e:
        raise CaseParseError(f"csv文件格式错误: {e}") from e
    except OSError as e:
        raise CaseParseError(f"文件读写IO错误: {e}") from e
    except Exception as e:
        raise CaseParseError(f"写入csv报告未知异常: {e}") from e



# ---------------------- csv读文件函数 ----------------------
def read_csv_file(file_path: str) -> List[Dict]:
    """
    读取csv文件，返回字典列表
    :param file_path: csv文件路径
    :return: 每行数据转为字典组成的列表
    :raises CaseParseError: 文件不存在、解析异常抛出
    """
    result = []
    try:
        with open(file_path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                result.append(dict(row))
    except FileNotFoundError as e:
        raise CaseParseError(f"csv文件不存在：{file_path}") from e
    except csv.Error as e:
        raise CaseParseError(f"csv文件解析格式错误：{e}") from e
    except OSError as e:
        raise CaseParseError(f"文件IO读取失败：{e}") from e
    except Exception as e:
        raise CaseParseError(f"读取csv未知异常：{e}") from e
    return result
