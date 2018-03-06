import logging

logger = logging.getLogger('TEST-LOG')#创建日志对象
logger.setLevel(logging.DEBUG)#设置日志等级

ch = logging.StreamHandler()#创建控制台对象
ch.setLevel(logging.DEBUG)

fh = logging.FileHandler(r'D:\s14\day4test\loging_test.log')#创建文件对象
fh.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s')#创建格式对象

fh.setFormatter(formatter)#添加文件输出格式
ch.setFormatter(formatter)#添加控制台输出格式

logger.addHandler(fh)#添加日志对象的文件对象
logger.addHandler(ch)#添加日志对象的控制台输出对象


logger.debug('debug message')
logger.info('info message')
logger.error('error message')
logger.critical('critical message')

# import logging
#
# # create logger
# logger = logging.getLogger('TEST-LOG')
# logger.setLevel(logging.DEBUG)
#
# # create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# # create file handler and set level to warning
# fh = logging.FileHandler(r"D:\s14\day4test\access.log")
# fh.setLevel(logging.WARNING)
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # add formatter to ch and fh
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)
#
# # add ch and fh to logger
# logger.addHandler(ch)
# logger.addHandler(fh)
#
# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')
