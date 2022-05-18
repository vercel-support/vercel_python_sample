from setuptools import setup, find_packages

setup(
    name='vercel sample',
    version='0.1',
    url='http://cros-nest.com',
    license='MIT',
    author='galadrin',
    author_email='dapie@cros-nest.com',
    description='sample app for vercel',
    packages=find_packages(),
    install_requires=[
        "uvicorn",
        "fastapi",
        "starlette",
        "requests",
        "dnspython",
        "rich",
    ]
)
