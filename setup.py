import setuptools

setuptools.setup(include_package_data=True,
                 name='CattleScanner',
                 version='0.1.1',
                 description="Cattle Scanner",
                 author="Aftaab Hussain",
                 author_email="aftaabhussaint@gmail.com",
                 package=setuptools.find_packages(),
                 install_requires=['pandas', 'numpy', 'opencv-python', 'ultralytics', 'joblib', 'scikit-learn'],
                 package_data={
                     'CattleScanner': ['*.pt', '*.csv', '*.txt',
                                      'requirements.txt', '*.pkl']
                 }
                 )
