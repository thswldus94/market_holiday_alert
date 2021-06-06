import os
import configparser
import ast


def load_config_from_section(config_file, section, current_config=None) -> dict:

    if os.path.exists(config_file):

        parser = configparser.ConfigParser()

        parser.optionxform = str
        parser.read(config_file, 'utf-8')

        config = dict()

        if parser.has_section(section):
            for key, value in parser.items(section):
                config[key] = ast.literal_eval(value)

            # update config
            if current_config is not None:
                current_config.update(config)

        else:
            raise configparser.NoSectionError(section)

        return config

    else:
        raise FileNotFoundError(config_file)

