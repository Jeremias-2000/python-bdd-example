this is just a python bdd example, if You enjoyed it and want to improve this code
create a new branch and feel free !


python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

behave -f allure_behave.formatter:AllureFormatter -o bdd/reports/

allure serve bdd/reports