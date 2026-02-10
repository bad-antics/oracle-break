from setuptools import setup,find_packages
setup(name="oracle-break",version="2.0.0",author="bad-antics",description="Oracle database security testing and vulnerability assessment",packages=find_packages(where="src"),package_dir={"":"src"},python_requires=">=3.8")
