from setuptools import setup, find_packages

setup(
    name='combine_ome_tiff',
    version='0.1.0',
    description='A tool to combine OME-TIFF files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Arjun Raj',
    packages=find_packages(),
    install_requires=[
        'tifffile',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'combine_ome_tiff=combine_ome_tiff.combine_ome_tiff:main',
        ],
    },
)
