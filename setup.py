import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PointInPolygon",
    version="1.0.2",
    author="Hurin Hu",
    author_email="hurin@live.ca",
    description="This python package is used to check point inside/outside of polygon/multipolygon. It is supported polygon to array, convert multipolygon dataframe to polygon, find the min and max item in 2D array.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Iceloof/PointInPolygon",
    packages=setuptools.find_packages(),
    install_requires=['numpy','pandas','geopandas','shapely'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
