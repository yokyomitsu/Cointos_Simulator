import yaml

class ConfigLoader:
    def load(self, filename):
        raise NotImplementedError("This method should be overridden by subclasses")

class YAMLConfigLoader(ConfigLoader):
    def load(self, filename):
        with open(filename, 'r') as f:
            return yaml.safe_load(f)
