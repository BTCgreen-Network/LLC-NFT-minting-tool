from setuptools import find_packages, setup

with open("README.md", "rt", encoding="UTF-8") as fh:
    long_description = fh.read()

dependencies = [
    "littlelambocoin-blockchain @ git+https://github.com/BTCgreen-Network/littlelambocoin-blockchain.git",
    "packaging==21.3",
]

dev_dependencies = [
    "build",
    "click~=8.1",
    "coverage",
    "pre-commit",
    "pylint",
    "pytest",
    "pytest-asyncio>=0.18.1",  # require attribute 'fixture'
    "pytest-monitor; sys_platform == 'linux'",
    "pytest-xdist",
    "twine",
    "isort",
    "faker",
    "flake8",
    "mypy",
    "black==21.12b0",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "pyinstaller==5.0",
    "pytest",
    "pytest-asyncio",
    "pytest-env",
    "types-aiofiles",
    "types-click",
    "types-cryptography",
    "types-pkg_resources",
    "types-pyyaml",
    "types-setuptools",
    "types-docutils",
]

setup(
    name="littlelambocoinnft",
    version="0.1",
    packages=find_packages(exclude=("tests",)),
    author="Geoff Walmsley",
    entry_points={
        "console_scripts": ["littlelambocoinnft = littlelambocoinnft.cmds.cli:main"],
    },
    package_data={
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clsp", "*.clsp.hex"],
    },
    author_email="g.walmsley@littlelambocoin.net",
    setup_requires=["setuptools_scm"],
    install_requires=dependencies,
    url="https://github.com/BTCgreen-Network",
    license="https://opensource.org/licenses/Apache-2.0",
    description="Littlelambocoin NFT minting toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(
        dev=dev_dependencies,
    ),
    project_urls={
        "Bug Reports": "https://github.com/BTCgreen-Network/littlelambocoin-nft-minting-tool",
        "Source": "https://github.com/BTCgreen-Network/littlelambocoin-nft-minting-tool",
    },
)
