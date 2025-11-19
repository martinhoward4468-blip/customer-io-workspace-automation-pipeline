thonimport yaml
import os

def load_yaml_config(path):
 with open(path, "r") as f:
 return yaml.safe_load(f)

def load_env(path):
 env = {}
 with open(path, "r") as f:
 for line in f:
 if "=" in line:
 k, v = line.strip().split("=", 1)
 env[k] = v
 return env