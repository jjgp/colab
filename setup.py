from setuptools import find_packages, setup

install_requires = []

extras_require = {
    "dev": ["black", "flake8 >= 4.0", "isort >= 5.9", "pre-commit >= 2.16"],
}

setup(
    name="colab",
    version="0.0.1",
    url="https://github.com/jjgp/colab",
    author="Jason Prasad",
    author_email="jasongprasad@gmail.com",
    description="colab tools and notebooks",
    install_requires=install_requires,
    extras_require=extras_require,
    packages=find_packages(),
    python_requires=">=3.7",
)
