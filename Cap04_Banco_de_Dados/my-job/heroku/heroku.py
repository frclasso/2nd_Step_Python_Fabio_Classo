# Install the Heroku CLI
# Download and install the Heroku CLI.
#
# If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
#
# $ heroku login
# Create a new Git repository
# Initialize a git repository in a new or existing directory
#


###Deploy your application
# Commit your code to the repository and deploy it to Heroku using Git.
# $ cd my-project/
# $ git init
# $ git add .
# $ git commit -am "make it better"
# $ git push -U heroku master
#
# Existing Git repository
# For existing repositories, simply add the heroku remote
#
# $ heroku git:remote -a simuladorapp
#

# instalando gunicorn - para criar lista de requirements
# pip install gunicorn
# rodar pip freeze - para ver todas as instalacoes feitas pelo pip
# copiar todas as aplicacoese colar em requirements.txt
# pip freeze > requirements.txt


#-----
# .gitignore python

#--------------
# criando aplicacao Heroku
# heroku create 'myapp'
# heroku open -a simuladorapp- abre a url no browser


# instalando heroku database
# heroku addons
#heroku addons:create heroku-postgresql:hobby-dev -a simuladorapp


# heroku pg -a 'nomedo app'# exibe dados da database


# configurando as urls da database automaticamente
#pip install django-heroku


### get info
#heroku info - a herokusimapp
#
#
# ### repositorio
# https://git.heroku.com/simuladorapp.git

#dominio
# https://simuladorapp.herokuapp.com/