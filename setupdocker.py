from setuptools import setup, find_packages

setup(
    name="UniDec",
    version="5.1.2",
    author="Michael Marty",
    author_email="mtmarty@arizona.edu",
    keywords="UniDec Mass Spectrometry Deconvolution Ion Mobility",
    url="https://github.com/michaelmarty/UniDec",

    install_requires=["numpy>=1.16", "scipy>=1.2", "matplotlib>=3.1", "lxml", "mpld3",'pandas',
                      "pymzml", "natsort", "networkx", "h5py", "multiplierz", "pyimzml", "pyteomics"],
    python_requires='>=3.6',

    packages=find_packages(exclude=["Scripts", "Scripts.*", "*.Scripts", "*.Scripts.*"]),
    include_package_data=True,
    package_data={"": ["logo.ico", "readme.md", "UniDecLogoMR.png", "LICENSE"]},
    exclude_package_data={"": ["Scripts", "Scripts.*", "*.Scripts", "*.Scripts.*"]}
)
