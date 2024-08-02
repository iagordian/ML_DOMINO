
import json

from config.config import DATA_PACKAGES_DIR, UPLOAD_LOG_DIR

class Uploader:

    def __init__(self, files, funcs):
        self.files = files
        self.funcs = funcs
        self.names = list(files.keys())
        self.total = 0
        self.successful = 0
        self.errors = {}

    def upload(self):

        for name in self.names:

            func = self.funcs[name]
            file = DATA_PACKAGES_DIR + self.files[name]

            with open(file) as file:
                content = file.read()

            try:
                func(content)

            except Exception as e:
                self.errors[name] = str(e)

            else:
                self.successful += 1

            finally:
                self.total += 1

    def print_message(self):

        print(f'{self.successful} / {self.total} пакетов данных загружены успешно')

        if self.total != self.successful:
            print(f'Ошибки произошли при загрузке {", ".join(list(self.errors.keys()))}')
            print('Ошибки сохранены в файл upload_log')

    def log(self):

        if self.errors:
            file_name = UPLOAD_LOG_DIR + 'upload_error.json'
            with open(file_name, 'w') as file:
                json.dump(self.errors, file, indent=3, ensure_ascii=False)

