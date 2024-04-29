import setuptools


# get __version__
exec(open('oriel_cornerstone_260/_version.py').read())

with open("README.md", "r") as fh:
    long_description = fh.read()

project_urls = {
    'Source Code': 'https://github.com/bicarlsen/oriel-cornerstone-260',
    'Bug Tracker': 'https://github.com/bicarlsen/oriel-cornerstone-260/issues'
}

setuptools.setup(
    name="oriel-cornerstone-260",
    version=__version__,
    author="Brian Carlsen",
    author_email="carlsen.bri@gmail.com",
    description="Controller class for communicating with an Oriel Cornerstone 260 monochromator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['oriel', 'cornerstone', 'newport', 'monochromator'],
    url="",
    project_urls = project_urls,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    install_requires=[
        'pyserial'
    ]
)