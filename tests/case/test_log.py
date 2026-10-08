from utils.log_util import LogUtil

# 获取日志实例
logger = LogUtil.get_logger()

def test_log_output():
    """测试日志工具能否正常输出日志到控制台+文件"""
    logger.info("===== 测试日志用例开始 =====")
    logger.debug("这是debug级别日志")
    logger.warning("这是warning警告日志")
    logger.error("这是error错误日志")
    logger.info("===== 测试日志用例结束 =====")