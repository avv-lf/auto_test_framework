import logging
import os
from datetime import datetime


class LogUtil:
    # 单例标记，保存全局唯一logger实例
    _logger = None

    @classmethod
    def get_logger(cls):
        if cls._logger is None:
            # 1. 创建logger对象，设置日志总级别
            cls._logger = logging.getLogger("auto_test_framework")
            cls._logger.setLevel(logging.DEBUG)

            # 清空旧处理器，防止多次实例化造成日志重复打印
            cls._logger.handlers.clear()

            # 2. 定义日志输出格式：时间 - 日志器名 - 日志级别 - 日志内容
            log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

            # 3. 自动创建logs文件夹
            log_dir = "logs"
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)

            # 按年月日生成日志文件名
            log_file_path = os.path.join(log_dir, f"{datetime.now().strftime('%Y%m%d')}.log")

            # 4. 文件处理器：写入日志文件，只记录INFO及以上级别
            file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
            file_handler.setFormatter(log_formatter)
            file_handler.setLevel(logging.INFO)

            # 5. 控制台处理器：终端打印，DEBUG级别全部输出
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(log_formatter)
            console_handler.setLevel(logging.DEBUG)

            # 6. 把两个处理器挂载到logger
            cls._logger.addHandler(file_handler)
            cls._logger.addHandler(console_handler)
        return cls._logger


# 全局唯一logger实例，其他模块直接导入使用
logger = LogUtil.get_logger()


# 本地单独运行此文件时执行测试代码
if __name__ == "__main__":
    logger.debug("调试信息，仅控制台输出")
    logger.info("测试用例开始执行")
    logger.warning("警告：token即将过期")
    logger.error("接口请求异常", exc_info=True)
