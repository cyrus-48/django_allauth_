# Setting Up a Django Project with GitHub OAuth
This is a step-by-step guide to setting up a Django project with GitHub OAuth.
## Step 1: Install Virtualenv

### 1. Windows
```bash
pip install virtualenv
python -m venv myenv
myenv\Scripts\activate
```
### 2. linux and macOS
##### Install virtualenv using pip
```bash 
pip install virtualenv
```

##### Create a virtual environment
```bash
python3 -m venv myenv
```

##### Activate the virtual environment
```bash
source myenv/bin/activate
```
 

## Step 2: Install Django and Django Allauth
```bash
pip install django
pip install django-allauth
```
## Step 3: Create a new Django Project
```bash
django-admin startproject myproject
cd myproject
Step 4: Configure Django Allauth
```
## 4.1 Update INSTALLED_APPS in myproject/settings.py:

```python
INSTALLED_APPS = [
    # ...
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    # ...
]
```
## 4.2 Update AUTHENTICATION_BACKENDS:
 
 ```python
AUTHENTICATION_BACKENDS = [
    # ...
    'allauth.account.auth_backends.AuthenticationBackend',
    'allauth.socialaccount.auth_backends.AuthenticationBackend',
    # ...
]
```
## 4.3 Configure GitHub OAuth in myproject/settings.py:
```python
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': ['user:email'],
        'VERIFIED_EMAIL': True,
    }
}
```
## Step 5: Configure GitHub OAuth Application
Go to GitHub Developer Settings.

Click on "New OAuth App."

Fill in the details:

Application name: Your choice (e.g., MyDjangoApp)
Homepage URL: http://localhost:8000 (for development)
Authorization callback URL: http://localhost:8000/accounts/github/login/callback/
Click "Register Application" and note the "Client ID" and "Client Secret."

## Step 6: Update Django Allauth Settings with GitHub Credentials
Update myproject/settings.py:
```python
 
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'APP': {
            'client_id': 'your-github-client-id',
            'secret': 'your-github-client-secret',
        }
    }
}
```
Replace 'your-github-client-id' and 'your-github-client-secret' with your GitHub OAuth application values.

## Step 7: Run Migrations 
```bash
python manage.py migrate
Step 8: Create a Superuser (Optional)
python manage.py createsuperuser
```
 
 

## Step 9: Run the Development Server
 
python manage.py runserver
Visit http://localhost:8000/accounts/login/ in your browser, and you should see the GitHub login option