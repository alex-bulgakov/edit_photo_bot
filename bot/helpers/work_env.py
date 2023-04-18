import os


def write_env(var_env, value):
    os.environ[var_env] = value


def read_env(var_env):
    return os.environ.get(var_env)
