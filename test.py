import logging

#レベル設定
logging.basicConfig(level=logging.INFO,
format="%(asctime)s - %(levelname)s:%(name)s - %(message)s",
filename="test.log")
logging.info('hello python test515 log')

print('hello python test515')