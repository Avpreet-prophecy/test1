from setuptools import setup, find_packages
setup(
    name = 'pip1',
    version = '1.0',
    packages = find_packages(include = ('pip1*', )) + ['prophecy_config_instances.pip1'],
    package_dir = {'prophecy_config_instances.pip1' : 'configs/resources/pip1'},
    package_data = {'prophecy_config_instances.pip1' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.0.8'],
    entry_points = {
'console_scripts' : [
'main = pip1.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
