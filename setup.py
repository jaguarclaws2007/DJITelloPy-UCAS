import setuptools

with open("README.md", "r", encoding="utf-8") as fd:
    long_description = fd.read()

# replace relative urls to example files with absolute urls to the main git repo
repo_code_url = "https://github.com/damiafuentes/DJITelloPy/tree/master"
long_description = long_description.replace("](examples/", "]({}/examples/".format(repo_code_url))

setuptools.setup(
    name='tellopy',
    packages=['tellopy'],
    version='1.0.1',
    license='MIT',
    description='Tello drone library including support for video streaming, swarms, state packets and more',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Corbin Mounteer',
    author_email='tello@webtools.tools',
    url='https://github.com/jaguarclaws2007/DJITelloPy-UCAS',
    download_url='https://github.com/damiafuentes/DJITelloPy/archive/2.5.0.tar.gz',
    keywords=['tello', 'dji', 'drone', 'sdk', 'official sdk'],
    install_requires=[
        'numpy',
        'opencv-python',
        'av',
        'pillow'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
